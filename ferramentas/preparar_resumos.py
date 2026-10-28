"""Baixa os PDFs abertos e prepara uma pasta de resumo por artigo.

Uso: python preparar_resumos.py <cienciometria.csv> <pasta-pdfs> <pasta-resumos> <modelo-pedido.md> "<tema>"

Para cada linha com link de PDF (ou de acesso aberto), baixa com o
baixar_pdf.py (link direto, página do artigo, APIs e navegador headless
opcional), só aceita arquivo que começa com %PDF, extrai o texto com a página
marcada e cria <pasta-resumos>/<autor-ano>/ com TEXTO.txt e PEDIDO.md.

Quando um site bloqueia, o script grava <pasta-pdfs>/FALTANDO.md com o nome
que a pessoa deve usar ao salvar o PDF à mão. Com --abrir, ele já abre a pasta
na tela. Um PDF salvo com outro nome é reconhecido pelo DOI ou pelo título.
Os PDFs ficam fora do repositório (direitos autorais); só os resumos são
publicados.
"""
import argparse
import csv
import datetime
import re
import shutil
import sys
import time
import unicodedata
from pathlib import Path

from pypdf import PdfReader

sys.path.insert(0, str(Path(__file__).resolve().parent))
import baixar_pdf  # noqa: E402
from projeto import barrar_exemplo, opcao_exemplo  # noqa: E402


def slug(autor, ano):
    autor = (autor or "anon").strip()
    nome = autor.split(",", 1)[0] if "," in autor else autor.split()[-1]
    nome = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", nome) + str(ano or "")


def _normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", texto[:20000]).strip()


def _sobrenome(autor):
    autor = (autor or "").strip()
    if "," in autor:
        return _normalizar(autor.split(",", 1)[0])
    partes = [p for p in re.split(r"\s+", autor) if p]
    return _normalizar(partes[-1]) if partes else ""


def combina(texto, doi, titulo, limiar=0.7, autor=""):
    """True se o texto traz o DOI ou o título e o sobrenome do primeiro autor."""
    inicio = _normalizar(texto)
    if doi and doi.lower() in inicio.replace(" ", ""):
        return True
    palavras = [p for p in re.findall(r"[a-z0-9]+", _normalizar(titulo)) if len(p) > 3]
    if not palavras or sum(p in inicio for p in palavras) / len(palavras) < limiar:
        return False
    sobrenome = _sobrenome(autor)
    if sobrenome and not re.search(r"\b" + re.escape(sobrenome) + r"\b", inicio):
        return False
    return True


def nao_confere(texto, doi, titulo, autor=""):
    """Motivo para recusar o PDF, ou "" se ele é mesmo o artigo do DOI."""
    if len(re.sub(r"\[página \d+\]|\s", "", texto or "")) < 2000:
        return "PDF sem texto extraível (escaneado ou em branco)"
    if combina(texto, doi, titulo, autor=autor):
        return ""
    return "o PDF não traz o DOI, o título ou o primeiro autor esperado (pode ser outro artigo)"


def baixar(url):
    """Compatibilidade: baixa um PDF direto, sem as camadas do baixar_pdf."""
    dados, _ = baixar_pdf.baixar_direto(url)
    return dados if dados and baixar_pdf.eh_pdf(dados) else None


def extrair_texto(caminho):
    leitor = PdfReader(str(caminho))
    return "\n\n".join(f"[página {i + 1}]\n{p.extract_text() or ''}" for i, p in enumerate(leitor.pages))


def primeiras_paginas(caminho, paginas=5):
    leitor = PdfReader(str(caminho))
    return "\n\n".join(f"[página {i + 1}]\n{p.extract_text() or ''}"
                       for i, p in enumerate(list(leitor.pages)[:paginas]))


