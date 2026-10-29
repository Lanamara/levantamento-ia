import csv
import json
import shutil
import signal
import subprocess
import sys
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "ferramentas"))

import baixar_pdf  # noqa: E402
import cienciometria  # noqa: E402
import conferir  # noqa: E402
import doi as doilib  # noqa: E402
import entrega  # noqa: E402
import juntar  # noqa: E402
import orquestrar  # noqa: E402
import painel  # noqa: E402
import preparar_resumos  # noqa: E402
import publicar  # noqa: E402


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


def test_slug_aceita_sobrenome_antes_do_nome():
    assert preparar_resumos.slug("Silva, João", 2020) == "silva2020"
    assert preparar_resumos.slug("João Silva", 2020) == "silva2020"


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


def test_nao_confere_autor_errado():
    texto = "Biomassa florestal e carbono na silvicultura " * 80
    motivo = preparar_resumos.nao_confere(
        texto, "10.1234/abc", "Biomassa florestal carbono silvicultura", "Pereira")
    assert "outro artigo" in motivo


def test_procurar_manual_ignora_pdf_reservado(tmp_path, monkeypatch):
    pdfs = tmp_path / "pdfs"
    pdfs.mkdir()
    arquivo = pdfs / "a.pdf"
    arquivo.write_bytes(b"%PDF-1.4")
    monkeypatch.setattr(preparar_resumos, "primeiras_paginas",
                        lambda _: "doi: 10.1234/abc " + "conteudo " * 300)
    assert preparar_resumos.procurar_manual(
        pdfs, "b", "10.1234/abc", "Biomassa florestal", {arquivo.resolve()}, "Silva") is None


def test_procurar_manual_nao_confunde_slug_prefixo(tmp_path, monkeypatch):
    pdfs = tmp_path / "pdfs"
    pdfs.mkdir()
    (pdfs / "li2022b.pdf").write_bytes(b"%PDF-1.4")
    monkeypatch.setattr(preparar_resumos, "primeiras_paginas",
                        lambda _: "outro artigo completamente diferente " * 100)
    assert preparar_resumos.procurar_manual(
        pdfs, "li2022", "10.1/x", "Título sem relação", set(), "Silva") is None


def test_procurar_manual_aceita_extensao_maiuscula(tmp_path, monkeypatch):
    pdfs = tmp_path / "pdfs"
    pdfs.mkdir()
    (pdfs / "SILVA2020.PDF").write_bytes(b"%PDF-1.4")
    monkeypatch.setattr(preparar_resumos, "primeiras_paginas",
                        lambda _: "doi: 10.1/x " + "conteudo " * 300)
    achado = preparar_resumos.procurar_manual(
        pdfs, "silva2020", "10.1/x", "Título", set(), "Silva")
    assert achado == pdfs / "silva2020.pdf"
    assert achado.exists()


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


def test_isolar_e_devolver(tmp_path):
    (tmp_path / "AGENTS.md").write_text("não é para os agentes", encoding="utf-8")
    (tmp_path / "opencode.json").write_text("{}", encoding="utf-8")
    frente = tmp_path / "1-frente"
    frente.mkdir()
    (frente / "PEDIDO.md").write_text("pedido", encoding="utf-8")
    (frente / "log.jsonl").write_text("log atual", encoding="utf-8")
    (frente / "RELATORIO.anterior1.md").write_text("antigo", encoding="utf-8")
    tmp = orquestrar.isolar(frente)
    try:
        trabalho = tmp / "1-frente"
        assert (trabalho / "PEDIDO.md").exists()
        assert (tmp / "opencode.json").exists()
        assert not (trabalho / "log.jsonl").exists()
        assert not (trabalho / "RELATORIO.anterior1.md").exists()
        # A cópia não fica abaixo da pasta que tem o AGENTS.md.
        assert tmp_path.resolve() not in trabalho.resolve().parents
        (trabalho / "RELATORIO.md").write_text("relatório", encoding="utf-8")
        (trabalho / "log.jsonl").write_text("não deve voltar", encoding="utf-8")
    finally:
        orquestrar.devolver(tmp, frente)
    assert (frente / "RELATORIO.md").read_text(encoding="utf-8") == "relatório"
    assert (frente / "log.jsonl").read_text(encoding="utf-8") == "log atual"
    assert not tmp.exists()


class _ProcFalso:
    pid = 1

    def poll(self):
        return 0


def _frente_temp(tmp_path, relatorio, pedido="Grave a tabela.", log=None):
    raiz = tmp_path / "frentes"
    frente = raiz / "1-frente"
    frente.mkdir(parents=True)
    (frente / "PEDIDO.md").write_text(pedido, encoding="utf-8")
    if relatorio is not None:
        (frente / "RELATORIO.md").write_text(relatorio, encoding="utf-8")
    if log is not None:
        (frente / "log.jsonl").write_text(log, encoding="utf-8")
    return raiz, frente


def test_avisos_graves_classificacao():
    assert orquestrar.aviso_grave("sem tabela de referências")
    assert orquestrar.aviso_grave("faltam seções: 2, 3")
    assert orquestrar.aviso_grave("colunas fora do contrato: dados")
    assert not orquestrar.aviso_grave("8 linhas de dados (o contrato pede 10 a 15)")
    assert not orquestrar.aviso_grave("poucas páginas citadas (2)")


def test_avisos_formato_usa_faixa_10_a_15(tmp_path):
    (tmp_path / "PEDIDO.md").write_text("Use websearch e grave a tabela.", encoding="utf-8")
    cabecalho = ("| Autores (ano) | Título | Revista | DOI/link | Dados | Método | "
                 "Área | Resultado principal |")
    for n in (8, 10, 16):
        linhas = [cabecalho, "|---|---|---|---|---|---|---|---|"]
        linhas += [f"| A{i} | T{i} | R{i} | 10.1/{i} | D | M | Á | X |" for i in range(n)]
        (tmp_path / "RELATORIO.md").write_text("\n".join(linhas), encoding="utf-8")
        avisos = orquestrar.avisos_formato(tmp_path)
        if n == 10:
            assert not any("linhas de dados" in a for a in avisos)
        else:
            assert any(f"{n} linhas de dados" in a for a in avisos)


