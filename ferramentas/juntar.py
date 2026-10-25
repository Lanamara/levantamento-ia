"""Junta as tabelas das frentes num só REFERENCIAS.md (sem repetidos) e gera o .bib.

Uso: python juntar.py <pasta-das-frentes> <pasta-de-saida> "<título do tema>"

Lê <frente>/RELATORIO.md, pega o primeiro bloco de tabela, junta os DOIs
repetidos entre frentes (fica a linha mais completa) e copia o texto que vem
depois da tabela. O .bib vem do próprio doi.org (Accept: application/x-bibtex).
"""
import html
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import doi as doilib  # noqa: E402


def bibtex(doi):
    req = urllib.request.Request("https://doi.org/" + doi, headers={
        "Accept": "application/x-bibtex; charset=utf-8",
        "User-Agent": "levantamento-ia/1.0"})
    try:
        return html.unescape(urllib.request.urlopen(req, timeout=25).read().decode("utf-8").strip())
    except Exception as e:
        return f"% falhou: {doi} ({type(e).__name__})"


def primeira_tabela(linhas):
    """(índice do cabeçalho, índice da linha depois da tabela) do primeiro bloco contíguo."""
    ini = next((i for i, l in enumerate(linhas) if l.startswith("|")), None)
    if ini is None:
        return None, None
    fim = ini
    while fim < len(linhas) and linhas[fim].startswith("|"):
        fim += 1
    return ini, fim


def preenchimento(linha):
    return sum(len(c.strip()) for c in linha.split("|"))


def main():
    frentes, saida, tema = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
    saida.mkdir(parents=True, exist_ok=True)
    blocos, melhor = [], {}  # melhor[doi] = (preenchimento, índice do bloco, posição)
    for rel in sorted(frentes.glob("*/RELATORIO.md")):
        linhas = rel.read_text(encoding="utf-8").splitlines()
        ini, fim = primeira_tabela(linhas)
        if ini is None or fim - ini < 3:
            continue
        corpo = [l.replace("**†**", "").replace("**‡**", "") for l in linhas[ini + 2:fim]]
        b = len(blocos)
        for pos, l in enumerate(corpo):
            d = doilib.achar(l)
            if d:
                d = d.lower()
                if d not in melhor or preenchimento(l) > melhor[d][0]:
                    melhor[d] = (preenchimento(l), b, pos)
        resto = [l for l in linhas[fim:] if l.strip() and not l.startswith(">")]
        blocos.append((rel.parent.name, linhas[ini], linhas[ini + 1], corpo, resto))

    texto, dois = [f"# Referências: {tema}", ""], []
    for b, (nome, cab, sep, corpo, resto) in enumerate(blocos):
        manter = []
        for pos, l in enumerate(corpo):
            d = doilib.achar(l)
            if d and melhor[d.lower()][1:] != (b, pos):
                continue  # a versão mais completa desta referência está em outra linha
            if d:
                dois.append(d.lower())
            manter.append(l)
        texto += [f"## {nome}", "", cab, sep, *manter, "", *resto, ""]
    (saida / "REFERENCIAS.md").write_text("\n".join(texto), encoding="utf-8")
    (saida / "referencias.bib").write_text("\n\n".join(bibtex(d) for d in dois) + "\n", encoding="utf-8")
    print(f"{len(dois)} DOIs únicos -> {saida}")


if __name__ == "__main__":
    main()
