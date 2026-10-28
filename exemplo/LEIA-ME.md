# Levantamento: Sensoriamento remoto multissensorial aplicado à estimativa de biomassa e estoque de carbono da silvicultura no estado de Goiás

Gerado em 28/10/2026.

## Abra primeiro

- [`RELATORIO.html`](RELATORIO.html) — tabela navegável, com busca, filtro e os resumos.
- [`TABELA.md`](TABELA.md) — a mesma lista em texto, ordenada por citações.
- [`REFERENCIAS.md`](REFERENCIAS.md) — as referências separadas por frente e o que cada busca concluiu.
- [`referencias.bib`](referencias.bib) — para importar no Zotero ou no Mendeley.

## O que já está pronto

- 49 referências com DOI.
- 47 em acesso aberto.
- 42 resumos de leitura integral.
- 4 bases e relatórios oficiais sem DOI.

## PDFs que faltam

6 PDFs não foram baixados. A lista com o nome de arquivo de cada um está em [`pdfs/FALTANDO.md`](pdfs/FALTANDO.md).

Para completar: baixe o artigo pelo navegador (só acesso aberto), salve em `pdfs/` com o nome indicado e rode de novo o comando abaixo. O script aproveita o que já está na pasta.

- `silva2020.pdf` — Fusing simulated GEDI, ICESat-2 and NISAR data for regional aboveground biomass mapping
- `nesha2020.pdf` — Modeling and mapping aboveground biomass of the restored mangroves using ALOS-2 PALSAR-2 in East Kalimantan, Indonesia
- `yang2025.pdf` — Mapping above-ground biomass and canopy mean height in high mountainous forest areas with Sentinel-2 multi-spectral image based on machine learning algorithms
- `enriquez2024.pdf` — Estimation of height and aerial biomass in Eucalyptus globulus plantations using UAV-LiDAR
- `saim2025.pdf` — Machine Learning and Multisensor Data Fusion for Forest above Ground Biomass Estimation in Arkansas
- `goral2025.pdf` — Monitoring the early growth of forest plantations with Sentinel-2 satellite time-series

## Como continuar

Rode a partir da pasta do repositório:

```bash
python ferramentas/preparar_resumos.py "exemplo/cienciometria.csv" "exemplo/pdfs" "exemplo/resumos" modelos/PEDIDO-resumo.md "Sensoriamento remoto multissensorial aplicado à estimativa de biomassa e estoque de carbono da silvicultura no estado de Goiás" --abrir
python ferramentas/orquestrar.py "exemplo/resumos" --paralelo 2
python ferramentas/painel.py "exemplo"
python ferramentas/publicar.py "exemplo"
```

## Formatos

| Camada | Arquivos | Para quê |
|---|---|---|
| Para ler | `RELATORIO.html`, `TABELA.md`, `REFERENCIAS.md` | consulta e leitura |
| Para citar | `referencias.bib` | Zotero, Mendeley, LaTeX |
| Para analisar | `cienciometria.csv`, `tabela.json`, `verificacao.csv`, `download.csv` | planilha e scripts |
| Interno | `pdfs/`, `resumos/*/TEXTO.txt`, `log.jsonl` | não publicar (direitos autorais) |

Os números dos resumos vêm com a página; confira no artigo antes de citar.
