"""Gera um RELATORIO.html autocontido a partir de tabela.json e dos resumos.

Uso: python publicar.py <pasta-do-levantamento> [--saida RELATORIO.html]

O HTML abre com dois cliques, sem servidor e sem internet: a tabela tem busca,
filtro por acesso e ordenação, e cada resumo abre numa janela. É a camada
humana da entrega; o TABELA.md continua sendo a versão de texto, e o
tabela.json / cienciometria.csv são a camada de dados.
"""
import argparse
import csv
import datetime
import html
import json
import re
import sys
import urllib.parse
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import painel  # noqa: E402
from projeto import barrar_exemplo, opcao_exemplo  # noqa: E402

try:
    import markdown
except ImportError:  # pragma: no cover - só acontece se faltar a dependência
    markdown = None


def md_para_html(texto):
    """Markdown -> HTML, sem deixar HTML cru do modelo passar."""
    seguro = (texto or "").replace("&", "&amp;").replace("<", "&lt;")
    if markdown:
        try:
            corpo = markdown.markdown(seguro, extensions=["tables", "sane_lists"])
        except Exception:
            return "<pre>" + seguro + "</pre>"
        # Markdown permite links com esquemas perigosos; o resumo vem de um PDF,
        # então não dá para confiar cegamente no texto.
        return re.sub(r'\b(href|src)="(?:javascript|data|vbscript):[^"]*"',
                      r'\1="#"', corpo, flags=re.I)
    return "<pre>" + seguro + "</pre>"


def _resumo_rel(caminho):
    """Só aceita caminhos relativos dentro de resumos/ (sem .. ou absoluto)."""
    caminho = str(caminho or "").replace("\\", "/")
    partes = caminho.split("/")
    if not caminho.startswith("resumos/") or ".." in partes or ":" in partes[0]:
        return ""
    return caminho


def _titulo(pasta):
    try:
        texto = (pasta / "REFERENCIAS.md").read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return pasta.name
    m = re.search(r"^#\s+Referências:\s*(.+)$", texto, re.M)
    return m.group(1).strip() if m else pasta.name


def _celula(texto):
    return html.escape(str(texto or ""))


def _numero(valor):
    try:
        return float(valor)
    except (TypeError, ValueError):
        return 0


def _linha(l):
    autores = l.get("autores") or (f'{l.get("autor") or ""} ({l.get("ano") or ""})'.strip())
    titulo = _celula(l.get("titulo"))
    doi = urllib.parse.quote(str(l.get("doi") or ""), safe="/()")
    acesso = _celula(l.get("acesso") or "—")
    resumo = _resumo_rel(l.get("resumo"))
    if resumo:
        nome = Path(resumo).parent.name
        botao = (f'<a class="ler" href="{html.escape(resumo, quote=True)}" '
                 f'data-resumo="{html.escape(nome)}">ler</a>')
        if l.get("preprint"):
            botao += ' <span class="mudo">(preprint)</span>'
    else:
        botao = '<span class="mudo">—</span>'
    return (
        f'<tr data-citacoes="{int(_numero(l.get("citacoes")))}" '
        f'data-fwci="{_numero(l.get("fwci"))}" data-percentil="{_numero(l.get("percentil"))}" '
        f'data-ano="{_numero(l.get("ano"))}" data-acesso="{html.escape(l.get("acesso") or "", quote=True)}">'
        f'<td class="n">{int(_numero(l.get("citacoes")))}</td>'
        f'<td class="n">{_celula(l.get("fwci")) or "—"}</td>'
        f'<td class="n">{_celula(l.get("percentil")) or "—"}</td>'
        f'<td class="n">{_celula(l.get("ano")) or "—"}</td>'
        f'<td>{_celula(autores)}. <a href="https://doi.org/{doi}" target="_blank" rel="noopener">{titulo}</a>. '
        f'<span class="mudo">{_celula(l.get("revista"))}</span></td>'
        f'<td>{acesso}</td><td>{botao}</td></tr>')


def _opcoes_acesso(linhas):
    valores = sorted({l.get("acesso") or "" for l in linhas if l.get("acesso")})
    return "\n".join(
        f'        <option value="{html.escape(v, quote=True)}">{html.escape(v)}</option>'
        for v in valores)


def _resumos(pasta, linhas):
    blocos = []
    for l in linhas:
        caminho_rel = _resumo_rel(l.get("resumo"))
        if not caminho_rel:
            continue
        caminho = pasta / caminho_rel
        try:
            texto = caminho.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        nome = caminho.parent.name
        titulo = l.get("autores") or f'{l.get("autor") or ""} ({l.get("ano") or ""})'
        blocos.append(
            f'<section class="resumo" id="resumo-{html.escape(nome, quote=True)}" '
            f'data-titulo="{html.escape(titulo, quote=True)}">'
            f'<div class="md">{md_para_html(texto)}</div></section>')
    return "\n".join(blocos)


def _bases(pasta):
    try:
        texto = (pasta / "REFERENCIAS.md").read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return []
    return painel.bases_sem_doi(texto)


