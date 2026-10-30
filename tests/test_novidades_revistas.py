"""Testes das partes acrescentadas no fork: revistas, lista própria, atualização e relatório.

Nenhum teste usa a rede: as respostas do OpenAlex e do Crossref são simuladas.
"""
import csv
import datetime
import json
import sys
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "ferramentas"))

import atualizar  # noqa: E402
import conferir_lista  # noqa: E402
import painel  # noqa: E402
import publicar  # noqa: E402
import revistas  # noqa: E402

FONTE_OK = {"display_name": "Remote Sensing of Environment", "issn_l": "0034-4257",
            "issn": ["0034-4257", "1879-0704"], "host_organization_name": "Elsevier BV",
            "is_in_doaj": False, "is_core": True, "apc_usd": 3790,
            "summary_stats": {"h_index": 300}}
FONTE_FORA = {"display_name": "Revista X", "issn_l": "1234-5678", "issn": ["1234-5678"],
              "host_organization_name": "Editora X", "is_in_doaj": False, "is_core": False}


# --- revistas -------------------------------------------------------------

def test_issn_normal():
    assert revistas.issn_normal("23171782") == "2317-1782"
    assert revistas.issn_normal("0034-425x") == "0034-425X"
    assert revistas.issn_normal("abc") == ""


def test_indicadores_ok_por_cwts():
    ind = revistas.indicadores(FONTE_OK)
    assert ind["sinal_revista"] == "ok"
    assert ind["cwts_core"] == "sim" and ind["doaj"] == "não"
    assert ind["editora"] == "Elsevier BV" and ind["h_index_revista"] == 300


def test_indicadores_conferir_sem_listas():
    assert revistas.indicadores(FONTE_FORA)["sinal_revista"] == "conferir"


def test_indicadores_qualis_tira_do_conferir():
    ind = revistas.indicadores(FONTE_FORA, {"1234-5678": "B1"})
    assert ind["qualis"] == "B1" and ind["sinal_revista"] == "ok"


def test_indicadores_retratado_tem_prioridade():
    assert revistas.indicadores(FONTE_OK, retratado=True)["sinal_revista"] == "retratado"


def test_indicadores_sem_fonte():
    assert revistas.indicadores({})["sinal_revista"] == ""


def test_ler_qualis_ponto_e_virgula_fica_o_melhor(tmp_path):
    p = tmp_path / "qualis.csv"
    p.write_text("ISSN;Título;Área de Avaliação;Estrato\n"
                 "1234-5678;Revista X;GEOGRAFIA;B2\n"
                 "12345678;Revista X;CIÊNCIAS AMBIENTAIS;A3\n", encoding="utf-8")
    assert revistas.ler_qualis(p) == {"1234-5678": "A3"}


def test_ler_qualis_sem_colunas(tmp_path):
    p = tmp_path / "q.csv"
    p.write_text("a,b\n1,2\n", encoding="utf-8")
    with pytest.raises(ValueError):
        revistas.ler_qualis(p)


def test_do_work_usa_fonte_completa():
    class Fontes:
        def __call__(self, sid):
            assert sid == "https://openalex.org/S1"
            return FONTE_OK
    w = {"primary_location": {"source": {"id": "https://openalex.org/S1", "display_name": "RSE"}},
         "is_retracted": False}
    saida = revistas.do_work(w, Fontes())
    assert saida["revista"] == "Remote Sensing of Environment" and saida["sinal_revista"] == "ok"


# --- conferir_lista -------------------------------------------------------

REF = ("CERIANI, R. et al. Hyperspectral and LiDAR space-borne data for assessing structure and "
       "above-ground biomass in mixed mountain forests. Remote Sensing of Environment, v. 305, "
       "p. 114906, 2025. DOI: https://doi.org/10.1016/j.rse.2024.114906.")


def msg(volume="305", ano=2025, titulo=None):
    return {"title": [titulo or "Hyperspectral and LiDAR space-borne data for assessing structure "
                      "and above-ground biomass in mixed mountain forests"],
            "container-title": ["Remote Sensing of Environment"], "volume": volume,
            "page": "114906", "issued": {"date-parts": [[ano]]}}


def test_separar_por_paragrafo_ignora_cabecalho():
    texto = "REFERÊNCIAS\n\n" + REF + "\n\nROSS, J. L. S. Ecogeografia do Brasil. São Paulo: Oficina de Textos, 2012.\n"
    assert len(conferir_lista.separar(texto)) == 2


def test_anos_ignora_doi():
    assert conferir_lista.anos(REF) == {"2025"}


