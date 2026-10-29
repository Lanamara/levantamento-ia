"""Confere uma lista de referências sua (ABNT, APA...) contra o registro oficial.

Uso: python conferir_lista.py <minhas_referencias.txt> <pasta-do-projeto> [--email E] [--api-key K]

Uma referência por parágrafo (separe com linha em branco) ou, se não houver
linha em branco, uma por linha. Para cada uma:

- com DOI: consulta o Crossref e compara título, ano, volume e páginas com o
  que você escreveu. Estados: OK, CONFERIR (algo difere; veja a observação),
  TITULO-DIFERE, NAO-EXISTE (404 no Crossref) ou ERRO (rede);
- sem DOI: procura no OpenAlex e só sugere um DOI se o título do registro
  aparecer na sua referência e o ano bater (estado SUGERIDO). Se não, SEM-DOI.
  Uma sugestão nunca é aplicada sozinha: confira antes de usar.

Grava <pasta>/minhas_referencias.csv e <pasta>/MINHAS_REFERENCIAS.md. O
painel.py usa o CSV para marcar, na tabela, os artigos que você já cita.
"""
import argparse
import csv
import html
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import doi as doilib  # noqa: E402
import revistas  # noqa: E402
from projeto import barrar_exemplo, opcao_exemplo  # noqa: E402

CAMPOS = ["n", "estado", "doi", "observacao", "titulo_registro", "revista_registro",
          "ano_registro", "volume_registro", "paginas_registro", "referencia"]
CABECALHOS = {"referencias", "referencias bibliograficas", "bibliografia", "references"}


def sem_acento(t):
    return "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn")


def normal(t):
    t = re.sub(r"<[^>]+>", " ", html.unescape(t or ""))
    t = sem_acento(t).lower()
    t = re.sub(r"https?://\S+", " ", t)
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def separar(texto):
    """Lista de referências: por parágrafo; sem linha em branco, por linha."""
    texto = texto.replace("\r\n", "\n")
    blocos = re.split(r"\n\s*\n", texto) if re.search(r"\n\s*\n", texto) else texto.split("\n")
    saida = []
    for b in blocos:
        b = re.sub(r"\s+", " ", b).strip()
        if not b or normal(b) in CABECALHOS or len(b) < 25:
            continue
        saida.append(b)
    return saida


def titulo_na_referencia(titulo, referencia):
    """Similaridade (0 a 1) entre o título do registro e o melhor trecho da referência."""
    t, r = normal(titulo).split(), normal(referencia).split()
    if not t or not r:
        return 0.0
    alvo = " ".join(t)
    if alvo in " ".join(r):
        return 1.0
    n, melhor = len(t), 0.0
    for i in range(max(1, len(r) - n + 1)):
        janela = " ".join(r[i:i + n])
        melhor = max(melhor, SequenceMatcher(None, alvo, janela).ratio())
    return melhor


def anos(referencia):
    """Anos citados na referência, sem contar os que aparecem em links e DOIs."""
    texto = re.sub(r"https?://\S+|\b10\.\d{4,9}/\S+", " ", referencia)
    return set(re.findall(r"\b(19\d{2}|20\d{2})\b", texto))


def volume(referencia):
    m = re.search(r"\b(?:v\.|vol\.?|volume)\s*(\d+)", referencia, re.I)
    return m.group(1) if m else ""


def primeira_pagina(texto):
    m = re.search(r"\d+", texto or "")
    return m.group(0) if m else ""


def paginas(referencia):
    m = re.search(r"\b(?:p\.|pp\.)\s*(\d[\d\s–—-]*)", referencia)
    return m.group(1).strip() if m else ""


