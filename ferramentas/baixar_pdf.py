"""Baixa PDFs de artigos de acesso aberto, tentando vários caminhos.

Uso principal: o preparar_resumos.py chama obter_pdf(). Também dá para testar
um DOI sozinho:

    python ferramentas/baixar_pdf.py 10.3390/rs11141721 --email voce@exemplo.org

Ordem das tentativas:
1. link direto, com requests, curl e urllib;
2. página do artigo: meta citation_pdf_url, link alternate e âncoras de PDF;
3. fontes por DOI: OpenAlex, Unpaywall (se houver --email), Europe PMC e
   Semantic Scholar;
4. navegador headless (Playwright), se instalado, para páginas com JavaScript.

Só tenta o que é de acesso aberto. Não contorna paywall, login, captcha nem
bloqueio contra robôs: o script se identifica como robô e desiste quando o site
recusa. Insistir com truques de disfarce pode fazer a editora bloquear a faixa
de endereços da instituição inteira.
"""
import argparse
import html as htmlmod
import json
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path

UA = ("Mozilla/5.0 (compatible; levantamento-ia/1.0; "
      "+https://github.com/VictorGit10/levantamento-ia)")
MAX_BYTES = 80 * 1024 * 1024

# Nome usado no CDN da MDPI (mdpi-res.com), que não é sempre o nome da revista.
MDPI_APELIDOS = {
    "remote sensing": "remotesensing",
    "forests": "forests",
    "sensors": "sensors",
    "plants": "plants",
    "sustainability": "sustainability",
    "applied sciences": "applsci",
    "journal of clinical medicine": "jcm",
    "international journal of molecular sciences": "ijms",
    "land": "land",
    "water": "water",
    "agriculture": "agriculture",
    "agronomy": "agronomy",
    "fire": "fire",
    "biology": "biology",
    "genes": "genes",
    "materials": "materials",
    "energies": "energies",
    "mathematics": "mathematics",
    "electronics": "electronics",
    "foods": "foods",
    "nutrients": "nutrients",
    "cancers": "cancers",
    "diagnostics": "diagnostics",
}

MDPI_POR_ISSN = {
    "2072-4292": "remotesensing",
    "1999-4907": "forests",
    "1424-8220": "sensors",
    "2223-7747": "plants",
    "2071-1050": "sustainability",
    "2076-3417": "applsci",
    "2077-0383": "jcm",
    "1422-0067": "ijms",
    "2073-445X": "land",
    "2073-4441": "water",
    "2077-0472": "agriculture",
    "2073-4395": "agronomy",
    "2571-6255": "fire",
    "2079-7737": "biology",
    "2073-4425": "genes",
    "1996-1944": "materials",
    "1996-1073": "energies",
    "2227-7390": "mathematics",
    "2079-9292": "electronics",
    "2304-8158": "foods",
    "2072-6643": "nutrients",
    "2072-6694": "cancers",
    "2075-4418": "diagnostics",
}


@dataclass
class Resultado:
    """O PDF baixado (ou None), de onde veio e o que foi tentado."""
    dados: bytes | None = None
    fonte: str = ""
    url: str = ""
    motivo: str = ""
    tentativas: list = field(default_factory=list)


def _cabecalhos(referer=None):
    h = {
        "User-Agent": UA,
        "Accept": "application/pdf,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8",
    }
    if referer:
        h["Referer"] = referer
    return h


_SESSAO_REQUESTS = None


def _sessao_requests():
    global _SESSAO_REQUESTS
    if _SESSAO_REQUESTS is None:
        import requests
        _SESSAO_REQUESTS = requests.Session()
    return _SESSAO_REQUESTS


def mdpi_cdn_de_url(url, revista=""):
    """Converte a página/PDF da MDPI no PDF do CDN aberto (mdpi-res.com).

    Ex.: https://www.mdpi.com/2072-4292/11/14/1721/pdf
      -> https://mdpi-res.com/d_attachment/remotesensing/remotesensing-11-01721/
         article_deploy/remotesensing-11-01721.pdf
    """
    m = re.match(r"https?://(?:www\.)?mdpi\.com/(\d{4}-\d{3}[\dxX])/(\d+)/(\d+)/(\d+)",
                 url or "", re.I)
    if not m:
        return ""
    issn, volume, _, artigo = m.groups()
    apelido = (MDPI_POR_ISSN.get(issn.upper())
               or MDPI_APELIDOS.get((revista or "").lower().strip())
               or re.sub(r"[^a-z0-9]", "", (revista or "").lower()))
    if not apelido:
        return ""
    arquivo = f"{apelido}-{volume}-{int(artigo):05d}"
    return (f"https://mdpi-res.com/d_attachment/{apelido}/{arquivo}/"
            f"article_deploy/{arquivo}.pdf")