def test_renomear_relatorio_para_refazer(tmp_path):
    (tmp_path / "RELATORIO.md").write_text("antigo", encoding="utf-8")
    assert orquestrar.renomear_relatorio(tmp_path).name == "RELATORIO.anterior1.md"
    assert not (tmp_path / "RELATORIO.md").exists()
    (tmp_path / "RELATORIO.md").write_text("outro", encoding="utf-8")
    assert orquestrar.renomear_relatorio(tmp_path).name == "RELATORIO.anterior2.md"


def test_opcoes_processo(monkeypatch):
    monkeypatch.setattr(orquestrar.os, "name", "posix")
    assert orquestrar.opcoes_processo() == {"start_new_session": True}
    if sys.platform == "win32":
        monkeypatch.setattr(orquestrar.os, "name", "nt")
        assert orquestrar.opcoes_processo() == {
            "creationflags": subprocess.CREATE_NEW_PROCESS_GROUP}


@pytest.mark.skipif(sys.platform != "win32", reason="taskkill só existe no Windows")
def test_encerrar_usa_taskkill_no_windows(monkeypatch):
    chamadas = []
    monkeypatch.setattr(orquestrar.subprocess, "run",
                        lambda cmd, **kwargs: chamadas.append(cmd))

    class Proc:
        pid = 123

        def poll(self):
            return None

        def wait(self, timeout=None):
            self.esperou = timeout
            return 0

    proc = Proc()
    orquestrar.encerrar(proc)
    assert chamadas == [["taskkill", "/T", "/F", "/PID", "123"]]
    assert proc.esperou == 5


def test_encerrar_usa_killpg_no_posix(monkeypatch):
    monkeypatch.setattr(orquestrar.os, "name", "posix")
    monkeypatch.setattr(orquestrar.os, "getpgid", lambda pid: 99, raising=False)
    chamadas = []
    monkeypatch.setattr(orquestrar.os, "killpg",
                        lambda pg, sig: chamadas.append((pg, sig)), raising=False)

    class Proc:
        pid = 123

        def poll(self):
            return None

        def wait(self, timeout=None):
            return 0

    orquestrar.encerrar(Proc())
    assert chamadas == [(99, signal.SIGTERM)]


def test_orquestrar_raiz_inexistente(tmp_path, capsys):
    assert orquestrar.main([str(tmp_path / "nao-existe"), "--paralelo", "1"]) == 2
    assert "pasta não encontrada" in capsys.readouterr().err


def test_orquestrar_refazer_renomeia(tmp_path, monkeypatch):
    raiz, frente = _frente_temp(tmp_path, "x" * 200)
    monkeypatch.setattr(orquestrar, "lancar",
                        lambda pasta, modelo: (_ProcFalso(), tmp_path))
    monkeypatch.setattr(orquestrar, "devolver", lambda tmp, pasta: None)
    codigo = orquestrar.main([str(raiz), "--refazer", "1-frente",
                              "--intervalo", "0", "--paralelo", "1"])
    assert codigo == 1
    assert (frente / "RELATORIO.anterior1.md").read_text(encoding="utf-8") == "x" * 200
    assert not (frente / "RELATORIO.md").exists()


def test_orquestrar_formato_grave_entra_em_falhas(tmp_path, monkeypatch, capsys):
    raiz, frente = _frente_temp(tmp_path, None)

    def lancar(pasta, modelo):
        (pasta / "RELATORIO.md").write_text("Não consegui buscar nada. " * 20,
                                            encoding="utf-8")
        return _ProcFalso(), tmp_path

    monkeypatch.setattr(orquestrar, "lancar", lancar)
    monkeypatch.setattr(orquestrar, "devolver", lambda tmp, pasta: None)
    codigo = orquestrar.main([str(raiz), "--intervalo", "0", "--paralelo", "1"])
    saida = capsys.readouterr().out
    assert codigo == 1
    assert "FORMATO 1-frente: sem tabela de referências" in saida
    assert "FALHAS: 1-frente" in saida
    assert (frente / "RELATORIO.md").exists()


def test_orquestrar_limite_com_formato_grave_volta_fila(tmp_path, monkeypatch, capsys):
    raiz, frente = _frente_temp(tmp_path, None)

    def lancar(pasta, modelo):
        (pasta / "RELATORIO.md").write_text("Não consegui buscar nada. " * 20,
                                            encoding="utf-8")
        (pasta / "log.jsonl").write_text(
            '{"type":"error","message":"FreeUsageLimitError"}\n', encoding="utf-8")
        return _ProcFalso(), tmp_path

    monkeypatch.setattr(orquestrar, "lancar", lancar)
    monkeypatch.setattr(orquestrar, "devolver", lambda tmp, pasta: None)
    codigo = orquestrar.main([str(raiz), "--intervalo", "0", "--paralelo", "1"])
    saida = capsys.readouterr().out
    assert codigo == 1
    assert "LIMITE 1-frente" in saida
    assert (frente / "RELATORIO.parcial1.md").exists()
    assert (frente / "log.anterior1.jsonl").exists()


def test_orquestrar_formato_leve_nao_falha(tmp_path, monkeypatch, capsys):
    cabecalho = ("| Autores (ano) | Título | Revista | DOI/link | Dados | Método | "
                 "Área | Resultado principal |")
    linhas = [cabecalho, "|---|---|---|---|---|---|---|---|"]
    linhas += [f"| A{i} | T{i} | R{i} | 10.1/{i} | D | M | Á | X |" for i in range(8)]
    raiz, _ = _frente_temp(tmp_path, None, pedido="Grave a tabela.")

    def lancar(pasta, modelo):
        (pasta / "RELATORIO.md").write_text("\n".join(linhas), encoding="utf-8")
        return _ProcFalso(), tmp_path

    monkeypatch.setattr(orquestrar, "lancar", lancar)
    monkeypatch.setattr(orquestrar, "devolver", lambda tmp, pasta: None)
    codigo = orquestrar.main([str(raiz), "--intervalo", "0", "--paralelo", "1"])
    saida = capsys.readouterr().out
    assert codigo == 0
    assert "FORMATO 1-frente: 8 linhas de dados" in saida
    assert "FALHAS" not in saida


