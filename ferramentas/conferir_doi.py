"""Confere os DOIs citados nos RELATORIO.md: existe no Crossref? o título bate?

Uso: python conferir_doi.py <pasta-das-frentes>

Saída, uma linha por DOI: OK (título igual), CONFERIR (parecido, ver à mão),
TITULO-DIFERE ou NAO-EXISTE. Termina com a contagem de cada caso.
"""
import html
import json
import re
import sys
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


def main():
    raiz = Path(sys.argv[1])
    contagem = Counter()
    for rel in sorted(raiz.glob("*/RELATORIO.md")):
        for linha in rel.read_text(encoding="utf-8").splitlines():
            if not linha.startswith("|"):
                continue
            doi = doilib.achar(linha)
            if not doi:
                continue
            celulas = [c.strip() for c in linha.split("|")]
            titulo = celulas[2] if len(celulas) > 3 else ""
            try:
                r = urllib.request.urlopen(urllib.request.Request(
                    "https://api.crossref.org/works/" + urllib.parse.quote(doi),
                    headers={"User-Agent": "levantamento-ia/1.0"}), timeout=20)
                d = json.loads(r.read())["message"]
                t = (d.get("title") or [""])[0]
                sim = SequenceMatcher(None, normal(t), normal(titulo)).ratio()
                estado = "OK" if sim >= 0.85 else "CONFERIR" if sim >= 0.6 else "TITULO-DIFERE"
                print(f"{estado}\t{rel.parent.name}\t{doi}\t{sim:.2f}\t{normal(t)[:70]}")
            except Exception as e:
                estado = "NAO-EXISTE"
                print(f"{estado}\t{rel.parent.name}\t{doi}\t{type(e).__name__}")
            contagem[estado] += 1
    print("\n" + ", ".join(f"{k}: {v}" for k, v in sorted(contagem.items())))


if __name__ == "__main__":
    main()
