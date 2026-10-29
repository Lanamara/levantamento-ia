"""Mapa de lacunas: o que os artigos lidos cobrem (sensor, variável, plantio, região, método).

Uso: python lacunas.py <pasta-do-projeto>

Lê <pasta>/resumos/*/RELATORIO.md e procura palavras-chave nas seções
1 (Referência), 2 (Pergunta), 3 (Área e dados) e 4 (Método). As seções 6 e 7
ficam de fora de propósito: nelas o resumo costuma dizer o que o artigo NÃO faz
("não separa eucalipto de Pinus"), o que geraria marcações falsas.

Grava:
- <pasta>/lacunas.csv  uma linha por artigo, com as marcações e o trecho de
  resultado que traz R², RMSE ou acurácia (copiado do resumo, com a página);
- <pasta>/LACUNAS.md   contagens por sensor x variável e sensor x plantio,
  combinações vazias e a lista por artigo.

É uma triagem automática por palavras-chave: confira no resumo antes de usar
um número na tese. Artigos sem resumo (PDF que não foi lido) não entram.
"""
import argparse
import csv
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from projeto import barrar_exemplo, opcao_exemplo  # noqa: E402

# Cada categoria: rótulo -> expressão regular (sem acento, minúsculas).
SENSORES = {
    "GEDI": r"\bgedi\b",
    "ICESat-2": r"icesat-?2|\batl08\b",
    "LiDAR aéreo": r"airborne (?:laser|lidar)|\bals\b|lidar aerotransportado|laser aerotransportado",
    "LiDAR/imagem de drone": r"\buav\b|\bdrone|\bvant\b|\brpa\b",
    "LiDAR terrestre": r"\btls\b|terrestrial laser|laser terrestre",
    "Hiperespectral orbital": r"\bprisma\b|\benmap\b|\bhyperion\b|\bdesis\b|\bemit\b",
    "Hiperespectral (outro)": r"hyperspectral|hiperespectral",
    "Sentinel-2": r"sentinel-?2",
    "Landsat": r"landsat",
    "MODIS": r"\bmodis\b",
    "Radar (SAR)": r"\bsar\b|sentinel-?1|\balos\b|palsar|\bradar\b|nisar|polsar|biomass mission",
}
VARIAVEIS = {
    "Biomassa": r"biomass|biomassa|\bagbd?\b",
    "Carbono": r"carbon|carbono",
    "Altura": r"canopy height|tree height|\baltura\b",
    "Volume": r"\bvolume\b",
    "Idade": r"\bage\b|\bidade\b|stand age|planting history",
    "Espécies": r"\bspecies\b|\bespecies\b",
    "Área plantada": r"mapeament|mapping of plantation|area plantada|planted area",
    "Fragilidade/aptidão": r"fragilidade|fragility|aptidao|suitability|vulnerab",
}
PLANTIOS = {
    "Eucalipto": r"eucalyp|eucalipto",
    "Pinus": r"\bpinus\b|\bpine\b",
    "Seringueira": r"rubber|hevea|seringueira",
    "Floresta plantada (geral)": r"plantation|plantio|planted forest|floresta plantada|silvicultur",
    "Floresta nativa/tropical": r"tropical forest|floresta tropical|natural forest|floresta nativa|amazon",
    "Savana/Cerrado": r"savanna|savana|cerrado",
}
REGIOES = {
    "Goiás": r"\bgoias\b",
    "Cerrado": r"cerrado",
    "Brasil": r"\bbrasil\b|\bbrazil|mato grosso|minas gerais|sao paulo|bahia|parana|distrito federal|espirito santo",
}
METODOS = {
    "Random Forest": r"random forest|\brf\b",
    "XGBoost/boosting": r"xgboost|gradient boost|lightgbm|catboost",
    "Redes neurais/deep learning": r"\bcnn\b|deep learning|neural network|rede neural|redes neurais|u-net|transformer|aprendizado profundo|convolucion",
    "SVM": r"\bsvm\b|\bsvr\b|support vector",
    "Regressão": r"regress|lasso|\bols\b",
    "AHP/multicritério": r"\bahp\b|analytic hierarchy|multicriter|\bwlc\b",
    "Máxima verossimilhança": r"maxver|maxima verossimilhanca|maximum likelihood",
}
CATEGORIAS = {"sensores": SENSORES, "variaveis": VARIAVEIS, "plantios": PLANTIOS,
              "regioes": REGIOES, "metodos": METODOS}


def sem_acento(t):
    return "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn")


def secoes(texto):
    """{número: texto} das seções '## N. Título' do resumo."""
    partes = re.split(r"^##\s*(\d+)\.", texto, flags=re.M)
    return {int(partes[i]): partes[i + 1] for i in range(1, len(partes) - 1, 2)}


NEGACAO = re.compile(r"\b(?:nao|nenhum|nenhuma|sem|not|without|nor)\b[^.;\n]{0,40}$")


def marcar(texto, dicionario):
    """Rótulos cujo termo aparece sem negação logo antes ("nenhum sítio em Goiás" não conta)."""
    alvo = sem_acento(texto).lower()
    saida = []
    for rotulo, rx in dicionario.items():
        for m in re.finditer(rx, alvo):
            if not NEGACAO.search(alvo[max(0, m.start() - 60):m.start()]):
                saida.append(rotulo)
                break
    return saida


def trecho_metrica(texto):
    """Primeira linha da seção 5 com R², RMSE ou acurácia (Kappa, OA), como está no resumo."""
    for linha in texto.splitlines():
        if re.search(r"R²|R2\b|RMSE|rRMSE|kappa|acur[aá]cia|overall accuracy|\bOA\b", linha, re.I):
            return re.sub(r"\s+", " ", linha.strip(" -*")).strip()[:300]
    return ""


