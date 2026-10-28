"""Cienciometria das referências pelo OpenAlex (gratuito, sem conta).

Uso: python cienciometria.py <referencias.bib> <saida.csv> [seu-email]

Para cada DOI do .bib: ano, primeiro autor, revista, citações, FWCI (citações
normalizadas pela área e ano; 1 = média), percentil de citação, status de acesso
aberto e links do PDF aberto (do editor e de repositórios), quando existem.
DOI que falhar no OpenAlex continua no CSV principal com ano, primeiro autor e
título do .bib e as métricas vazias; ele também vai para <saida>-falhas.csv,
com as colunas doi e erro. Uma falha de rede é tentada de novo uma vez.
"""
import argparse
import csv
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from projeto import barrar_exemplo, opcao_exemplo  # noqa: E402

CAMPOS = ["doi", "ano", "primeiro_autor", "titulo", "revista", "citacoes", "fwci",
          "percentil", "acesso", "pdf", "pdf_alternativos"]


def url_openalex(doi, email):
    url = "https://api.openalex.org/works/doi:" + urllib.parse.quote(doi)
    if email:
        url += "?mailto=" + urllib.parse.quote(email, safe="")
    return url


def _consultar_uma(doi, email):
    w = json.loads(urllib.request.urlopen(url_openalex(doi, email), timeout=25).read())
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


def consulta(doi, email):
    """Tenta duas vezes: uma falha passageira não tira o artigo do CSV."""
    ultimo = None
    for tentativa in range(2):
        try:
            return _consultar_uma(doi, email)
        except Exception as e:
            ultimo = e
            if tentativa == 0:
                time.sleep(2)
    raise ultimo


def _campo(entrada, nome):
    m = re.search(rf"\b{nome}\s*=\s*\{{((?:[^{{}}]|\{{[^{{}}]*\}})*)\}}",
                  entrada, re.I)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""


def metadados_do_bib(texto):
    """DOI -> ano, primeiro autor e título, para preencher uma falha do OpenAlex."""
    saida = {}
    for entrada in re.split(r"\n(?=@)", texto or ""):
        doi = _campo(entrada, "DOI")
        if not doi:
            continue
        autores = _campo(entrada, "author")
        primeiro = ""
        if autores:
            primeiro = re.split(r"\s+and\s+", autores, flags=re.I)[0].strip().strip("{}").strip()
            if "," in primeiro:
                primeiro = primeiro.split(",", 1)[0].strip()
            elif primeiro.split():
                primeiro = primeiro.split()[-1]
        saida[doi.lower()] = {
            "ano": _campo(entrada, "year"),
            "primeiro_autor": primeiro,
            "titulo": _campo(entrada, "title"),
        }
    return saida


def main(argv=None):
    ap = argparse.ArgumentParser(description="Busca citações, FWCI, percentil e acesso aberto no OpenAlex.")
    ap.add_argument("bib", help="referencias.bib")
    ap.add_argument("saida", help="CSV de saída (ex.: cienciometria.csv)")
    ap.add_argument("email", nargs="?", default="", help="e-mail para o mailto do OpenAlex (opcional)")
    opcao_exemplo(ap)
    a = ap.parse_args(argv)
    barrar_exemplo(ap, a, a.saida)
    saida = Path(a.saida)
    texto_bib = Path(a.bib).read_text(encoding="utf-8-sig")
    dois = re.findall(r"DOI\s*=\s*\{([^}]+)\}", texto_bib, re.I)
    meta = metadados_do_bib(texto_bib)
    linhas, falhas = [], []
    for i, doi in enumerate(dois, 1):
        if i == 1 or i % 10 == 0:
            print(f"OpenAlex {i}/{len(dois)}: {doi}", flush=True)
        try:
            linhas.append(consulta(doi, a.email))
        except Exception as e:
            falhas.append({"doi": doi, "erro": f"{type(e).__name__}: {e}"})
            dados = meta.get(doi.lower(), {})
            linhas.append({
                "doi": doi,
                "ano": dados.get("ano", ""),
                "primeiro_autor": dados.get("primeiro_autor", ""),
                "titulo": dados.get("titulo", ""),
                "revista": "",
                "citacoes": "",
                "fwci": "",
                "percentil": "",
                "acesso": "",
                "pdf": "",
                "pdf_alternativos": "",
            })
        time.sleep(0.2)
    linhas.sort(key=lambda r: -(r.get("citacoes") or 0))
    with open(saida, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        w.writeheader()
        w.writerows(linhas)
    falhas_path = saida.with_name(saida.stem + "-falhas.csv")
    if falhas:
        with open(falhas_path, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["doi", "erro"])
            w.writeheader()
            w.writerows(falhas)
    elif falhas_path.exists():
        falhas_path.unlink()
    abertos = sum(1 for r in linhas if r.get("acesso") and r["acesso"] != "closed")
    com_pdf = sum(1 for r in linhas if r.get("pdf"))
    aviso = f"{len(falhas)} falharam (ver {falhas_path})" if falhas else "0 falharam"
    print(f"{len(linhas)} referências; {abertos} em acesso aberto; {com_pdf} com PDF direto; {aviso} -> {saida}")


if __name__ == "__main__":
    sys.exit(main())
