# RELATÓRIO — James R. Kellner (2022)

## 1. Referência

Kellner, J. R.; Armston, J.; Duncanson, L. (2022). Algorithm theoretical basis document for GEDI footprint aboveground biomass density. *Earth and Space Science* — preprint submetido à EarthArXiv, em revisão pela Earth and Space Science [p. 1]. DOI: 10.1029/2022EA002516.

## 2. Pergunta do estudo

Qual é a base teórica, científica e matemática que permite converter métricas RH do GEDI02_A em densidade de biomassa acima do solo por footprint (AGBD), com modelos transferíveis para todo o domínio de observação da ISS?

## 3. Área e dados

- **Área:** domínio global de observação da ISS, 51,6° N–S [p. 29], estratificado em 7 regiões mundiais e 5 PFT [pp. 4–5].
- **Período:** período de coleta dos dados de campo não informado; a avaliação de desempenho usa as *mission weeks* 16–153 da release 2, geração 2 [p. 15].
- **Sensores/fontes:** lidar de forma de onda multifeixe GEDI na ISS; waveforms GEDI simulados a partir de ALS de retorno discreto; métricas RH do GEDI02_A; PFT do MODIS MCD12Q1 V006 corrigido e preenchido; DEM TanDEM-X 90 m; *Landsat water persistence*; VIIRS VNP22Q2 [pp. 3, 9].
- **Amostras:** 31.414 waveforms simulados na base bruta; 12.140 após excluir projetos incompletos; 8.587 após os filtros de qualidade, provenientes de 21 países [p. 5]; 32 estratos de predição [p. 2].

## 4. Método

- Estratificação por PFT (DBT, DNT, EBT, ENT, GSW) × região mundial, com 13 modelos lineares para 32 combinações [p. 2].
- Geração de candidatos: 4 cenários de transformação (raiz quadrada ou log natural na resposta, com ou sem a mesma transformação nos preditores) e todas as matrizes de 1 a 4 variáveis, com métricas RH em incrementos de 10%, RH98 e produtos de pares de RH; matrizes com |r| > 0,9 ou VIF > 10 foram eliminadas [pp. 6–7].
- Validação cruzada geográfica: retém-se uma célula de 5° para teste e treina-se com as demais; o ranqueamento usa erro residual médio, RMSE% arredondado para baixo em 5%, percentil máximo de RH, número de coeficientes e número de métricas RH [pp. 4, 8].
- Ajuste de modelo linear ponderado (pesos inversamente proporcionais ao número de footprints por célula de 5°), correção de viés de retrotransformação de Snowdon e intervalos de predição calculados a partir do erro padrão e da distribuição *t* [pp. 8, 13–14].

## 5. Resultados principais

- Base final: 8.587 waveforms simulados de 21 países; 3.553 removidos dos 12.140 [p. 5].
- Exclusões por filtro: AGBD < 1 Mg/ha com RH98 > 5 m, 113 footprints (0,93%); AGBD > 150 Mg/ha com RH98 < 5 m, 7 (0,06%); CCF = 0 com RH98 > 5 m, 158 (1,30%); diferença entre altura de campo e RH98 > 10 m, 997 (8,21%); extrapolação da alometria, 640 (5,27%); footprint com mais de 10% da área fora da parcela, 129 (1,06%) [pp. 5–6].
- 24 dos 32 estratos têm menos de 50 footprints; nesses casos o modelo veio do melhor estrato de PFT em 17 casos e de um modelo PFT × região alternativo em 7 casos [p. 7].
- Amostras por estrato: EBT × América do Sul 3.441; ENT global 1.986; DBT × Europa 333; região Europa 750; DBT global 1.698 [p. 7]. Totais por PFT: DBT 1.698; EBT 4.814; ENT 1.986; GSW 89 [p. 31].
- Todos os modelos selecionados usam raiz quadrada na resposta e a correção de viés da equação 8 [p. 14].
- Retenção após `l4_quality_flag`: DBT 12,0% (*coverage*) e 33,3% (*power*) [p. 15]; EBT 51,5% e 73,7% [p. 15]; DNT 8,9% e 15,4% [p. 43]; ENT 40,5% e 69,9% [p. 44]; GSW 4,7% e 65,7% [p. 45].
- Causas de `l4_quality_flag` = 0 em DBT (médias): *sensitivity* 72,6% *coverage* e 32,1% *power*; `l2_quality_flag` 37,4% e 21,1%; `leaf_off_flag` 55,1% e 55,0% [p. 40]. Em EBT: *sensitivity* 54,2% e 20,6%; `l2_quality_flag` 24,1% e 15,4% [p. 41].
- O limiar de *sensitivity* 0,98 do GEDI04_B em EBT da África, América do Sul e Sul da Ásia retém 10,4–22,0% (*coverage*) e 32,2–44,1% (*power*) [p. 15].
- Observação de consistência interna: o texto cita 13 modelos [p. 2], a Table 2 lista 14 nomes de modelos [p. 32] e a Table 3 menciona 34 estratos de predição [p. 33].

## 6. Limitações que os próprios autores reconhecem

- Regiões sub-representadas: florestas da Ásia continental, florestas decíduas e savanas do trópico seco e EBT ao norte da Austrália [p. 2; p. 4].
- Em 24 dos 32 estratos não foi possível desenvolver ou testar um modelo candidato, incluindo todo o Norte da Ásia, as savanas secas da América do Sul e do Sul da Ásia e todos os estratos GSW [p. 16].
- O treino de EBT × Austrália/Oceania vem de dois projetos em Queensland, embora o estrato inclua a Nova Guiné e outras ilhas [p. 16].
- Modelos treinados com waveforms sem ruído; erros na detecção do solo se propagam para as métricas RH e para a AGBD [pp. 12, 16].
- Modelos alométricos subestimam sistematicamente a massa de árvores grandes, e as árvores colhidas que os originaram não foram amostradas aleatoriamente [p. 11].
- Um único coeficiente de correção de viés pode não valer para valores altos de AGBD prevista [p. 14].
- O pressuposto de footprint circular de 12,5 m (copas fora do raio, material de copa fora do footprint) pode gerar *dilution bias* [pp. 11–12].
- As perdas de dados impostas pelos filtros de qualidade são esperadas e substanciais [p. 15].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o desenho de calibração e validação (parcelas de campo + waveforms simulados de ALS, validação cruzada geográfica, seleção por parcimônia) é replicável para plantios e Cerrado em Goiás, desde que com modelos ajustados localmente.
- **Serve:** a estrutura de incerteza (erro padrão, matriz de covariância dos parâmetros, intervalos de predição) e a lógica dos estimadores híbridos para agregar footprints a áreas.
- **Serve:** os critérios de qualidade (`sensitivity` > 0,95, `l2_quality_flag`, `leaf_off_flag`, `urban_proportion`, `landsat_water_persistence`) como checklist de filtragem de dados GEDI.
- **Não serve:** o artigo não trata de silvicultura nem de Goiás, não define PFT para plantios de *Eucalyptus*/*Pinus*, não faz fusão com óptico ou SAR, não informa fração de carbono e afirma que os modelos não devem ser aplicados a outros sensores [p. 15].

## 8. Frases citáveis (literais)

- "Although this is the most geographically comprehensive data available for the development of AGBD models using lidar remote sensing, important regions are underrepresented, including the forests of continental Asia, deciduous broadleaf forests and savannas of the dry tropics, and evergreen broadleaf forests north of Australia." [p. 2]
- "Although the approach developed here could be replicated for other sensors, the GEDI04_A models should not be directly applied to alternative sensor data." [p. 15]
