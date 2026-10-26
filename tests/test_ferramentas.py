import csv
import subprocess
import sys
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "ferramentas"))

import cienciometria  # noqa: E402
import doi as doilib  # noqa: E402
import juntar  # noqa: E402
import orquestrar  # noqa: E402
import painel  # noqa: E402
import preparar_resumos  # noqa: E402


@pytest.mark.parametrize("texto, esperado", [
    ("doi: 10.1016/S0034-4257(01)00302-9.", "10.1016/S0034-4257(01)00302-9"),
    ('<a href="https://doi.org/10.1234/abc.def">x</a>', "10.1234/abc.def"),
    ("https://doi.org/10.1234/abc).", "10.1234/abc"),
    ("Veja 10.1000/xyz, no texto", "10.1000/xyz"),
    ("10.1016/S0034-4257(01)00302-9).", "10.1016/S0034-4257(01)00302-9"),
])
def test_doi_achar(texto, esperado):
    assert doilib.achar(texto) == esperado


def test_doi_achar_sem_doi():
    assert doilib.achar("nenhum identificador aqui") is None


def test_primeira_tabela_indentada():
    linhas = ["# x", "", "   | A | B |", "   |---|---|", "   | 1 | 2 |", "", "fim"]
    assert juntar.primeira_tabela(linhas) == (2, 5)


def test_primeira_tabela_para_na_segunda():
    linhas = ["| A | B |", "|---|---|", "| 1 | 2 |", "", "| C | D |", "|---|---|", "| 3 | 4 |"]
    assert juntar.primeira_tabela(linhas) == (0, 3)


def test_primeira_tabela_sem_tabela():
    assert juntar.primeira_tabela(["só texto"]) == (None, None)


def test_limpar_bib_chave_repetida():
    chaves = set()
    a = juntar.limpar_bib("@article{Silva_2020, title={Um}, year={2020}}", chaves)
    b = juntar.limpar_bib("@article{Silva_2020, title={Dois}, year={2021}}", chaves)
    assert a.startswith("@article{Silva_2020,")
    assert b.startswith("@article{Silva_2020a,")


def test_limpar_bib_html_ampersand_mes():
    entrada = juntar.limpar_bib(
        "@article{X, title={<i>Floresta</i> &amp; Água}, month={September}, year={2020}}", set())
    assert "<i>" not in entrada
    assert r"Floresta \& Água" in entrada
    assert "month=sep" in entrada


def test_limpar_bib_mes_sem_chaves_preserva_fechamento():
    entrada = juntar.limpar_bib("@article{X, month=September}", set())
    assert entrada == "@article{X, month=sep}"


def test_nao_confere_pdf_certo():
    texto = "doi: 10.1234/abc</a>\n" + "conteudo " * 400
    assert preparar_resumos.nao_confere(texto, "10.1234/abc", "Título") == ""


def test_nao_confere_titulo_certo():
    texto = "Biomassa florestal e carbono na silvicultura " * 80
    assert preparar_resumos.nao_confere(texto, "10.1234/abc", "Biomassa florestal carbono silvicultura") == ""


def test_nao_confere_pdf_de_outro_artigo():
    texto = "Este texto fala de peixes e oceanos. " * 100
    motivo = preparar_resumos.nao_confere(texto, "10.1234/abc", "Biomassa florestal carbono silvicultura")
    assert "outro artigo" in motivo


def test_nao_confere_texto_vazio():
    assert "sem texto" in preparar_resumos.nao_confere("", "10.1234/abc", "Título")


def test_bateu_limite_ignora_nao_objeto(tmp_path):
    (tmp_path / "log.jsonl").write_text("\n".join([
        "FreeUsageLimitError",
        '"FreeUsageLimitError"',
        '[{"type": "error", "message": "FreeUsageLimitError"}]',
        '{"type": "tool", "part": {"text": "FreeUsageLimitError"}}',
    ]), encoding="utf-8")
    assert orquestrar.bateu_limite(tmp_path) is False


def test_bateu_limite_evento_de_erro(tmp_path):
    (tmp_path / "log.jsonl").write_text(
        '{"type": "error", "message": "Rate limit exceeded"}\n', encoding="utf-8")
    assert orquestrar.bateu_limite(tmp_path) is True


def test_contar_busca(tmp_path):
    (tmp_path / "log.jsonl").write_text("\n".join([
        '{"type": "tool_use", "part": {"tool": "websearch"}}',
        '{"type": "tool_use", "part": {"tool": "webfetch"}}',
        '{"type": "tool_use", "part": {"tool": "websearch"}}',
        "não é json",
    ]), encoding="utf-8")
    assert orquestrar.contar_busca(tmp_path) == 2


def test_relatorio_ok(tmp_path):
    (tmp_path / "RELATORIO.md").write_text("x" * 199, encoding="utf-8")
    assert orquestrar.relatorio_ok(tmp_path) is False
    (tmp_path / "RELATORIO.md").write_text("x" * 200, encoding="utf-8")
    assert orquestrar.relatorio_ok(tmp_path) is True