def eh_pdf(dados):
    """True se os bytes começam com a assinatura de um PDF."""
    return bool(dados) and b"%PDF-" in dados[:1024]


def _get_requests(url, referer, timeout):
    try:
        sessao = _sessao_requests()
    except Exception:
        return None
    try:
        with sessao.get(url, headers=_cabecalhos(referer), timeout=timeout,
                        allow_redirects=True, stream=True) as r:
            if r.status_code >= 400:
                return None
            partes, total, truncado = [], 0, False
            for bloco in r.iter_content(65536):
                if not bloco:
                    continue
                total += len(bloco)
                if total > MAX_BYTES:
                    truncado = True
                    break
                partes.append(bloco)
            if truncado:
                return None
            return b"".join(partes)
    except Exception:
        return None


def _get_curl(url, referer, timeout):
    cmd = ["curl", "-fsL", "--compressed", "--max-time", str(timeout),
           "--max-filesize", str(MAX_BYTES), "-A", UA,
           "-H", "Accept-Language: pt-BR,pt;q=0.9,en;q=0.8"]
    if referer:
        cmd += ["-e", referer]
    cmd.append(url)
    try:
        r = subprocess.run(cmd, capture_output=True, timeout=timeout + 5)
    except Exception:
        return None
    if r.returncode != 0 or not r.stdout:
        return None
    return r.stdout


def _get_urllib(url, referer, timeout):
    try:
        req = urllib.request.Request(url, headers=_cabecalhos(referer))
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read(MAX_BYTES + 1)
    except Exception:
        return None


ESTRATEGIAS = (
    ("requests", _get_requests),
    ("curl", _get_curl),
    ("urllib", _get_urllib),
)


def baixar_direto(url, referer=None, timeout=60):
    """Tenta o link com clientes diferentes; devolve (bytes, nome da fonte).

    O orçamento de tempo vale para o endereço inteiro (todos os clientes e uma
    repetição), não para cada cliente. Assim um servidor que não responde não
    prende o script por minutos.
    """
    if not re.match(r"https?://", url or "", re.I):
        return None, ""
    limite = time.time() + max(1, timeout)
    for tentativa in range(2):
        for nome, funcao in ESTRATEGIAS:
            restante = limite - time.time()
            if restante <= 1:
                return None, ""
            dados = funcao(url, referer, max(1, min(timeout, int(restante))))
            if dados and len(dados) >= MAX_BYTES:
                continue
            if dados:
                return dados, nome
        if tentativa == 0 and limite - time.time() > 3:
            time.sleep(2)
    return None, ""


def _decodificar(dados):
    for codificacao in ("utf-8", "latin-1"):
        try:
            return dados.decode(codificacao)
        except UnicodeDecodeError:
            continue
    return dados.decode("utf-8", "replace")


class _LinksPdf(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.metas = []
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or "") for k, v in attrs}
        if tag == "meta":
            nome = (a.get("name") or a.get("property") or "").lower()
            if nome in ("citation_pdf_url", "og:pdf", "pdf_url") and a.get("content"):
                self.metas.append(a["content"])
        elif tag == "link":
            if "pdf" in (a.get("type") or "").lower() and a.get("href"):
                self.hrefs.append(a["href"])
        elif tag in ("a", "iframe", "embed", "object"):
            href = a.get("href") or a.get("src") or a.get("data")
            if href:
                self.hrefs.append(href)


def links_pdf_do_html(texto, base):
    """Links prováveis de PDF numa página de artigo, já absolutos."""
    if not texto:
        return []
    parser = _LinksPdf()
    try:
        parser.feed(texto)
    except Exception:
        return []
    candidatos = list(parser.metas)
    for href in parser.hrefs:
        baixo = href.lower()
        if any(marca in baixo for marca in (".pdf", "/pdf", "pdf?", "download", "fulltext")):
            candidatos.append(href)
    saida = []
    for c in candidatos:
        c = htmlmod.unescape(c.strip())
        if c.startswith("//"):
            c = "https:" + c
        u = urllib.parse.urljoin(base, c)
        if u.lower().startswith("http") and u not in saida:
            saida.append(u)
    return saida[:10]


def _json(url, timeout=25):
    ultimo = None
    for tentativa in range(2):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8", "replace"))
        except Exception as e:
            ultimo = e
            if tentativa == 0:
                time.sleep(1)
    raise ultimo