def procurar_manual(pdfs, nome, doi, titulo, reservados, autor=""):
    """PDF que a pessoa já salvou em pdfs/, mesmo com outro nome.

    Procura primeiro o nome canônico, depois um nome parecido e, por fim,
    o conteúdo (DOI ou título + primeiro autor). Se achar, renomeia para
    <nome>.pdf. PDFs já usados por outro artigo ficam fora da busca.
    """
    exato = pdfs / f"{nome}.pdf"
    if exato.exists():
        reservados.add(exato.resolve())
        return exato
    nome_norm = _normalizar(nome).replace(" ", "")
    candidatos = sorted(p for p in pdfs.iterdir()
                        if p.is_file() and p.suffix.lower() == ".pdf")
    for arq in candidatos:
        if arq.resolve() in reservados:
            continue
        stem = _normalizar(arq.stem).replace(" ", "")
        if not (nome_norm and re.fullmatch(re.escape(nome_norm) + r"(?:[^a-z0-9].*)?", stem)):
            continue
        try:
            texto = primeiras_paginas(arq)
        except Exception:
            continue
        if combina(texto, doi, titulo, limiar=0.5, autor=autor):
            return _canonico(pdfs, nome, arq, reservados)
    for arq in candidatos:
        if arq.resolve() in reservados:
            continue
        try:
            texto = primeiras_paginas(arq)
        except Exception:
            continue
        if combina(texto, doi, titulo, limiar=0.85, autor=autor):
            return _canonico(pdfs, nome, arq, reservados)
    return None


def _canonico(pdfs, nome, arq, reservados):
    destino = pdfs / f"{nome}.pdf"
    if arq != destino and not destino.exists():
        shutil.move(str(arq), str(destino))
    reservados.add(destino.resolve())
    return destino


def escrever_instrucoes(pdfs):
    (pdfs / "COLOQUE-OS-PDFS-AQUI.md").write_text(
        "# Coloque os PDFs aqui\n\n"
        "O script tenta baixar sozinho os artigos de acesso aberto. Quando o site bloqueia,\n"
        "ele grava a lista do que faltou em `FALTANDO.md`, com o nome de arquivo que você deve usar.\n\n"
        "1. Baixe o PDF pelo navegador (só artigos de acesso aberto).\n"
        "2. Salve nesta pasta com o nome da coluna **Arquivo** de `FALTANDO.md`\n"
        "   (ex.: `silva2020.pdf`). Se salvar com outro nome, o script tenta reconhecer\n"
        "   pelo DOI, pelo título ou pelo primeiro autor.\n"
        "3. Rode o mesmo comando do `preparar_resumos.py` de novo. Ele aproveita os PDFs\n"
        "   que já estão aqui e não baixa de novo.\n\n"
        "Os PDFs e o texto integral não vão para o Git; só os resumos são publicados.\n",
        encoding="utf-8")


def _celula(texto):
    texto = re.sub(r"[\r\n]+", " ", str(texto or ""))
    return re.sub(r"(?<!\\)\|", r"\\|", texto)


def escrever_faltando(pdfs, falhas):
    if not falhas:
        antigo = pdfs / "FALTANDO.md"
        if antigo.exists():
            antigo.unlink()
        return
    linhas = [
        "# PDFs que faltam",
        "",
        "Salve cada arquivo nesta pasta (`pdfs/`) com o nome da primeira coluna.",
        "Depois rode o comando do `preparar_resumos.py` de novo: ele não baixa outra vez",
        "o que já está aqui.",
        "",
        "| Arquivo | DOI | Título | Motivo |",
        "|---|---|---|---|",
    ]
    for f in falhas:
        linhas.append(f"| {_celula(f['slug'])}.pdf | {_celula(f['doi'])} | "
                      f"{_celula(f['titulo'])} | {_celula(f['motivo'])} |")
    linhas += [
        "",
        "Artigos fechados não têm PDF de acesso aberto; nesses casos, o resumo fica sem.",
        "Se o PDF for de outro artigo, o script recusa e guarda o arquivo como `.rejeitado`.",
        "",
    ]
    (pdfs / "FALTANDO.md").write_text("\n".join(linhas), encoding="utf-8")


