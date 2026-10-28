"""Gera docs/index.html a partir de docs/modelo.html e dos arquivos de exemplo/."""
import csv
import html
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
GH = "https://github.com/VictorGit10/levantamento-ia/blob/main/exemplo/"

sys.path.insert(0, str(RAIZ / "ferramentas"))
import painel  # noqa: E402

linhas = json.loads((RAIZ / "exemplo" / "tabela.json").read_text(encoding="utf-8"))
abertos = sum(1 for l in linhas if l["acesso"] and l["acesso"] != "fechado")
resumos = sum(1 for l in linhas if l["resumo"])
com_pdf = sum(1 for r in csv.DictReader(open(RAIZ / "exemplo" / "cienciometria.csv", encoding="utf-8-sig"))
              if r.get("pdf") or r.get("pdf_alternativos"))
# Resultado real da conferência (gerado por conferir_doi.py), não uma contagem.
verif = list(csv.DictReader(open(RAIZ / "exemplo" / "verificacao.csv", encoding="utf-8-sig")))
# Uma linha por indicação de frente; o mesmo DOI pode vir de mais de uma frente.
estados = {}
for v in verif:
    estados.setdefault(v["doi"].lower(), set()).add(v["estado"])
assert all(e <= {"OK", "CONFERIR"} for e in estados.values()), "há DOI com erro ou inexistente: rode conferir_doi.py e veja"
assert len(estados) == len(linhas), "a conferência e a tabela não têm os mesmos DOIs"
n_indicacoes = len(verif)
n_repetidos = sum(1 for d in estados if sum(v["doi"].lower() == d for v in verif) > 1)
n_ok = sum(1 for e in estados.values() if e == {"OK"})
n_conferir = len(estados) - n_ok
bases = painel.bases_sem_doi((RAIZ / "exemplo" / "REFERENCIAS.md").read_text(encoding="utf-8"))

tabela = []
for l in linhas[:10]:
    autores = l.get("autores") or f'{l["autor"]} et al. ({l["ano"]})'
    ref = (f'{html.escape(autores)}. '
           f'<a href="https://doi.org/{l["doi"]}">{html.escape(l["titulo"])}</a>. '
           f'<span class="small">{html.escape(l["revista"])}</span>')
    res = f'<a href="{GH}{l["resumo"]}">ler</a>' if l["resumo"] else '<span class="small">—</span>'
    tabela.append(f'    <tr><td class="n">{l["citacoes"]}</td><td class="n">{l["fwci"]}</td>'
                  f'<td class="n">{l["percentil"]}</td><td>{ref}</td><td>{res}</td></tr>')

pagina = (RAIZ / "docs" / "modelo.html").read_text(encoding="utf-8")
for chave, valor in {"TABELA": "\n".join(tabela), "N_REFS": len(linhas), "N_INDICACOES": n_indicacoes, "N_REPETIDOS": n_repetidos, "N_OK": n_ok,
                     "N_CONFERIR": n_conferir, "N_ABERTOS": abertos, "N_RESUMOS": resumos,
                     "N_PDF": com_pdf, "N_SEM_DOI": len(bases)}.items():
    pagina = pagina.replace("{{" + chave + "}}", str(valor))
assert "{{" not in pagina, "sobrou marcador no modelo.html"
(RAIZ / "docs" / "index.html").write_text(pagina, encoding="utf-8")

# O RELATORIO.html do exemplo já traz os resumos dentro; publicado no site, ele
# abre direto no navegador. Os links "ler" de reserva apontam para o GitHub.
relatorio = (RAIZ / "exemplo" / "RELATORIO.html").read_text(encoding="utf-8")
relatorio = relatorio.replace('href="resumos/', f'href="{GH}resumos/')
(RAIZ / "docs" / "exemplo.html").write_text(relatorio, encoding="utf-8")
print(f"index.html: {len(linhas)} artigos, {n_indicacoes} indicações ({n_repetidos} repetidos), {abertos} abertos, "
      f"{resumos} resumos, {com_pdf} com PDF, {len(bases)} sem DOI")
