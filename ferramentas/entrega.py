"""Abre a pasta do levantamento e o relatório na tela da pessoa.

Uso: python entrega.py <pasta-do-levantamento> [--nao-abrir] [--servir] [--porta 8765]

Faz a ponte entre a IA e a pessoa:
- gera o RELATORIO.html (se ainda não existir ou estiver desatualizado);
- escreve o LEIA-ME.md, com o que abrir, o que já está pronto e o que falta;
- abre a pasta no Explorador (Windows), Finder (macOS) ou xdg-open (Linux);
- opcionalmente serve o HTML em http://127.0.0.1:8765/RELATORIO.html.

O navegador não é obrigatório para o HTML: ele é um arquivo único, sem servidor.
O --servir existe para quem preferir uma URL local em vez do arquivo (por
exemplo, para abrir numa aba do navegador). Ele escuta só em 127.0.0.1.
"""
import argparse
import datetime
import json
import os
import subprocess
import sys
import webbrowser
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import publicar  # noqa: E402
from projeto import barrar_exemplo, opcao_exemplo  # noqa: E402


def abrir(caminho):
    """Abre uma pasta ou arquivo no programa padrão do sistema."""
    caminho = Path(caminho).resolve()
    if not caminho.exists():
        return False, f"não existe: {caminho}"
    try:
        if sys.platform.startswith("win"):
            os.startfile(str(caminho))  # type: ignore[attr-defined]
        elif sys.platform == "darwin":
            subprocess.Popen(["open", str(caminho)])
        elif os.environ.get("WSL_DISTRO_NAME"):
            traduzido = subprocess.run(["wslpath", "-w", str(caminho)],
                                       capture_output=True, text=True).stdout.strip()
            subprocess.Popen(["explorer.exe", traduzido or str(caminho)])
        else:
            subprocess.Popen(["xdg-open", str(caminho)])
        return True, ""
    except Exception as e:
        return False, f"{type(e).__name__}: {e}"


def _tem_resumo(pasta, linha):
    rel = publicar._resumo_rel(linha.get("resumo"))
    return bool(rel) and (pasta / rel).is_file()


def _plural(n, singular, plural):
    return singular if n == 1 else plural