def fontes_por_doi(doi, email="", timeout=25):
    """URLs de PDF que as APIs abertas conhecem para este DOI."""
    urls = []

    def add(u):
        if isinstance(u, str) and u.startswith("http") and u not in urls:
            urls.append(u)

    if not doi:
        return urls
    doi_url = urllib.parse.quote(doi, safe="")
    try:
        url_openalex = ("https://api.openalex.org/works/doi:" + doi_url
                        + (f"?mailto={urllib.parse.quote(email)}" if email else ""))
        w = _json(url_openalex, timeout)
        for local in [w.get("best_oa_location")] + (w.get("locations") or []):
            if local:
                add(local.get("pdf_url"))
                add(local.get("landing_page_url"))
        # A MDPI bloqueia o domínio www.mdpi.com para scripts, mas o PDF fica
        # num CDN aberto (mdpi-res.com) com um endereço previsível.
        if doi.lower().startswith("10.3390/"):
            fonte = ((w.get("primary_location") or {}).get("source") or {})
            biblio = w.get("biblio") or {}
            volume, artigo = biblio.get("volume"), biblio.get("first_page")
            if volume and artigo and str(artigo).isdigit():
                nome = (fonte.get("display_name") or "").lower().strip()
                apelido = (MDPI_POR_ISSN.get((fonte.get("issn_l") or "").upper())
                           or MDPI_APELIDOS.get(nome)
                           or re.sub(r"[^a-z0-9]", "", nome))
                if apelido:
                    arquivo = f"{apelido}-{volume}-{int(artigo):05d}"
                    add(f"https://mdpi-res.com/d_attachment/{apelido}/{arquivo}/"
                        f"article_deploy/{arquivo}.pdf")
    except Exception:
        pass
    if email:
        try:
            u = _json("https://api.unpaywall.org/v2/" + doi_url + "?email=" +
                      urllib.parse.quote(email), timeout)
            for local in [u.get("best_oa_location")] + (u.get("oa_locations") or []):
                if local:
                    add(local.get("url_for_pdf"))
                    add(local.get("url"))
        except Exception:
            pass
    try:
        consulta = urllib.parse.quote(f'DOI:"{doi}"')
        e = _json("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=" +
                  consulta + "&format=json&resultType=core&pageSize=5", timeout)
        for trabalho in (e.get("resultList") or {}).get("result") or []:
            for ft in (trabalho.get("fullTextUrlList") or {}).get("fullTextUrl") or []:
                if (ft.get("documentStyle") or "").lower() in ("pdf", "pdf_only"):
                    add(ft.get("url"))
                elif "pdf" in (ft.get("url") or "").lower():
                    add(ft.get("url"))
            if trabalho.get("pmcid"):
                add(f"https://europepmc.org/articles/{trabalho['pmcid']}/pdf")
    except Exception:
        pass
    try:
        s = _json("https://api.semanticscholar.org/graph/v1/paper/DOI:" + doi_url +
                  "?fields=openAccessPdf", timeout)
        add((s.get("openAccessPdf") or {}).get("url"))
    except Exception:
        pass
    return urls


