"""Protege a pasta exemplo/: os scripts que gravam não mexem nela sem --exemplo.

O exemplo é o levantamento de demonstração do repositório. A IA que conduz o
levantamento de outra pessoa pode confundi-lo com o trabalho dela; esta
barreira impede que um comando apontado para exemplo/ sobrescreva o exemplo.
"""
from pathlib import Path

EXEMPLO = Path(__file__).resolve().parent.parent / "exemplo"


def no_exemplo(*caminhos):
    """True se algum caminho é exemplo/ ou fica dentro dele."""
    for caminho in caminhos:
        if not caminho:
            continue
        p = Path(caminho).resolve()
        if p == EXEMPLO or EXEMPLO in p.parents:
            return True
    return False


def opcao_exemplo(ap):
    ap.add_argument("--exemplo", action="store_true",
                    help="permite gravar em exemplo/ (só para quem mantém o repositório)")


def barrar_exemplo(ap, a, *caminhos):
    """Encerra com erro (código 2) se o comando grava em exemplo/ sem --exemplo."""
    if no_exemplo(*caminhos) and not a.exemplo:
        ap.error("exemplo/ é o levantamento de demonstração do repositório, não o seu. "
                 "O seu levantamento vai em projetos/<tema>/. "
                 "Para atualizar o exemplo de propósito, use --exemplo.")
