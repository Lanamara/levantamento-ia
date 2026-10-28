"""Confere o que o levantamento precisa, sem instalar nada.

Uso:
    python ferramentas/conferir.py [--json] [--testar-modelo]

Imprime uma linha por item, com OK, FALTA ou AVISO, e o comando que resolve
no sistema da pessoa. Sem --testar-modelo não usa a rede nem chama o modelo.
Com --testar-modelo faz uma chamada curta ao modelo grátis e diz se ele
respondeu, se bateu no limite do dia (429/FreeUsageLimit) ou se deu erro.

Sai com 0 quando dá para seguir e 1 quando falta algo obrigatório.
"""
import argparse
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
REQUISITOS = RAIZ / "requirements.txt"
MODELO = "opencode/deepseek-v4.1-flash-free"
MIN_PYTHON = (3, 10)
LIMITE = ("FreeUsageLimitError", "Rate limit exceeded", '"status":429', '"status": 429')

COMANDOS = {
    "python": {
        "windows": "winget install Python.Python.3.12",
        "macos": "brew install python@3.12",
        "linux": "sudo apt install python3 python3-venv python3-pip",
    },
    "node": {
        "windows": "winget install OpenJS.NodeJS.LTS",
        "macos": "brew install node",
        "linux": "sudo apt install nodejs npm",
    },
    "opencode": {
        "windows": "npm install -g @opencode/cli",
        "macos": "npm install -g @opencode/cli",
        "linux": "npm install -g @opencode/cli",
    },
    "opencode_novo": {
        "windows": "npm install -g @opencode/cli@latest",
        "macos": "npm install -g @opencode/cli@latest",
        "linux": "npm install -g @opencode/cli@latest",
    },
    "git": {
        "windows": "winget install Git.Git",
        "macos": "xcode-select --install",
        "linux": "sudo apt install git",
    },
    "curl": {
        "windows": "winget install curl.curl",
        "macos": "brew install curl",
        "linux": "sudo apt install curl",
    },
}


def sistema():
    """Nome do sistema, para escolher o comando que a pessoa vai colar."""
    if sys.platform.startswith("win"):
        return "windows"
    if sys.platform == "darwin":
        return "macos"
    return "linux"


def _aspas(caminho):
    return f'"{caminho}"' if any(c.isspace() for c in caminho) else caminho


def comando_pacotes():
    """Instala no mesmo interpretador que está rodando este script."""
    return f"{_aspas(sys.executable)} -m pip install -r requirements.txt"


def comando(chave):
    if chave == "pacotes":
        return comando_pacotes()
    return COMANDOS.get(chave, {}).get(sistema(), "")


def item(estado, nome, detalhe, comando=""):
    return {"estado": estado, "item": nome, "detalhe": detalhe, "comando": comando}


def achar(nome):
    """Atalho para shutil.which, que os testes trocam."""
    return shutil.which(nome)


def rodar(cmd, timeout=20, cwd=None, env=None):
    """Roda sem levantar exceção: falha de comando vira código -1."""
    try:
        return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                              errors="replace", timeout=timeout, cwd=cwd, env=env)
    except (OSError, subprocess.TimeoutExpired) as erro:
        return subprocess.CompletedProcess(cmd, -1, "", f"{type(erro).__name__}: {erro}")


def _primeira_linha(saida):
    for linha in (saida or "").splitlines():
        if linha.strip():
            return linha.strip()
    return "versão não informada"


def _versao(saida):
    achado = re.search(r"\d+\.\d+\.\d+", saida or "")
    return achado.group(0) if achado else _primeira_linha(saida)


def versao_python_ok(versao=None):
    versao = versao or sys.version_info
    return tuple(versao[:2]) >= MIN_PYTHON


def conferir_python():
    v = sys.version_info
    texto = f"{v.major}.{v.minor}.{v.micro}"
    if not versao_python_ok(v):
        return item("FALTA", "Python 3.10+", f"encontrei {texto}; o mínimo é 3.10",
                    comando("python"))
    return item("OK", "Python 3.10+", texto)