def test_comparar_ok():
    assert conferir_lista.comparar(REF, conferir_lista.registro_crossref(msg()))[0] == "OK"


def test_comparar_volume_e_ano_diferentes():
    estado, obs = conferir_lista.comparar(REF, conferir_lista.registro_crossref(msg("303", 2024)))
    assert estado == "CONFERIR" and "volume" in obs and "ano" in obs


def test_comparar_aceita_ano_impresso():
    m = msg(ano=2024)
    m["published-print"] = {"date-parts": [[2025, 4]]}
    assert conferir_lista.comparar(REF, conferir_lista.registro_crossref(m))[0] == "OK"


def test_comparar_titulo_difere():
    estado, _ = conferir_lista.comparar(REF, conferir_lista.registro_crossref(msg(titulo="Algo totalmente diferente sobre peixes")))
    assert estado == "TITULO-DIFERE"


def test_sugerir_so_quando_titulo_e_ano_batem():
    ref = "ROSS, J. Mapping forest age from space using machine learning. RSE, 2022."
    bom = {"title": "Mapping forest age from space using machine learning", "publication_year": 2022,
           "doi": "https://doi.org/10.1/abc"}
    ano_errado = dict(bom, publication_year=2019)
    assert conferir_lista.sugerir(ref, [ano_errado]) is None
    assert conferir_lista.sugerir(ref, [ano_errado, bom])["doi"] == "10.1/abc"


def test_conferir_e_gravar(tmp_path):
    refs = [REF, "ROSS, J. L. S. Ecogeografia do Brasil: subsídios para o planejamento ambiental. 2012."]
    linhas = conferir_lista.conferir(refs, crossref=lambda d: ("ok", msg()),
                                     openalex=lambda *a: [])
    assert [l["estado"] for l in linhas] == ["OK", "SEM-DOI"]
    conferir_lista.gravar(linhas, tmp_path)
    assert conferir_lista.dois_citados(tmp_path) == {"10.1016/j.rse.2024.114906"}
    assert "SEM-DOI" in (tmp_path / "MINHAS_REFERENCIAS.md").read_text(encoding="utf-8")


# --- atualizar ------------------------------------------------------------

def projeto(tmp_path):
    (tmp_path / "consultas.json").write_text(json.dumps({
        "desde": "2026-10-29", "frentes": {"1-a": "GEDI AND biomass", "2-b": "EnMAP"}}), encoding="utf-8")
    (tmp_path / "referencias.bib").write_text("@article{x, DOI={10.1/ja-tenho}}\n", encoding="utf-8")
    return tmp_path


def work(doi, titulo="T", retratado=False):
    return {"doi": f"https://doi.org/{doi}", "title": titulo, "publication_year": 2026,
            "publication_date": "2026-11-10", "cited_by_count": 0, "is_retracted": retratado,
            "authorships": [{"author": {"display_name": "Ana Silva"}}],
            "primary_location": {"source": {"id": "S1", "display_name": "Revista X"}}}


class FontesFalsas:
    email, api_key = "", ""

    def __call__(self, sid):
        return FONTE_FORA


def test_data_inicio_usa_janela_sem_passar_do_desde(tmp_path):
    p = projeto(tmp_path)
    cfg = atualizar.ler_consultas(p)
    hoje = datetime.date(2026, 12, 1)
    assert atualizar.data_inicio(cfg, p, hoje) == "2026-10-29"
    (p / "atualizacao.json").write_text('{"ultima_busca": "2027-03-01"}', encoding="utf-8")
    assert atualizar.data_inicio(cfg, p, hoje) == "2026-12-31"


def test_url_busca_tem_filtro_e_tipos():
    url = atualizar.url_busca('"GEDI" AND biomass', "2026-10-01", "article|review")
    assert "search.title_and_abstract=" in url
    assert "from_publication_date%3A2026-10-01%2Ctype%3Aarticle%7Creview" in url
    assert "per_page=100" in url


def test_buscar_descarta_conhecidos_e_repetidos(tmp_path):
    p = projeto(tmp_path)
    respostas = {
        "1-a": {"meta": {"count": 3}, "results": [work("10.1/ja-tenho"), work("10.1/novo"), work("10.1/dois")]},
        "2-b": {"meta": {"count": 150}, "results": [work("10.1/novo"), work("10.1/ret", retratado=True)]},
    }

    def get(url, email, key):
        return respostas["1-a"] if "GEDI" in url else respostas["2-b"]

    novas, avisos = atualizar.buscar(atualizar.ler_consultas(p), "2026-10-29", datetime.date(2026, 11, 1),
                                     atualizar.dois_conhecidos(p), FontesFalsas(), {}, get=get)
    assert [n["doi"] for n in novas] == ["10.1/novo", "10.1/dois", "10.1/ret"]
    assert novas[-1]["sinal_revista"] == "retratado" and novas[0]["sinal_revista"] == "conferir"
    assert any(a.startswith("AMPLA 2-b") for a in avisos)


