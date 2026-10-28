Hoje é {DATA}. Responda em português. Contexto: projeto de pesquisa sobre "{TEMA}". O objetivo é buscar e organizar referências recentes.

## Formato obrigatório

Grave `RELATORIO.md` nesta pasta, exatamente nesta ordem (não copie as cercas de código abaixo; escreva só o conteúdo):

```markdown
# Referências — {FRENTE}

**Tema:** {TEMA}
**Frente:** {FRENTE}
**Data:** {DATA}

## Notas de verificação

- (o que você conferiu, o que não abriu e por quê; use † e ‡ se precisar)

## Tabela de referências

| Autores (ano) | Título | Revista | DOI/link | Dados | Método | Área | Resultado principal |
|---|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... | ... | ... |

## O que essas referências sugerem para o projeto

- (5 linhas curtas, ligando as referências ao projeto)
```

## Regras

- As linhas com `...` no exemplo são só formato: substitua por 10 a 15 referências reais e não copie os `...`.
- Use `websearch` (e `webfetch` só para abrir a página do artigo e conferir). No máximo ~25 passos.
- Só artigos revisados por pares, relatórios oficiais ou bases de dados oficiais, preferindo os últimos 6 anos.
- A tabela é a primeira e única tabela do arquivo. Não acrescente, retire nem reordene colunas.
- De 10 a 15 linhas, uma por referência. Não repita a mesma referência em duas linhas.
- Para cada referência, confira que o DOI/link abre. Se não conseguiu abrir, marque "(não verificado)".
- Se não houver DOI, use o link oficial e escreva "(sem DOI)" na coluna DOI/link.
- Marque com **†** quando o DOI abriu mas o PDF foi bloqueado, e com **‡** quando a página estava instável mas o PDF abriu. Explique os marcadores nas notas.
- Nunca invente DOI, autor, título, revista ou número. Se não tiver certeza, deixe explícito.
- Prefira dados e resultados concretos (local, período, sensores, amostra, R², RMSE, erro) em vez de adjetivos.
- Não escreva o relatório em outro arquivo e não use a pasta para baixar PDFs; só grave o `RELATORIO.md`.

Frente: {FRENTE}
