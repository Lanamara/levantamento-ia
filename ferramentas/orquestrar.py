"""Orquestra vários `opencode run` com modelos grátis numa fila, poucos de cada vez.

Uso:
    python orquestrar.py <pasta-do-trabalho> [--paralelo 2] [--modelo opencode/deepseek-v4.1-flash-free]

A pasta tem uma subpasta por frente, cada uma com PEDIDO.md. Cada frente roda
`opencode run` dentro da própria subpasta e deve gravar RELATORIO.md ali.
- No máximo --paralelo ao mesmo tempo, com intervalo entre os inícios (o grátis
  limita requisições por minuto por IP).
- Se o log mostrar limite (429 / FreeUsageLimit), a frente volta para o fim da
  fila uma vez, com o modelo reserva.
- Frente que já tem RELATORIO.md é pulada (dá para rodar de novo sem refazer).
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


def lancar(pasta, modelo):
    # O opencode decide a pasta de trabalho pelo PWD herdado, não só pelo cwd:
    # sem isto, todos os agentes abrem na pasta de quem chamou.
    env = dict(os.environ, OPENCODE_ENABLE_EXA="1", PWD=str(pasta.resolve()))
    log = open(pasta / "log.jsonl", "w", encoding="utf-8")
    cmd = [shutil.which("opencode") or "opencode", "run", "--format", "json", "-m", modelo,
           "Leia PEDIDO.md e faça o que ele pede. Grave RELATORIO.md nesta pasta."]
    return subprocess.Popen(cmd, cwd=pasta, stdout=log, stderr=subprocess.STDOUT, env=env)


def bateu_limite(pasta):
    """Só conta erro de limite vindo de evento de erro, não de texto que o agente leu."""
    try:
        linhas = (pasta / "log.jsonl").read_text(encoding="utf-8", errors="ignore").splitlines()
    except OSError:
        return False
    for linha in linhas:
        try:
            ev = json.loads(linha)
        except ValueError:
            ev = None
        if ev is not None and ev.get("type") != "error":
            continue
        if any(s in linha for s in LIMITE):
            return True
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("raiz")
    ap.add_argument("--paralelo", type=int, default=2)
    ap.add_argument("--modelo", default="opencode/deepseek-v4.1-flash-free")
    ap.add_argument("--intervalo", type=int, default=20, help="segundos entre inícios")
    a = ap.parse_args()
    if a.paralelo < 1 or a.intervalo < 0:
        ap.error("--paralelo precisa ser 1 ou mais, e --intervalo 0 ou mais")

    raiz = Path(a.raiz)
    fila = [(p, a.modelo, 0) for p in sorted(raiz.iterdir())
            if (p / "PEDIDO.md").exists() and not (p / "RELATORIO.md").exists()]
    rodando = {}
    print(f"{len(fila)} frentes, {a.paralelo} por vez", flush=True)
    while fila or rodando:
        for pasta, (proc, modelo, tent, ini) in list(rodando.items()):
            if proc.poll() is None:
                continue
            del rodando[pasta]
            dur = round(time.time() - ini)
            if (pasta / "RELATORIO.md").exists():
                print(f"OK    {pasta.name} ({modelo}, {dur}s)", flush=True)
            elif bateu_limite(pasta) and tent == 0:
                print(f"LIMITE {pasta.name}: volta à fila com {RESERVA}", flush=True)
                fila.append((pasta, RESERVA, 1))
            else:
                print(f"FALHOU {pasta.name} ({modelo}, {dur}s): ver log.jsonl", flush=True)
        if fila and len(rodando) < a.paralelo:
            pasta, modelo, tent = fila.pop(0)
            rodando[pasta] = (lancar(pasta, modelo), modelo, tent, time.time())
            print(f"inicio {pasta.name} ({modelo})", flush=True)
            time.sleep(a.intervalo)
        else:
            time.sleep(5)
    print("FIM", flush=True)


if __name__ == "__main__":
    sys.exit(main())
