"""Monta a tabela final: cienciometria + link para o resumo de cada artigo.

Uso: python painel.py <pasta-do-exemplo>

Lê <pasta>/cienciometria.csv, <pasta>/referencias.bib (autores e ano, como no
registro do DOI), <pasta>/REFERENCIAS.md (bases e relatórios sem DOI),
<pasta>/resumos/*/RELATORIO.md, <pasta>/frentes/*/RELATORIO.md (de que frente
veio cada artigo) e, se existir, <pasta>/minhas_referencias.csv (o que você já
cita; ver conferir_lista.py). Grava <pasta>/TABELA.md, ordenada por citações,
com uma seção final para as bases sem DOI, e <pasta>/tabela.json (usada pelo site).
"""
import argparse
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import doi as doilib  # noqa: E402
import revistas  # noqa: E402
from conferir_lista import dois_citados  # noqa: E402
from projeto import barrar_exemplo, opcao_exemplo  # noqa: E402

ACESSO = {"gold": "aberto (revista)", "diamond": "aberto (sem taxa)", "hybrid": "aberto (híbrido)",
          "green": "aberto (repositório)", "bronze": "aberto (bronze)", "closed": "fechado"}


def autores_do_bib(entrada):
    """Sobrenomes do campo author, na ordem em que aparecem no .bib."""
    m = re.search(r"author\s*=\s*\{((?:[^{}]|\{[^{}]*\})*)\}", entrada, re.I)
    if not m:
        return []
    autores = []
    for nome in re.split(r"\s+and\s+", m.group(1), flags=re.I):
        nome = nome.strip().strip("{}").strip()
        if not nome or nome.lower() == "others":
            continue
        sobrenome = nome.split(",", 1)[0].strip()
        if not sobrenome:
            sobrenome = nome.split()[-1]
        autores.append(re.sub(r"\s+", " ", sobrenome))
    return autores


def autor_ano_do_bib(bib):
    """{doi: (lista de sobrenomes, ano)} a partir do .bib do doi.org."""
    saida = {}
    for entrada in re.split(r"\n(?=@)", bib):
        doi = re.search(r"DOI\s*=\s*\{([^}]+)\}", entrada, re.I)
        if not doi:
            continue
        ano = re.search(r"year\s*=\s*\{?(\d{4})", entrada, re.I)
        saida[doi.group(1).strip().lower()] = (autores_do_bib(entrada),
                                               ano.group(1) if ano else "")
    return saida


def formatar_autores(autores, ano):
    """'Sobrenome (ano)', 'Sobrenome & Sobrenome (ano)' ou 'Sobrenome et al. (ano)'."""
    autores = [a for a in autores if a]
    if not autores:
        return ""
    if len(autores) == 1:
        nome = autores[0]
    elif len(autores) == 2:
        nome = f"{autores[0]} & {autores[1]}"
    else:
        nome = f"{autores[0]} et al."
    return f"{nome} ({ano})" if ano else nome


def sobrenome(nome):
    """Sobrenome de um nome de exibição ('Nico Lang') ou de um nome do .bib ('Lang, Nico')."""
    nome = (nome or "").strip()
    if not nome:
        return ""
    if "," in nome:
        return nome.split(",", 1)[0].strip()
    return nome.split()[-1]


def celula(texto):
    """Texto seguro para uma célula de tabela markdown."""
    return re.sub(r"(?<!\\)\|", r"\\|", str(texto))


def _celulas(linha):
    s = linha.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in re.split(r"(?<!\\)\|", s)]


def _separador(celulas):
    return bool(celulas) and all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in celulas)


def bases_sem_doi(texto):
    """(autor, título, link) das linhas de tabela do REFERENCIAS.md que não têm DOI."""
    saida = []
    for linha in texto.splitlines():
        if not linha.lstrip().startswith("|"):
            continue
        celulas = _celulas(linha)
        if len(celulas) < 3 or _separador(celulas):
            continue
        if celulas[0].lower().startswith(("autor", "autores", "referência", "referencia")):
            continue
        if doilib.achar(linha):
            continue
        link = ""
        for c in celulas:
            m = re.search(r"https?://[^\s|\]\)>]+", c)
            if m:
                link = m.group(0).rstrip(".,;:")
                break
        if not link:
            continue
        saida.append((celulas[0], celulas[1], link))
    return saida


def frentes_por_doi(pasta):
    """{doi: [frentes]} a partir das tabelas de frentes/*/RELATORIO.md."""
    saida = {}
    for rel in sorted(Path(pasta).glob("frentes/*/RELATORIO.md")):
        for linha in rel.read_text(encoding="utf-8").splitlines():
            if not linha.lstrip().startswith("|"):
                continue
            d = doilib.achar(linha)
            if d and rel.parent.name not in saida.setdefault(d.lower(), []):
                saida[d.lower()].append(rel.parent.name)
    return saida


