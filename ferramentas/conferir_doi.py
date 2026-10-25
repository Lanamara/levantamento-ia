"""Confere os DOIs citados nos RELATORIO.md: existe no Crossref? o título bate?

Uso: python conferir_doi.py <pasta-das-frentes>

Saída, uma linha por DOI: OK (título igual), CONFERIR (parecido, ver à mão),
TITULO-DIFERE, NAO-EXISTE (o Crossref respondeu 404) ou ERRO (rede, depois de
3 tentativas). Grava também <pasta>/../verificacao.csv, que o site usa.
"""
import csv
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import doi as doilib  # noqa: E402


def normal(t):
    t = re.sub(r"<[^>]+>", "", html.unescape(t or ""))
    t = re.sub(r"[*_]", "", t)
    return re.sub(r"\s+", " ", t).strip().lower()


def consultar(doi, titulo):
    """(estado, similaridade, título no Crossref). Tenta 3 vezes antes de dizer ERRO."""
    for tentativa in range(3):
        try:
            r = urllib.request.urlopen(urllib.request.Request(
                "https://api.crossref.org/works/" + urllib.parse.quote(doi),
                headers={"User-Agent": "levantamento-ia/1.0"}), timeout=20)
            t = (json.loads(r.read())["message"].get("title") or [""])[0]
            sim = SequenceMatcher(None, normal(t), normal(titulo)).ratio()
            return ("OK" if sim >= 0.85 else "CONFERIR" if sim >= 0.6 else "TITULO-DIFERE"), sim, t
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return "NAO-EXISTE", 0.0, ""
        except Exception:
            pass
        time.sleep(2 * (tentativa + 1))
    return "ERRO", 0.0, ""


def main():
    raiz = Path(sys.argv[1])
    contagem, linhas = Counter(), []
    for rel in sorted(raiz.glob("*/RELATORIO.md")):
        for linha in rel.read_text(encoding="utf-8").splitlines():
            if not linha.lstrip().startswith("|"):
                continue
            doi = doilib.achar(linha)
            if not doi:
                continue
            celulas = [c.strip() for c in linha.split("|")]
            titulo = celulas[2] if len(celulas) > 3 else ""
            estado, sim, t = consultar(doi, titulo)
            print(f"{estado}\t{rel.parent.name}\t{doi}\t{sim:.2f}\t{normal(t)[:70]}")
            linhas.append({"frente": rel.parent.name, "doi": doi, "estado": estado,
                           "similaridade": f"{sim:.2f}"})
            contagem[estado] += 1
    with open(raiz.parent / "verificacao.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["frente", "doi", "estado", "similaridade"])
        w.writeheader()
        w.writerows(linhas)
    print("\n" + ", ".join(f"{k}: {v}" for k, v in sorted(contagem.items())))


if __name__ == "__main__":
    main()