def _contagens(pasta):
    dados = {"refs": 0, "abertos": 0, "resumos": 0, "bases": 0, "faltando": 0,
             "sem_log": True, "tema": pasta.name, "linhas_faltando": []}
    try:
        linhas = json.loads((pasta / "tabela.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return dados
    dados["refs"] = len(linhas)
    dados["abertos"] = sum(1 for l in linhas
                           if l.get("acesso") and l.get("acesso") not in ("fechado", "closed"))
    dados["resumos"] = sum(1 for l in linhas if _tem_resumo(pasta, l))
    dados["tema"] = publicar._titulo(pasta)
    dados["bases"] = len(publicar._bases(pasta))
    faltando = publicar._faltando(pasta)
    if faltando is not None:
        dados["sem_log"] = False
        dados["faltando"] = len(faltando)
        dados["linhas_faltando"] = faltando
    return dados


def escrever_leia_me(pasta):
    """LEIA-ME.md curto, para a pessoa saber o que abrir e o que fazer."""
    pasta = Path(pasta).resolve()
    try:
        base = pasta.relative_to(Path.cwd().resolve()).as_posix()
    except ValueError:
        base = pasta.as_posix()
    d = _contagens(pasta)
    linhas = [
        f"# Levantamento: {d['tema']}",
        "",
        f"Gerado em {datetime.date.today().strftime('%d/%m/%Y')}.",
        "",
        "## Abra primeiro",
        "",
        "- [`RELATORIO.html`](RELATORIO.html) — tabela navegável, com busca, filtro e os resumos.",
        "- [`TABELA.md`](TABELA.md) — a mesma lista em texto, ordenada por citações.",
        "- [`REFERENCIAS.md`](REFERENCIAS.md) — as referências separadas por frente e o que cada busca concluiu.",
        "- [`referencias.bib`](referencias.bib) — para importar no Zotero ou no Mendeley.",
        "",
        "## O que já está pronto",
        "",
        f"- {d['refs']} {_plural(d['refs'], 'referência', 'referências')} com DOI.",
        f"- {d['abertos']} em acesso aberto.",
        f"- {d['resumos']} {_plural(d['resumos'], 'resumo', 'resumos')} de leitura integral.",
        f"- {d['bases']} {_plural(d['bases'], 'base ou relatório oficial', 'bases e relatórios oficiais')} sem DOI.",
        "",
    ]
    if d["sem_log"]:
        linhas += ["## PDFs", "",
                   "Este projeto não tem `download.csv`. No exemplo do repositório, o log da "
                   "primeira execução não foi preservado; num projeto novo, rode o "
                   "`preparar_resumos.py` para gerar a lista do que falta.", ""]
    elif d["faltando"]:
        if d["faltando"] == 1:
            resumo_pdf = "1 PDF não foi baixado."
        else:
            resumo_pdf = f"{d['faltando']} PDFs não foram baixados."
        linhas += ["## PDFs que faltam", "",
                   resumo_pdf + " A lista com o nome de arquivo "
                   "de cada um está em [`pdfs/FALTANDO.md`](pdfs/FALTANDO.md).", "",
                   "Para completar: baixe o artigo pelo navegador (só acesso aberto), salve em "
                   "`pdfs/` com o nome indicado e rode de novo o comando abaixo. O script "
                   "aproveita o que já está na pasta.", ""]
        for f in d["linhas_faltando"][:10]:
            linhas.append(f"- `{f.get('slug', '')}.pdf` — {f.get('titulo', '')}")
        if len(d["linhas_faltando"]) > 10:
            linhas.append(f"- … e mais {len(d['linhas_faltando']) - 10}.")
        linhas.append("")
    else:
        linhas += ["## PDFs", "",
                   "Todos os PDFs de acesso aberto foram baixados e resumidos.", ""]

    linhas += [
        "## Como continuar",
        "",
        "Rode a partir da pasta do repositório:",
        "",
        "```bash",
        f'python ferramentas/preparar_resumos.py "{base}/cienciometria.csv" '
        f'"{base}/pdfs" "{base}/resumos" modelos/PEDIDO-resumo.md "{d["tema"]}" --abrir',
        f'python ferramentas/orquestrar.py "{base}/resumos" --paralelo 2',
        f'python ferramentas/painel.py "{base}"',
        f'python ferramentas/publicar.py "{base}"',
        "```",
        "",
        "## Formatos",
        "",
        "| Camada | Arquivos | Para quê |",
        "|---|---|---|",
        "| Para ler | `RELATORIO.html`, `TABELA.md`, `REFERENCIAS.md` | consulta e leitura |",
        "| Para citar | `referencias.bib` | Zotero, Mendeley, LaTeX |",
        "| Para analisar | `cienciometria.csv`, `tabela.json`, `verificacao.csv`, `download.csv` | planilha e scripts |",
        "| Interno | `pdfs/`, `resumos/*/TEXTO.txt`, `log.jsonl` | não publicar (direitos autorais) |",
        "",
        "Os números dos resumos vêm com a página; confira no artigo antes de citar.",
        "",
    ]
    (pasta / "LEIA-ME.md").write_text("\n".join(linhas), encoding="utf-8")
    return pasta / "LEIA-ME.md"


def _servir(pasta, porta):
    handler = partial(SimpleHTTPRequestHandler, directory=str(pasta))
    try:
        servidor = ThreadingHTTPServer(("127.0.0.1", porta), handler)
    except OSError as e:
        print(f"ERRO: não consegui abrir a porta {porta}: {e}", file=sys.stderr)
        return 2
    url = f"http://127.0.0.1:{porta}/RELATORIO.html"
    print(f"SERVIDOR: {url} (Ctrl+C para parar)", flush=True)
    webbrowser.open(url)
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado.", flush=True)
    finally:
        servidor.server_close()
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="Abre a pasta e o relatório do levantamento.")
    ap.add_argument("pasta", help="pasta do levantamento (ex.: projetos/meu-tema)")
    ap.add_argument("--nao-abrir", action="store_true", help="só gera os arquivos, sem abrir janelas")
    ap.add_argument("--servir", action="store_true", help="serve o HTML numa URL local em vez de abrir o arquivo")
    ap.add_argument("--porta", type=int, default=8765, help="porta do --servir (padrão: 8765)")
    opcao_exemplo(ap)
    a = ap.parse_args(argv)
    barrar_exemplo(ap, a, a.pasta)
    pasta = Path(a.pasta).resolve()
    if not pasta.is_dir():
        print(f"ERRO: pasta não encontrada: {pasta}", file=sys.stderr)
        return 2

    html_path = None
    if (pasta / "tabela.json").exists():
        try:
            html_path = publicar.gerar(pasta)
        except Exception as e:
            print(f"AVISO: não gerei o RELATORIO.html ({type(e).__name__}: {e})", file=sys.stderr)
            html_path = pasta / "RELATORIO.html"
    leia = escrever_leia_me(pasta)

    print(f"PASTA: {pasta}")
    if html_path:
        print(f"HTML: {html_path}")
    print(f"LEIA-ME: {leia}")
    if a.servir:
        return _servir(pasta, a.porta)
    if a.nao_abrir:
        return 0
    abriu_pasta, erro = abrir(pasta)
    if html_path:
        abriu_html, erro_html = abrir(html_path)
    else:
        abriu_html, erro_html = False, "sem RELATORIO.html"
    print("ABRIU: " + ", ".join(
        nome for nome, ok in (("pasta", abriu_pasta), ("html", abriu_html)) if ok))
    if not abriu_pasta:
        print(f"AVISO: não consegui abrir a pasta: {erro}", file=sys.stderr)
    if not abriu_html and html_path:
        print(f"AVISO: não consegui abrir o HTML: {erro_html}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
