# Levantamento bibliográfico com agentes de IA gratuitos

Um tema de pesquisa vira uma lista de referências conferidas, com dados de citação e um resumo de cada artigo aberto, usando o [opencode](https://opencode.ai) com o modelo **DeepSeek V4.1 Flash gratuito**. Não precisa de conta nem de assinatura.

**Site com a explicação e o exemplo:** https://victorgit10.github.io/levantamento-ia/

## O que sai no fim

| Etapa | Ferramenta | Saída |
|---|---|---|
| 1. Busca por frentes | `orquestrar.py` + agentes com busca na web | uma tabela por frente |
| 2. Junção e DOI | `juntar.py` + `conferir_doi.py` (Crossref) | `REFERENCIAS.md`, `referencias.bib` |
| 3. Cienciometria | `cienciometria.py` (OpenAlex) | citações, FWCI, percentil, acesso aberto |
| 4. Leitura integral | `preparar_resumos.py` + `orquestrar.py` | um resumo por artigo aberto, com página em todo número |
| 5. Tabela final | `painel.py` | `TABELA.md` ordenada por citações, com link para o resumo e as bases sem DOI |

## Exemplo real

Tema: *sensoriamento remoto multissensorial aplicado à estimativa de biomassa e carbono da silvicultura em Goiás*. Pasta [`exemplo/`](exemplo/).

- 4 frentes (sensores ópticos, radar e LiDAR, fusão com aprendizado de máquina, dados de Goiás), 2 agentes por vez, cerca de 10 minutos.
- 49 artigos diferentes com DOI, mais 4 bases oficiais sem DOI (IBGE, Ibá, MapBiomas, Embrapa). As frentes somaram 56 indicações porque 5 artigos apareceram em duas ou três delas. Os 49 DOIs existem no Crossref; em 48 o título bateu sozinho, e 1 (título bilíngue) foi conferido à mão.
- Dos 47 artigos abertos, 38 tinham link de PDF e o download automático funcionou em 19 (12 dos que falharam são da MDPI, que bloqueia download por script).
- Esses 19 foram lidos por inteiro e resumidos, em cerca de 12 minutos: [`exemplo/resumos/`](exemplo/resumos/).
- Na frente de radar e LiDAR o agente ficou sem a busca na web e buscou direto nas APIs do Crossref e do OpenAlex; o resultado tem a mesma qualidade.
- Comece por [`exemplo/TABELA.md`](exemplo/TABELA.md).

## Como usar

Precisa de Python 3.10+, Node.js e do opencode:

```bash
npm install -g @opencode/cli
pip install -r requirements.txt
```

**Busca na web:** se o opencode estiver configurado para negar `websearch` ou `webfetch`, copie [`modelos/opencode.json`](modelos/opencode.json) para a pasta que contém as frentes (`meu-tema/frentes/opencode.json`) antes de rodar. Ele libera as duas ferramentas. O orquestrador conta as chamadas a `websearch` no log e imprime `SEM-BUSCA <frente>` quando não houver nenhuma.

**1. Uma pasta por frente**, cada uma com um `PEDIDO.md` feito a partir de [`modelos/PEDIDO-busca.md`](modelos/PEDIDO-busca.md) (troque `{TEMA}`, `{FRENTE}` e `{DATA}`):

```
meu-tema/frentes/1-algum-recorte/PEDIDO.md
meu-tema/frentes/2-outro-recorte/PEDIDO.md
```

**2. Rodar os agentes** (2 por vez; o script liga a busca na web do opencode):

```bash
python ferramentas/orquestrar.py meu-tema/frentes --paralelo 2
```

Cada frente tem até 30 minutos (`--timeout 1800`); se o log indicar limite, ela volta uma vez com o modelo reserva, guardando o relatório parcial e o log anterior. O script sai com código 1 se alguma frente não terminar com um `RELATORIO.md` de pelo menos 200 caracteres.

**3. Juntar, conferir os DOIs e buscar a cienciometria:**

```bash
python ferramentas/juntar.py meu-tema/frentes meu-tema "Título do tema"
python ferramentas/conferir_doi.py meu-tema/frentes
python ferramentas/cienciometria.py meu-tema/referencias.bib meu-tema/cienciometria.csv
```

O `juntar.py` guarda as notas de método e verificação que cada frente escreveu antes da tabela, inclusive a legenda dos marcadores † e ‡. Se o OpenAlex falhar em algum DOI, ele fica em `meu-tema/cienciometria-falhas.csv` e a mensagem final diz quantos falharam.

**4. Ler os artigos abertos e montar a tabela:**

```bash
python ferramentas/preparar_resumos.py meu-tema/cienciometria.csv pdfs meu-tema/resumos modelos/PEDIDO-resumo.md "Título do tema"
python ferramentas/orquestrar.py meu-tema/resumos --paralelo 2
python ferramentas/painel.py meu-tema
```

No passo 4 não há aviso de `SEM-BUSCA`: ele só aparece quando o `PEDIDO.md` manda usar `websearch`, e o pedido de resumo proíbe a web.

O `painel.py` usa os autores do `.bib` ("Silva (ano)", "Silva & Souza (ano)", "Silva et al. (ano)") e põe as bases e relatórios sem DOI numa seção no fim da `TABELA.md`.

Quem usa um assistente com acesso ao terminal (Claude Code, Codex, opencode) pode pedir a ele para fazer tudo isso a partir do tema.

**Testes:** `python -m pytest -q` (não usa a rede).

## Limites

- **Gratuito tem limite por conexão de internet**, somado entre os modelos gratuitos. 2 agentes por vez funcionam; 5 estouram em minutos. Por dia, o limite acabou depois de cerca de 200 chamadas ao modelo: deu para as 4 frentes e os 19 resumos do exemplo, mas não para mais. Ao estourar, o orquestrador tenta o modelo reserva e, se também estiver no limite, marca a frente como falha (código de saída 1); rode de novo no dia seguinte e ele continua de onde parou.
- **Privacidade:** segundo a [documentação do opencode](https://opencode.ai/docs/zen/) (consultada em 25/10/2026), os provedores do DeepSeek V4.1 Flash e do GLM 5.3 Flash gratuitos não guardam nem treinam com o que é enviado; outros modelos gratuitos têm exceções. Políticas mudam: confira antes de enviar dados sensíveis.
- **PDF:** MDPI, ScienceDirect, IOP e Wiley bloqueiam download por script. O `preparar_resumos.py` tenta também as cópias em repositórios (universidades, PMC, HAL). No exemplo, 19 dos 38 artigos com link de PDF aberto foram lidos.
- **Números:** o resumo cita a página de cada número, mas confira no artigo antes de citar.
- **Direitos autorais:** os PDFs, o texto integral extraído e os registros dos agentes ficam fora do repositório (`.gitignore`). Só os resumos são publicados.

## Estrutura

```
ferramentas/   scripts (Python; pypdf para extrair os PDFs)
modelos/       pedidos para a busca e para o resumo, e a configuração que libera a busca na web
tests/         testes (pytest, sem rede)
exemplo/       o levantamento completo usado como exemplo
docs/          o site (GitHub Pages)
```

Código sob licença MIT. Feito por Victor Amaral (LAPIG/UFG), com Claude Code e DeepSeek.