def baixar_com_navegador(urls, timeout=60):
    """Último recurso: Chromium headless (Playwright) para páginas com JavaScript."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return None, "", "", "Playwright não instalado"
    urls = [u for u in urls if u and re.match(r"https?://", u, re.I)][:2]
    if not urls:
        return None, "", "", "sem URL para o navegador"
    try:
        with sync_playwright() as p:
            try:
                navegador = p.chromium.launch(headless=True)
            except Exception as e:
                return None, "", "", (f"Chromium indisponível ({type(e).__name__}); "
                                      "rode: playwright install chromium")
            contexto = navegador.new_context(
                user_agent=UA, locale="pt-BR", accept_downloads=True,
                viewport={"width": 1366, "height": 900})
            for url in urls:
                pagina = contexto.new_page()
                try:
                    pagina.goto(url, wait_until="domcontentloaded",
                                timeout=min(timeout, 45) * 1000)
                    pagina.wait_for_timeout(1000)
                    # Tela de verificação contra robôs: desiste, não espera passar.
                    titulo = (pagina.title() or "").lower()
                    if "just a moment" in titulo or "checking" in titulo:
                        continue
                    info = pagina.evaluate("""() => {
                        const meta = document.querySelector('meta[name="citation_pdf_url"]');
                        const links = [...document.querySelectorAll('a[href]')]
                          .filter(a => /pdf|download/i.test(a.href) || /pdf/i.test(a.textContent || ''))
                          .map(a => a.href).slice(0, 10);
                        return {meta: meta ? meta.content : '', links, tipo: document.contentType};
                    }""")
                    candidatos = ([info.get("meta")] + (info.get("links") or [])) if info else []
                    if info and info.get("tipo") == "application/pdf":
                        candidatos.insert(0, pagina.url)
                    for alvo in candidatos:
                        if not alvo:
                            continue
                        alvo = urllib.parse.urljoin(pagina.url, alvo)
                        try:
                            resposta = contexto.request.get(alvo, timeout=min(timeout, 45) * 1000)
                            if resposta.ok and eh_pdf(resposta.body()):
                                return resposta.body(), "playwright", alvo, ""
                        except Exception:
                            pass
                    try:
                        with pagina.expect_download(timeout=15000) as espera:
                            pagina.locator("a").filter(has_text=re.compile("pdf", re.I)).first.click()
                        baixado = espera.value
                        caminho = baixado.path()
                        if caminho:
                            dados = Path(caminho).read_bytes()
                            if eh_pdf(dados):
                                return dados, "playwright", pagina.url, ""
                    except Exception:
                        pass
                except Exception:
                    pass
                finally:
                    pagina.close()
            contexto.close()
            navegador.close()
    except Exception as e:
        return None, "", "", f"navegador: {type(e).__name__}: {e}"
    return None, "", "", "o navegador não achou um PDF"


def obter_pdf(doi, titulo="", links=None, email="", navegador=True, timeout=60, revista=""):
    """Tenta links, página do DOI, APIs e (por último) o navegador headless."""
    resultado = Resultado()
    links = [l.strip() for l in (links or []) if l and l.strip()]
    expandidos = []
    for link in links:
        cdn = mdpi_cdn_de_url(link, revista)
        if cdn:
            expandidos.append(cdn)
        expandidos.append(link)
    links = expandidos
    vistos = set()

    def tentar(lista):
        for url in lista:
            if not url or url in vistos:
                continue
            vistos.add(url)
            dados, fonte = baixar_direto(url, referer=f"https://doi.org/{doi}", timeout=timeout)
            resultado.tentativas.append(f"{url} ({fonte or 'sem resposta'})")
            if not dados:
                continue
            if eh_pdf(dados):
                resultado.dados, resultado.fonte, resultado.url = dados, fonte, url
                return True
            for sub in links_pdf_do_html(_decodificar(dados), url):
                if sub in vistos:
                    continue
                vistos.add(sub)
                d2, f2 = baixar_direto(sub, referer=url, timeout=timeout)
                resultado.tentativas.append(f"{sub} ({f2 or 'sem resposta'})")
                if d2 and eh_pdf(d2):
                    resultado.dados, resultado.fonte = d2, f"página:{f2}"
                    resultado.url = sub
                    return True
        return False

    if tentar(links):
        return resultado
    if doi and tentar(["https://doi.org/" + doi]):
        return resultado
    if doi and tentar(fontes_por_doi(doi, email, min(timeout, 25))):
        return resultado
    if navegador:
        dados, fonte, url, motivo = baixar_com_navegador(
            links + (["https://doi.org/" + doi] if doi else []), timeout=timeout)
        if dados:
            resultado.dados, resultado.fonte, resultado.url = dados, fonte, url
            return resultado
        if motivo:
            resultado.tentativas.append(motivo)
    resultado.motivo = ("nenhum link entregou PDF"
                        + (f"; {len(resultado.tentativas)} tentativas" if resultado.tentativas else ""))
    return resultado


def main(argv=None):
    ap = argparse.ArgumentParser(description="Baixa um PDF de acesso aberto pelo DOI.")
    ap.add_argument("doi", help="DOI do artigo (ex.: 10.3390/rs11141721)")
    ap.add_argument("--saida", default="", help="arquivo PDF de saída")
    ap.add_argument("--email", default="", help="e-mail para o Unpaywall (opcional)")
    ap.add_argument("--sem-navegador", action="store_true", help="não tenta o Chromium headless")
    ap.add_argument("--timeout", type=int, default=60, help="segundos por endereço (padrão: 60)")
    a = ap.parse_args(argv)
    r = obter_pdf(a.doi, "", [], a.email, not a.sem_navegador, a.timeout)
    if not r.dados:
        print("FALHOU: " + r.motivo)
        for t in r.tentativas:
            print("  -", t)
        return 1
    if a.saida:
        destino = Path(a.saida)
    else:
        nome = re.sub(r"[^a-z0-9]+", "", a.doi.lower().split("/")[-1])[:60] or "artigo"
        destino = Path(nome + ".pdf")
    destino.write_bytes(r.dados)
    print(f"OK {len(r.dados)} bytes, fonte {r.fonte}: {r.url}")
    print("->", destino)
    return 0


if __name__ == "__main__":
    sys.exit(main())
