# RELATÓRIO — Yangyang Zhou (2023)

## 1. Referência

Zhou, Y.; Feng, Z. **Estimation of Forest Stock Volume Using Sentinel-2 MSI, Landsat 8 OLI Imagery and Forest Inventory Data**. *Forests*, 2023, 14(7), 1345. DOI: 10.3390/f14071345. Publicado em 29/06/2023. Texto integral recebido (21 páginas), compatível com o DOI.

## 2. Pergunta do estudo

Comparar Landsat 8 OLI, Sentinel-2 MSI e a combinação dos dois na estimativa de forest stock volume (FSV) por modelos MLR, BP e RF, testando dois métodos de seleção de variáveis (LSR e RFE).

## 3. Área e dados

- Local: distrito de Huairou, Pequim, China (116°17′–116°53′ E, 40°41′–41°4′ N), 2.122,6 km², elevação de 34 a 1.661 m; floresta temperada semi-úmida, com *Pinus tabulaeformis*, *Populus tomentosa*, *Quercus mongolica*, *Platycladus orientalis* e *Betula platyphylla* [p. 4].
- Período: inventário de 2016 e imagens de 2016 — Landsat 8 de 11/10/2016 e Sentinel-2 de setembro/2016 [p. 5–6].
- Inventário: 9º Beijing Forest Inventory Data (FID), parcelas fixas de 0,067 ha (25,8 × 25,8 m), em malha de 2 × 2 km; 273 parcelas após remoção de outliers pela regra três-sigma [p. 5].
- Sensores/fontes: Landsat 8 OLI (bandas 2–7, 30 m), Sentinel-2 MSI (L1C convertido a L2A no Sen2Cor 2.5.5; 11 bandas B2–B12 reamostradas para 25,8 m no SNAP 8.0), DEM de 30 m [p. 5–6], máscara de uso do solo de 10 m do GEE [p. 15].
- Amostras: 203 parcelas de treino e 70 de teste [p. 10]; a seção 2.2 afirma divisão 7:3 "com 70 parcelas cada" [p. 5] e a seção 2.7.4 cita "207 parcelas" no treino [p. 9] — números internamente inconsistentes no artigo.

## 4. Método

- Extração de 159 variáveis: 69 do Landsat 8 (reflectância, índices de vegetação, textura GLCM em janela 3 × 3), 84 do Sentinel-2, 3 topográficas (DEM, declividade, orientação) e 3 do inventário (idade média, DBH médio, densidade de copa); normalização 0–1 [p. 7–8].
- Filtro por coeficiente de Pearson e duas seleções de variáveis — linear stepwise regression (LSR) e recursive feature elimination (RFE) com Random Forest — gerando seis conjuntos de variáveis [p. 8–9, 11].
- Três modelos por conjunto: MLR (SPSS 26, stepwise, F ≤ 0,05 entrada e ≥ 0,10 saída), BP neural network (MATLAB R2019a) e RF, com ntree ajustado pelo erro OOB (310 para Landsat 8, 280 para Sentinel-2, 265 para o conjunto combinado) [p. 9–10, 12].
- Validação em 70 parcelas independentes com R², RMSE, rRMSE e MAE [p. 10]; mapa final com o melhor modelo (RFE-RF combinado) sobre a máscara florestal de 2016 [p. 15].

## 5. Resultados principais

- Melhor modelo: Landsat 8 + Sentinel-2, RFE-RF — R² = 0,831; RMSE = 12,604 m³ ha⁻¹; rRMSE = 36,411%; MAE = 9,366 m³ ha⁻¹ [p. 12–13].
- Melhores modelos de fonte única: Sentinel-2 RFE-RF, R² = 0,799, RMSE = 13,743 m³ ha⁻¹, MAE = 8,899 m³ ha⁻¹ [p. 12]; Landsat 8 RFE-RF, R² = 0,782, RMSE = 14,317 m³ ha⁻¹ [p. 12].
- Ordem de desempenho em todos os conjuntos: RF > BP > MLR; o pior caso foi Landsat 8 LSR-MLR, R² = 0,595, RMSE = 19,491 m³ ha⁻¹ [p. 12–13].
- RFE superou LSR em todas as fontes; com LSR, o RF combinado deu R² = 0,830 e RMSE = 12,616 m³ ha⁻¹ [p. 12–13].
- A textura reduziu o rRMSE em 3,7% no RFE-RF combinado, comparado ao mesmo modelo sem textura [p. 17].
- Aumento de acurácia do conjunto combinado sobre a melhor fonte única: queda de RMSE entre 2 e 4 m³ ha⁻¹ [p. 18].
- Variáveis mais contributivas: textura e derivadas da banda red-edge do Sentinel-2 (Sen B5, Sen RVI, SenmNDVIre, Sen B5Mean) [p. 1, 17]; a B5 (red-edge 1) foi a variável de maior correlação com FSV [p. 16].
- Correlação de Pearson: 23 variáveis do Landsat 8 significativas a 0,05 e 13 a 0,01; 24 variáveis do Sentinel-2 a 0,01; DEM com r = 0,340 [p. 11].
- Estatística das parcelas: treino (203) média 32,176 m³ ha⁻¹, DP 35,229; teste (70) média 28,897 m³ ha⁻¹; total 31,279 m³ ha⁻¹ [p. 11].
- Mapa: FSV de 150–200 m³ ha⁻¹ no norte, centro e noroeste; 0–50 m³ ha⁻¹ no sul e sudeste [p. 15].

## 6. Limitações que os próprios autores reconhecem

- O estudo comparou os métodos de seleção de variáveis apenas em uma área, com o mesmo conjunto de dados; recomendam aplicá-los em outras áreas [p. 18].
- A combinação dos sensores foi feita só no nível de variáveis, sem fusão de bandas entre as duas imagens; sugerem testar fusão de imagens em trabalhos futuros [p. 18].
- Dados do FID são confidenciais e não podem ser disponibilizados, o que restringe a replicação [p. 18].
- Custo elevado dos levantamentos de campo e desvios de posição das parcelas, que geram viés no pareamento parcela–pixel, são apontados como obstáculos gerais do método [p. 3].

## 7. O que serve ao projeto e o que não serve

- Serve: o desenho comparativo (fonte A, fonte B e fontes combinadas; LSR vs RFE; MLR/BP/RF; validação em conjunto separado) é diretamente replicável para silvicultura em Goiás com Sentinel-2 e Landsat 8/9.
- Serve: a evidência quantitativa de que bandas red-edge do Sentinel-2 (B5) e índices derivados, mais textura GLCM, carregam o maior ganho de acurácia — orienta a escolha de variáveis para biomassa em plantios.
- Serve: rRMSE de 36,4% como referência de erro relativo para volume em escala de parcela, e o RFE-RF como baseline de machine learning.
- Não serve: o artigo estima volume (FSV, m³ ha⁻¹), não biomassa nem carbono; não há fator de expansão, densidade da madeira ou teor de carbono, e não há sensores ativos (SAR/LiDAR) — para "multissensorial" e "carbono" o projeto precisa de outra base. Também não transfere coeficientes: são 273 parcelas de floresta temperada de Pequim, imagem única de 2016, sem eucalipto ou plantio comercial, e com inconsistência nos números de amostra (203/207/70).

## 8. Frases citáveis (literais)

- "The correlation between the red-edge band of Sentinel-2 imagery and FSV is more significant than that of other characteristic variables used." [p. 1]
- "Compared to the optimal model constructed using a single data source, the root mean square error of the best model constructed using combined data has decreased by 2–4 m3 ha−1." [p. 18]
