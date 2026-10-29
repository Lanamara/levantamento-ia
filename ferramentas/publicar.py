"""Gera um RELATORIO.html autocontido a partir de tabela.json e dos resumos.

Uso: python publicar.py <pasta-do-levantamento> [--saida RELATORIO.html]

O HTML abre com dois cliques, sem servidor e sem internet: a tabela tem busca,
filtros (acesso, frente, indicador da revista, já citado) e ordenação, e cada
resumo abre numa janela. Se existir novidades.csv (atualizar.py), a página mostra
os trabalhos novos encontrados na última atualização. É a camada
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


SINAIS = {"ok": ("ok", "revista listada"), "conferir": ("conferir", "⚠ conferir revista"),
          "retratado": ("retratado", "⛔ retratado")}


def _indicadores(l):
    """Selos dos indicadores da revista (só fatos da fonte; nada de "predatória")."""
    selos = []
    if l.get("sinal_revista") == "retratado":
        selos.append('<span class="selo ruim" title="Artigo retratado (Retraction Watch, via OpenAlex)">⛔ retratado</span>')
    if l.get("doaj") == "sim":
        selos.append('<span class="selo" title="Revista no DOAJ (OpenAlex)">DOAJ</span>')
    if l.get("cwts_core") == "sim":
        selos.append('<span class="selo" title="Revista na lista CWTS Core (OpenAlex)">CWTS</span>')
    if l.get("qualis"):
        selos.append(f'<span class="selo" title="Qualis CAPES 2021-2024 (planilha da Sucupira)">Qualis {_celula(l["qualis"])}</span>')
    if l.get("sinal_revista") == "conferir":
        selos.append('<span class="selo alerta" title="A revista não está no DOAJ, no CWTS Core nem na planilha do Qualis. '
                     'Isso não quer dizer que seja predatória: confira à mão.">⚠ conferir</span>')
    extra = []
    if l.get("editora"):
        extra.append(_celula(l["editora"]))
    if l.get("issn_l"):
        extra.append("ISSN " + _celula(l["issn_l"]))
    if l.get("h_index_revista") not in (None, ""):
        extra.append("h " + _celula(l["h_index_revista"]))
    if l.get("apc_usd") not in (None, ""):
        extra.append(f"APC US$ {_celula(l['apc_usd'])}")
    detalhes = f'<div class="mudo pequeno">{" · ".join(extra)}</div>' if extra else ""
    return (" ".join(selos) or '<span class="mudo">—</span>') + detalhes


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
    frentes = l.get("frentes") or []
    classe = ' class="retratado"' if l.get("sinal_revista") == "retratado" else ""
    citado = '<span class="selo citado" title="Já está na sua lista de referências">já cito</span> ' if l.get("ja_citado") else ""
    return (
        f'<tr{classe} data-sinal="{html.escape(l.get("sinal_revista") or "", quote=True)}" '
        f'data-frentes="{html.escape("|".join(frentes), quote=True)}" '
        f'data-citado="{"sim" if l.get("ja_citado") else "nao"}" '
        f'data-citacoes="{int(_numero(l.get("citacoes")))}" '
        f'data-fwci="{_numero(l.get("fwci"))}" data-percentil="{_numero(l.get("percentil"))}" '
        f'data-ano="{_numero(l.get("ano"))}" data-acesso="{html.escape(l.get("acesso") or "", quote=True)}">'
        f'<td class="n">{int(_numero(l.get("citacoes")))}</td>'
        f'<td class="n">{_celula(l.get("fwci")) or "—"}</td>'
        f'<td class="n">{_celula(l.get("percentil")) or "—"}</td>'
        f'<td class="n">{_celula(l.get("ano")) or "—"}</td>'
        f'<td>{citado}{_celula(autores)}. <a href="https://doi.org/{doi}" target="_blank" rel="noopener">{titulo}</a>. '
        f'<span class="mudo">{_celula(l.get("revista"))}</span>'
        f'<div class="mudo pequeno">{_celula(", ".join(frentes))}</div></td>'
        f'<td>{_indicadores(l)}</td>'
        f'<td>{acesso}</td><td>{botao}</td></tr>')


def _opcoes_acesso(linhas):
    valores = sorted({l.get("acesso") or "" for l in linhas if l.get("acesso")})
    return "\n".join(
        f'        <option value="{html.escape(v, quote=True)}">{html.escape(v)}</option>'
        for v in valores)


def _opcoes(valores):
    return "\n".join(
        f'        <option value="{html.escape(v, quote=True)}">{html.escape(v)}</option>'
        for v in valores)


def _opcoes_frente(linhas):
    return _opcoes(sorted({f for l in linhas for f in (l.get("frentes") or [])}))


def _novidades(pasta):
    """(texto da data, HTML) dos trabalhos da última atualização, ou ("", aviso)."""
    caminho = pasta / "novidades.csv"
    if not caminho.exists():
        return "—", ('<p class="mudo">Ainda não houve atualização. Rode '
                     '<code>ferramentas/atualizar.py</code> (ou espere a atualização mensal).</p>')
    try:
        with open(caminho, encoding="utf-8-sig") as f:
            todas = list(csv.DictReader(f))
    except (OSError, UnicodeError):
        return "—", '<p class="mudo">Não consegui ler <code>novidades.csv</code>.</p>'
    if not todas:
        return "0", '<p class="ok">Nenhum trabalho novo nas buscas feitas até agora.</p>'
    ultima = max(r.get("data_busca") or "" for r in todas)
    recentes = [r for r in todas if (r.get("data_busca") or "") == ultima]
    partes = [f'<p class="mudo">Última atualização: {_celula(ultima)} · {len(recentes)} trabalho(s) novo(s) · '
              f'{len(todas)} no total desde a primeira atualização (ver <code>NOVIDADES.md</code>). '
              'Encontrados por busca automática no OpenAlex: leia o resumo antes de incluir.</p>',
              '<div class="tablewrap"><table><thead><tr><th>Ano</th><th>Referência</th>'
              '<th>Indicadores</th><th>Frente</th></tr></thead><tbody>']
    for r in recentes:
        doi = urllib.parse.quote(str(r.get("doi") or ""), safe="/()")
        partes.append(
            f'<tr><td class="n">{_celula(r.get("ano"))}</td>'
            f'<td><a href="https://doi.org/{doi}" target="_blank" rel="noopener">{_celula(r.get("titulo"))}</a>. '
            f'<span class="mudo">{_celula(r.get("primeiro_autor"))} · {_celula(r.get("revista"))}</span></td>'
            f'<td>{_indicadores(r)}</td><td class="mudo">{_celula(r.get("frente"))}</td></tr>')
    partes.append("</tbody></table></div>")
    return str(len(recentes)), "\n".join(partes)


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
    a_conferir = sum(1 for l in linhas if l.get("sinal_revista") in ("conferir", "retratado"))
    citados = sum(1 for l in linhas if l.get("ja_citado"))
    n_novos, bloco_novidades = _novidades(pasta)

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
        "OPCOES_FRENTE": _opcoes_frente(linhas),
        "N_CONFERIR": a_conferir,
        "N_CITADOS": citados,
        "N_NOVOS": n_novos,
        "NOVIDADES": bloco_novidades,
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