def test_orquestrar_devolver_avisa_pasta_presa(tmp_path, monkeypatch, capsys):
    frente = tmp_path / "1-frente"
    frente.mkdir()
    (frente / "PEDIDO.md").write_text("pedido", encoding="utf-8")
    tmp = orquestrar.isolar(frente)
    monkeypatch.setattr(orquestrar.shutil, "rmtree", lambda *a, **k: None)
    monkeypatch.setattr(orquestrar.time, "sleep", lambda *_: None)
    try:
        orquestrar.devolver(tmp, frente)
        saida = capsys.readouterr().out
        assert "AVISO: não consegui apagar a pasta temporária" in saida
        assert str(tmp) in saida
    finally:
        monkeypatch.undo()
        shutil.rmtree(tmp, ignore_errors=True)


def _item_conferir(estado="OK", nome="item", detalhe="", comando=""):
    return {"estado": estado, "item": nome, "detalhe": detalhe, "comando": comando}


@pytest.mark.parametrize("versao, esperado", [
    ((3, 9, 9), False),
    ((3, 10, 0), True),
    ((3, 12, 4), True),
])
def test_conferir_versao_python(versao, esperado):
    assert conferir.versao_python_ok(versao) is esperado


def test_conferir_ler_requirements(tmp_path):
    arquivo = tmp_path / "requirements.txt"
    arquivo.write_text(
        "# comentário\npypdf>=3\nrequests\n\nmarkdown # para o HTML\npytest==8\n",
        encoding="utf-8")
    assert conferir.pacotes_do_arquivo(arquivo) == [
        "pypdf", "requests", "markdown", "pytest"]


def test_conferir_faltando_pacotes(monkeypatch):
    monkeypatch.setattr(conferir, "tem_modulo", lambda nome: nome != "pypdf")
    assert conferir.faltando_pacotes(["pypdf", "requests"]) == ["pypdf"]


@pytest.mark.parametrize("python, esperado", [
    ("/usr/bin/python3", "/usr/bin/python3 -m pip install -r requirements.txt"),
    (r"C:\Python 3.12\python.exe",
     r'"C:\Python 3.12\python.exe" -m pip install -r requirements.txt'),
])
def test_conferir_pacotes_usa_o_python_atual(monkeypatch, python, esperado):
    monkeypatch.setattr(conferir.sys, "executable", python)
    assert conferir.comando("pacotes") == esperado


def test_conferir_requirements_ausente_lembra_do_zip(monkeypatch):
    monkeypatch.setattr(conferir, "pacotes_do_arquivo", lambda: None)
    achado = conferir.conferir_pacotes()
    assert achado["estado"] == "FALTA"
    assert "levantamento-ia-main" in achado["detalhe"]


def _rodar_falso(saidas):
    def falso(cmd, **kwargs):
        for chave, (codigo, texto) in saidas.items():
            if chave in cmd:
                return subprocess.CompletedProcess(cmd, codigo, texto, "")
        return subprocess.CompletedProcess(cmd, 1, "", "comando inesperado")
    return falso


@pytest.mark.parametrize("plataforma", ["win32", "darwin", "linux"])
def test_conferir_comando_por_sistema(monkeypatch, plataforma):
    monkeypatch.setattr(conferir.sys, "platform", plataforma)
    for chave in ("python", "pacotes", "node", "opencode", "git", "curl"):
        assert conferir.comando(chave)


def test_conferir_node_ausente(monkeypatch):
    monkeypatch.setattr(conferir, "achar", lambda nome: None)
    achado = conferir.conferir_node()
    assert achado["estado"] == "FALTA"
    assert "Node.js" in achado["detalhe"]


def test_conferir_opencode_ausente(monkeypatch):
    monkeypatch.setattr(conferir, "achar", lambda nome: None)
    achado = conferir.conferir_opencode()
    assert achado["estado"] == "FALTA"
    assert "@opencode/cli" in achado["comando"]


def test_conferir_opencode_sem_standalone(monkeypatch):
    monkeypatch.setattr(conferir, "achar", lambda nome: "opencode")
    monkeypatch.setattr(conferir, "rodar", _rodar_falso({
        "--version": (0, "opencode v2.1.0\n"),
        "--help": (0, "USAGE\n  opencode run [flags]\n"),
    }))
    achado = conferir.conferir_opencode()
    assert achado["estado"] == "FALTA"
    assert "--standalone" in achado["detalhe"]
    assert "@latest" in achado["comando"]


def test_conferir_opencode_ok(monkeypatch):
    monkeypatch.setattr(conferir, "achar", lambda nome: "opencode")
    monkeypatch.setattr(conferir, "rodar", _rodar_falso({
        "--version": (0, "opencode v2.2.0\n"),
        "--help": (0, "GLOBAL FLAGS\n  --standalone  Run with a private server\n"),
    }))
    achado = conferir.conferir_opencode()
    assert achado["estado"] == "OK"
    assert "2.2.0" in achado["detalhe"]


def test_conferir_modelo_python_antigo_nao_tenta(monkeypatch):
    monkeypatch.setattr(conferir, "versao_python_ok", lambda: False)
    monkeypatch.setattr(conferir, "achar",
                        lambda nome: pytest.fail("não devia procurar o opencode"))
    achado = conferir.testar_modelo()
    assert achado["estado"] == "FALTA"
    assert "Python 3.10+" in achado["detalhe"]


def test_conferir_modelo_responde(monkeypatch):
    monkeypatch.setattr(conferir, "achar", lambda nome: "opencode")
    monkeypatch.setattr(conferir, "rodar", lambda *a, **k: subprocess.CompletedProcess(
        a[0], 0, '{"type":"text","part":{"text":"ok"}}\n', ""))
    achado = conferir.testar_modelo()
    assert achado["estado"] == "OK"
    assert "respondeu" in achado["detalhe"]


