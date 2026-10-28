"""Orquestra vários `opencode run` com modelos grátis numa fila, poucos de cada vez.

Uso:
    python orquestrar.py <pasta-do-trabalho> [--paralelo 2] [--modelo opencode/deepseek-v4.1-flash-free]
                         [--intervalo 20] [--timeout 1800]

A pasta tem uma subpasta por frente, cada uma com PEDIDO.md. Cada frente roda
`opencode run` dentro da própria subpasta e deve gravar RELATORIO.md ali.
- No máximo --paralelo ao mesmo tempo, com intervalo entre os inícios (o grátis
  limita requisições por minuto por IP).
- Se o log mostrar limite (429 / FreeUsageLimit), a frente volta para o fim da
  fila uma vez, com o modelo reserva. O relatório parcial e o log antigo são
  guardados antes da nova tentativa.
- Frente que já tem um RELATORIO.md com pelo menos 200 caracteres é pulada.
- Cada agente tem --timeout segundos (padrão 1800); passou disso, é encerrado.
- Cada agente roda numa cópia da frente fora do repositório, para não ler o
  AGENTS.md da IA principal; o que ele grava volta para a pasta da frente.
- Ao fim, imprime SEM-BUSCA <frente> para quem não chamou websearch no log.
- Depois de OK, imprime FORMATO <frente>: ... quando o relatório não segue as
  colunas da busca ou as seções do resumo.
- Sai com código 1 se alguma frente não produziu um relatório válido.
"""
import argparse
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from projeto import barrar_exemplo, opcao_exemplo  # noqa: E402

RESERVA = "opencode/glm-5.3-flash-free"
LIMITE = ("FreeUsageLimitError", "Rate limit exceeded", '"status":429')
MIN_RELATORIO = 200
CAMPOS_BUSCA = ("autores (ano)", "título", "revista", "doi/link", "dados",
                "método", "área", "resultado principal")
GRAVES = ("sem tabela de referências", "faltam seções", "colunas fora do contrato",
          "sem coluna de DOI/link", "o resumo tem tabela")


def ler_eventos(pasta):
    """(evento, linha crua) para cada linha JSON que seja um objeto."""
    try:
        linhas = (pasta / "log.jsonl").read_text(encoding="utf-8", errors="ignore").splitlines()
    except OSError:
        return []
    saida = []
    for linha in linhas:
        try:
            ev = json.loads(linha)
        except ValueError:
            continue
        if isinstance(ev, dict):
            saida.append((ev, linha))
    return saida


def contar_busca(pasta):
    """Quantas chamadas à ferramenta websearch aparecem no log."""
    return sum(
        1 for ev, _ in ler_eventos(pasta)
        if ev.get("type") == "tool_use"
        and isinstance(ev.get("part"), dict)
        and ev["part"].get("tool") == "websearch"
    )


def relatorio_ok(pasta):
    """Só vale o RELATORIO.md que existe e tem pelo menos MIN_RELATORIO caracteres."""
    try:
        texto = (pasta / "RELATORIO.md").read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return False
    return len(texto.strip()) >= MIN_RELATORIO


def avisos_formato(pasta):
    """Confere o contrato do RELATORIO.md: colunas da busca ou seções do resumo."""
    try:
        texto = (pasta / "RELATORIO.md").read_text(encoding="utf-8", errors="ignore")
        pedido = (pasta / "PEDIDO.md").read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []
    avisos = []
    if "```" in texto:
        avisos.append("o relatório tem cerca de código; escreva o conteúdo sem copiar o bloco de formato")
    if "TEXTO.txt" in pedido:
        faltando = [n for n in range(1, 9) if not re.search(rf"^##\s*{n}\.", texto, re.M)]
        if faltando:
            avisos.append("faltam seções: " + ", ".join(str(n) for n in faltando))
        paginas = len(re.findall(r"\[p\.\s*\d+", texto))
        if paginas < 5:
            avisos.append(f"poucas páginas citadas ({paginas}); o contrato pede página em todo número")
        if any(l.lstrip().startswith("|") for l in texto.splitlines()):
            avisos.append("o resumo tem tabela; o contrato pede listas")
    else:
        linhas = [l for l in texto.splitlines() if l.lstrip().startswith("|")]
        if not linhas:
            avisos.append("sem tabela de referências")
        else:
            cabecalho = linhas[0].lower()
            faltando = [c for c in CAMPOS_BUSCA
                        if c not in cabecalho and not (c == "dados" and "sensor" in cabecalho)]
            if faltando:
                avisos.append("colunas fora do contrato: " + ", ".join(faltando))
            corpo = [l for l in linhas[1:]
                     if not re.fullmatch(r"\|[\s:|\-]+\|?", l.strip())]
            if not 10 <= len(corpo) <= 15:
                avisos.append(f"{len(corpo)} linhas de dados (o contrato pede 10 a 15)")
            if "doi" not in cabecalho and "link" not in cabecalho:
                avisos.append("sem coluna de DOI/link")
    return avisos


