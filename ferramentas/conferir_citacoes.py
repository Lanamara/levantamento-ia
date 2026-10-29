"""Cruza as citações do texto com a lista de referências (formato autor-data, ABNT).

Uso: python conferir_citacoes.py <texto.docx|.txt|.md> <saida.md>

Lê o documento, separa o corpo da lista de referências (a partir do título
"REFERÊNCIAS" ou "REFERÊNCIAS BIBLIOGRÁFICAS") e confere:

- CITADA-SEM-REFERENCIA: citação no texto, como (IMB, 2022) ou Ross (1994),
  sem entrada correspondente na lista;
- ANO-DIFERE: o autor está na lista, mas com outro ano;
- NAO-CITADA: entrada da lista que não aparece citada no texto;
- MESMO-AUTOR-ANO: duas entradas com o mesmo autor e o mesmo ano sem letra
  (a ABNT pede 2025a, 2025b para diferenciar).

A comparação usa o primeiro autor (sobrenome ou entidade, sem acento, em
maiúsculas) e o ano. Datas de acesso ("Acesso em: ...") e anos dentro de links
e DOIs são ignorados. O script não altera o documento; confira cada caso no
texto antes de corrigir, porque citações fora do padrão autor-data podem não ser
reconhecidas.
"""
import argparse
import html
import re
import sys
import unicodedata
import zipfile
from pathlib import Path

ANO = r"(?:19|20)\d{2}"


def sem_acento(t):
    return "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn")


def chave_nome(nome):
    """'Ross', 'ROSS', 'Martins-Neto', 'IMB' -> 'ROSS', 'MARTINS-NETO', 'IMB'."""
    nome = sem_acento(re.sub(r"[*_]", "", nome or "")).upper().strip()
    nome = re.split(r"\s+(?:ET\s+AL\.?|E|&)(?:\s+|$)|;|,", nome)[0].strip()
    return re.sub(r"[^A-Z0-9\- ]", "", nome).strip()


def ler_paragrafos(caminho):
    """Lista de parágrafos de um .docx (sem dependência extra) ou de um texto."""
    caminho = Path(caminho)
    if caminho.suffix.lower() == ".docx":
        with zipfile.ZipFile(caminho) as z:
            xml = z.read("word/document.xml").decode("utf-8")
        paragrafos = []
        for p in re.findall(r"<w:p[ >].*?</w:p>", xml, re.S):
            p = re.sub(r"<w:tab/>|<w:br/>", " ", p)
            texto = "".join(re.findall(r"<w:t(?: [^>]*)?>(.*?)</w:t>", p, re.S))
            paragrafos.append(html.unescape(texto))
        return paragrafos
    texto = caminho.read_text(encoding="utf-8-sig")
    return texto.replace("\r\n", "\n").split("\n")


def separar(paragrafos):
    """(corpo, lista de referências) a partir do último título REFERÊNCIAS."""
    limpo = [re.sub(r"[*#_]", "", p).strip() for p in paragrafos]
    idx = None
    for i, p in enumerate(limpo):
        if re.fullmatch(r"(?:\d+\.?\s*)?REFER[EÊ]NCIAS(?:\s+BIBLIOGR[AÁ]FICAS)?", p, re.I):
            idx = i
    if idx is None:
        return "\n".join(paragrafos), []
    lista = [re.sub(r"\s+", " ", p).strip() for p in paragrafos[idx + 1:]]
    lista = [re.sub(r"[*]", "", p) for p in lista if len(p) >= 25]
    return "\n".join(paragrafos[:idx]), lista


def chave_referencia(ref):
    """Primeiro autor da entrada: 'IMB – INSTITUTO...' -> 'IMB'; 'ROSS, J. L. S.' -> 'ROSS'."""
    inicio = re.split(r"\s+[–—-]\s+|,|\.\s", ref, maxsplit=1)[0]
    return chave_nome(inicio.rstrip("."))


def ano_referencia(ref):
    """Ano da entrada (o último, sem datas de acesso, links e DOIs). Mantém a letra (2025a)."""
    texto = re.sub(rf"Acesso em:.*?\b{ANO}\b", " ", ref, flags=re.I)
    texto = re.sub(r"https?://\S+|\b10\.\d{4,9}/\S+", " ", texto)
    anos = re.findall(rf"\b({ANO}[a-z]?)\b", texto)
    return anos[-1] if anos else ""