def test_conferir_modelo_no_limite(monkeypatch):
    monkeypatch.setattr(conferir, "achar", lambda nome: "opencode")
    monkeypatch.setattr(conferir, "rodar", lambda *a, **k: subprocess.CompletedProcess(
        a[0], 0, '{"type":"error","message":"FreeUsageLimitError"}\n', ""))
    achado = conferir.testar_modelo()
    assert achado["estado"] == "FALTA"
    assert "limite" in achado["detalhe"]


def test_conferir_modelo_com_evento_de_erro(monkeypatch):
    monkeypatch.setattr(conferir, "achar", lambda nome: "opencode")
    monkeypatch.setattr(conferir, "rodar", lambda *a, **k: subprocess.CompletedProcess(
        a[0], 0, '{"type":"error","message":"modelo inexistente"}\n', ""))
    achado = conferir.testar_modelo()
    assert achado["estado"] == "FALTA"
    assert "modelo inexistente" in achado["detalhe"]


def test_conferir_modelo_com_erro(monkeypatch):
    monkeypatch.setattr(conferir, "achar", lambda nome: "opencode")
    monkeypatch.setattr(conferir, "rodar", lambda *a, **k: subprocess.CompletedProcess(
        a[0], 1, "", "erro de rede\n"))
    achado = conferir.testar_modelo()
    assert achado["estado"] == "FALTA"
    assert "código 1" in achado["detalhe"]


def test_conferir_deu_limite_ignora_texto_do_modelo():
    assert conferir.deu_limite('{"type":"error","message":"FreeUsageLimitError"}')
    assert conferir.deu_limite("Error: Rate limit exceeded")
    assert not conferir.deu_limite('{"type":"text","part":{"text":"Rate limit exceeded"}}')


def test_conferir_json_sinaliza_falta(monkeypatch, capsys):
    monkeypatch.setattr(conferir, "conferir_tudo", lambda com_modelo=False, modelo=None: [
        _item_conferir("FALTA", "opencode", "não está no PATH",
                       "npm install -g @opencode/cli")])
    assert conferir.main(["--json"]) == 1
    dados = json.loads(capsys.readouterr().out)
    assert dados["ok"] is False
    assert dados["itens"][0]["item"] == "opencode"


def test_conferir_json_sai_em_ascii(monkeypatch, capsys):
    monkeypatch.setattr(conferir, "conferir_tudo", lambda com_modelo=False, modelo=None: [
        _item_conferir("OK", "opencode", "versão 2.2.0")])
    assert conferir.main(["--json"]) == 0
    saida = capsys.readouterr().out
    assert "vers\\u00e3o 2.2.0" in saida
    assert json.loads(saida)["itens"][0]["detalhe"] == "versão 2.2.0"


def test_conferir_json_libera_quando_tudo_ok(monkeypatch, capsys):
    monkeypatch.setattr(conferir, "conferir_tudo", lambda com_modelo=False, modelo=None: [
        _item_conferir()])
    assert conferir.main(["--json"]) == 0
    dados = json.loads(capsys.readouterr().out)
    assert dados["ok"] is True


def test_conferir_texto_mostra_o_comando(monkeypatch, capsys):
    monkeypatch.setattr(conferir, "conferir_tudo", lambda com_modelo=False, modelo=None: [
        _item_conferir("FALTA", "opencode", "não está no PATH",
                       "npm install -g @opencode/cli")])
    assert conferir.main([]) == 1
    saida = capsys.readouterr().out
    assert "FALTA opencode" in saida
    assert "resolva com: npm install -g @opencode/cli" in saida


def test_conferir_sem_opcao_nao_chama_modelo(monkeypatch):
    for nome in ("conferir_python", "conferir_pacotes", "conferir_node",
                 "conferir_opencode", "conferir_git", "conferir_curl"):
        monkeypatch.setattr(conferir, nome, lambda: _item_conferir())
    monkeypatch.setattr(conferir, "testar_modelo",
                        lambda: pytest.fail("não devia chamar o modelo sem --testar-modelo"))
    assert len(conferir.conferir_tudo()) == 6


def test_avisos_formato_resumo_ok(tmp_path):
    (tmp_path / "PEDIDO.md").write_text("Leia TEXTO.txt e resuma.", encoding="utf-8")
    secoes = "\n".join(f"## {n}. Seção" for n in range(1, 9))
    (tmp_path / "RELATORIO.md").write_text(
        secoes + "\n" + "Número [p. 1]. " * 6, encoding="utf-8")
    assert orquestrar.avisos_formato(tmp_path) == []


def test_avisos_formato_resumo_fora_do_contrato(tmp_path):
    (tmp_path / "PEDIDO.md").write_text("Leia TEXTO.txt e resuma.", encoding="utf-8")
    (tmp_path / "RELATORIO.md").write_text(
        "## 1. Referência\n\n| a | b |\n|---|---|\n| 1 | 2 |\n", encoding="utf-8")
    avisos = orquestrar.avisos_formato(tmp_path)
    assert any("faltam seções" in a for a in avisos)
    assert any("poucas páginas" in a for a in avisos)
    assert any("tabela" in a for a in avisos)


def test_avisos_formato_cerca_de_codigo(tmp_path):
    (tmp_path / "PEDIDO.md").write_text("Use websearch.", encoding="utf-8")
    (tmp_path / "RELATORIO.md").write_text(
        "```markdown\n| Autores (ano) | Título | Revista | DOI/link | Dados | Método | Área | Resultado principal |\n"
        "|---|---|---|---|---|---|---|---|\n| A | T | R | 10.1/x | D | M | Á | X |\n```\n",
        encoding="utf-8")
    assert any("cerca de código" in a for a in orquestrar.avisos_formato(tmp_path))