def pacotes_do_arquivo(caminho=REQUISITOS):
    """Nomes dos pacotes no requirements.txt, sem versão nem comentário."""
    try:
        texto = Path(caminho).read_text(encoding="utf-8")
    except OSError:
        return None
    nomes = []
    for linha in texto.splitlines():
        linha = linha.split("#", 1)[0].strip()
        if not linha or linha.startswith("-"):
            continue
        nome = re.split(r"[<>=!~;\[\] ]", linha, maxsplit=1)[0].strip()
        if nome:
            nomes.append(nome)
    return nomes


def tem_modulo(nome):
    try:
        return importlib.util.find_spec(nome) is not None
    except (ImportError, ValueError):
        return False


def importacao(nome):
    """Nome do pacote no pip costuma ser o mesmo do import; ajuste aqui se mudar."""
    return {"pypdf": "pypdf", "requests": "requests",
            "markdown": "markdown", "pytest": "pytest"}.get(
                nome.lower(), nome.lower().replace("-", "_"))


def faltando_pacotes(nomes):
    return [n for n in nomes if not tem_modulo(importacao(n))]


def conferir_pacotes():
    nomes = pacotes_do_arquivo()
    if nomes is None:
        return item("FALTA", "requirements.txt",
                    f"não encontrei {REQUISITOS}; entre na pasta "
                    "`levantamento-ia` ou `levantamento-ia-main` (ZIP)",
                    "cd levantamento-ia")
    if not nomes:
        return item("AVISO", "requirements.txt", "está vazio")
    faltando = faltando_pacotes(nomes)
    if faltando:
        return item("FALTA", "pacotes do Python", "faltam: " + ", ".join(faltando),
                    comando("pacotes"))
    return item("OK", "pacotes do Python", ", ".join(nomes) + " instalados")


def conferir_node():
    node, npm = achar("node"), achar("npm")
    if not node or not npm:
        faltam = [nome for nome, caminho in (("Node.js", node), ("npm", npm)) if not caminho]
        return item("FALTA", "Node.js e npm", "não encontrado: " + ", ".join(faltam),
                    comando("node"))
    vnode = _versao(rodar([node, "--version"]).stdout)
    vnpm = _versao(rodar([npm, "--version"]).stdout)
    return item("OK", "Node.js e npm", f"Node {vnode}, npm {vnpm}")


def conferir_opencode():
    caminho = achar("opencode")
    if not caminho:
        return item("FALTA", "opencode", "não está no PATH", comando("opencode"))
    log_versao = rodar([caminho, "--version"])
    versao = _versao((log_versao.stdout or "") + (log_versao.stderr or ""))
    ajuda = rodar([caminho, "run", "--help"], timeout=30)
    texto = (ajuda.stdout or "") + (ajuda.stderr or "")
    if ajuda.returncode != 0 or "--standalone" not in texto:
        return item("FALTA", "opencode",
                    f"versão {versao}, mas não aceita --standalone",
                    comando("opencode_novo"))
    return item("OK", "opencode", f"versão {versao}, aceita --standalone")


def conferir_git():
    caminho = achar("git")
    if not caminho:
        return item("AVISO", "git", "não está no PATH; sem ele, baixe o ZIP do GitHub",
                    comando("git"))
    return item("OK", "git", _versao(rodar([caminho, "--version"]).stdout))


def conferir_curl():
    caminho = achar("curl")
    if not caminho:
        return item("AVISO", "curl", "não está no PATH; o download usa urllib como reserva",
                    comando("curl"))
    return item("OK", "curl", _versao(rodar([caminho, "--version"]).stdout))


def primeiro_erro(saida):
    """Mensagem do primeiro evento de erro do log, se houver."""
    for linha in (saida or "").splitlines():
        try:
            evento = json.loads(linha)
        except ValueError:
            continue
        if isinstance(evento, dict) and evento.get("type") == "error":
            return str(evento.get("message") or evento.get("error") or "erro não detalhado")[:160]
    return ""