def aviso_grave(aviso):
    """Aviso que impede considerar a frente pronta (o resto é só FORMATO)."""
    return any(aviso.startswith(prefixo) for prefixo in GRAVES)


def renomear_relatorio(pasta):
    """Guarda o relatório atual para o --refazer rodar a frente de novo."""
    origem = pasta / "RELATORIO.md"
    if not origem.exists():
        return None
    n = 1
    while (pasta / f"RELATORIO.anterior{n}.md").exists():
        n += 1
    destino = pasta / f"RELATORIO.anterior{n}.md"
    origem.replace(destino)
    return destino


def opcoes_processo():
    """Isola o agente num grupo de processos, para encerrar os filhos."""
    if os.name == "nt":
        return {"creationflags": subprocess.CREATE_NEW_PROCESS_GROUP}
    return {"start_new_session": True}


def encerrar(proc):
    """Mata o agente e a árvore de processos, com taskkill ou killpg."""
    if proc.poll() is not None:
        return
    if os.name == "nt":
        subprocess.run(["taskkill", "/T", "/F", "/PID", str(proc.pid)],
                       capture_output=True, text=True, errors="replace")
    else:
        try:
            os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
        except OSError:
            pass
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        if os.name == "nt":
            proc.kill()
        else:
            try:
                os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
            except OSError:
                pass
        try:
            proc.wait(timeout=2)
        except subprocess.TimeoutExpired:
            pass


INTERNOS = ("log.jsonl",)


def isolar(pasta):
    """Copia a frente para uma pasta temporária, fora do repositório.

    O opencode lê todo AGENTS.md que achar subindo a partir da pasta de trabalho,
    sem parar na raiz do Git. Dentro do repositório, cada agente receberia o
    AGENTS.md escrito para a IA principal ("confirme com a pessoa", "rode o
    orquestrar") e poderia tentar conduzir o levantamento em vez de cumprir o
    PEDIDO.md. Na pasta temporária ele só enxerga o pedido. O opencode.json da
    pasta das frentes vai junto, para a busca na web continuar liberada.
    """
    tmp = Path(tempfile.mkdtemp(prefix="levantamento-"))
    config = pasta.parent / "opencode.json"
    if config.exists():
        shutil.copy2(config, tmp / "opencode.json")
    shutil.copytree(pasta, tmp / pasta.name,
                    ignore=shutil.ignore_patterns(*INTERNOS, "log.anterior*",
                                                  "RELATORIO.parcial*", "RELATORIO.anterior*"))
    return tmp


def devolver(tmp, pasta):
    """Traz de volta o que o agente gravou e apaga a pasta temporária."""
    origem = tmp / pasta.name
    for arq in origem.rglob("*"):
        if arq.is_file() and arq.name not in INTERNOS:
            destino = pasta / arq.relative_to(origem)
            destino.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(arq, destino)
    # No Windows o opencode segura a pasta por um instante depois de sair.
    for _ in range(10):
        shutil.rmtree(tmp, ignore_errors=True)
        if not tmp.exists():
            break
        time.sleep(1)
    if tmp.exists():
        print(f"AVISO: não consegui apagar a pasta temporária: {tmp}", flush=True)


def lancar(pasta, modelo):
    """Roda o agente na cópia isolada; o log fica na pasta real da frente."""
    tmp = isolar(pasta)
    trabalho = tmp / pasta.name
    # O opencode decide a pasta de trabalho pelo PWD herdado, não só pelo cwd:
    # sem isto, todos os agentes abrem na pasta de quem chamou.
    env = dict(os.environ, OPENCODE_ENABLE_EXA="1", PWD=str(trabalho))
    # --standalone: o agente roda no próprio processo. Sem isso, o opencode 2.x
    # usa um serviço de fundo que continua segurando a pasta temporária (e não
    # morre quando o --timeout encerra o agente).
    cmd = [shutil.which("opencode") or "opencode", "run", "--standalone", "--format", "json",
           "-m", modelo, "Leia PEDIDO.md e faça o que ele pede. Grave RELATORIO.md nesta pasta."]
    with open(pasta / "log.jsonl", "w", encoding="utf-8") as log:
        proc = subprocess.Popen(cmd, cwd=trabalho, stdout=log,
                                stderr=subprocess.STDOUT, env=env, **opcoes_processo())
    return proc, tmp


def renomear_anterior(pasta, tentativa):
    """Guarda o relatório parcial e o log da tentativa que bateu no limite."""
    for nome, novo in (("RELATORIO.md", f"RELATORIO.parcial{tentativa}.md"),
                       ("log.jsonl", f"log.anterior{tentativa}.jsonl")):
        origem = pasta / nome
        if not origem.exists():
            continue
        destino = pasta / novo
        n = 1
        while destino.exists():
            destino = pasta / f"{Path(novo).stem}-{n}{Path(novo).suffix}"
            n += 1
        origem.replace(destino)


