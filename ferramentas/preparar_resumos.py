"""Baixa os PDFs abertos e prepara uma pasta de resumo por artigo.

Uso: python preparar_resumos.py <cienciometria.csv> <pasta-pdfs> <pasta-resumos> <modelo-pedido.md> "<tema>"

Para cada linha com link de PDF: baixa (só aceita arquivo que começa com %PDF;
alguns editores, como a MDPI, devolvem uma página de verificação e ficam de fora),
extrai o texto com a página marcada e cria <pasta-resumos>/<autor-ano>/ com
TEXTO.txt e PEDIDO.md. Depois rode o orquestrar.py nessa pasta.
Os PDFs ficam fora do repositório (direitos autorais); só os resumos são publicados.
"""
import argparse
import csv
import datetime
import re
import subprocess
import sys
import unicodedata
import urllib.request
from pathlib import Path

from pypdf import PdfReader


def slug(autor, ano):
    nome = (autor or "anon").split()[-1]
    nome = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", nome) + str(ano or "")


def nao_confere(texto, doi, titulo):
    """Motivo para recusar o PDF, ou "" se ele é mesmo o artigo do DOI."""
    if len(re.sub(r"\[página \d+\]|\s", "", texto)) < 2000:
        return "PDF sem texto extraível (escaneado ou em branco)"
    inicio = re.sub(r"\s+", " ", texto[:15000]).lower()
    if doi.lower() in inicio.replace(" ", ""):
        return ""
    palavras = [p for p in re.findall(r"[a-zà-ú0-9]+", titulo.lower()) if len(p) > 3]
    if palavras and sum(p in inicio for p in palavras) / len(palavras) >= 0.7:
        return ""
    return "o PDF não traz o DOI nem o título esperado (pode ser outro artigo)"


def baixar(url):
    """urllib primeiro; se falhar ou não vier PDF, tenta o curl (alguns sites só aceitam ele)."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        dados = urllib.request.urlopen(req, timeout=60).read()
        if dados.startswith(b"%PDF"):
            return dados
    except Exception:
        pass
    try:
        dados = subprocess.run(["curl", "-sL", "--max-time", "90", "-A", "Mozilla/5.0", url],
                               capture_output=True, timeout=120).stdout
    except Exception:
        return None
    return dados if dados.startswith(b"%PDF") else None


def main(argv=None):
    ap = argparse.ArgumentParser(description="Baixa os PDFs abertos e prepara uma pasta de resumo por artigo.")
    ap.add_argument("cienciometria", help="CSV gerado por cienciometria.py")
    ap.add_argument("pdfs", help="pasta para os PDFs baixados")
    ap.add_argument("resumos", help="pasta das frentes de resumo")
    ap.add_argument("modelo", help="modelo de PEDIDO.md")
    ap.add_argument("tema", help="título do tema")
    a = ap.parse_args(argv)
    csv_ref, pdfs, resumos, modelo, tema = (a.cienciometria, a.pdfs, a.resumos, a.modelo, a.tema)
    pdfs, resumos = Path(pdfs), Path(resumos)
    pdfs.mkdir(parents=True, exist_ok=True)
    resumos.mkdir(parents=True, exist_ok=True)
    pedido = (Path(modelo).read_text(encoding="utf-8")
              .replace("{TEMA}", tema).replace("{DATA}", datetime.date.today().strftime("%d/%m/%Y")))
    ok, falhas, usados = 0, [], set()
    for r in csv.DictReader(open(csv_ref, encoding="utf-8-sig")):
        links = list(dict.fromkeys([r.get("pdf") or ""] + (r.get("pdf_alternativos") or "").split()))
        links = [l for l in links if l]
        if not links:
            continue
        base = nome = slug(r.get("primeiro_autor"), r.get("ano"))
        letra = ord("b")
        while nome in usados:
            nome, letra = base + chr(letra), letra + 1
        usados.add(nome)
        destino = pdfs / f"{nome}.pdf"
        if not destino.exists():
            dados = next((d for d in map(baixar, links) if d), None)
            if not dados:
                falhas.append(f"{nome}: nenhum dos {len(links)} endereços entregou o PDF")
                continue
            destino.write_bytes(dados)
        try:
            leitor = PdfReader(str(destino))
            texto = "\n\n".join(f"[página {i + 1}]\n{p.extract_text() or ''}" for i, p in enumerate(leitor.pages))
        except Exception as e:
            # PDF truncado ou corrompido: guarda à parte e segue com os outros.
            destino.replace(destino.with_suffix(".invalido"))
            falhas.append(f"{nome}: PDF ilegível ({type(e).__name__})")
            continue
        motivo = nao_confere(texto, r["doi"], r.get("titulo", ""))
        if motivo:
            # Link errado (outro artigo) ou PDF sem texto (escaneado): não resumir.
            destino.replace(destino.with_suffix(".rejeitado"))
            falhas.append(f"{nome}: {motivo}")
            continue
        pasta = resumos / nome
        pasta.mkdir(exist_ok=True)
        (pasta / "TEXTO.txt").write_text(texto, encoding="utf-8")
        (pasta / "PEDIDO.md").write_text(pedido + f"\n\nDOI deste artigo: {r['doi']}\n", encoding="utf-8")
        ok += 1
    print(f"{ok} artigos prontos para resumo; {len(falhas)} sem PDF legível:")
    for f in falhas:
        print("  -", f)


if __name__ == "__main__":
    sys.exit(main())
