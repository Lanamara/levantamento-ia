"""Indicadores da revista: fatos conferíveis, nunca um veredito de "predatória".

Não existe lista aberta e oficial de revistas predatórias: a lista de Beall saiu
do ar em 2017 e o Cabells Predatory Reports é pago. Por isso este módulo só
reúne o que dá para conferir na fonte:

- DOAJ e lista CWTS Core: campos `is_in_doaj` e `is_core` do source no OpenAlex;
- editora, ISSN-L, preço de lista da APC (USD) e índice h da revista: OpenAlex;
- artigo retratado: campo `is_retracted` do work no OpenAlex (Retraction Watch);
- Qualis CAPES 2021-2024: só se a pessoa der a planilha exportada da Plataforma
  Sucupira (`--qualis`), cruzada pelo ISSN.

A coluna `sinal_revista` resume esses fatos:
  "retratado"  o artigo foi retratado;
  "ok"         a revista está em pelo menos uma lista (DOAJ, CWTS Core ou Qualis);
  "conferir"   a revista não está em nenhuma delas: confira à mão (Cabells, se a
               instituição assinar; site da revista; Think. Check. Submit.);
  ""           sem dados da revista no OpenAlex.
"conferir" não quer dizer predatória: muitas revistas regionais legítimas não
estão no DOAJ nem no CWTS Core.
"""
import csv
import json
import os
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

CAMPOS = ["issn_l", "editora", "doaj", "cwts_core", "qualis", "apc_usd",
          "h_index_revista", "retratado", "sinal_revista"]

ORDEM_QUALIS = ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C"]


def chave_api(valor=""):
    """Chave gratuita do OpenAlex: argumento ou variável OPENALEX_API_KEY (opcional)."""
    return (valor or os.environ.get("OPENALEX_API_KEY", "")).strip()


def parametros(email="", api_key=""):
    p = {}
    if email:
        p["mailto"] = email
    if api_key:
        p["api_key"] = api_key
    return p


def get_json(url, email="", api_key="", tentativas=2):
    p = parametros(email, api_key)
    if p:
        url += ("&" if "?" in url else "?") + urllib.parse.urlencode(p)
    ultimo = None
    for tentativa in range(tentativas):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "levantamento-ia/1.0"})
            return json.loads(urllib.request.urlopen(req, timeout=25).read())
        except Exception as e:  # rede instável: tenta de novo uma vez
            ultimo = e
            if tentativa + 1 < tentativas:
                time.sleep(2)
    raise ultimo


def issn_normal(issn):
    """'2317-1782' e '23171782' viram '2317-1782'; o resto vira ''."""
    s = re.sub(r"[^0-9Xx]", "", str(issn or "")).upper()
    return f"{s[:4]}-{s[4:]}" if len(s) == 8 else ""


def melhor_estrato(a, b):
    """O estrato mais alto entre dois (A1 > A2 > ... > C)."""
    def pos(e):
        return ORDEM_QUALIS.index(e) if e in ORDEM_QUALIS else len(ORDEM_QUALIS)
    return a if pos(a) <= pos(b) else b


def ler_qualis(caminho):
    """{issn: estrato} a partir da planilha do Qualis exportada da Sucupira.

    Aceita CSV com ';', ',' ou tabulação, com colunas cujo nome contém "ISSN" e
    "Estrato" (é o que a Sucupira exporta). Se uma revista aparecer mais de uma
    vez, fica o estrato mais alto. Caminho vazio devolve {}.
    """
    if not caminho:
        return {}
    texto = Path(caminho).read_text(encoding="utf-8-sig", errors="replace")
    try:
        dialeto = csv.Sniffer().sniff(texto[:4096], delimiters=";,\t")
    except csv.Error:
        dialeto = csv.excel
    leitor = csv.DictReader(texto.splitlines(), dialect=dialeto)
    nomes = leitor.fieldnames or []
    col_issn = next((c for c in nomes if "issn" in c.lower()), None)
    col_estrato = next((c for c in nomes if "estrato" in c.lower()), None)
    if not col_issn or not col_estrato:
        raise ValueError(f"{caminho}: preciso das colunas ISSN e Estrato; achei {nomes}")
    saida = {}
    for linha in leitor:
        issn = issn_normal(linha.get(col_issn))
        estrato = (linha.get(col_estrato) or "").strip().upper()
        if issn and estrato:
            saida[issn] = melhor_estrato(saida.get(issn, estrato), estrato)
    return saida


def indicadores(fonte, qualis=None, retratado=False):
    """Campos de CAMPOS a partir do source completo do OpenAlex (ou {})."""
    fonte = fonte or {}
    qualis = qualis or {}
    issns = [issn_normal(i) for i in (fonte.get("issn") or [])] + [issn_normal(fonte.get("issn_l"))]
    estrato = ""
    for i in filter(None, issns):
        if i in qualis:
            estrato = melhor_estrato(estrato or qualis[i], qualis[i])
    stats = fonte.get("summary_stats") or {}
    doaj = fonte.get("is_in_doaj")
    core = fonte.get("is_core")
    if retratado:
        sinal = "retratado"
    elif not fonte:
        sinal = ""
    elif doaj or core or estrato:
        sinal = "ok"
    else:
        sinal = "conferir"
    sim_nao = {True: "sim", False: "não", None: ""}
    return {
        "issn_l": fonte.get("issn_l") or "",
        "editora": fonte.get("host_organization_name") or "",
        "doaj": sim_nao.get(doaj, ""),
        "cwts_core": sim_nao.get(core, ""),
        "qualis": estrato,
        "apc_usd": fonte.get("apc_usd") if fonte.get("apc_usd") is not None else "",
        "h_index_revista": stats.get("h_index") if stats.get("h_index") is not None else "",
        "retratado": "sim" if retratado else "não",
        "sinal_revista": sinal,
    }


class Fontes:
    """Busca cada revista uma vez só no OpenAlex (/sources/{id})."""

    def __init__(self, email="", api_key=""):
        self.email, self.api_key, self.cache = email, chave_api(api_key), {}

    def __call__(self, source_id):
        if not source_id:
            return {}
        sid = str(source_id).rstrip("/").rsplit("/", 1)[-1]
        if sid not in self.cache:
            try:
                self.cache[sid] = get_json("https://api.openalex.org/sources/" + sid,
                                           self.email, self.api_key)
            except Exception:
                self.cache[sid] = {}
        return self.cache[sid]


def do_work(work, fontes, qualis=None):
    """Revista oficial + indicadores de um work do OpenAlex."""
    src = ((work.get("primary_location") or {}).get("source") or {})
    fonte = fontes(src.get("id")) if src.get("id") else {}
    saida = indicadores(fonte, qualis, bool(work.get("is_retracted")))
    saida["revista"] = fonte.get("display_name") or src.get("display_name") or ""
    return saida