def citacoes(corpo):
    """Lista de (chave, ano, trecho) das citações autor-data do texto."""
    saida = []
    texto = re.sub(r"https?://\S+", " ", corpo)
    # Entre parênteses: (AUTOR, 2020), (AUTOR et al., 2020; OUTRO, 2019a, p. 12)
    for m in re.finditer(r"\(([^()]*?\b" + ANO + r"[^()]*)\)", texto):
        for parte in m.group(1).split(";"):
            c = re.match(rf"\s*([^,\d][^,]*?),\s*({ANO}[a-z]?)\b", parte)
            if c and re.match(r"[A-ZÀ-Ý]", c.group(1).strip()):
                saida.append((chave_nome(c.group(1)), c.group(2), f"({m.group(1).strip()})"))
    # Narrativa: Ross (1994), Gorelick et al. (2017), Costa e Quintanilha (2024)
    padrao = (r"\b([A-ZÀ-Ý][\wÀ-ÿ'\-]+)(?:\s+et\s+al\.)?(?:\s+(?:e|&)\s+[A-ZÀ-Ý][\wÀ-ÿ'\-]+)?"
              rf"\s*\(({ANO}[a-z]?)(?:,\s*p\.[^)]*)?\)")
    for m in re.finditer(padrao, texto):
        saida.append((chave_nome(m.group(1)), m.group(2), m.group(0)))
    return saida


def conferir(corpo, lista):
    """Lista de achados (estado, chave, ano, detalhe)."""
    refs = [(chave_referencia(r), ano_referencia(r), r) for r in lista]
    anos_por_chave = {}
    for chave, ano, _ in refs:
        anos_por_chave.setdefault(chave, []).append(ano)
    achados, citadas = [], set()
    vistos = set()
    for chave, ano, trecho in citacoes(corpo):
        if (chave, ano) in vistos:
            continue
        vistos.add((chave, ano))
        if ano in anos_por_chave.get(chave, []):
            citadas.add((chave, ano))
            achados.append(("OK", chave, ano, trecho))
        elif chave in anos_por_chave:
            achados.append(("ANO-DIFERE", chave, ano,
                            f"{trecho}: na lista, {chave} tem {', '.join(sorted(set(anos_por_chave[chave])))}"))
        else:
            achados.append(("CITADA-SEM-REFERENCIA", chave, ano, trecho))
    contagem = {}
    for chave, ano, _ in refs:
        contagem[(chave, ano)] = contagem.get((chave, ano), 0) + 1
    for (chave, ano), n in sorted(contagem.items()):
        if n > 1 and not re.search(r"[a-z]$", ano):
            achados.append(("MESMO-AUTOR-ANO", chave, ano,
                            f"{n} entradas de {chave} em {ano}: use {ano}a, {ano}b no texto e na lista"))
    for chave, ano, ref in refs:
        if (chave, ano) not in citadas:
            achados.append(("NAO-CITADA", chave, ano, ref))
    return achados


ORDEM = ["CITADA-SEM-REFERENCIA", "ANO-DIFERE", "MESMO-AUTOR-ANO", "NAO-CITADA", "OK"]


def relatorio(achados, n_refs, nome):
    cont = {e: sum(1 for a in achados if a[0] == e) for e in ORDEM}
    md = [f"# Citações x referências — {nome}", "",
          f"{n_refs} entradas na lista. " + ", ".join(f"{e}: {n}" for e, n in cont.items()), "",
          "Comparação pelo primeiro autor e pelo ano (formato autor-data). Confira cada caso "
          "no texto antes de corrigir: citações fora desse formato podem não ser reconhecidas.", ""]
    for estado in ORDEM:
        grupo = [a for a in achados if a[0] == estado]
        if not grupo:
            continue
        md += [f"## {estado} ({len(grupo)})", "", "| Autor | Ano | Detalhe |", "|---|---|---|"]
        md += [f"| {c} | {a} | {d.replace('|', '/')[:220]} |" for _, c, a, d in grupo]
        md.append("")
    return "\n".join(md) + "\n", cont


def main(argv=None):
    ap = argparse.ArgumentParser(description="Cruza as citações do texto com a lista de referências.")
    ap.add_argument("documento", help=".docx, .txt ou .md com o texto e a lista de referências")
    ap.add_argument("saida", help="arquivo Markdown com o resultado")
    a = ap.parse_args(argv)
    corpo, lista = separar(ler_paragrafos(a.documento))
    if not lista:
        print("AVISO: não achei o título REFERÊNCIAS; nada a comparar.")
        return 1
    texto, cont = relatorio(conferir(corpo, lista), len(lista), Path(a.documento).name)
    Path(a.saida).write_text(texto, encoding="utf-8")
    print(", ".join(f"{e}: {n}" for e, n in cont.items()) + f" -> {a.saida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
