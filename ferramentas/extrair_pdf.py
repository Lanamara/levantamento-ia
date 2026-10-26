"""Extrai o texto de um PDF para um .txt (para o agente ler sem abrir o PDF)."""
import argparse
import sys
from pathlib import Path

from pypdf import PdfReader


def main(argv=None):
    ap = argparse.ArgumentParser(description="Extrai o texto de um PDF para um .txt.")
    ap.add_argument("pdf", help="arquivo PDF")
    ap.add_argument("saida", help="arquivo .txt de saída")
    a = ap.parse_args(argv)
    r = PdfReader(a.pdf)
    texto = "\n\n".join(f"[página {i + 1}]\n{p.extract_text() or ''}" for i, p in enumerate(r.pages))
    Path(a.saida).write_text(texto, encoding="utf-8")
    print(len(r.pages), "páginas,", len(texto) // 4, "tokens (aprox.)")


if __name__ == "__main__":
    sys.exit(main())