def test_avisos_formato_busca_ok(tmp_path):
    (tmp_path / "PEDIDO.md").write_text("Use websearch e grave a tabela.", encoding="utf-8")
    cabecalho = ("| Autores (ano) | Título | Revista | DOI/link | Dados | Método | "
                 "Área | Resultado principal |")
    linhas = [cabecalho, "|---|---|---|---|---|---|---|---|"]
    linhas += [f"| A{i} | T{i} | R{i} | 10.1/{i} | D | M | Á | X |" for i in range(10)]
    (tmp_path / "RELATORIO.md").write_text("\n".join(linhas), encoding="utf-8")
    assert orquestrar.avisos_formato(tmp_path) == []


def test_avisos_formato_busca_fora_do_contrato(tmp_path):
    (tmp_path / "PEDIDO.md").write_text("Use websearch e grave a tabela.", encoding="utf-8")
    (tmp_path / "RELATORIO.md").write_text(
        "| Autor | Título |\n|---|---|\n| A | T |\n", encoding="utf-8")
    avisos = orquestrar.avisos_formato(tmp_path)
    assert any("colunas fora do contrato" in a for a in avisos)
    assert any("linhas de dados" in a for a in avisos)
    assert any("DOI" in a for a in avisos)


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


def test_painel_aceita_metricas_vazias(tmp_path):
    pasta = tmp_path / "projeto"
    pasta.mkdir()
    (pasta / "referencias.bib").write_text(
        "@article{x, DOI={10.1/x}, author={Silva, A.}, year={2020}}",
        encoding="utf-8")
    (pasta / "cienciometria.csv").write_text(
        "doi,ano,primeiro_autor,titulo,revista,citacoes,fwci,percentil,acesso,pdf,pdf_alternativos\n"
        "10.1/x,2020,Silva,Titulo,,,,,,,\n",
        encoding="utf-8")
    (pasta / "REFERENCIAS.md").write_text("# Referências: Tema\n", encoding="utf-8")
    painel.main([str(pasta)])
    linha = json.loads((pasta / "tabela.json").read_text(encoding="utf-8"))[0]
    assert linha["citacoes"] == 0
    assert linha["fwci"] == ""
    assert linha["percentil"] == ""
    assert linha["acesso"] == ""


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
    assert juntar.main([str(frentes), str(saida), "Tema"]) == 0
    refs = (saida / "REFERENCIAS.md").read_text(encoding="utf-8")
    assert "não havia busca web" in refs
    assert "**†**" in refs
    assert "## 1-teste" in refs
    assert "Um artigo" in refs
    assert "10.1234/abc" in (saida / "referencias.bib").read_text(encoding="utf-8")


def test_juntar_sem_tabela_avisa_e_sai_1(tmp_path, capsys):
    frentes = tmp_path / "frentes"
    frente = frentes / "1-quebrada"
    frente.mkdir(parents=True)
    (frente / "RELATORIO.md").write_text(
        "# Relatório\n\nNão consegui buscar nada.\n", encoding="utf-8")
    saida = tmp_path / "saida"
    assert juntar.main([str(frentes), str(saida), "Tema"]) == 1
    assert "SEM-TABELA 1-quebrada" in capsys.readouterr().out
    assert (saida / "REFERENCIAS.md").exists()
    assert (saida / "referencias.bib").exists()


def test_juntar_sem_doi_tambem_sai_1(tmp_path, capsys):
    frentes = tmp_path / "frentes"
    frente = frentes / "1-bases"
    frente.mkdir(parents=True)
    (frente / "RELATORIO.md").write_text(
        "| Autores (ano) | Título | Revista | DOI/link |\n"
        "|---|---|---|---|\n"
        "| IBGE (2026) | Base oficial | Base | https://exemplo.org/base |\n",
        encoding="utf-8")
    saida = tmp_path / "saida"
    assert juntar.main([str(frentes), str(saida), "Tema"]) == 1
    assert "0 DOIs únicos" in capsys.readouterr().out
    assert (saida / "REFERENCIAS.md").exists()


def test_juntar_progresso_a_cada_10(tmp_path, monkeypatch, capsys):
    frentes = tmp_path / "frentes"
    frente = frentes / "1-teste"
    frente.mkdir(parents=True)
    linhas = ["| Autores (ano) | Título | Revista | DOI/link |", "|---|---|---|---|"]
    linhas += [f"| A{i} (2020) | T{i} | R | https://doi.org/10.1234/{i} |" for i in range(11)]
    (frente / "RELATORIO.md").write_text("\n".join(linhas), encoding="utf-8")
    monkeypatch.setattr(juntar, "bibtex", lambda doi: f"% falhou: {doi}")
    assert juntar.main([str(frentes), str(tmp_path / "saida"), "Tema"]) == 0
    assert "BibTeX 10/11" in capsys.readouterr().out


def test_cienciometria_separa_falhas(tmp_path, monkeypatch, capsys):
    bib = tmp_path / "referencias.bib"
    bib.write_text("@article{a, DOI={10.1/ok}}\n@article{b, DOI={10.1/falha}}\n", encoding="utf-8")
    saida = tmp_path / "cienciometria.csv"

    def fake(doi, email, *_):
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
    assert [r["doi"] for r in linhas] == ["10.1/ok", "10.1/falha"]
    falha = linhas[1]
    assert falha["citacoes"] == ""
    assert falha["fwci"] == ""
    assert falha["acesso"] == ""
    with open(tmp_path / "cienciometria-falhas.csv", encoding="utf-8-sig") as f:
        falhas = list(csv.DictReader(f))
    assert falhas == [{"doi": "10.1/falha", "erro": "RuntimeError: sem rede"}]
    assert "1 falharam" in capsys.readouterr().out