def registro_crossref(msg):
    """Campos que interessam do 'message' do Crossref."""
    data = (msg.get("issued") or {}).get("date-parts") or [[None]]
    # Ano impresso e ano on-line podem diferir (publicação antecipada); aceitamos os dois.
    todos = set()
    for chave in ("issued", "published-print", "published-online"):
        partes = (msg.get(chave) or {}).get("date-parts") or [[None]]
        if partes and partes[0] and partes[0][0]:
            todos.add(str(partes[0][0]))
    return {
        "anos_registro": todos,
        "titulo_registro": (msg.get("title") or [""])[0],
        "revista_registro": (msg.get("container-title") or [""])[0],
        "ano_registro": str(data[0][0] or ""),
        "volume_registro": str(msg.get("volume") or ""),
        "paginas_registro": str(msg.get("page") or msg.get("article-number") or ""),
    }


def comparar(referencia, reg):
    """(estado, observação) comparando a referência com o registro oficial."""
    sim = titulo_na_referencia(reg["titulo_registro"], referencia)
    if sim < 0.6:
        return "TITULO-DIFERE", f"título no registro: {reg['titulo_registro']}"
    obs = []
    if sim < 0.9:
        obs.append(f"título parecido ({sim:.2f}); registro: {reg['titulo_registro']}")
    anos_reg = reg.get("anos_registro") or ({reg["ano_registro"]} if reg["ano_registro"] else set())
    if anos_reg and anos(referencia) and not (anos_reg & anos(referencia)):
        obs.append(f"ano no registro: {'/'.join(sorted(anos_reg))}")
    v = volume(referencia)
    if v and reg["volume_registro"] and v != reg["volume_registro"]:
        obs.append(f"volume: você escreveu {v}, registro {reg['volume_registro']}")
    p = primeira_pagina(paginas(referencia))
    pr = primeira_pagina(reg["paginas_registro"])
    if p and pr and p != pr:
        obs.append(f"páginas: você escreveu {paginas(referencia)}, registro {reg['paginas_registro']}")
    return ("CONFERIR" if obs else "OK"), "; ".join(obs)


def consultar_crossref(doi):
    """(estado, message ou None). Tenta 3 vezes antes de ERRO."""
    for tentativa in range(3):
        try:
            r = urllib.request.urlopen(urllib.request.Request(
                "https://api.crossref.org/works/" + urllib.parse.quote(doi),
                headers={"User-Agent": "levantamento-ia/1.0"}), timeout=20)
            return "ok", json.loads(r.read())["message"]
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return "NAO-EXISTE", None
        except Exception:
            pass
        time.sleep(2 * (tentativa + 1))
    return "ERRO", None


def busca_openalex(referencia, email="", api_key=""):
    """Até 5 candidatos do OpenAlex para uma referência sem DOI."""
    termos = " ".join(w for w in normal(referencia).split() if len(w) > 2)[:300]
    url = "https://api.openalex.org/works?per_page=5&search=" + urllib.parse.quote(termos)
    try:
        return revistas.get_json(url, email, api_key).get("results") or []
    except Exception:
        return []


def sugerir(referencia, candidatos):
    """Primeiro candidato cujo título aparece na referência e cujo ano bate, ou None."""
    for w in candidatos:
        titulo, ano, doi = w.get("title") or "", str(w.get("publication_year") or ""), w.get("doi") or ""
        if not doi or len(normal(titulo).split()) < 4:
            continue
        if titulo_na_referencia(titulo, referencia) >= 0.9 and (not anos(referencia) or ano in anos(referencia)):
            return {"doi": doilib.limpar(doi.replace("https://doi.org/", "")), "titulo_registro": titulo,
                    "revista_registro": ((w.get("primary_location") or {}).get("source") or {}).get("display_name") or "",
                    "ano_registro": ano, "volume_registro": str((w.get("biblio") or {}).get("volume") or ""),
                    "paginas_registro": str((w.get("biblio") or {}).get("first_page") or "")}
    return None


