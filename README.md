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
| 5. Tabela final | `painel.py` | `TABELA.md` ordenada por citações, com link para o resumo |

## Exemplo real

Tema: *sensoriamento remoto multissensorial aplicado à estimativa de biomassa e carbono da silvicultura em Goiás*. Pasta [`exemplo/`](exemplo/).

- 4 frentes (sensores ópticos, radar e LiDAR, fusão com aprendizado de máquina, dados de Goiás), 2 agentes por vez, cerca de 10 minutos.
- 49 artigos únicos com DOI, mais 4 bases oficiais sem DOI (IBGE, Ibá, MapBiomas, Embrapa). Os 56 DOIs citados nas frentes existem no Crossref.
- 47 dos 49 artigos estão em acesso aberto. 19 foram lidos por inteiro e resumidos, em cerca de 12 minutos: [`exemplo/resumos/`](exemplo/resumos/).
- Na frente de radar e LiDAR o agente ficou sem a busca na web e buscou direto nas APIs do Crossref e do OpenAlex; o resultado tem a mesma qualidade.
- Comece por [`exemplo/TABELA.md`](exemplo/TABELA.md).

## Como usar

Precisa de Python 3.10+, Node.js e do opencode:

```bash
npm install -g @opencode/cli
pip install pypdf
```

**1. Uma pasta por frente**, cada uma com um `PEDIDO.md` feito a partir de [`modelos/PEDIDO-busca.md`](modelos/PEDIDO-busca.md) (troque `{TEMA}`, `{FRENTE}` e `{DATA}`):

```
meu-tema/frentes/1-algum-recorte/PEDIDO.md
meu-tema/frentes/2-outro-recorte/PEDIDO.md
```

**2. Rodar os agentes** (2 por vez; o script liga a busca na web do opencode):

```bash
python ferramentas/orquestrar.py meu-tema/frentes --paralelo 2
```

**3. Juntar, conferir os DOIs e buscar a cienciometria:**

```bash
python ferramentas/juntar.py meu-tema/frentes meu-tema "Título do tema"
python ferramentas/conferir_doi.py meu-tema/frentes
python ferramentas/cienciometria.py meu-tema/referencias.bib meu-tema/cienciometria.csv
```

**4. Ler os artigos abertos e montar a tabela:**

```bash
python ferramentas/preparar_resumos.py meu-tema/cienciometria.csv pdfs meu-tema/resumos modelos/PEDIDO-resumo.md "Título do tema"
python ferramentas/orquestrar.py meu-tema/resumos --paralelo 2
python ferramentas/painel.py meu-tema
```

Quem usa um assistente com acesso ao terminal (Claude Code, Codex, opencode) pode pedir a ele para fazer tudo isso a partir do tema.

## Limites

- **Gratuito tem limite por conexão de internet.** 2 agentes por vez funcionam; 5 estouram em minutos.
- **Privacidade:** segundo a [documentação do opencode](https://opencode.ai/docs/zen/) (consultada em 25/10/2026), os provedores do DeepSeek V4.1 Flash e do GLM 5.3 Flash gratuitos não guardam nem treinam com o que é enviado; outros modelos gratuitos têm exceções. Políticas mudam: confira antes de enviar dados sensíveis.
- **PDF:** MDPI, ScienceDirect, IOP e Wiley bloqueiam download por script. O `preparar_resumos.py` tenta também as cópias em repositórios (universidades, PMC, HAL). No exemplo, 19 dos 38 artigos com link de PDF aberto foram lidos.
- **Números:** o resumo cita a página de cada número, mas confira no artigo antes de citar.
- **Direitos autorais:** os PDFs, o texto integral extraído e os registros dos agentes ficam fora do repositório (`.gitignore`). Só os resumos são publicados.

## Estrutura

```
ferramentas/   scripts (Python, sem dependências além de pypdf)
modelos/       pedidos para a busca e para o resumo
exemplo/       o levantamento completo usado como exemplo
docs/          o site (GitHub Pages)
```

Código sob licença MIT. Feito por Victor Amaral (LAPIG/UFG), com Claude Code e DeepSeek.