def test_cienciometria_falha_usa_metadados_do_bib(tmp_path, monkeypatch):
    bib = tmp_path / "referencias.bib"
    bib.write_text(
        "@article{b, DOI={10.1/falha}, title={Um artigo}, "
        "author={Silva, Ana and Souza, B.}, year={2021}}",
        encoding="utf-8")
    def falha(doi, email, *_):
        raise RuntimeError("sem rede")

    monkeypatch.setattr(cienciometria, "consulta", falha)
    monkeypatch.setattr(cienciometria.time, "sleep", lambda *_: None)
    cienciometria.main([str(bib), str(tmp_path / "cienciometria.csv")])
    with open(tmp_path / "cienciometria.csv", encoding="utf-8-sig") as f:
        linha = list(csv.DictReader(f))[0]
    assert linha["doi"] == "10.1/falha"
    assert linha["ano"] == "2021"
    assert linha["primeiro_autor"] == "Silva"
    assert linha["titulo"] == "Um artigo"


def test_cienciometria_tenta_duas_vezes(monkeypatch):
    chamadas = []

    def fake(doi, email, *_):
        chamadas.append(doi)
        if len(chamadas) == 1:
            raise RuntimeError("429")
        return {"doi": doi}

    monkeypatch.setattr(cienciometria, "_consultar_uma", fake)
    monkeypatch.setattr(cienciometria.time, "sleep", lambda *_: None)
    assert cienciometria.consulta("10.1/x", "") == {"doi": "10.1/x"}
    assert len(chamadas) == 2


def test_cienciometria_codifica_email_no_mailto():
    url = cienciometria.url_openalex("10.1/x", "user+tag@example.org")
    assert "mailto=user%2Btag%40example.org" in url


def test_cienciometria_progresso_a_cada_10(tmp_path, monkeypatch, capsys):
    bib = tmp_path / "referencias.bib"
    bib.write_text("\n".join(f"@article{{a{i}, DOI={{10.1/{i}}}}}" for i in range(11)),
                   encoding="utf-8")
    monkeypatch.setattr(cienciometria, "consulta", lambda doi, email, *_: {
        "doi": doi, "ano": 2020, "primeiro_autor": "S", "titulo": "T", "revista": "R",
        "citacoes": 0, "fwci": "", "percentil": "", "acesso": "", "pdf": "",
        "pdf_alternativos": ""})
    monkeypatch.setattr(cienciometria.time, "sleep", lambda *_: None)
    cienciometria.main([str(bib), str(tmp_path / "cienciometria.csv")])
    assert "OpenAlex 10/11" in capsys.readouterr().out


