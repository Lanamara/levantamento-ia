"""Avisa quando sai versão nova das bases de dados usadas no projeto.

Uso: python bases.py <pasta-do-projeto>

Lê <pasta>/bases.json:

    {
      "PEVS (IBGE, tabela 5930)": {"tipo": "ibge", "agregado": 5930, "versao_usada": 2025},
      "MapBiomas Brasil": {"tipo": "pagina", "url": "https://brasil.mapbiomas.org/",
                           "padrao": "Cole[çc][ãa]o\\s+(\\d{1,2})\\b", "versao_usada": 11}
    }

- tipo "ibge": consulta https://servicodados.ibge.gov.br/api/v3/agregados/<n>/periodos
  e compara o ano mais recente com `versao_usada`;
- tipo "pagina": baixa a página, procura `padrao` (expressão regular com um grupo
  numérico) e compara o maior número encontrado com `versao_usada`.

Estados: NOVA (saiu versão maior que a usada), ATUAL, NAO-VERIFICADO (a página
ou a API não respondeu, ou o padrão não achou nada; confira à mão).
Grava <pasta>/BASES.md e, se houver NOVA, <pasta>/bases_aviso.txt (usado pela
atualização mensal para abrir um aviso no GitHub). Sai com 0 mesmo com NOVA.
"""
import argparse
import html
import json
import re
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from projeto import barrar_exemplo, opcao_exemplo  # noqa: E402

UA = {"User-Agent": "levantamento-ia/1.0 (verificador de versões; uso acadêmico)"}


def baixar(url):
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", errors="replace")


def versao_ibge(agregado, baixar=baixar):
    """Ano mais recente disponível numa tabela do IBGE (API de agregados v3)."""
    periodos = json.loads(baixar(f"https://servicodados.ibge.gov.br/api/v3/agregados/{agregado}/periodos"))
    anos = [int(p["id"]) for p in periodos if str(p.get("id", "")).isdigit()]
    return max(anos) if anos else None


def versao_pagina(url, padrao, baixar=baixar):
    """Maior número capturado por `padrao` no texto da página."""
    texto = re.sub(r"<[^>]+>", " ", baixar(url))
    texto = html.unescape(texto)
    numeros = [int(g) for m in re.finditer(padrao, texto, re.I) for g in m.groups() if g and g.isdigit()]
    return max(numeros) if numeros else None


def verificar(bases, baixar=baixar):
    linhas = []
    for nome, cfg in bases.items():
        usada = cfg.get("versao_usada")
        try:
            if cfg["tipo"] == "ibge":
                achada = versao_ibge(cfg["agregado"], baixar)
                fonte = f"API do IBGE, agregado {cfg['agregado']}"
            else:
                achada = versao_pagina(cfg["url"], cfg["padrao"], baixar)
                fonte = cfg["url"]
            erro = ""
        except Exception as e:
            achada, fonte, erro = None, cfg.get("url") or f"agregado {cfg.get('agregado')}", f"{type(e).__name__}: {e}"
        if achada is None:
            estado = "NAO-VERIFICADO"
        elif usada is not None and achada > usada:
            estado = "NOVA"
        else:
            estado = "ATUAL"
        linhas.append({"base": nome, "estado": estado, "usada": usada, "achada": achada,
                       "fonte": fonte, "erro": erro})
    return linhas


def gravar(pasta, linhas, hoje):
    pasta = Path(pasta)
    md = ["# Versões das bases de dados", "",
          f"Verificado em {hoje}. NOVA = saiu versão maior que a usada no projeto; "
          "NAO-VERIFICADO = a fonte não respondeu ou mudou de formato (confira à mão). "
          "Depois de atualizar o projeto, mude `versao_usada` em `bases.json`.", "",
          "| Base | Estado | Versão usada | Mais recente encontrada | Fonte |", "|---|---|---:|---:|---|"]
    for l in linhas:
        achada = l["achada"] if l["achada"] is not None else "—"
        fonte = l["fonte"] + (f" ({l['erro']})" if l["erro"] else "")
        md.append(f"| {l['base']} | {l['estado']} | {l['usada']} | {achada} | {fonte} |")
    (pasta / "BASES.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    novas = [l for l in linhas if l["estado"] == "NOVA"]
    aviso = pasta / "bases_aviso.txt"
    if novas:
        aviso.write_text("\n".join(f"- {l['base']}: versão {l['achada']} disponível (o projeto usa {l['usada']}). "
                                   f"Fonte: {l['fonte']}" for l in novas) + "\n", encoding="utf-8")
    elif aviso.exists():
        aviso.unlink()
    return novas


def main(argv=None, hoje=None):
    import datetime
    ap = argparse.ArgumentParser(description="Verifica se saíram versões novas das bases de dados.")
    ap.add_argument("pasta", help="pasta do projeto (com bases.json)")
    opcao_exemplo(ap)
    a = ap.parse_args(argv)
    barrar_exemplo(ap, a, a.pasta)
    bases = json.loads((Path(a.pasta) / "bases.json").read_text(encoding="utf-8"))
    linhas = verificar(bases)
    novas = gravar(a.pasta, linhas, (hoje or datetime.date.today()).isoformat())
    for l in linhas:
        print(f"{l['estado']}\t{l['base']}\tusada {l['usada']}\tencontrada {l['achada']}"
              + (f"\t{l['erro']}" if l["erro"] else ""), flush=True)
    print(f"{len(novas)} base(s) com versão nova -> {Path(a.pasta) / 'BASES.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