def conferir(referencias, email="", api_key="", crossref=consultar_crossref, openalex=busca_openalex):
    linhas = []
    for n, ref in enumerate(referencias, 1):
        linha = {c: "" for c in CAMPOS}
        linha.update(n=n, referencia=ref)
        doi = doilib.achar(ref)
        if doi:
            linha["doi"] = doi
            estado, msg = crossref(doi)
            if msg is None:
                linha["estado"] = estado
            else:
                reg = registro_crossref(msg)
                linha.update({k: v for k, v in reg.items() if k in CAMPOS})
                linha["estado"], linha["observacao"] = comparar(ref, reg)
        else:
            sug = sugerir(ref, openalex(ref, email, api_key))
            if sug:
                linha.update(sug)
                linha["estado"] = "SUGERIDO"
                linha["observacao"] = "DOI sugerido pelo OpenAlex: confira antes de usar"
            else:
                linha["estado"] = "SEM-DOI"
        print(f"{linha['estado']}\t{n}\t{linha['doi']}\t{ref[:70]}", flush=True)
        linhas.append(linha)
        time.sleep(0.2)
    return linhas


def gravar(linhas, pasta):
    pasta = Path(pasta)
    pasta.mkdir(parents=True, exist_ok=True)
    with open(pasta / "minhas_referencias.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        w.writeheader()
        w.writerows(linhas)
    cont = {}
    for l in linhas:
        cont[l["estado"]] = cont.get(l["estado"], 0) + 1
    md = ["# Conferência das minhas referências", "",
          "Registro oficial: Crossref (com DOI) ou OpenAlex (sugestão, sem DOI). "
          "Nenhuma referência foi alterada: decida você o que corrigir.", "",
          "**Resumo:** " + ", ".join(f"{k}: {v}" for k, v in sorted(cont.items())), "",
          "| # | Estado | DOI | Observação | Referência |", "|---:|---|---|---|---|"]
    ordem = {"NAO-EXISTE": 0, "TITULO-DIFERE": 1, "ERRO": 2, "CONFERIR": 3, "SUGERIDO": 4, "SEM-DOI": 5, "OK": 6}
    for l in sorted(linhas, key=lambda l: (ordem.get(l["estado"], 9), int(l["n"]))):
        def cel(t):
            return str(t).replace("|", "\\|")
        doi = f"[{l['doi']}](https://doi.org/{l['doi']})" if l["doi"] else ""
        md.append(f"| {l['n']} | {l['estado']} | {doi} | {cel(l['observacao'])} | {cel(l['referencia'][:160])} |")
    (pasta / "MINHAS_REFERENCIAS.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    return cont


def dois_citados(pasta):
    """DOIs (minúsculos) que a pessoa já cita, a partir de minhas_referencias.csv."""
    caminho = Path(pasta) / "minhas_referencias.csv"
    if not caminho.exists():
        return set()
    with open(caminho, encoding="utf-8-sig") as f:
        return {r["doi"].lower() for r in csv.DictReader(f)
                if r.get("doi") and r.get("estado") in ("OK", "CONFERIR", "SUGERIDO")}


def main(argv=None):
    ap = argparse.ArgumentParser(description="Confere sua lista de referências no Crossref e no OpenAlex.")
    ap.add_argument("lista", help="arquivo de texto com as referências")
    ap.add_argument("pasta", help="pasta do projeto (onde gravar o resultado)")
    ap.add_argument("--email", default="", help="e-mail para o mailto do OpenAlex (opcional)")
    ap.add_argument("--api-key", default="", help="chave gratuita do OpenAlex (ou OPENALEX_API_KEY)")
    opcao_exemplo(ap)
    a = ap.parse_args(argv)
    barrar_exemplo(ap, a, a.pasta)
    refs = separar(Path(a.lista).read_text(encoding="utf-8-sig"))
    linhas = conferir(refs, a.email, revistas.chave_api(a.api_key))
    cont = gravar(linhas, a.pasta)
    print("\n" + ", ".join(f"{k}: {v}" for k, v in sorted(cont.items()))
          + f" -> {Path(a.pasta) / 'MINHAS_REFERENCIAS.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