def indicadores_texto(l):
    """Texto curto dos indicadores da revista, para a tabela em Markdown."""
    partes = []
    if l.get("sinal_revista") == "retratado":
        partes.append("⛔ retratado")
    if l.get("doaj") == "sim":
        partes.append("DOAJ")
    if l.get("cwts_core") == "sim":
        partes.append("CWTS Core")
    if l.get("qualis"):
        partes.append(f"Qualis {l['qualis']}")
    if l.get("sinal_revista") == "conferir":
        partes.append("⚠ conferir")
    return " · ".join(partes)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Monta TABELA.md e tabela.json a partir da cienciometria e dos resumos.")
    ap.add_argument("pasta", help="pasta do levantamento (ex.: exemplo)")
    opcao_exemplo(ap)
    a = ap.parse_args(argv)
    barrar_exemplo(ap, a, a.pasta)
    pasta = Path(a.pasta)
    bib = autor_ano_do_bib((pasta / "referencias.bib").read_text(encoding="utf-8"))
    # O DOI de cada resumo está no PEDIDO.md que o preparar_resumos.py escreveu.
    resumos, preprint = {}, set()
    for rel in (pasta / "resumos").glob("*/RELATORIO.md"):
        m = re.search(r"DOI deste artigo: (\S+)", (rel.parent / "PEDIDO.md").read_text(encoding="utf-8"))
        if not m:
            continue
        d = m.group(1).lower()
        resumos[d] = f"resumos/{rel.parent.name}/RELATORIO.md"
        if re.search(r"arxiv|preprint", rel.read_text(encoding="utf-8")[:3000], re.I):
            preprint.add(d)
    frentes = frentes_por_doi(pasta)
    citados = dois_citados(pasta)
    linhas = []
    for r in csv.DictReader(open(pasta / "cienciometria.csv", encoding="utf-8-sig")):
        d = r["doi"].lower()
        autores, ano = bib.get(d, (None, None))
        if not autores:
            autores = [sobrenome(r.get("primeiro_autor", ""))] if r.get("primeiro_autor") else []
        if not ano:
            ano = r.get("ano", "")
        linhas.append({
            "doi": r["doi"], "ano": ano, "autor": autores[0] if autores else "",
            "autores": formatar_autores(autores, ano), "titulo": r.get("titulo", ""),
            "revista": r.get("revista", ""), "citacoes": int(r.get("citacoes") or 0),
            "fwci": r.get("fwci", ""), "percentil": r.get("percentil", ""),
            "acesso": ACESSO.get(r.get("acesso", ""), r.get("acesso", "")),
            "resumo": resumos.get(d, ""), "preprint": d in preprint,
            **{c: r.get(c, "") for c in revistas.CAMPOS},
            "frentes": frentes.get(d, []), "ja_citado": d in citados,
        })
    linhas.sort(key=lambda l: -l["citacoes"])
    md = ["# Referências por citação", "",
          "Fonte: OpenAlex. FWCI = citações normalizadas por área e ano (1 = média mundial). "
          "Percentil = posição do artigo entre os da mesma área e ano (99 = entre os 1% mais citados). "
          "Autores e ano como no registro do DOI.", "",
          "Indicadores da revista: DOAJ e CWTS Core (OpenAlex), Qualis (planilha da Sucupira, se dada), "
          "⛔ = artigo retratado (Retraction Watch, via OpenAlex), ⚠ conferir = a revista não está em "
          "nenhuma dessas listas; isso não quer dizer que seja predatória.", "",
          "| Citações | FWCI | Percentil | Autores (ano) | Título | Revista | Indicadores | Frente | Já cito | Acesso | Resumo |",
          "|---:|---:|---:|---|---|---|---|---|---|---|---|"]
    for l in linhas:
        res = f"[ler]({l['resumo']})" + (" (preprint)" if l["preprint"] else "") if l["resumo"] else ""
        md.append(f"| {l['citacoes']} | {l['fwci']} | {l['percentil']} | {celula(l['autores'])} | "
                  f"[{celula(l['titulo'])}](https://doi.org/{l['doi']}) | {celula(l['revista'])} | "
                  f"{celula(indicadores_texto(l))} | {celula(', '.join(l['frentes']))} | "
                  f"{'sim' if l['ja_citado'] else ''} | {l['acesso']} | {res} |")
    bases = bases_sem_doi((pasta / "REFERENCIAS.md").read_text(encoding="utf-8"))
    if bases:
        md += ["", "## Bases e relatórios sem DOI", "",
               "| Autor (ano) | Título | Link |", "|---|---|---|"]
        md += [f"| {celula(autor)} | {celula(titulo)} | {link} |" for autor, titulo, link in bases]
    (pasta / "TABELA.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (pasta / "tabela.json").write_text(json.dumps(linhas, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(linhas)} referências, {len(resumos)} com resumo, {len(bases)} sem DOI -> {pasta / 'TABELA.md'}")
    if citados:
        print(f"{sum(1 for l in linhas if l['ja_citado'])} já citadas na sua lista")


if __name__ == "__main__":
    sys.exit(main())