def _faltando(pasta):
    # O caminho oficial é a raiz do projeto; o fallback aceita o log antigo
    # que o preparar_resumos.py gravava dentro de pdfs/.
    for caminho in (pasta / "download.csv", pasta / "pdfs" / "download.csv"):
        if not caminho.exists():
            continue
        try:
            with open(caminho, encoding="utf-8-sig") as f:
                return [r for r in csv.DictReader(f)
                        if (r.get("estado") or "") in ("falhou", "rejeitado", "invalido")]
        except (OSError, UnicodeError):
            continue
    return None


def gerar(pasta, saida=None):
    pasta = Path(pasta)
    if not (pasta / "tabela.json").exists():
        raise FileNotFoundError(f"{pasta/'tabela.json'} não existe; rode o painel.py antes.")
    linhas = json.loads((pasta / "tabela.json").read_text(encoding="utf-8"))
    # Não mostre "ler" para um resumo que não existe mais (tabela.json antigo).
    for linha in linhas:
        rel = _resumo_rel(linha.get("resumo"))
        if linha.get("resumo") and not (rel and (pasta / rel).is_file()):
            linha["resumo"] = ""
    tema = _titulo(pasta)
    bases = _bases(pasta)
    faltando = _faltando(pasta)
    abertos = sum(1 for l in linhas
                  if l.get("acesso") and l.get("acesso") not in ("fechado", "closed"))
    resumos = sum(1 for l in linhas if l.get("resumo"))
    subtitulo = f"{len(linhas)} referências · {abertos} em acesso aberto · {resumos} resumos"

    if faltando is None:
        bloco_faltando = ('<p class="mudo">Sem <code>download.csv</code> neste projeto. '
                          'No exemplo do repositório, o log da primeira execução não foi '
                          'preservado; num projeto novo, rode o <code>preparar_resumos.py</code> '
                          'para gerar a lista do que falta.</p>')
        n_faltando = "—"
    elif not faltando:
        bloco_faltando = '<p class="ok">Todos os PDFs de acesso aberto foram baixados.</p>'
        n_faltando = 0
    else:
        linhas_f = ["<div class=\"tablewrap\"><table><thead><tr><th>Arquivo</th><th>DOI</th>"
                    "<th>Título</th><th>Motivo</th></tr></thead><tbody>"]
        for r in faltando:
            linhas_f.append(
                f'<tr><td><code>{_celula(r.get("slug"))}.pdf</code></td>'
                f'<td>{_celula(r.get("doi"))}</td><td>{_celula(r.get("titulo"))}</td>'
                f'<td>{_celula(r.get("detalhe"))}</td></tr>')
        linhas_f.append("</tbody></table></div>")
        linhas_f.append('<p class="aviso">Salve cada PDF em <code>pdfs/</code> com o nome da '
                        'primeira coluna e rode o <code>preparar_resumos.py</code> de novo. '
                        'A lista também está em <code>pdfs/FALTANDO.md</code>.</p>')
        bloco_faltando = "\n".join(linhas_f)
        n_faltando = len(faltando)

    blocos_bases = []
    for autor, titulo, link in bases:
        blocos_bases.append(
            f'<tr><td>{_celula(autor)}</td><td>{_celula(titulo)}</td>'
            f'<td><a href="{html.escape(link, quote=True)}" target="_blank" rel="noopener">{_celula(link)}</a></td></tr>')
    bloco_bases = "\n".join(blocos_bases) or '<tr><td colspan="3" class="mudo">Nenhuma base sem DOI.</td></tr>'

    pagina = (RAIZ / "modelos" / "relatorio.html").read_text(encoding="utf-8")
    trocas = {
        "TITULO": html.escape(tema),
        "SUBTITULO": html.escape(subtitulo),
        "DATA": datetime.date.today().strftime("%d/%m/%Y"),
        "N_REFS": len(linhas),
        "N_ABERTOS": abertos,
        "N_RESUMOS": resumos,
        "N_BASES": len(bases),
        "N_FALTANDO": n_faltando,
        "OPCOES_ACESSO": _opcoes_acesso(linhas),
        "TABELA": "\n".join(_linha(l) for l in linhas),
        "BASES": bloco_bases,
        "FALTANDO": bloco_faltando,
        "RESUMOS": _resumos(pasta, linhas),
    }
    marcadores = set(re.findall(r"\{\{([A-Z_]+)\}\}", pagina))
    assert marcadores <= set(trocas), f"marcadores sem valor: {sorted(marcadores - set(trocas))}"
    pagina = re.sub(r"\{\{([A-Z_]+)\}\}",
                    lambda m: str(trocas[m.group(1)]), pagina)
    destino = Path(saida) if saida else pasta / "RELATORIO.html"
    destino.write_text(pagina, encoding="utf-8")
    print(f"{len(linhas)} referências, {resumos} resumos, {len(bases)} bases sem DOI -> {destino}")
    return destino


def main(argv=None):
    ap = argparse.ArgumentParser(description="Gera um RELATORIO.html autocontido a partir da tabela e dos resumos.")
    ap.add_argument("pasta", help="pasta do levantamento (ex.: projetos/meu-tema)")
    ap.add_argument("--saida", default="", help="arquivo de saída (padrão: <pasta>/RELATORIO.html)")
    opcao_exemplo(ap)
    a = ap.parse_args(argv)
    barrar_exemplo(ap, a, a.pasta, a.saida)
    gerar(a.pasta, a.saida or None)
    return 0


if __name__ == "__main__":
    sys.exit(main())
