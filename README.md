# Levantamento bibliográfico do doutorado — Lana Teixeira (PPGCA/UFG)

Levantamento e acompanhamento da literatura para a tese *Sensoriamento remoto multissensorial aplicado à estimativa de biomassa e estoque de carbono da silvicultura no estado de Goiás*.

**Relatório do levantamento:** https://lanamara.github.io/levantamento-ia/projetos/doutorado-silvicultura-go/RELATORIO.html

Ferramenta original: [VictorGit10/levantamento-ia](https://github.com/VictorGit10/levantamento-ia), de Victor Amaral (LAPIG/UFG), com explicação em https://victorgit10.github.io/levantamento-ia/. Um tema de pesquisa vira uma lista de referências conferidas, com dados de citação e um resumo de cada artigo aberto, usando o [opencode](https://opencode.ai) com o modelo **DeepSeek V4.1 Flash gratuito**. Não precisa de conta nem de assinatura.

## Neste fork

Fork de [VictorGit10/levantamento-ia](https://github.com/VictorGit10/levantamento-ia) para o doutorado de Lana Teixeira (PPGCA/UFG), com estes acréscimos:

| O quê | Onde | Como |
|---|---|---|
| Projeto do doutorado, 6 frentes | `projetos/doutorado-silvicultura-go/` | hiperespectral (PRISMA/EnMAP); LiDAR GEDI e ICESat-2 como referência; fusão com aprendizado de máquina; idade e produtividade; fragilidade e AHP/WLC; Goiás, Cerrado e seringueira |
| Revista oficial e indicadores | `ferramentas/revistas.py`, usado pelo `cienciometria.py` | nome, ISSN-L, editora, APC e índice h (OpenAlex); DOAJ e CWTS Core (OpenAlex); retratação (Retraction Watch, via OpenAlex); Qualis CAPES 2021–2024 com `--qualis planilha.csv` exportada da Sucupira |
| Conferência das suas referências | `ferramentas/conferir_lista.py` | confere título, ano, volume e páginas no Crossref; sugere DOI (OpenAlex) só quando título e ano batem; grava `MINHAS_REFERENCIAS.md` |
| Citações x lista de referências | `ferramentas/conferir_citacoes.py` | lê um `.docx` (ou `.txt`/`.md`) e aponta citação sem referência, ano diferente, referência nunca citada e mesmo autor/ano sem letra (2025a, 2025b) |
| Mapa de lacunas | `ferramentas/lacunas.py` | marca em cada resumo sensor, variável, plantio, região e método (seções 1 a 4, ignorando menções negadas) e grava `LACUNAS.md` com as matrizes e as combinações centrais do projeto, e `lacunas.csv` |
| Relatório com filtros | `ferramentas/publicar.py`, `modelos/relatorio.html` | filtros por frente, indicador da revista e "já cito"; retratados em vermelho; seção Novidades |
| Atualização mensal | `ferramentas/atualizar.py`, `.github/workflows/atualizar.yml` | busca no OpenAlex o que foi publicado desde a última vez, com as consultas de `consultas.json`; grava `NOVIDADES.md` |

**Sobre "revista predatória".** Não existe lista aberta e oficial: a lista de Beall saiu do ar em 2017 e o Cabells Predatory Reports é pago. Por isso a tabela não rotula revistas como predatórias. Ela mostra fatos conferíveis (DOAJ, CWTS Core, Qualis, retratação) e marca "⚠ conferir" quando a revista não está em nenhuma dessas listas, o que pede uma conferência à mão, não uma condenação.

**Atualização mensal.** Roda no dia 1 de cada mês pelo GitHub Actions. Em forks, os agendamentos começam desativados: abra a aba **Actions** e ative os workflows. O GitHub também desativa agendamentos de repositórios públicos sem atividade por 60 dias; como cada execução grava `atualizacao.json`, o próprio workflow mantém o repositório ativo. Para rodar na hora: **Actions → Atualização mensal do levantamento → Run workflow**. À mão: `python ferramentas/atualizar.py projetos/doutorado-silvicultura-go`.

```
# referências do pré-projeto
python ferramentas/conferir_lista.py projetos/doutorado-silvicultura-go/minhas_referencias.txt projetos/doutorado-silvicultura-go
# cienciometria com Qualis (opcional)
python ferramentas/cienciometria.py projetos/doutorado-silvicultura-go/referencias.bib projetos/doutorado-silvicultura-go/cienciometria.csv --qualis projetos/doutorado-silvicultura-go/qualis.csv
# trabalhos novos
python ferramentas/atualizar.py projetos/doutorado-silvicultura-go
```

## Peça à sua IA (o jeito mais fácil)

Você precisa de um assistente com acesso a terminal, arquivos e internet (Claude Code, Codex, opencode, Cursor e afins). Ele confere o que falta, pede seu ok e instala o resto com você; você não precisa digitar comando nem entender de programação. Cole isto no chat:

> Leia o repositório https://github.com/Lanamara/levantamento-ia e faça um levantamento bibliográfico sobre: **<seu tema>**.

A IA lê o [`AGENTS.md`](AGENTS.md), confere o Python (`python --version`, 3.10 ou mais) e roda o `ferramentas/conferir.py`, que mostra o que falta instalar, com o comando de cada sistema. Só depois do seu ok ela instala e testa o modelo grátis. Em seguida combina com você o recorte e as frentes, cria a pasta em `projetos/`, roda as etapas, confere os DOIs e abre a pasta e o `RELATORIO.html` na sua tela. As buscas e a leitura dos artigos rodam nos agentes grátis do opencode; a IA que conversa com você confere, corrige e junta. Se algum PDF não baixar, ela mostra o nome do arquivo e espera você salvar em `pdfs/`; depois continua de onde parou.

Um chat sem terminal (ChatGPT, Claude web, Gemini web) consegue ajudar a planejar as frentes e escrever os pedidos, mas não consegue baixar PDF, rodar o opencode nem abrir a pasta. Nesse caso, use um assistente com terminal.

O seu levantamento fica em `projetos/<seu-tema>/`. A pasta `exemplo/` é um levantamento pronto de outro tema, só para você ver como fica o resultado; a IA não mexe nela.

## Por que usar isto

O Consensus e o Elicit atendem bem a perguntas rápidas. Este repositório serve para você montar a base de referências de um projeto, guardar todos os arquivos e conferir cada dado, sem precisar pagar assinatura.

| Este repositório | Consensus, Elicit e afins |
| --- | --- |
| Usa modelos grátis do opencode e não pede assinatura. Precisa de um assistente de IA com terminal (Claude Code, Codex, opencode ou Cursor) para conduzir. | Respondem rápido em interface pronta no navegador, sem instalar nada. Têm plano grátis com limites; o uso intenso é pago. |
| O tema é dividido em 3 a 5 frentes combinadas com a IA; cada uma vira uma busca separada. Aceita recortes regionais e em português. | Buscam numa base própria de artigos indexados, muito grande. |
| Baixa e lê artigos de acesso aberto inteiros, não só o resumo. Cada número citado no resumo traz a página do artigo no formato [p. 7] para conferência. | O critério de busca e de resumo fica dentro da ferramenta; você vê o resultado, não o processo. |
| Confere cada DOI no Crossref (o DOI existe e o título bate) e traz métricas do OpenAlex (citações, FWCI, percentil, acesso aberto). Aceita relatórios e bases oficiais sem DOI (IBGE, Ibá, MapBiomas, Embrapa). | Depende da ferramenta e do plano. |
| Tudo fica em arquivos seus: BibTeX (Zotero, Mendeley), CSV, resumos em Markdown e um RELATORIO.html com busca e filtro. Os registros ficam na pasta para ver como cada resultado foi obtido e refazer. | Depende da ferramenta e do plano; vale conferir o que dá para exportar. |

### Quanto dá para confiar

No exemplo deste repositório (tema de biomassa florestal em Goiás):
- São 49 artigos com DOI; os 49 DOIs existem no Crossref; em 48 o título bateu automaticamente e 1 (título bilíngue) foi conferido à mão.
- Artigos fechados entram na lista com as métricas, mas não são lidos.
- O resumo pode errar um número: por isso a página vem indicada. Confira no artigo antes de citar.
- Não é revisão sistemática: a busca feita pelos modelos pode deixar artigos de fora, e não há garantia de cobertura completa. Para revisão sistemática, use também Scopus, Web of Science e um protocolo como o PRISMA.

Para uma pergunta rápida, Consensus ou Elicit; para montar e guardar a base de referências de um projeto, com cada número rastreável, este repositório.

## Os modelos grátis podem mudar

Em outubro de 2026, o DeepSeek V4.1 Flash é gratuito no opencode, com o GLM 5.3 Flash gratuito como reserva. Isso pode mudar, mas o opencode costuma manter algum modelo gratuito, que traz "free" no nome.

Para ver os disponíveis: `opencode models`. Para usar outro: `--modelo <nome>` no `orquestrar.py`. A IA que conduz o levantamento faz essa troca se o modelo padrão falhar.

O plano gratuito tem limite diário por conexão de internet. Quando acaba, retoma-se no dia seguinte.

## O que sai no fim

| Camada | Arquivo | Formato | Para quê |
|---|---|---|---|
| Para começar | `LEIA-ME.md` | Markdown | o que abrir, o que está pronto e o que falta |
| Plano | `PLANO.md` | Markdown | tema, frentes e decisões combinadas |
| Para ler | `RELATORIO.html` | HTML único, sem servidor | busca, filtro, ordenação e resumos numa janela |
| Para ler | `TABELA.md`, `REFERENCIAS.md` | Markdown | texto, GitHub, diff |
| Para citar | `referencias.bib` | BibTeX | Zotero, Mendeley, LaTeX |
| Para analisar | `cienciometria.csv`, `tabela.json`, `verificacao.csv`, `download.csv` | CSV e JSON | planilha e scripts |
| Para o agente | `frentes/*/RELATORIO.md`, `resumos/*/RELATORIO.md` | Markdown com contrato fixo | as etapas seguintes |
| Interno | `pdfs/`, `resumos/*/TEXTO.txt`, `log.jsonl` | — | não publicar (direitos autorais) |

O HTML é a entrega humana; o Markdown é a fonte editável; o CSV/JSON é a camada de dados. Não é preciso subir um servidor: o `RELATORIO.html` abre com dois cliques. Se você quiser uma URL local (para abrir numa aba em vez do arquivo), use `python ferramentas/entrega.py projetos/meu-tema --servir`.

**Por que esses formatos.** O agente escreve Markdown porque é o que ele faz bem e porque o texto continua legível e comparável. Os scripts convertem o que precisa de precisão para CSV/JSON/BibTeX, em vez de pedir que o modelo acerte a sintaxe. O `.txt` existe só como texto integral extraído, para o agente ler sem abrir o PDF; ele fica fora do Git por direitos autorais e não é uma entrega. O HTML é um arquivo único, sem dependência de servidor ou internet.

## Exemplo real

Tema: *sensoriamento remoto multissensorial aplicado à estimativa de biomassa e carbono da silvicultura em Goiás*. Pasta [`exemplo/`](exemplo/).

- 4 frentes (sensores ópticos, radar e LiDAR, fusão com aprendizado de máquina, dados de Goiás), 2 agentes por vez, cerca de 10 minutos.
- 49 artigos diferentes com DOI, mais 4 bases oficiais sem DOI (IBGE, Ibá, MapBiomas, Embrapa). As frentes somaram 56 indicações porque 5 artigos apareceram em duas ou três delas. Os 49 DOIs existem no Crossref; em 48 o título bateu sozinho, e 1 (título bilíngue) foi conferido à mão.
- Dos 47 artigos abertos, o download automático trouxe 41 (os da MDPI vêm do CDN aberto `mdpi-res.com`, porque o domínio `www.mdpi.com` bloqueia script). Os 6 que faltaram são da Elsevier, da Taylor & Francis e da Springer, que bloqueiam download por script; estão em `exemplo/pdfs/FALTANDO.md`, com o nome que o arquivo deve ter se alguém salvar à mão.
- 42 artigos foram lidos por inteiro e resumidos, 2 agentes por vez, cerca de 1 minuto cada: [`exemplo/resumos/`](exemplo/resumos/). Um deles (Saim et al., 2025) foi lido numa execução anterior, quando o PDF ainda baixava.
- Na frente de radar e LiDAR o agente ficou sem a busca na web e buscou direto nas APIs do Crossref e do OpenAlex; o resultado tem a mesma qualidade.
- **Veja o resultado do exemplo do repositório original no navegador:** https://victorgit10.github.io/levantamento-ia/exemplo.html (o mesmo `RELATORIO.html` que a IA abre na sua tela no fim). Em texto, comece por [`exemplo/TABELA.md`](exemplo/TABELA.md).

## Como funciona

| Etapa | Ferramenta | Saída |
|---|---|---|
| 1. Busca por frentes | `orquestrar.py` + agentes com busca na web | uma tabela por frente |
| 2. Junção e DOI | `juntar.py` + `conferir_doi.py` (Crossref) | `REFERENCIAS.md`, `referencias.bib` |
| 3. Cienciometria | `cienciometria.py` (OpenAlex) | citações, FWCI, percentil, acesso aberto |
| 4. Leitura integral | `preparar_resumos.py` + `orquestrar.py` | um resumo por artigo aberto, com página em todo número |
| 5. Entrega | `painel.py`, `publicar.py`, `entrega.py` | `TABELA.md`, `tabela.json`, `RELATORIO.html`, `LEIA-ME.md` |

O `AGENTS.md` descreve o contrato de conversa e de arquivos para a IA. O `modelos/PEDIDO-busca.md` e o `modelos/PEDIDO-resumo.md` fixam as colunas e as seções que os scripts esperam; se um agente mudar a ordem, a IA deve corrigir o pedido, não o script. O `orquestrar.py` imprime `FORMATO <frente>` quando o relatório foge do contrato (coluna ou seção faltando, tabela no resumo, poucas páginas citadas). Avisos graves também marcam a frente como falha; use `--refazer <frente>` para rodá-la de novo.

## Se preferir rodar à mão

Precisa de Python 3.10+ e Node.js. O `conferir.py` diz o que falta, sem instalar nada:

```bash
git clone https://github.com/Lanamara/levantamento-ia
cd levantamento-ia
python --version   # no Windows, também py -3 --version; no Mac/Linux, python3 --version
python ferramentas/conferir.py
# instale o que ele apontar; por exemplo:
npm install -g @opencode/cli
python -m pip install -r requirements.txt
python ferramentas/conferir.py --testar-modelo
```

Se o `python --version` falhar ou mostrar menos de 3.10, instale o Python 3.10+ (Windows `winget install Python.Python.3.12`; Mac `brew install python@3.12` ou o instalador de python.org; Linux pelo gerenciador de pacotes) e abra um terminal novo.

Se o `pip` recusar com `externally-managed-environment` (Mac/Linux), crie um ambiente na raiz do clone e use o Python dele em todos os comandos:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python ferramentas/conferir.py --testar-modelo
```

**Busca na web:** copie [`modelos/opencode.json`](modelos/opencode.json) para a pasta que contém as frentes (`projetos/meu-tema/frentes/opencode.json`). Ele libera `websearch` e `webfetch`. O orquestrador conta as chamadas e imprime `SEM-BUSCA <frente>` quando não houver nenhuma.

**1. Uma pasta por frente**, cada uma com um `PEDIDO.md` feito a partir de [`modelos/PEDIDO-busca.md`](modelos/PEDIDO-busca.md) (troque `{TEMA}`, `{FRENTE}` e `{DATA}`):

```
projetos/meu-tema/frentes/1-algum-recorte/PEDIDO.md
projetos/meu-tema/frentes/2-outro-recorte/PEDIDO.md
```

**2. Rodar os agentes** (2 por vez; o script liga a busca na web do opencode):

```bash
python ferramentas/orquestrar.py projetos/meu-tema/frentes --paralelo 2
```

**3. Juntar, conferir os DOIs e buscar a cienciometria:**

```bash
python ferramentas/juntar.py projetos/meu-tema/frentes projetos/meu-tema "Título do tema"
python ferramentas/conferir_doi.py projetos/meu-tema/frentes
python ferramentas/cienciometria.py projetos/meu-tema/referencias.bib projetos/meu-tema/cienciometria.csv
```

**4. Baixar os PDFs e preparar os resumos:**

```bash
python ferramentas/preparar_resumos.py projetos/meu-tema/cienciometria.csv projetos/meu-tema/pdfs \
  projetos/meu-tema/resumos modelos/PEDIDO-resumo.md "Título do tema" --email voce@seuemail.com --abrir
python ferramentas/orquestrar.py projetos/meu-tema/resumos --paralelo 2
```

O `--email` é opcional e serve para o Unpaywall e para o `mailto` do OpenAlex; ele não é publicado. Use um e-mail real: o Unpaywall recusa domínios de exemplo. O `--abrir` abre a pasta `pdfs/` quando faltar algum artigo.

**5. Montar a tabela e entregar:**

```bash
python ferramentas/painel.py projetos/meu-tema
python ferramentas/entrega.py projetos/meu-tema
```

O `entrega.py` gera o `RELATORIO.html` e o `LEIA-ME.md`, abre a pasta e o relatório e, com `--servir`, sobe uma URL local. Funciona em Windows (Explorador), macOS (Finder) e Linux (`xdg-open`); no WSL, usa o Explorer do Windows. Se estiver sem interface gráfica, use `--nao-abrir`.

## Quando o PDF não baixa

O `preparar_resumos.py` tenta, em camadas:

1. o link direto do OpenAlex, com `requests`, `curl` e `urllib`; se for MDPI, troca o endereço `www.mdpi.com` pelo CDN aberto `mdpi-res.com`, que não bloqueia o script;
2. a página do artigo, procurando `citation_pdf_url` e links de PDF;
3. OpenAlex, Unpaywall (com `--email`), Europe PMC e Semantic Scholar;
4. Chromium headless via Playwright, se estiver instalado.

No exemplo, o download automático trouxe 41 dos 47 artigos abertos, sem navegador headless; os 6 restantes são de editoras que bloqueiam script, e um repositório às vezes não responde. Se algum falhar por instabilidade da rede, rode de novo: o que já está em `pdfs/` é aproveitado e o script não baixa outra vez.

Para habilitar o reforço opcional:

```bash
python -m pip install -r requirements-opcional.txt
playwright install chromium
```

O Playwright é o último recurso, para páginas que só mostram o link do PDF depois de rodar JavaScript. No Windows, na primeira vez, o Firewall pode perguntar se o `chrome-headless-shell` pode acessar a rede; pode permitir ou cancelar, o download funciona nos dois casos. O script não contorna paywall, login, captcha nem bloqueio contra robôs: ele se identifica como robô, só tenta o que é de acesso aberto e desiste quando o site recusa. Insistir com disfarce poderia fazer a editora bloquear a rede da instituição inteira.

Quando ainda assim faltar, o script grava `projetos/meu-tema/download.csv` e `projetos/meu-tema/pdfs/FALTANDO.md` com o nome esperado, o DOI, o título e o motivo. A pessoa pode baixar pelo navegador, salvar em `pdfs/` com esse nome (ou com outro; o script reconhece pelo DOI, pelo título ou pelo primeiro autor) e rodar o mesmo comando de novo. O que já está na pasta é aproveitado.

## Limites

- **Gratuito tem limite por conexão de internet**, somado entre os modelos gratuitos. 2 agentes por vez funcionam; 5 estouram em minutos. Por dia, o limite acabou depois de cerca de 200 chamadas ao modelo: a primeira execução fez as 4 frentes e 19 resumos do exemplo; os outros 23 resumos rodaram em outro dia. Ao estourar, o orquestrador tenta o modelo reserva e, se também estiver no limite, marca a frente como falha (código de saída 1); rode de novo no dia seguinte e ele continua de onde parou.
- **Privacidade:** segundo a [documentação do opencode](https://opencode.ai/docs/zen/) (consultada em 25/10/2026), os provedores do DeepSeek V4.1 Flash e do GLM 5.3 Flash gratuitos não guardam nem treinam com o que é enviado; outros modelos gratuitos têm exceções. Políticas mudam: confira antes de enviar dados sensíveis.
- **PDF:** ScienceDirect, IOP e Wiley bloqueiam download por script. A MDPI bloqueia o domínio `www`, mas o CDN `mdpi-res.com` funciona. O downloader novo tenta mais caminhos e o fallback manual resolve o resto; no exemplo, o download automático trouxe 41 dos 47 artigos abertos.
- **Números:** o resumo cita a página de cada número, mas confira no artigo antes de citar.
- **Direitos autorais:** os PDFs, o texto integral extraído e os registros dos agentes ficam fora do repositório (`.gitignore`). Só os resumos são publicados.

## Estrutura

```
AGENTS.md      contrato de conversa e de arquivos para a IA que usa o repositório
ferramentas/   scripts (Python; pypdf para extrair os PDFs)
modelos/       pedidos para a busca e para o resumo, o PLANO.md e o modelo do RELATORIO.html
tests/         testes (pytest, sem rede)
exemplo/       o levantamento completo usado como exemplo
projetos/      os levantamentos feitos com o repositório (fora do Git)
docs/          o site (GitHub Pages)
```

**Testes:** `python -m pytest -q` (não usa a rede).

Código sob licença MIT. Ferramenta original de Victor Amaral (LAPIG/UFG), feita com Claude Code e DeepSeek. Adaptações para o doutorado: Lana Teixeira.