def analisar(pasta):
    linhas = []
    for rel in sorted(Path(pasta).glob("resumos/*/RELATORIO.md")):
        texto = rel.read_text(encoding="utf-8")
        sec = secoes(texto)
        base = " ".join(sec.get(n, "") for n in (1, 2, 3, 4))
        titulo = re.search(r"^#\s*RELAT[ÓO]RIO\s*[—-]\s*(.+)$", texto, re.M)
        linha = {"artigo": rel.parent.name, "autor_ano": titulo.group(1).strip() if titulo else rel.parent.name}
        for nome, dic in CATEGORIAS.items():
            linha[nome] = marcar(base, dic)
        if "Hiperespectral orbital" in linha["sensores"] and "Hiperespectral (outro)" in linha["sensores"]:
            linha["sensores"].remove("Hiperespectral (outro)")
        linha["metrica"] = trecho_metrica(sec.get(5, ""))
        linhas.append(linha)
    return linhas


def matriz(linhas, cat_linhas, cat_colunas):
    rotulos_l = list(CATEGORIAS[cat_linhas])
    rotulos_c = list(CATEGORIAS[cat_colunas])
    return rotulos_l, rotulos_c, {
        (a, b): sum(1 for l in linhas if a in l[cat_linhas] and b in l[cat_colunas])
        for a in rotulos_l for b in rotulos_c}


def tabela_md(titulo, linhas, cat_l, cat_c):
    rl, rc, m = matriz(linhas, cat_l, cat_c)
    md = [f"## {titulo}", "", "| | " + " | ".join(rc) + " |", "|---|" + "---:|" * len(rc)]
    for a in rl:
        md.append(f"| {a} | " + " | ".join(str(m[(a, b)]) or "0" for b in rc) + " |")
    return md + [""]


def combinacoes_vazias(linhas):
    """Combinações centrais do projeto com nenhum ou só um artigo lido."""
    alvos = [("Hiperespectral orbital", "Eucalipto"), ("Hiperespectral orbital", "Biomassa"),
             ("GEDI", "Eucalipto"), ("GEDI", "Savana/Cerrado"), ("ICESat-2", "Eucalipto"),
             ("GEDI", "Seringueira"), ("Sentinel-2", "Seringueira")]
    saida = []
    for s, x in alvos:
        cat = "plantios" if x in PLANTIOS else "variaveis"
        n = sum(1 for l in linhas if s in l["sensores"] and x in l[cat])
        artigos = [l["artigo"] for l in linhas if s in l["sensores"] and x in l[cat]]
        saida.append((s, x, n, artigos))
    goias = [l for l in linhas if "Goiás" in l["regioes"]]
    saida.append(("Goiás + Biomassa ou Carbono", "",
                  sum(1 for l in goias if {"Biomassa", "Carbono"} & set(l["variaveis"])),
                  [l["artigo"] for l in goias if {"Biomassa", "Carbono"} & set(l["variaveis"])]))
    return saida


def gravar(pasta, linhas):
    pasta = Path(pasta)
    with open(pasta / "lacunas.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["artigo", "autor_ano"] + list(CATEGORIAS) + ["metrica"])
        for l in linhas:
            w.writerow([l["artigo"], l["autor_ano"]] + ["; ".join(l[c]) for c in CATEGORIAS] + [l["metrica"]])
    md = ["# Mapa de lacunas", "",
          f"{len(linhas)} artigos com resumo de leitura integral. Marcações por palavras-chave nas seções "
          "1 a 4 de cada resumo (referência, pergunta, área e dados, método): é uma triagem, confira no "
          "resumo antes de usar. Artigos sem resumo não entram.", ""]
    md += ["## Combinações centrais do projeto", "", "| Combinação | Artigos lidos | Quais |", "|---|---:|---|"]
    for s, x, n, artigos in combinacoes_vazias(linhas):
        rot = f"{s} × {x}" if x else s
        md.append(f"| {rot} | {n} | {', '.join(artigos) or '—'} |")
    md.append("")
    md += tabela_md("Sensor × variável estimada", linhas, "sensores", "variaveis")
    md += tabela_md("Sensor × tipo de plantio ou vegetação", linhas, "sensores", "plantios")
    md += tabela_md("Método × variável estimada", linhas, "metodos", "variaveis")
    md += ["## Por artigo", "", "| Artigo | Sensores | Variáveis | Plantio | Região | Método | Métrica (trecho do resumo) |",
           "|---|---|---|---|---|---|---|"]
    for l in linhas:
        cel = [", ".join(l[c]) or "—" for c in ("sensores", "variaveis", "plantios", "regioes", "metodos")]
        md.append(f"| [{l['autor_ano']}](resumos/{l['artigo']}/RELATORIO.md) | " + " | ".join(cel)
                  + f" | {l['metrica'].replace('|', '/') or '—'} |")
    (pasta / "LACUNAS.md").write_text("\n".join(md) + "\n", encoding="utf-8")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Mapa de lacunas a partir dos resumos de leitura integral.")
    ap.add_argument("pasta", help="pasta do projeto (com resumos/)")
    opcao_exemplo(ap)
    a = ap.parse_args(argv)
    barrar_exemplo(ap, a, a.pasta)
    linhas = analisar(a.pasta)
    if not linhas:
        print("AVISO: nenhum resumo encontrado em resumos/*/RELATORIO.md")
        return 1
    gravar(a.pasta, linhas)
    print(f"{len(linhas)} artigos -> {Path(a.pasta) / 'LACUNAS.md'} e lacunas.csv")
    return 0


if __name__ == "__main__":
    sys.exit(main())