def test_renomear_anterior(tmp_path):
    (tmp_path / "RELATORIO.md").write_text("parcial", encoding="utf-8")
    (tmp_path / "log.jsonl").write_text("log", encoding="utf-8")
    orquestrar.renomear_anterior(tmp_path, 1)
    assert (tmp_path / "RELATORIO.parcial1.md").read_text(encoding="utf-8") == "parcial"
    assert (tmp_path / "log.anterior1.jsonl").read_text(encoding="utf-8") == "log"
    assert not (tmp_path / "RELATORIO.md").exists()
    assert not (tmp_path / "log.jsonl").exists()


def test_formatar_autores():
    assert painel.formatar_autores(["Silva"], "2020") == "Silva (2020)"
    assert painel.formatar_autores(["Silva", "Souza"], "2020") == "Silva & Souza (2020)"
    assert painel.formatar_autores(["Silva", "Souza", "Lima"], "2020") == "Silva et al. (2020)"
    assert painel.formatar_autores([], "2020") == ""


def test_celula_escapa_pipe():
    assert painel.celula("a | b") == r"a \| b"
    assert painel.celula(r"a \| b") == r"a \| b"


def test_autor_ano_do_bib():
    bib = ("@article{x, DOI={10.1/x}, author={Silva, A. and Souza, B. and Lima, C.}, "
           "year={2020}}")
    assert painel.autor_ano_do_bib(bib)["10.1/x"] == (["Silva", "Souza", "Lima"], "2020")


def test_bases_sem_doi():
    texto = """
| Autores (ano) | Título | Revista | DOI/link |
|---|---|---|---|
| Silva (2020) | Artigo | Rev | https://doi.org/10.1234/abc |
| IBGE (2026) | Base oficial | Base | https://sidra.ibge.gov.br/tabela/5930 |
"""
    assert painel.bases_sem_doi(texto) == [
        ("IBGE (2026)", "Base oficial", "https://sidra.ibge.gov.br/tabela/5930")]


def test_juntar_preserva_notas_e_marcadores(tmp_path, monkeypatch):
    frentes = tmp_path / "frentes"
    frente = frentes / "1-teste"
    frente.mkdir(parents=True)
    (frente / "RELATORIO.md").write_text(
        "# Relatório\n\n"
        "**Nota de método:** não havia busca web nesta sessão.\n\n"
        "| Autores (ano) | Título | Revista | DOI/link |\n"
        "|---|---|---|---|\n"
        "| Silva & Souza (2020) | Um artigo | Rev | https://doi.org/10.1234/abc **†** |\n",
        encoding="utf-8")
    monkeypatch.setattr(
        juntar, "bibtex",
        lambda doi: f"@article{{X, DOI={{{doi}}}, title={{T}}, author={{Silva, A. and Souza, B.}}, year={{2020}}}}")
    saida = tmp_path / "saida"
    juntar.main([str(frentes), str(saida), "Tema"])
    refs = (saida / "REFERENCIAS.md").read_text(encoding="utf-8")
    assert "não havia busca web" in refs
    assert "**†**" in refs
    assert "## 1-teste" in refs
    assert "Um artigo" in refs
    assert "10.1234/abc" in (saida / "referencias.bib").read_text(encoding="utf-8")


def test_cienciometria_separa_falhas(tmp_path, monkeypatch, capsys):
    bib = tmp_path / "referencias.bib"
    bib.write_text("@article{a, DOI={10.1/ok}}\n@article{b, DOI={10.1/falha}}\n", encoding="utf-8")
    saida = tmp_path / "cienciometria.csv"

    def fake(doi, email):
        if doi.endswith("falha"):
            raise RuntimeError("sem rede")
        return {"doi": doi, "ano": 2020, "primeiro_autor": "Silva", "titulo": "T",
                "revista": "R", "citacoes": 1, "fwci": 1.0, "percentil": 50,
                "acesso": "gold", "pdf": "", "pdf_alternativos": ""}

    monkeypatch.setattr(cienciometria, "consulta", fake)
    monkeypatch.setattr(cienciometria.time, "sleep", lambda *_: None)
    cienciometria.main([str(bib), str(saida)])
    with open(saida, encoding="utf-8-sig") as f:
        linhas = list(csv.DictReader(f))
    assert [r["doi"] for r in linhas] == ["10.1/ok"]
    with open(tmp_path / "cienciometria-falhas.csv", encoding="utf-8-sig") as f:
        falhas = list(csv.DictReader(f))
    assert falhas == [{"doi": "10.1/falha", "erro": "RuntimeError: sem rede"}]
    assert "1 falharam" in capsys.readouterr().out


@pytest.mark.parametrize("script", [
    "juntar.py", "painel.py", "cienciometria.py", "conferir_doi.py",
    "preparar_resumos.py", "extrair_pdf.py", "orquestrar.py",
])
def test_argparse_help(script):
    r = subprocess.run([sys.executable, str(RAIZ / "ferramentas" / script), "--help"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    assert r.returncode == 0, r.stderr
    assert "usage:" in r.stdout.lower()