def test_main_grava_e_acumula(tmp_path, monkeypatch):
    p = projeto(tmp_path)
    lotes = iter([[work("10.1/um")], [work("10.1/um"), work("10.1/dois")]])

    def get(url, email, key):
        return {"meta": {"count": 1}, "results": next(lotes) if "GEDI" in url else []}

    monkeypatch.setattr(atualizar.revistas, "get_json", get)
    monkeypatch.setattr(atualizar.revistas, "Fontes", lambda *a: FontesFalsas())
    monkeypatch.setattr(atualizar.buscar, "__defaults__", (get,))
    assert atualizar.main([str(p)], hoje=datetime.date(2026, 11, 1)) == 0
    assert atualizar.main([str(p)], hoje=datetime.date(2026, 12, 1)) == 0
    with open(p / "novidades.csv", encoding="utf-8") as f:
        todas = list(csv.DictReader(f))
    assert [(r["doi"], r["data_busca"]) for r in todas] == [("10.1/um", "2026-11-01"), ("10.1/dois", "2026-12-01")]
    md = (p / "NOVIDADES.md").read_text(encoding="utf-8")
    assert md.index("2026-12-01") < md.index("2026-11-01")
    assert json.loads((p / "atualizacao.json").read_text())["ultima_busca"] == "2026-12-01"


def test_main_com_erro_nao_avanca_data(tmp_path, monkeypatch):
    p = projeto(tmp_path)

    def get(url, email, key):
        raise OSError("sem rede")

    monkeypatch.setattr(atualizar.revistas, "Fontes", lambda *a: FontesFalsas())
    monkeypatch.setattr(atualizar.buscar, "__defaults__", (get,))
    assert atualizar.main([str(p)], hoje=datetime.date(2026, 11, 1)) == 1
    assert not (p / "atualizacao.json").exists()


# --- painel e relatório -----------------------------------------------------

