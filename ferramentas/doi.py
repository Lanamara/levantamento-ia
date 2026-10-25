"""Extrai DOIs de texto. Aceita parênteses balanceados (ex.: 10.1016/S0034-4257(01)00302-9)."""
import re

_DOI = re.compile(r"10\.\d{4,9}/[^\s|\]<>*\"']+")


def limpar(doi):
    doi = doi.rstrip(".,;:")
    # Tira ")" final que não fecha nenhum "(" do próprio DOI (vem do markdown ou do texto).
    while doi.endswith(")") and doi.count(")") > doi.count("("):
        doi = doi[:-1].rstrip(".,;:")
    return doi


def achar(texto):
    """Primeiro DOI do texto, já limpo, ou None."""
    m = _DOI.search(texto)
    return limpar(m.group(0)) if m else None