def deu_limite(saida):
    """Limite só conta quando aparece na mensagem do próprio erro.

    Um texto do modelo que fale em "rate limit" não é erro; por isso a linha
    JSON só conta quando o evento é do tipo error.
    """
    marcadores = tuple(s.lower() for s in LIMITE)
    for linha in (saida or "").splitlines():
        if not linha.strip():
            continue
        baixo = linha.lower()
        if not any(s in baixo for s in marcadores):
            continue
        try:
            evento = json.loads(linha)
        except ValueError:
            return True
        if isinstance(evento, dict) and evento.get("type") == "error":
            return True
    return False


def testar_modelo(modelo=MODELO):
    """Uma chamada curta ao modelo grátis; só roda com --testar-modelo."""
    if not versao_python_ok():
        return item("FALTA", "modelo grátis",
                    "Python 3.10+ necessário para testar o modelo", comando("python"))
    caminho = achar("opencode")
    if not caminho:
        return item("FALTA", "modelo grátis", "opencode não está no PATH",
                    comando("opencode"))
    pasta = tempfile.mkdtemp(prefix="conferir-")
    try:
        env = dict(os.environ, PWD=pasta)
        r = rodar([caminho, "run", "--standalone", "--format", "json", "-m", modelo,
                   "Responda apenas: ok"], timeout=120, cwd=pasta, env=env)
    finally:
        shutil.rmtree(pasta, ignore_errors=True)
    saida = (r.stdout or "") + "\n" + (r.stderr or "")
    if deu_limite(saida):
        return item("FALTA", "modelo grátis",
                    "limite do dia (429/FreeUsageLimit); retome amanhã ou faça a etapa com a sua cota")
    erro = primeiro_erro(saida)
    if erro:
        return item("FALTA", "modelo grátis", "erro: " + erro)
    if r.returncode != 0:
        motivo = _primeira_linha(r.stderr) or _primeira_linha(r.stdout)
        detalhe = f"erro (código {r.returncode})"
        if motivo != "versão não informada":
            detalhe += ": " + motivo[:160]
        return item("FALTA", "modelo grátis", detalhe)
    return item("OK", "modelo grátis", f"{modelo} respondeu")


def conferir_tudo(com_modelo=False, modelo=MODELO):
    itens = [conferir_python(), conferir_pacotes(), conferir_node(),
             conferir_opencode(), conferir_git(), conferir_curl()]
    if com_modelo:
        itens.append(testar_modelo(modelo))
    return itens


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Confere Python, pacotes, Node, opencode, git e curl, sem instalar nada.")
    ap.add_argument("--json", action="store_true", help="imprime o resultado em JSON")
    ap.add_argument("--testar-modelo", action="store_true",
                    help="faz uma chamada curta ao modelo grátis (usa a rede)")
    ap.add_argument("--modelo", default=MODELO,
                    help=f"modelo do --testar-modelo (padrão: {MODELO}); veja os grátis com: opencode models")
    a = ap.parse_args(argv)
    itens = conferir_tudo(a.testar_modelo, a.modelo)
    falta = [i for i in itens if i["estado"] == "FALTA"]
    if a.json:
        print(json.dumps({"ok": not falta, "itens": itens}, ensure_ascii=True, indent=2))
    else:
        for i in itens:
            print(f'{i["estado"]:<5} {i["item"]}: {i["detalhe"]}')
            if i["comando"]:
                print(f'      resolva com: {i["comando"]}')
        print()
        if falta:
            print("NÃO DÁ PARA SEGUIR AGORA: veja os FALTA acima.")
        else:
            print("PODE SEGUIR: tudo o que o levantamento precisa está pronto.")
    return 1 if falta else 0


if __name__ == "__main__":
    sys.exit(main())
