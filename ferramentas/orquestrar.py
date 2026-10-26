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
- Ao fim, imprime SEM-BUSCA <frente> para quem não chamou websearch no log.
- Sai com código 1 se alguma frente não produziu um relatório válido.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

RESERVA = "opencode/glm-5.3-flash-free"
LIMITE = ("FreeUsageLimitError", "Rate limit exceeded", '"status":429')
MIN_RELATORIO = 200


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


def lancar(pasta, modelo):
    # O opencode decide a pasta de trabalho pelo PWD herdado, não só pelo cwd:
    # sem isto, todos os agentes abrem na pasta de quem chamou.
    env = dict(os.environ, OPENCODE_ENABLE_EXA="1", PWD=str(pasta.resolve()))
    cmd = [shutil.which("opencode") or "opencode", "run", "--format", "json", "-m", modelo,
           "Leia PEDIDO.md e faça o que ele pede. Grave RELATORIO.md nesta pasta."]
    with open(pasta / "log.jsonl", "w", encoding="utf-8") as log:
        return subprocess.Popen(cmd, cwd=pasta, stdout=log, stderr=subprocess.STDOUT, env=env)


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
    a = ap.parse_args(argv)
    if a.paralelo < 1 or a.intervalo < 0 or a.timeout < 1:
        ap.error("--paralelo precisa ser 1 ou mais, --intervalo 0 ou mais e --timeout 1 ou mais")

    raiz = Path(a.raiz)
    fila = [(p, a.modelo, 0) for p in sorted(raiz.iterdir())
            if (p / "PEDIDO.md").exists() and not relatorio_ok(p)]
    rodando = {}
    falhas, sem_busca = [], []
    print(f"{len(fila)} frentes, {a.paralelo} por vez", flush=True)
    while fila or rodando:
        for pasta, (proc, modelo, tent, ini) in list(rodando.items()):
            expirou = time.time() - ini > a.timeout
            if proc.poll() is None and expirou:
                proc.kill()
                try:
                    proc.wait(timeout=2)
                except subprocess.TimeoutExpired:
                    pass
            if proc.poll() is None:
                continue
            del rodando[pasta]
            dur = round(time.time() - ini)
            if relatorio_ok(pasta):
                print(f"OK    {pasta.name} ({modelo}, {dur}s)", flush=True)
                # Só avisa quando o pedido manda buscar na web (o pedido de resumo proíbe).
                pede_busca = "websearch" in (pasta / "PEDIDO.md").read_text(encoding="utf-8", errors="ignore")
                if pede_busca and contar_busca(pasta) == 0:
                    print(f"SEM-BUSCA {pasta.name}", flush=True)
                    sem_busca.append(pasta.name)
            elif bateu_limite(pasta) and tent == 0:
                print(f"LIMITE {pasta.name}: volta à fila com {RESERVA}", flush=True)
                renomear_anterior(pasta, tent + 1)
                fila.append((pasta, RESERVA, 1))
                continue
            else:
                motivo = "tempo esgotado" if expirou else "sem RELATORIO.md válido"
                print(f"FALHOU {pasta.name} ({modelo}, {dur}s): {motivo}; ver log.jsonl", flush=True)
                falhas.append(pasta.name)
        if fila and len(rodando) < a.paralelo:
            pasta, modelo, tent = fila.pop(0)
            rodando[pasta] = (lancar(pasta, modelo), modelo, tent, time.time())
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
