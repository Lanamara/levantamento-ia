"""Extrai o texto de um PDF para um .txt (para o agente ler sem abrir o PDF)."""
import sys
from pypdf import PdfReader
r = PdfReader(sys.argv[1])
texto = "\n\n".join(f"[página {i+1}]\n{p.extract_text() or ''}" for i, p in enumerate(r.pages))
open(sys.argv[2], "w", encoding="utf-8").write(texto)
print(len(r.pages), "páginas,", len(texto) // 4, "tokens (aprox.)")
