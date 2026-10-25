"""Cienciometria das referências pelo OpenAlex (gratuito, sem conta).

Uso: python cienciometria.py <referencias.bib> <saida.csv> [seu-email]

Para cada DOI do .bib: ano, primeiro autor, revista, citações, FWCI (citações
normalizadas pela área e ano; 1 = média), percentil de citação, status de acesso
aberto e links do PDF aberto (do editor e de repositórios), quando existem.
"""
import csv
import json
import re
import sys
import time
import urllib.parse
import urllib.request

CAMPOS = ["doi", "ano", "primeiro_autor", "titulo", "revista", "citacoes", "fwci",
          "percentil", "acesso", "pdf", "pdf_alternativos"]


def consulta(doi, email):
    url = ("https://api.openalex.org/works/doi:" + urllib.parse.quote(doi)
           + (f"?mailto={email}" if email else ""))
    w = json.loads(urllib.request.urlopen(url, timeout=25).read())
    autores = w.get("authorships") or []
    fonte = ((w.get("primary_location") or {}).get("source") or {})
    oa = w.get("open_access") or {}
    pct = (w.get("citation_normalized_percentile") or {}).get("value")
    return {
        "doi": doi,
        "ano": w.get("publication_year"),
        "primeiro_autor": (autores[0]["author"]["display_name"] if autores else ""),
        "titulo": w.get("title") or "",
        "revista": fonte.get("display_name") or "",
        "citacoes": w.get("cited_by_count"),
        "fwci": round(w["fwci"], 2) if w.get("fwci") is not None else "",
        "percentil": min(99, int(100 * pct)) if pct is not None else "",
        "acesso": oa.get("oa_status") or "",
        "pdf": (w.get("best_oa_location") or {}).get("pdf_url") or "",
        # Cópias em repositórios (universidades, PMC, HAL...): o editor às vezes bloqueia script.
        "pdf_alternativos": " ".join(dict.fromkeys(
            l["pdf_url"] for l in w.get("locations") or [] if l.get("pdf_url"))),
    }


def main():
    bib, saida = sys.argv[1], sys.argv[2]
    email = sys.argv[3] if len(sys.argv) > 3 else ""
    dois = re.findall(r"DOI\s*=\s*\{([^}]+)\}", open(bib, encoding="utf-8").read(), re.I)
    linhas = []
    for doi in dois:
        try:
            linhas.append(consulta(doi, email))
        except Exception as e:
            linhas.append({"doi": doi, "titulo": f"(não achado no OpenAlex: {type(e).__name__})"})
        time.sleep(0.2)
    linhas.sort(key=lambda r: -(r.get("citacoes") or 0))
    with open(saida, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        w.writeheader()
        w.writerows(linhas)
    abertos = sum(1 for r in linhas if r.get("acesso") and r["acesso"] != "closed")
    com_pdf = sum(1 for r in linhas if r.get("pdf"))
    print(f"{len(linhas)} referências; {abertos} em acesso aberto; {com_pdf} com PDF direto -> {saida}")


if __name__ == "__main__":
    main()