def bateu_limite(pasta):
    """Só conta erro de limite vindo de evento de erro, não de texto que o agente leu."""
    for ev, linha in ler_eventos(pasta):
        if ev.get("type") == "error" and any(s in linha for s in LIMITE):
            return True
    return False


def main(argv=None):
    ap = argparse.ArgumentParser(description="Roda os agentes das frentes, com fila e limite de tempo.")
    ap.add_argument("raiz", help="pasta com uma subpasta por frente, cada uma com PEDIDO.md")
    ap.add_argument("--paralelo", type=int, default=2, help="agentes ao mesmo tempo (padrão: 2)")
    ap.add_argument("--modelo", default="opencode/deepseek-v4.1-flash-free",
                    help="modelo principal (padrão: opencode/deepseek-v4.1-flash-free)")
    ap.add_argument("--intervalo", type=int, default=20, help="segundos entre inícios (padrão: 20)")
    ap.add_argument("--timeout", type=int, default=1800,
                    help="segundos por agente; passou disso, o processo é encerrado (padrão: 1800)")
    ap.add_argument("--refazer", nargs="+", default=[], metavar="FRENTE",
                    help="guarda o RELATORIO.md atual e roda esta frente de novo")
    opcao_exemplo(ap)
    a = ap.parse_args(argv)
    barrar_exemplo(ap, a, a.raiz)
    if a.paralelo < 1 or a.intervalo < 0 or a.timeout < 1:
        ap.error("--paralelo precisa ser 1 ou mais, --intervalo 0 ou mais e --timeout 1 ou mais")

    raiz = Path(a.raiz)
    if not raiz.is_dir():
        print(f"ERRO: pasta não encontrada: {raiz}", file=sys.stderr, flush=True)
        return 2
    for nome in a.refazer:
        pasta = raiz / nome
        if not pasta.is_dir():
            print(f"ERRO: frente não encontrada: {pasta}", file=sys.stderr, flush=True)
            return 2
        renomear_relatorio(pasta)

    fila = [(p, a.modelo, 0) for p in sorted(raiz.iterdir())
            if (p / "PEDIDO.md").exists() and not relatorio_ok(p)]
    rodando = {}
    falhas, sem_busca = [], []
    print(f"{len(fila)} frentes, {a.paralelo} por vez", flush=True)
    while fila or rodando:
        for pasta, (proc, tmp, modelo, tent, ini) in list(rodando.items()):
            expirou = time.time() - ini > a.timeout
            if proc.poll() is None and expirou:
                encerrar(proc)
            if proc.poll() is None:
                continue
            del rodando[pasta]
            devolver(tmp, pasta)
            dur = round(time.time() - ini)
            ok = relatorio_ok(pasta)
            avisos = avisos_formato(pasta) if ok else []
            graves = [aviso for aviso in avisos if aviso_grave(aviso)]
            tem_limite = bateu_limite(pasta)
            if tem_limite and tent == 0 and (not ok or graves):
                print(f"LIMITE {pasta.name}: volta à fila com {RESERVA}", flush=True)
                renomear_anterior(pasta, tent + 1)
                fila.append((pasta, RESERVA, 1))
                continue
            if ok and not graves:
                print(f"OK    {pasta.name} ({modelo}, {dur}s)", flush=True)
                for aviso in avisos:
                    print(f"FORMATO {pasta.name}: {aviso}", flush=True)
                # Só avisa quando o pedido manda buscar na web (o pedido de resumo proíbe).
                pede_busca = "websearch" in (pasta / "PEDIDO.md").read_text(encoding="utf-8", errors="ignore")
                if pede_busca and contar_busca(pasta) == 0:
                    print(f"SEM-BUSCA {pasta.name}", flush=True)
                    sem_busca.append(pasta.name)
            elif ok:
                for aviso in avisos:
                    print(f"FORMATO {pasta.name}: {aviso}", flush=True)
                print(f"FALHOU {pasta.name} ({modelo}, {dur}s): formato grave; relatório mantido",
                      flush=True)
                falhas.append(pasta.name)
            else:
                motivo = "tempo esgotado" if expirou else "sem RELATORIO.md válido"
                print(f"FALHOU {pasta.name} ({modelo}, {dur}s): {motivo}; ver log.jsonl", flush=True)
                falhas.append(pasta.name)
        if fila and len(rodando) < a.paralelo:
            pasta, modelo, tent = fila.pop(0)
            proc, tmp = lancar(pasta, modelo)
            rodando[pasta] = (proc, tmp, modelo, tent, time.time())
            print(f"inicio {pasta.name} ({modelo})", flush=True)
            time.sleep(a.intervalo)
        else:
            time.sleep(5)
    if sem_busca:
        print("AVISO: SEM-BUSCA em: " + ", ".join(sem_busca), flush=True)
    if falhas:
        print("FALHAS: " + ", ".join(falhas), flush=True)
    print("FIM", flush=True)
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
