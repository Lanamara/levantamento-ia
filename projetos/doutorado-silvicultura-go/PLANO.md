# Plano do levantamento

**Tema:** Sensoriamento remoto multissensorial aplicado à estimativa de biomassa e estoque de carbono da silvicultura no estado de Goiás
**Pergunta do projeto:** Como a integração de dados ópticos, hiperespectrais e LiDAR com aprendizado de máquina pode estimar produção, idade, biomassa e estoques de carbono dos diferentes perfis da silvicultura goiana?
**Recorte:** Brasil e Cerrado (Goiás em destaque), florestas plantadas (eucalipto, pinus, seringueira), sensoriamento remoto orbital; artigos revisados por pares, relatórios e bases oficiais, de preferência 2020–2026
**Data:** 29/10/2026
**Pasta:** `projetos/doutorado-silvicultura-go/`
**Base:** pré-projeto de doutorado (PPGCIAMB/UFG), versão de 29/06/2026 — hipóteses H1 a H4 e etapas 1 a 5 da metodologia

## Frentes

| # | Pasta | Recorte | O que entra | O que fica fora |
|---|---|---|---|---|
| 1 | `frentes/1-hiperespectral` | PRISMA e EnMAP | espécies, biomassa, red-edge/NIR/SWIR, fusão com LiDAR | hiperespectral aerotransportado sem relação com satélite |
| 2 | `frentes/2-lidar-referencia` | GEDI e ICESat-2 | GEDI L2A/L4A e ATL08 como referência para extrapolar biomassa | LiDAR terrestre isolado |
| 3 | `frentes/3-fusao-ml` | fusão + RF, XGBoost, CNN | biomassa e carbono de plantios, comparação com regressão, R²/RMSE/MAE | aprendizado de máquina sem estimativa de biomassa |
| 4 | `frentes/4-idade-produtividade` | séries Landsat/Sentinel-2 | idade, plantio/corte, rotação e produtividade | mapeamento de uso da terra sem idade |
| 5 | `frentes/5-fragilidade-ahp` | AHP/WLC e fragilidade | fragilidade (Ross), vulnerabilidade, aptidão territorial | multicritério sem relação com uso da terra |
| 6 | `frentes/6-goias-seringueira` | Goiás, Cerrado, seringueira | PEVS, Ibá, MapBiomas, IMB, carvão, borracha, alometria, ABC+ | outros estados sem comparação com Goiás |

## Decisões combinadas com a pessoa

- 6 frentes (29/10/2026). Com o limite gratuito (~200 chamadas/dia), as buscas e os resumos devem levar 2 dias.
- Pasta do projeto versionada no Git (exceção no `.gitignore`), para a atualização mensal automática funcionar. PDFs, `TEXTO.txt` e logs continuam fora do Git.
- Revista: nome, ISSN e editora pelo OpenAlex; indicadores DOAJ, CWTS Core, Qualis (planilha da Sucupira em `qualis.csv`, se for fornecida) e retratação. Nunca rotular revista como "predatória".
- Referências do pré-projeto em `minhas_referencias.txt`, conferidas com `conferir_lista.py`; o relatório marca o que já é citado.
- Atualização mensal (`ferramentas/atualizar.py` + GitHub Actions) com as consultas de `consultas.json`; resultado em `NOVIDADES.md`.
- Idioma dos resumos: português. Limite: 2 agentes por vez. PDFs: só acesso aberto.

## Entrega

- `RELATORIO.html` para ler e navegar (com filtros por frente, indicador da revista e "já cito", e a seção Novidades).
- `TABELA.md` e `REFERENCIAS.md` para texto e GitHub.
- `referencias.bib` para Zotero/Mendeley.
- `cienciometria.csv` e `tabela.json` para análise.
- `MINHAS_REFERENCIAS.md` com a conferência das referências do pré-projeto.
- `NOVIDADES.md` com os trabalhos novos de cada mês.