def test_painel_e_publicar_mostram_indicadores(tmp_path):
    (tmp_path / "frentes" / "1-a").mkdir(parents=True)
    (tmp_path / "frentes" / "1-a" / "RELATORIO.md").write_text(
        "| a | b |\n|---|---|\n| Silva (2025) | https://doi.org/10.1234/ok |\n"
        "| Souza (2024) | https://doi.org/10.1234/x |\n", encoding="utf-8")
    (tmp_path / "referencias.bib").write_text(
        "@article{a, author={Silva, Ana}, year={2025}, DOI={10.1234/ok}}\n"
        "@article{b, author={Souza, B}, year={2024}, DOI={10.1234/x}}\n", encoding="utf-8")
    (tmp_path / "REFERENCIAS.md").write_text("# Referências: Tema\n", encoding="utf-8")
    campos = ["doi", "ano", "primeiro_autor", "titulo", "revista", "citacoes", "fwci", "percentil",
              "acesso", "pdf", "pdf_alternativos"] + revistas.CAMPOS
    with open(tmp_path / "cienciometria.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerow({"doi": "10.1234/ok", "titulo": "Bom", "revista": "RSE", "citacoes": 5,
                    **revistas.indicadores(FONTE_OK)})
        w.writerow({"doi": "10.1234/x", "titulo": "Retratado", "revista": "X", "citacoes": 1,
                    **revistas.indicadores(FONTE_FORA, retratado=True)})
    conferir_lista.gravar([{**{c: "" for c in conferir_lista.CAMPOS}, "n": 1, "estado": "OK",
                            "doi": "10.1234/ok", "referencia": "Silva"}], tmp_path)
    with open(tmp_path / "novidades.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=atualizar.CAMPOS)
        w.writeheader()
        w.writerow({"data_busca": "2026-11-01", "frente": "1-a", "doi": "10.1/novo", "titulo": "Novo",
                    "ano": 2026, **revistas.indicadores(FONTE_FORA)})
    painel.main([str(tmp_path)])
    tabela = json.loads((tmp_path / "tabela.json").read_text(encoding="utf-8"))
    ok = next(l for l in tabela if l["doi"] == "10.1234/ok")
    assert ok["ja_citado"] and ok["frentes"] == ["1-a"] and ok["sinal_revista"] == "ok"
    assert "CWTS Core" in (tmp_path / "TABELA.md").read_text(encoding="utf-8")
    pagina = publicar.gerar(tmp_path).read_text(encoding="utf-8")
    assert 'class="retratado"' in pagina and "já cito" in pagina
    assert 'data-frentes="1-a"' in pagina and "Novo" in pagina
    assert "{{" not in pagina


def test_projeto_do_doutorado_bem_formado():
    p = RAIZ / "projetos" / "doutorado-silvicultura-go"
    if not p.exists():
        pytest.skip("projeto do doutorado não está neste clone")
    cfg = atualizar.ler_consultas(p)
    pedidos = sorted(x.parent.name for x in p.glob("frentes/*/PEDIDO.md"))
    assert pedidos == sorted(cfg["frentes"]) and len(pedidos) == 6
    for x in p.glob("frentes/*/PEDIDO.md"):
        assert "{" + "TEMA}" not in x.read_text(encoding="utf-8")


# --- conferir_citacoes ----------------------------------------------------

import conferir_citacoes  # noqa: E402

LISTA_CIT = [
    "ROSS, J. L. S. Análise empírica da fragilidade dos ambientes naturais. Revista do Departamento de Geografia, n. 8, p. 63–74, 1994.",
    "GORELICK, N. et al. Google Earth Engine. Remote Sensing of Environment, v. 202, p. 18–27, 2017.",
    "IMB – INSTITUTO MAURO BORGES. Goiás em dados – 2022. Goiânia: IMB, 2022. Disponível em: https://www.imb.go.gov.br/. Acesso em: 03 out. 2025.",
    "GOIÁS. Decreto nº 9.891 (Alterado pelo Decreto nº 10.683). Goiânia, 2025.",
    "GOIÁS. Resolução nº 001. Goiânia: SEAPA, 2025.",
    "MARTINS-NETO, R. P. et al. Tree Species Classification. Forests, v. 14, 2023. DOI: https://doi.org/10.3390/f14050945.",
]


def test_citacoes_parenteses_e_narrativa():
    texto = ("Perfil diversificado (IMB, 2022; GORELICK et al., 2017, p. 20). Segundo Ross (1994), "
             "e Martins-Neto et al. (2023). Entre 2012 e 2021 (ODS 13).")
    achadas = {(c, a) for c, a, _ in conferir_citacoes.citacoes(texto)}
    assert achadas == {("IMB", "2022"), ("GORELICK", "2017"), ("ROSS", "1994"), ("MARTINS-NETO", "2023")}


def test_ano_referencia_ignora_acesso_e_doi():
    assert conferir_citacoes.ano_referencia(LISTA_CIT[2]) == "2022"
    assert conferir_citacoes.ano_referencia(LISTA_CIT[5]) == "2023"
    assert conferir_citacoes.chave_referencia(LISTA_CIT[2]) == "IMB"


def test_conferir_citacoes_estados():
    texto = "Texto (IMB, 2022). Ross (2012) e (SILVA, 2020)."
    achados = conferir_citacoes.conferir(texto, LISTA_CIT)
    por_estado = {}
    for estado, chave, ano, _ in achados:
        por_estado.setdefault(estado, set()).add((chave, ano))
    assert por_estado["OK"] == {("IMB", "2022")}
    assert por_estado["ANO-DIFERE"] == {("ROSS", "2012")}
    assert por_estado["CITADA-SEM-REFERENCIA"] == {("SILVA", "2020")}
    assert por_estado["MESMO-AUTOR-ANO"] == {("GOIAS", "2025")}
    assert ("GORELICK", "2017") in por_estado["NAO-CITADA"]


def test_conferir_citacoes_le_docx(tmp_path):
    docx = pytest.importorskip("docx")
    d = docx.Document()
    d.add_paragraph("Introdução com citação (IMB, 2022).")
    d.add_paragraph("REFERÊNCIAS BIBLIOGRÁFICAS")
    for r in LISTA_CIT:
        d.add_paragraph(r)
    arq = tmp_path / "texto.docx"
    d.save(arq)
    saida = tmp_path / "CITACOES.md"
    assert conferir_citacoes.main([str(arq), str(saida)]) == 0
    md = saida.read_text(encoding="utf-8")
    assert "OK: 1" in md and "MESMO-AUTOR-ANO: 1" in md


# --- lacunas ----------------------------------------------------------------

import lacunas  # noqa: E402

RESUMO_LAC = """# RELATÓRIO — Silva (2024)

## 1. Referência
Silva et al. GEDI and Sentinel-2 for eucalyptus biomass.

## 2. Pergunta do estudo
Estimar biomassa de eucalipto [p. 2].

## 3. Área e dados
- Local: Minas Gerais, Brasil; nenhum sítio em Goiás [p. 3].
- Sensores: GEDI L4A e Sentinel-2 [p. 3].

## 4. Método
- Random Forest e aprendizado profundo (CNN) [p. 4].

## 5. Resultados principais
- Contexto do estudo [p. 5].
- Melhor modelo: R² 0,81 e RMSE 18 Mg/ha [p. 6].

## 7. O que serve ao projeto e o que não serve
- Não serve: não usa PRISMA nem trata de Pinus [p. 7].
"""


def test_lacunas_marca_sem_negacoes_e_sem_secao_7(tmp_path):
    (tmp_path / "resumos" / "silva2024").mkdir(parents=True)
    (tmp_path / "resumos" / "silva2024" / "RELATORIO.md").write_text(RESUMO_LAC, encoding="utf-8")
    l = lacunas.analisar(tmp_path)[0]
    assert set(l["sensores"]) == {"GEDI", "Sentinel-2"}
    assert "Eucalipto" in l["plantios"] and "Pinus" not in l["plantios"]
    assert "Goiás" not in l["regioes"] and "Brasil" in l["regioes"]
    assert {"Random Forest", "Redes neurais/deep learning"} <= set(l["metodos"])
    assert l["metrica"].startswith("Melhor modelo: R² 0,81")


def test_lacunas_grava_matrizes(tmp_path):
    (tmp_path / "resumos" / "silva2024").mkdir(parents=True)
    (tmp_path / "resumos" / "silva2024" / "RELATORIO.md").write_text(RESUMO_LAC, encoding="utf-8")
    assert lacunas.main([str(tmp_path)]) == 0
    md = (tmp_path / "LACUNAS.md").read_text(encoding="utf-8")
    assert "| GEDI × Eucalipto | 1 | silva2024 |" in md
    assert "Sensor × variável estimada" in md


# --- atualizar: autores --------------------------------------------------------

def test_id_do_autor_casa_primeiro_e_ultimo_nome():
    w = {"authorships": [
        {"author": {"id": "https://openalex.org/A1", "display_name": "Lênio S. Galvão"}},
        {"author": {"id": "https://openalex.org/A2", "display_name": "Aliny Aparecida dos Reis"}},
        {"author": {"id": "https://openalex.org/A3", "display_name": "Maria Galvão"}}]}
    get = lambda url, e, k: w
    assert atualizar.id_do_autor("Lênio Soares Galvão", "10.1/x", FontesFalsas(), get) == "A1"
    assert atualizar.id_do_autor("Aliny Aparecida dos Reis", "10.1/x", FontesFalsas(), get) == "A2"
    assert atualizar.id_do_autor("Ralph Dubayah", "10.1/x", FontesFalsas(), get) == ""


def test_buscar_inclui_autores_com_rotulo(tmp_path):
    p = projeto(tmp_path)
    cfg = atualizar.ler_consultas(p)
    cfg["autores"] = {"Ana Silva": {"doi": "10.1/artigo"}}

    def get(url, email, key):
        if "/works/doi:" in url:
            return {"authorships": [{"author": {"id": "https://openalex.org/A9", "display_name": "Ana Silva"}}]}
        if "authorships.author.id%3AA9" in url:
            return {"meta": {"count": 2}, "results": [work("10.1/novo"), work("10.1/do-autor")]}
        return {"meta": {"count": 1}, "results": [work("10.1/novo")]}

    novas, avisos = atualizar.buscar(cfg, "2026-10-29", datetime.date(2026, 11, 1),
                                     set(), FontesFalsas(), {}, get=get)
    assert [(n["doi"], n["frente"]) for n in novas] == [("10.1/novo", "1-a"), ("10.1/do-autor", "autor: Ana Silva")]
    assert not avisos


def test_buscar_autor_nao_encontrado_vira_erro(tmp_path):
    cfg = atualizar.ler_consultas(projeto(tmp_path))
    cfg["frentes"] = {}
    cfg["autores"] = {"Ana Silva": {"doi": "10.1/artigo"}}
    novas, avisos = atualizar.buscar(cfg, "2026-10-29", datetime.date(2026, 11, 1), set(), FontesFalsas(), {},
                                     get=lambda url, e, k: {"authorships": []})
    assert not novas and avisos[0].startswith("ERRO autor: Ana Silva")
