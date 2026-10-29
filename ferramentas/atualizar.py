"""Procura trabalhos novos de cada frente no OpenAlex e grava as novidades.

Uso: python atualizar.py <pasta-do-projeto> [--email E] [--api-key K] [--qualis planilha.csv]

Lê <pasta>/consultas.json:

    {
      "desde": "2026-10-29",                 # data do levantamento inicial
      "tipos": "article|review|data-paper",  # tipos de trabalho do OpenAlex
      "janela_dias": 60,                      # sobreposição com a busca anterior
      "frentes": {"1-hiperespectral": "(PRISMA OR EnMAP) AND biomass", ...}
    }

Para cada frente, consulta /works com search.title_and_abstract e o filtro
from_publication_date. Como o filtro por data de entrada na base é pago,
cada busca começa `janela_dias` antes da anterior, para pegar o que entrou no
OpenAlex com atraso; os repetidos são descartados. Ficam de fora os DOIs que já
estão no referencias.bib, na sua lista (minhas_referencias.csv) e nas
novidades anteriores.

Grava (sem nunca alterar o levantamento principal):
- <pasta>/novidades.csv  todas as novidades, com a data de cada busca;
- <pasta>/NOVIDADES.md   a mesma lista, da busca mais recente para a mais antiga;
- <pasta>/atualizacao.json  a data da última busca.

As novidades são candidatas encontradas por busca automática: leia antes de
incluir no levantamento. O indicador da revista segue as regras de revistas.py.
"""
import argparse
import csv
import datetime
import json
import re
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import doi as doilib  # noqa: E402
import revistas  # noqa: E402
from conferir_lista import dois_citados  # noqa: E402
from projeto import barrar_exemplo, opcao_exemplo  # noqa: E402

CAMPOS = ["data_busca", "frente", "doi", "ano", "data_publicacao", "primeiro_autor", "titulo",
          "revista", "citacoes"] + revistas.CAMPOS
POR_PAGINA = 100  # máximo do OpenAlex; a 2.ª página com cursor exige chave


def ler_consultas(pasta):
    cfg = json.loads((Path(pasta) / "consultas.json").read_text(encoding="utf-8"))
    if not cfg.get("frentes"):
        raise ValueError("consultas.json sem a chave 'frentes'")
    return cfg


def data_inicio(cfg, pasta, hoje, desde=""):
    """Data inicial da busca: --desde, ou a última busca menos a janela, nunca antes de 'desde'."""
    if desde:
        return desde
    base = cfg.get("desde") or hoje.isoformat()
    estado = Path(pasta) / "atualizacao.json"
    if estado.exists():
        ultima = json.loads(estado.read_text(encoding="utf-8")).get("ultima_busca")
        if ultima:
            inicio = (datetime.date.fromisoformat(ultima)
                      - datetime.timedelta(days=int(cfg.get("janela_dias", 60)))).isoformat()
            return max(inicio, base)
    return base


def url_busca(consulta, inicio, tipos):
    filtro = f"from_publication_date:{inicio}"
    if tipos:
        filtro += f",type:{tipos}"
    return ("https://api.openalex.org/works?"
            + urllib.parse.urlencode({"search.title_and_abstract": consulta,
                                      "filter": filtro, "per_page": POR_PAGINA}))


def dois_conhecidos(pasta):
    pasta = Path(pasta)
    saida = set()
    bib = pasta / "referencias.bib"
    if bib.exists():
        saida |= {d.strip().lower() for d in
                  re.findall(r"DOI\s*=\s*\{([^}]+)\}", bib.read_text(encoding="utf-8"), re.I)}
    saida |= dois_citados(pasta)
    saida |= {r["doi"].lower() for r in ler_novidades(pasta) if r.get("doi")}
    return saida


