"""Monta a tabela final: cienciometria + link para o resumo de cada artigo.

Uso: python painel.py <pasta-do-exemplo>

Lê <pasta>/cienciometria.csv, <pasta>/referencias.bib (autor e ano, como no
registro do DOI) e <pasta>/resumos/*/RELATORIO.md. Grava <pasta>/TABELA.md,
ordenada por citações, e <pasta>/tabela.json (usada pelo site).
"""
import csv
import json
import re
import sys
from pathlib import Path

ACESSO = {"gold": "aberto (revista)", "diamond": "aberto (sem taxa)", "hybrid": "aberto (híbrido)",
          "green": "aberto (repositório)", "bronze": "aberto (bronze)", "closed": "fechado"}


def autor_ano_do_bib(bib):
    """{doi: (sobrenome do primeiro autor, ano)} a partir do .bib do doi.org."""
    saida = {}
    for entrada in re.split(r"\n(?=@)", bib):
        doi = re.search(r"DOI\s*=\s*\{([^}]+)\}", entrada, re.I)
        if not doi:
            continue
        autor = re.search(r"author\s*=\s*\{([^,}]+)", entrada, re.I)
        ano = re.search(r"year\s*=\s*\{?(\d{4})", entrada, re.I)
        saida[doi.group(1).lower()] = (autor.group(1).strip() if autor else "",
                                       ano.group(1) if ano else "")
    return saida


def main():
    pasta = Path(sys.argv[1])
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
    linhas = []
    for r in csv.DictReader(open(pasta / "cienciometria.csv", encoding="utf-8-sig")):
        d = r["doi"].lower()
        autor, ano = bib.get(d, (r.get("primeiro_autor", ""), r.get("ano", "")))
        linhas.append({
            "doi": r["doi"], "ano": ano, "autor": autor, "titulo": r.get("titulo", ""),
            "revista": r.get("revista", ""), "citacoes": int(r.get("citacoes") or 0),
            "fwci": r.get("fwci", ""), "percentil": r.get("percentil", ""),
            "acesso": ACESSO.get(r.get("acesso", ""), r.get("acesso", "")),
            "resumo": resumos.get(d, ""), "preprint": d in preprint,
        })
    linhas.sort(key=lambda l: -l["citacoes"])
    md = ["# Referências por citação", "",
          "Fonte: OpenAlex. FWCI = citações normalizadas por área e ano (1 = média mundial). "
          "Percentil = posição do artigo entre os da mesma área e ano (99 = entre os 1% mais citados). "
          "Autor e ano como no registro do DOI.", "",
          "| Citações | FWCI | Percentil | Autor (ano) | Título | Revista | Acesso | Resumo |",
          "|---:|---:|---:|---|---|---|---|---|"]
    for l in linhas:
        res = f"[ler]({l['resumo']})" + (" (preprint)" if l["preprint"] else "") if l["resumo"] else ""
        md.append(f"| {l['citacoes']} | {l['fwci']} | {l['percentil']} | {l['autor']} et al. ({l['ano']}) | "
                  f"[{l['titulo']}](https://doi.org/{l['doi']}) | {l['revista']} | {l['acesso']} | {res} |")
    (pasta / "TABELA.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (pasta / "tabela.json").write_text(json.dumps(linhas, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(linhas)} referências, {len(resumos)} com resumo -> {pasta / 'TABELA.md'}")


if __name__ == "__main__":
    main()
