"""Cienciometria das referências pelo OpenAlex (gratuito, sem conta).

Uso: python cienciometria.py <referencias.bib> <saida.csv> [seu-email]
       [--qualis planilha-sucupira.csv] [--api-key CHAVE]

Para cada DOI do .bib: ano, primeiro autor, revista, citações, FWCI (citações
normalizadas pela área e ano; 1 = média), percentil de citação, status de acesso
aberto e links do PDF aberto (do editor e de repositórios), quando existem.
DOI que falhar no OpenAlex continua no CSV principal com ano, primeiro autor e
título do .bib e as métricas vazias; ele também vai para <saida>-falhas.csv,
com as colunas doi e erro. Uma falha de rede é tentada de novo uma vez.

Indicadores da revista (ver revistas.py): ISSN-L, editora, DOAJ, CWTS Core,
Qualis (se --qualis), APC, índice h, retratação e sinal_revista (ok, conferir,
retratado). São fatos conferíveis, não um rótulo de "predatória".
A chave gratuita do OpenAlex é opcional (--api-key ou OPENALEX_API_KEY).
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
import revistas  # noqa: E402
from projeto import barrar_exemplo, opcao_exemplo  # noqa: E402

CAMPOS = ["doi", "ano", "primeiro_autor", "titulo", "revista", "citacoes", "fwci",
          "percentil", "acesso", "pdf", "pdf_alternativos"] + revistas.CAMPOS


def url_openalex(doi, email, api_key=""):
    url = "https://api.openalex.org/works/doi:" + urllib.parse.quote(doi)
    p = revistas.parametros(email, api_key)
    if p:
        url += "?" + urllib.parse.urlencode(p)
    return url


def _consultar_uma(doi, email, fontes=None, qualis=None):
    api_key = fontes.api_key if fontes else ""
    w = json.loads(urllib.request.urlopen(url_openalex(doi, email, api_key), timeout=25).read())
    autores = w.get("authorships") or []
    fonte = ((w.get("primary_location") or {}).get("source") or {})
    oa = w.get("open_access") or {}
    pct = (w.get("citation_normalized_percentile") or {}).get("value")
    rev = revistas.do_work(w, fontes, qualis) if fontes else {}
    return {
        **{c: rev.get(c, "") for c in revistas.CAMPOS},
        "doi": doi,
        "ano": w.get("publication_year"),
        "primeiro_autor": (autores[0]["author"]["display_name"] if autores else ""),
        "titulo": w.get("title") or "",
        "revista": rev.get("revista") or fonte.get("display_name") or "",
        "citacoes": w.get("cited_by_count"),
        "fwci": round(w["fwci"], 2) if w.get("fwci") is not None else "",
        "percentil": min(99, int(100 * pct)) if pct is not None else "",
        "acesso": oa.get("oa_status") or "",
        "pdf": (w.get("best_oa_location") or {}).get("pdf_url") or "",
        # Cópias em repositórios (universidades, PMC, HAL...): o editor às vezes bloqueia script.
        "pdf_alternativos": " ".join(dict.fromkeys(
            l["pdf_url"] for l in w.get("locations") or [] if l.get("pdf_url"))),
    }


def consulta(doi, email, fontes=None, qualis=None):
    """Tenta duas vezes: uma falha passageira não tira o artigo do CSV."""
    ultimo = None
    for tentativa in range(2):
        try:
            return _consultar_uma(doi, email, fontes, qualis)
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
    ap.add_argument("--qualis", default="", help="planilha do Qualis exportada da Sucupira (CSV com ISSN e Estrato)")
    ap.add_argument("--api-key", default="", help="chave gratuita do OpenAlex (ou OPENALEX_API_KEY)")
    opcao_exemplo(ap)
    a = ap.parse_args(argv)
    barrar_exemplo(ap, a, a.saida)
    saida = Path(a.saida)
    texto_bib = Path(a.bib).read_text(encoding="utf-8-sig")
    dois = re.findall(r"DOI\s*=\s*\{([^}]+)\}", texto_bib, re.I)
    meta = metadados_do_bib(texto_bib)
    qualis = revistas.ler_qualis(a.qualis)
    fontes = revistas.Fontes(a.email, a.api_key)
    linhas, falhas = [], []
    for i, doi in enumerate(dois, 1):
        if i == 1 or i % 10 == 0:
            print(f"OpenAlex {i}/{len(dois)}: {doi}", flush=True)
        try:
            linhas.append(consulta(doi, a.email, fontes, qualis))
        except Exception as e:
            falhas.append({"doi": doi, "erro": f"{type(e).__name__}: {e}"})
            dados = meta.get(doi.lower(), {})
            linhas.append({
                **{c: "" for c in revistas.CAMPOS},
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
    sinais = {s: sum(1 for r in linhas if r.get("sinal_revista") == s) for s in ("ok", "conferir", "retratado")}
    print(f"Revistas: {sinais['ok']} ok, {sinais['conferir']} a conferir, {sinais['retratado']} retratados")


if __name__ == "__main__":
    sys.exit(main())