def montar_pedido(modelo, tema, doi, titulo, autor, ano):
    trocas = {
        "TEMA": tema,
        "DATA": datetime.date.today().strftime("%d/%m/%Y"),
        "DOI": doi,
        "TITULO": titulo,
        "AUTOR": autor,
        "ANO": str(ano or ""),
    }
    texto = modelo
    for chave, valor in trocas.items():
        texto = texto.replace("{" + chave + "}", valor)
    return texto.rstrip() + f"\n\nDOI deste artigo: {doi}\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description="Baixa os PDFs abertos e prepara uma pasta de resumo por artigo.")
    ap.add_argument("cienciometria", help="CSV gerado por cienciometria.py")
    ap.add_argument("pdfs", help="pasta para os PDFs baixados")
    ap.add_argument("resumos", help="pasta das frentes de resumo")
    ap.add_argument("modelo", help="modelo de PEDIDO.md")
    ap.add_argument("tema", help="título do tema")
    ap.add_argument("--email", default="", help="e-mail para o Unpaywall (opcional; melhora o download)")
    grupo = ap.add_mutually_exclusive_group()
    grupo.add_argument("--navegador", dest="navegador", action="store_true",
                       help="tenta Chromium headless quando o download direto falha (padrão)")
    grupo.add_argument("--sem-navegador", dest="navegador", action="store_false",
                       help="não tenta o Chromium headless")
    ap.set_defaults(navegador=None)
    ap.add_argument("--timeout", type=int, default=60, help="segundos por endereço (padrão: 60)")
    ap.add_argument("--intervalo", type=float, default=1.0,
                    help="segundos entre um artigo e outro (padrão: 1; use 0 para não esperar)")
    ap.add_argument("--abrir", action="store_true", help="abre a pasta pdfs/ quando faltar algum PDF")
    opcao_exemplo(ap)
    a = ap.parse_args(argv)
    barrar_exemplo(ap, a, a.pdfs, a.resumos)
    csv_ref, pdfs, resumos, modelo, tema = (a.cienciometria, a.pdfs, a.resumos, a.modelo, a.tema)
    pdfs, resumos = Path(pdfs), Path(resumos)
    pdfs.mkdir(parents=True, exist_ok=True)
    resumos.mkdir(parents=True, exist_ok=True)
    escrever_instrucoes(pdfs)
    pedido_modelo = Path(modelo).read_text(encoding="utf-8")
    navegador = True if a.navegador is None else a.navegador

    tarefas, usados, fechados = [], set(), 0
    for r in csv.DictReader(open(csv_ref, encoding="utf-8-sig")):
        doi = (r.get("doi") or "").strip()
        if not doi:
            continue
        links = list(dict.fromkeys([r.get("pdf") or ""] + (r.get("pdf_alternativos") or "").split()))
        links = [l for l in links if l]
        acesso = (r.get("acesso") or "").strip().lower()
        if not links and acesso == "closed":
            fechados += 1
            continue
        base = nome = slug(r.get("primeiro_autor"), r.get("ano"))
        letra = ord("b")
        while nome in usados:
            nome, letra = base + chr(letra), letra + 1
        usados.add(nome)
        tarefas.append({
            "slug": nome,
            "doi": doi,
            "titulo": (r.get("titulo") or "").strip(),
            "revista": (r.get("revista") or "").strip(),
            "autor": (r.get("primeiro_autor") or "").strip(),
            "ano": (r.get("ano") or "").strip(),
            "links": links,
            "acesso": acesso,
        })
    reservados, registros, falhas, ok = set(), [], [], 0
    total = len(tarefas)

    def gravar_saidas():
        with open(pdfs.parent / "download.csv", "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["slug", "doi", "titulo", "estado", "fonte", "url", "detalhe"])
            w.writeheader()
            w.writerows(registros)
        escrever_faltando(pdfs, falhas)

    try:
        for indice, t in enumerate(tarefas):
            print(f"[{indice + 1}/{total}] {t['slug']}: baixando...", flush=True)
            if indice and a.intervalo > 0:
                time.sleep(a.intervalo)
            destino = pdfs / f"{t['slug']}.pdf"
            fonte, url, detalhe = "", "", ""
            if destino.exists():
                fonte, url = "já estava", destino.name
                reservados.add(destino.resolve())
            else:
                manual = procurar_manual(pdfs, t["slug"], t["doi"], t["titulo"], reservados, t["autor"])
                if manual:
                    destino, fonte, url = manual, "manual", manual.name
                    reservados.add(destino.resolve())
                else:
                    resultado = baixar_pdf.obter_pdf(
                        t["doi"], t["titulo"], t["links"], a.email, navegador, a.timeout,
                        t["revista"])
                    if resultado.dados:
                        destino.write_bytes(resultado.dados)
                        reservados.add(destino.resolve())
                        fonte, url = resultado.fonte or "download", resultado.url
                        detalhe = f"{len(resultado.dados)} bytes"
                    else:
                        falhas.append({"slug": t["slug"], "doi": t["doi"],
                                       "titulo": t["titulo"], "motivo": resultado.motivo})
                        registros.append({"slug": t["slug"], "doi": t["doi"], "titulo": t["titulo"],
                                          "estado": "falhou", "fonte": "", "url": "",
                                          "detalhe": resultado.motivo})
                        print(f"[{indice + 1}/{total}] {t['slug']}: falhou "
                              f"({resultado.motivo})", flush=True)
                        continue
            try:
                texto = extrair_texto(destino)
            except Exception as e:
                destino.replace(destino.with_suffix(".invalido"))
                motivo = f"PDF ilegível ({type(e).__name__})"
                falhas.append({"slug": t["slug"], "doi": t["doi"], "titulo": t["titulo"], "motivo": motivo})
                registros.append({"slug": t["slug"], "doi": t["doi"], "titulo": t["titulo"],
                                  "estado": "invalido", "fonte": fonte, "url": url, "detalhe": motivo})
                print(f"[{indice + 1}/{total}] {t['slug']}: {motivo}", flush=True)
                continue
            motivo = nao_confere(texto, t["doi"], t["titulo"], t["autor"])
            if motivo:
                destino.replace(destino.with_suffix(".rejeitado"))
                falhas.append({"slug": t["slug"], "doi": t["doi"], "titulo": t["titulo"], "motivo": motivo})
                registros.append({"slug": t["slug"], "doi": t["doi"], "titulo": t["titulo"],
                                  "estado": "rejeitado", "fonte": fonte, "url": url, "detalhe": motivo})
                print(f"[{indice + 1}/{total}] {t['slug']}: {motivo}", flush=True)
                continue
            pasta = resumos / t["slug"]
            pasta.mkdir(exist_ok=True)
            (pasta / "TEXTO.txt").write_text(texto, encoding="utf-8")
            (pasta / "PEDIDO.md").write_text(
                montar_pedido(pedido_modelo, tema, t["doi"], t["titulo"], t["autor"], t["ano"]),
                encoding="utf-8")
            ok += 1
            registros.append({"slug": t["slug"], "doi": t["doi"], "titulo": t["titulo"],
                              "estado": "ok", "fonte": fonte, "url": url, "detalhe": detalhe})
            print(f"[{indice + 1}/{total}] {t['slug']}: ok ({fonte or 'download'})",
                  flush=True)
    finally:
        gravar_saidas()

    print(f"{ok} artigos prontos para resumo; {len(falhas)} sem PDF legível; "
          f"{fechados} fechados sem link.")
    if falhas:
        print("Faltando (salve em pdfs/ com este nome):")
        for f in falhas:
            print(f"  - {f['slug']}.pdf — {f['doi']} — {f['titulo'][:90]}")
        print(f"Lista completa e instruções: {pdfs / 'FALTANDO.md'}")
        if a.abrir:
            try:
                from entrega import abrir
                abriu, detalhe = abrir(pdfs)
                print(("Pasta aberta: " if abriu else "Não consegui abrir a pasta: ")
                      + (str(pdfs) if abriu else detalhe))
            except Exception as e:
                print(f"Não consegui abrir a pasta ({type(e).__name__}): {pdfs}")
    else:
        print("Todos os PDFs abertos estão prontos para resumo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