@pytest.mark.parametrize("script", [
    "juntar.py", "painel.py", "cienciometria.py", "conferir_doi.py",
    "preparar_resumos.py", "extrair_pdf.py", "orquestrar.py",
    "baixar_pdf.py", "publicar.py", "entrega.py", "conferir.py",
])
def test_argparse_help(script):
    r = subprocess.run([sys.executable, str(RAIZ / "ferramentas" / script), "--help"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    assert r.returncode == 0, r.stderr
    assert "usage:" in r.stdout.lower()


def test_eh_pdf():
    assert baixar_pdf.eh_pdf(b"%PDF-1.7\nresto")
    assert baixar_pdf.eh_pdf(b"  %PDF-1.4")
    assert not baixar_pdf.eh_pdf(b"<html>pagina</html>")
    assert not baixar_pdf.eh_pdf(b"")


def test_baixar_pdf_recusa_pdf_no_limite(monkeypatch):
    monkeypatch.setattr(baixar_pdf, "MAX_BYTES", 10)
    monkeypatch.setattr(baixar_pdf, "ESTRATEGIAS", (
        ("fake", lambda *args: b"%PDF-" + b"x" * 5),
    ))
    dados, fonte = baixar_pdf.baixar_direto("https://exemplo.org/x.pdf", timeout=1)
    assert dados is None
    assert fonte == ""


def test_links_pdf_do_html():
    texto = """
    <meta name="citation_pdf_url" content="/artigo.pdf">
    <a href="files/paper.pdf">PDF</a>
    <a href="/sobre">Sobre</a>
    """
    assert baixar_pdf.links_pdf_do_html(texto, "https://exemplo.org/artigo") == [
        "https://exemplo.org/artigo.pdf",
        "https://exemplo.org/files/paper.pdf",
    ]


def test_mdpi_cdn_de_url():
    assert baixar_pdf.mdpi_cdn_de_url(
        "https://www.mdpi.com/2072-4292/11/14/1721/pdf?version=1563615509") == (
        "https://mdpi-res.com/d_attachment/remotesensing/remotesensing-11-01721/"
        "article_deploy/remotesensing-11-01721.pdf")
    assert baixar_pdf.mdpi_cdn_de_url(
        "https://www.mdpi.com/1999-4907/14/9/1748/pdf", "Forests") == (
        "https://mdpi-res.com/d_attachment/forests/forests-14-01748/"
        "article_deploy/forests-14-01748.pdf")
    assert baixar_pdf.mdpi_cdn_de_url("https://exemplo.org/artigo.pdf") == ""


def test_procurar_manual_reconhece_pelo_conteudo(tmp_path, monkeypatch):
    pdfs = tmp_path / "pdfs"
    pdfs.mkdir()
    (pdfs / "outro-nome.pdf").write_bytes(b"%PDF-1.4")
    monkeypatch.setattr(preparar_resumos, "primeiras_paginas",
                        lambda _: "doi: 10.1234/abc " + "conteudo " * 300)
    achado = preparar_resumos.procurar_manual(
        pdfs, "silva2020", "10.1234/abc", "Biomassa florestal", set())
    assert achado == pdfs / "silva2020.pdf"
    assert achado.exists()
    assert not (pdfs / "outro-nome.pdf").exists()


def _projeto_resumo(tmp_path):
    projeto = tmp_path / "projeto"
    (projeto / "pdfs").mkdir(parents=True)
    (projeto / "resumos").mkdir()
    (projeto / "cienciometria.csv").write_text(
        "doi,ano,primeiro_autor,titulo,revista,citacoes,fwci,percentil,acesso,pdf,pdf_alternativos\n"
        "10.1234/abc,2020,Silva,Biomassa florestal,Revista,3,1.2,50,aberto (revista),,"
        "https://exemplo.org/artigo.pdf\n",
        encoding="utf-8")
    modelo = tmp_path / "modelo.md"
    modelo.write_text("Tema {TEMA}; artigo {TITULO}; autor {AUTOR}; ano {ANO}; DOI {DOI}",
                      encoding="utf-8")
    return projeto, modelo


def test_preparar_resumos_fluxo_ok(tmp_path, monkeypatch, capsys):
    projeto, modelo = _projeto_resumo(tmp_path)
    monkeypatch.setattr(
        preparar_resumos.baixar_pdf, "obter_pdf",
        lambda *a, **k: baixar_pdf.Resultado(dados=b"%PDF-1.4 fake", fonte="teste",
                                             url="https://exemplo.org/artigo.pdf"))
    monkeypatch.setattr(
        preparar_resumos, "extrair_texto",
        lambda _: "doi: 10.1234/abc " + "conteudo " * 400)
    codigo = preparar_resumos.main([
        str(projeto / "cienciometria.csv"), str(projeto / "pdfs"),
        str(projeto / "resumos"), str(modelo), "Tema", "--sem-navegador", "--intervalo", "0"])
    assert codigo == 0
    saida = capsys.readouterr().out
    assert "[1/1] silva2020: baixando..." in saida
    assert "[1/1] silva2020: ok (teste)" in saida
    pedido = (projeto / "resumos" / "silva2020" / "PEDIDO.md").read_text(encoding="utf-8")
    assert "Tema; artigo Biomassa florestal" in pedido
    assert "DOI deste artigo: 10.1234/abc" in pedido
    assert (projeto / "resumos" / "silva2020" / "TEXTO.txt").exists()
    assert not (projeto / "pdfs" / "FALTANDO.md").exists()
    with open(projeto / "download.csv", encoding="utf-8-sig") as f:
        assert list(csv.DictReader(f))[0]["estado"] == "ok"


def test_preparar_resumos_fluxo_sem_pdf(tmp_path, monkeypatch):
    projeto, modelo = _projeto_resumo(tmp_path)
    monkeypatch.setattr(
        preparar_resumos.baixar_pdf, "obter_pdf",
        lambda *a, **k: baixar_pdf.Resultado(motivo="nenhum link entregou PDF"))
    codigo = preparar_resumos.main([
        str(projeto / "cienciometria.csv"), str(projeto / "pdfs"),
        str(projeto / "resumos"), str(modelo), "Tema", "--sem-navegador", "--intervalo", "0"])
    assert codigo == 0
    faltando = (projeto / "pdfs" / "FALTANDO.md").read_text(encoding="utf-8")
    assert "silva2020.pdf" in faltando
    assert "10.1234/abc" in faltando
    assert (projeto / "download.csv").exists()
    assert not (projeto / "pdfs" / "download.csv").exists()
    assert not (projeto / "resumos" / "silva2020").exists()


def test_preparar_resumos_grava_log_se_interromper(tmp_path, monkeypatch):
    projeto, modelo = _projeto_resumo(tmp_path)
    with open(projeto / "cienciometria.csv", "a", encoding="utf-8") as f:
        f.write("10.1234/def,2021,Souza,Outro artigo,Revista,2,1.0,40,aberto (revista),,\n")
    chamadas = []

    def obter(*args, **kwargs):
        chamadas.append(1)
        if len(chamadas) == 1:
            return baixar_pdf.Resultado(motivo="sem PDF")
        raise KeyboardInterrupt

    monkeypatch.setattr(preparar_resumos.baixar_pdf, "obter_pdf", obter)
    with pytest.raises(KeyboardInterrupt):
        preparar_resumos.main([
            str(projeto / "cienciometria.csv"), str(projeto / "pdfs"),
            str(projeto / "resumos"), str(modelo), "Tema", "--sem-navegador", "--intervalo", "0"])
    with open(projeto / "download.csv", encoding="utf-8-sig") as f:
        linhas = list(csv.DictReader(f))
    assert [r["estado"] for r in linhas] == ["falhou"]
    assert "silva2020.pdf" in (projeto / "pdfs" / "FALTANDO.md").read_text(encoding="utf-8")


def test_publicar_faltando_aceita_log_antigo_em_pdfs(tmp_path):
    (tmp_path / "pdfs").mkdir()
    (tmp_path / "pdfs" / "download.csv").write_text(
        "slug,doi,titulo,estado,fonte,url,detalhe\n"
        "x,10.1234/abc,Um artigo,falhou,,,sem PDF\n",
        encoding="utf-8")
    linhas = publicar._faltando(tmp_path)
    assert linhas and linhas[0]["slug"] == "x"


def test_publicar_remove_esquema_perigoso():
    html = publicar.md_para_html("[x](javascript:alert(1))")
    assert "javascript:" not in html


def test_publicar_aceita_so_resumo_dentro_de_resumos():
    assert publicar._resumo_rel("resumos/x/RELATORIO.md") == "resumos/x/RELATORIO.md"
    assert publicar._resumo_rel("../fora.md") == ""
    assert publicar._resumo_rel("C:/fora.md") == ""
    assert publicar._resumo_rel("resumos/../../fora.md") == ""


def test_publicar_linha_com_metricas_vazias():
    linha = publicar._linha({
        "autores": "Silva (2020)", "titulo": "Um artigo", "doi": "10.1/x",
        "acesso": "", "resumo": "", "citacoes": "", "fwci": "", "percentil": "",
        "ano": "", "revista": "Revista", "preprint": False,
    })
    assert "—" in linha


def test_publicar_gera_html(tmp_path):
    projeto = tmp_path / "projeto"
    (projeto / "resumos" / "x").mkdir(parents=True)
    (projeto / "resumos" / "x" / "RELATORIO.md").write_text(
        "# RELATÓRIO — X\n\n## 1. Referência\n\nTexto **forte** e [link](https://exemplo.org). {{isto}}",
        encoding="utf-8")
    (projeto / "REFERENCIAS.md").write_text(
        "# Referências: Tema & Teste\n\n"
        "| Autor (ano) | Título | Link |\n|---|---|---|\n"
        "| IBGE (2026) | Base oficial | https://exemplo.org/base |\n",
        encoding="utf-8")
    (projeto / "tabela.json").write_text(json.dumps([{
        "doi": "10.1234/abc", "ano": 2020, "autor": "Silva",
        "autores": "Silva (2020)", "titulo": "Um artigo", "revista": "Revista",
        "citacoes": 3, "fwci": 1.2, "percentil": 50,
        "acesso": "aberto (revista)", "resumo": "resumos/x/RELATORIO.md",
        "preprint": False,
    }], ensure_ascii=False), encoding="utf-8")
    (projeto / "download.csv").write_text(
        "slug,doi,titulo,estado,fonte,url,detalhe\n"
        "x,10.1234/abc,Um artigo,falhou,,,sem PDF\n",
        encoding="utf-8")
    destino = publicar.gerar(projeto)
    pagina = destino.read_text(encoding="utf-8")
    assert "Tema &amp; Teste" in pagina
    assert 'data-resumo="x"' in pagina
    assert "<strong>forte</strong>" in pagina
    assert "x.pdf" in pagina
    assert "IBGE" in pagina
    assert "{{TITULO}}" not in pagina
    assert "{{RESUMOS}}" not in pagina


def test_entrega_leia_me(tmp_path):
    projeto = tmp_path / "projeto"
    (projeto / "resumos" / "x").mkdir(parents=True)
    (projeto / "resumos" / "x" / "RELATORIO.md").write_text("# RELATÓRIO — X", encoding="utf-8")
    (projeto / "REFERENCIAS.md").write_text("# Referências: Tema\n", encoding="utf-8")
    (projeto / "tabela.json").write_text(json.dumps([{
        "doi": "10.1234/abc", "ano": 2020, "autor": "Silva", "autores": "Silva (2020)",
        "titulo": "Um artigo", "revista": "Revista", "citacoes": 3, "fwci": 1.2,
        "percentil": 50, "acesso": "aberto (revista)", "resumo": "resumos/x/RELATORIO.md",
        "preprint": False,
    }], ensure_ascii=False), encoding="utf-8")
    leia = entrega.escrever_leia_me(projeto)
    texto = leia.read_text(encoding="utf-8")
    assert "# Levantamento: Tema" in texto
    assert "RELATORIO.html" in texto
    assert "1 referência com DOI" in texto
    assert "1 resumo de leitura integral" in texto


def test_entrega_abrir_caminho_inexistente(tmp_path):
    abriu, motivo = entrega.abrir(tmp_path / "nao-existe")
    assert abriu is False
    assert "não existe" in motivo


def test_documentacao_cobre_python_venv_email_e_doi():
    agents = (RAIZ / "AGENTS.md").read_text(encoding="utf-8")
    assert "py -3 --version" in agents
    assert "winget install Python.Python.3.12" in agents
    assert "terminal novo" in agents
    assert "externally-managed-environment" in agents
    assert "--email" in agents
    assert "Quer informar um e-mail" in agents
    assert "CONFERIR" in agents
    assert "ERRO" in agents
    assert "cienciometria-falhas.csv" in agents
    assert "--refazer" in agents
    for nome in ("README.md", "docs/modelo.html"):
        texto = (RAIZ / nome).read_text(encoding="utf-8")
        assert "python --version" in texto
        assert "winget install Python.Python.3.12" in texto
        assert "terminal novo" in texto
        assert "externally-managed-environment" in texto


def test_entrega_leia_me_com_pendencias(tmp_path):
    projeto = tmp_path / "projeto"
    (projeto / "pdfs").mkdir(parents=True)
    (projeto / "REFERENCIAS.md").write_text("# Referências: Tema\n", encoding="utf-8")
    (projeto / "tabela.json").write_text(json.dumps([{
        "doi": "10.1234/abc", "ano": 2020, "autor": "Silva", "autores": "Silva (2020)",
        "titulo": "Um artigo", "revista": "Revista", "citacoes": 3, "fwci": 1.2,
        "percentil": 50, "acesso": "aberto (revista)", "resumo": "",
        "preprint": False,
    }], ensure_ascii=False), encoding="utf-8")
    (projeto / "download.csv").write_text(
        "slug,doi,titulo,estado,fonte,url,detalhe\n"
        "x,10.1234/abc,Um artigo,falhou,,,sem PDF\n",
        encoding="utf-8")
    texto = entrega.escrever_leia_me(projeto).read_text(encoding="utf-8")
    assert "1 PDF não foi baixado" in texto
    assert "x.pdf" in texto
    assert "FALTANDO.md" in texto


@pytest.mark.parametrize("modulo, args", [
    ("orquestrar", ["exemplo/frentes"]),
    ("preparar_resumos", ["x.csv", "exemplo/pdfs", "exemplo/resumos", "m.md", "tema"]),
    ("juntar", ["exemplo/frentes", "exemplo", "tema"]),
    ("conferir_doi", ["exemplo/frentes"]),
    ("cienciometria", ["exemplo/referencias.bib", "exemplo/cienciometria.csv"]),
    ("painel", ["exemplo"]),
    ("publicar", ["exemplo"]),
    ("entrega", ["exemplo", "--nao-abrir"]),
])
def test_scripts_recusam_gravar_no_exemplo(modulo, args, monkeypatch, capsys):
    monkeypatch.chdir(RAIZ)
    mod = __import__(modulo)
    with pytest.raises(SystemExit) as saida:
        mod.main(args)
    assert saida.value.code == 2
    assert "projetos/<tema>/" in capsys.readouterr().err


def test_projeto_reconhece_caminhos_do_exemplo(tmp_path):
    import projeto
    assert projeto.no_exemplo(RAIZ / "exemplo")
    assert projeto.no_exemplo(RAIZ / "exemplo" / "resumos" / "x")
    assert not projeto.no_exemplo(RAIZ / "projetos" / "meu-tema")
    assert not projeto.no_exemplo(tmp_path)