def ler_novidades(pasta):
    caminho = Path(pasta) / "novidades.csv"
    if not caminho.exists():
        return []
    with open(caminho, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def doi_do_work(w):
    bruto = (w.get("doi") or "").replace("https://doi.org/", "")
    return doilib.limpar(bruto).lower() if bruto else ""


def linha_do_work(w, frente, hoje, fontes, qualis):
    autores = w.get("authorships") or []
    rev = revistas.do_work(w, fontes, qualis)
    return {
        **{c: rev.get(c, "") for c in revistas.CAMPOS},
        "data_busca": hoje.isoformat(), "frente": frente, "doi": doi_do_work(w),
        "ano": w.get("publication_year") or "", "data_publicacao": w.get("publication_date") or "",
        "primeiro_autor": autores[0]["author"]["display_name"] if autores else "",
        "titulo": w.get("title") or "", "revista": rev.get("revista", ""),
        "citacoes": w.get("cited_by_count") or 0,
    }


def buscar(cfg, inicio, hoje, conhecidos, fontes, qualis, get=revistas.get_json):
    """(novas linhas, avisos). Um DOI encontrado em duas frentes fica na primeira."""
    novas, avisos, vistos = [], [], set(conhecidos)
    for frente, consulta in cfg["frentes"].items():
        try:
            dados = get(url_busca(consulta, inicio, cfg.get("tipos", "article|review|data-paper")),
                        fontes.email, fontes.api_key)
        except Exception as e:
            avisos.append(f"ERRO {frente}: {type(e).__name__}: {e}")
            continue
        total = (dados.get("meta") or {}).get("count") or 0
        if total > POR_PAGINA:
            avisos.append(f"AMPLA {frente}: {total} resultados; só os {POR_PAGINA} mais relevantes "
                          "foram vistos. Estreite a consulta em consultas.json.")
        n = 0
        for w in dados.get("results") or []:
            d = doi_do_work(w)
            if not d or d in vistos:
                continue
            vistos.add(d)
            novas.append(linha_do_work(w, frente, hoje, fontes, qualis))
            n += 1
        print(f"{frente}: {total} resultados desde {inicio}, {n} novos", flush=True)
    return novas, avisos


def gravar(pasta, todas, hoje, avancar=True):
    pasta = Path(pasta)
    with open(pasta / "novidades.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS, extrasaction="ignore")
        w.writeheader()
        w.writerows(todas)
    md = ["# Novidades", "",
          "Trabalhos encontrados pela atualização automática (OpenAlex), que ainda não estão no "
          "levantamento nem na sua lista de referências. São candidatos: leia antes de incluir. "
          "⚠ conferir = a revista não está no DOAJ, no CWTS Core nem na planilha do Qualis "
          "(não quer dizer predatória); ⛔ = artigo retratado.", ""]
    for data in sorted({r["data_busca"] for r in todas}, reverse=True):
        grupo = [r for r in todas if r["data_busca"] == data]
        md += [f"## Busca de {data} ({len(grupo)})", "",
               "| Frente | Ano | Referência | Revista | Indicadores |", "|---|---:|---|---|---|"]
        for r in sorted(grupo, key=lambda r: (r["frente"], str(r["ano"]))):
            sel = []
            if r.get("sinal_revista") == "retratado":
                sel.append("⛔ retratado")
            if r.get("doaj") == "sim":
                sel.append("DOAJ")
            if r.get("cwts_core") == "sim":
                sel.append("CWTS Core")
            if r.get("qualis"):
                sel.append(f"Qualis {r['qualis']}")
            if r.get("sinal_revista") == "conferir":
                sel.append("⚠ conferir")
            titulo = str(r["titulo"]).replace("|", "\\|")
            md.append(f"| {r['frente']} | {r['ano']} | {r['primeiro_autor']}. "
                      f"[{titulo}](https://doi.org/{r['doi']}) | "
                      f"{str(r['revista']).replace('|', '/')} | {' · '.join(sel)} |")
        md.append("")
    if not todas:
        md.append("Nenhum trabalho novo até agora.")
    (pasta / "NOVIDADES.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    if not avancar:  # houve erro: a próxima busca começa da mesma data
        return
    (pasta / "atualizacao.json").write_text(
        json.dumps({"ultima_busca": hoje.isoformat()}, indent=1) + "\n", encoding="utf-8")


def main(argv=None, hoje=None):
    ap = argparse.ArgumentParser(description="Procura trabalhos novos de cada frente no OpenAlex.")
    ap.add_argument("pasta", help="pasta do projeto (com consultas.json)")
    ap.add_argument("--desde", default="", help="força a data inicial (AAAA-MM-DD)")
    ap.add_argument("--email", default="", help="e-mail para o mailto do OpenAlex (opcional)")
    ap.add_argument("--api-key", default="", help="chave gratuita do OpenAlex (ou OPENALEX_API_KEY)")
    ap.add_argument("--qualis", default="", help="planilha do Qualis exportada da Sucupira (opcional)")
    opcao_exemplo(ap)
    a = ap.parse_args(argv)
    barrar_exemplo(ap, a, a.pasta)
    hoje = hoje or datetime.date.today()
    cfg = ler_consultas(a.pasta)
    inicio = data_inicio(cfg, a.pasta, hoje, a.desde)
    fontes = revistas.Fontes(a.email, a.api_key)
    novas, avisos = buscar(cfg, inicio, hoje, dois_conhecidos(a.pasta), fontes,
                           revistas.ler_qualis(a.qualis))
    todas = ler_novidades(a.pasta) + novas
    erro = any(x.startswith("ERRO") for x in avisos)
    gravar(a.pasta, todas, hoje, avancar=not erro)
    for aviso in avisos:
        print(aviso, flush=True)
    print(f"{len(novas)} trabalhos novos nesta busca; {len(todas)} no total -> "
          f"{Path(a.pasta) / 'NOVIDADES.md'}")
    return 1 if erro else 0


if __name__ == "__main__":
    sys.exit(main())
