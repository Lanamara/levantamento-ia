"""Gera docs/index.html a partir de docs/modelo.html e dos arquivos de exemplo/."""
import csv
import html
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
GH = "https://github.com/VictorGit10/levantamento-ia/blob/main/exemplo/"
sys.path.insert(0, str(RAIZ / "ferramentas"))
import doi as doilib  # noqa: E402

linhas = json.loads((RAIZ / "exemplo" / "tabela.json").read_text(encoding="utf-8"))
abertos = sum(1 for l in linhas if l["acesso"] and l["acesso"] != "fechado")
resumos = sum(1 for l in linhas if l["resumo"])
com_pdf = sum(1 for r in csv.DictReader(open(RAIZ / "exemplo" / "cienciometria.csv", encoding="utf-8-sig"))
              if r.get("pdf") or r.get("pdf_alternativos"))
# DOIs citados nas tabelas das frentes (cada linha de tabela com DOI é uma citação).
n_dois = sum(1 for f in (RAIZ / "exemplo" / "frentes").glob("*/RELATORIO.md")
             for l in f.read_text(encoding="utf-8").splitlines() if l.startswith("|") and doilib.achar(l))

tabela = []
for l in linhas[:10]:
    ref = (f'{html.escape(l["autor"])} et al. ({l["ano"]}). '
           f'<a href="https://doi.org/{l["doi"]}">{html.escape(l["titulo"])}</a>. '
           f'<span class="small">{html.escape(l["revista"])}</span>')
    res = f'<a href="{GH}{l["resumo"]}">ler</a>' if l["resumo"] else '<span class="small">—</span>'
    tabela.append(f'    <tr><td class="n">{l["citacoes"]}</td><td class="n">{l["fwci"]}</td>'
                  f'<td class="n">{l["percentil"]}</td><td>{ref}</td><td>{res}</td></tr>')

pagina = (RAIZ / "docs" / "modelo.html").read_text(encoding="utf-8")
for chave, valor in {"TABELA": "\n".join(tabela), "N_REFS": len(linhas), "N_DOIS": n_dois,
                     "N_ABERTOS": abertos, "N_RESUMOS": resumos, "N_PDF": com_pdf}.items():
    pagina = pagina.replace("{{" + chave + "}}", str(valor))
assert "{{" not in pagina, "sobrou marcador no modelo.html"
(RAIZ / "docs" / "index.html").write_text(pagina, encoding="utf-8")
print(f"index.html: {len(linhas)} artigos, {n_dois} DOIs citados, {abertos} abertos, "
      f"{resumos} resumos, {com_pdf} com PDF")
