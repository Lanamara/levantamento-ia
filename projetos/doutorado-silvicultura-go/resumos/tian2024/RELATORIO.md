# RELATÓRIO — Xin Li Tian (2024)

## 1. Referência

- Tian, X.; Li, J.; Zhang, F.; Zhang, H.; Jiang, M. Forest Aboveground Biomass Estimation Using Multisource Remote Sensing Data and Deep Learning Algorithms: A Case Study over Hangzhou Area in China. *Remote Sensing*, 2024, 16(6), 1074. DOI: 10.3390/rs16061074 [p. 1].
- O `TEXTO.txt` está completo (p. 1–20, incluindo referências) e corresponde ao DOI informado. O primeiro autor é **Xin Tian** — a grafia "Xin Li Tian" do pedido não aparece no artigo [p. 1].

## 2. Pergunta do estudo

A fusão de imagens ópticas (GF-6, Sentinel-2, Landsat-8) e SAR (GF-3, Sentinel-1, ALOS-2) com algoritmos de aprendizado profundo (RF, CNN, CNN-LSTM) eleva a acurácia da estimativa de biomassa acima do solo (AGB) florestal em relação a sensores e métodos isolados? [p. 1, p. 3]

## 3. Área e dados

- Local: distrito de Lin'an, Hangzhou, noroeste de Zhejiang, China (118°51′–119°52′ E; 29°56′–30°23′ N), altitude de 60–120 m, clima monçônico subtropical, florestas mistas de coníferas e folhosas [p. 3].
- Período: dados de campo de 2018 (9º Inventário Florestal Nacional) e imagens de setembro a novembro de 2018 [p. 5].
- Amostras: 160 parcelas com AGB calculada por equações alométricas por espécie (fir, horsetail pine, hard broad, soft broad); 130 para modelagem e 30 para teste [p. 5].
- Óptico: GF-6 WFV, 16 m, 05/09/2018; Sentinel-2 Level-1C, 10/20/60 m, 29/10 e 10/11/2018; Landsat-8 L1T, 30 m (15 m pancromática), 11/09 e 15/11/2018 [p. 5].
- SAR: GF-3 C-band HH+HV, 1 m, 17/11/2018; Sentinel-1 C-band VV+VH, modo IW 5×20 m, 01/10 e 13/10/2018; ALOS-2 PALSAR-2 L-band HH+HV, modo FBD, 25/10 e 08/11/2018 [p. 5–6].

## 4. Método

- Extração de variáveis: bandas, NDVI, DVI, GNDV, RVI, oito texturas (Mean, Variance, Entropy, Contrast, Homogeneity, Dissimilarity, Correlation, Second Moment) e componentes principais no óptico; retroespalhamento, texturas e decomposição dual-pol Cloude (H, A, α) no SAR — 21 variáveis por imagem SAR [p. 6, p. 9] e 19 por imagem óptica [p. 10].
- Seleção de variáveis pela correlação de Pearson com a AGB, retendo as mais correlacionadas de cada fonte (Tabelas 8, 10 e 12) [p. 11–12, p. 15].
- Modelos: RF com 500 árvores e m = 5 [p. 7]; CNN e CNN-LSTM (CNN como encoder e LSTM como decoder) [p. 8–9]; 27 combinações de dados × modelos [p. 17].
- Avaliação nas 30 parcelas de teste com pseudo-R², RMSE, rRMSE, Bias e rBias [p. 9].

## 5. Resultados principais

- Melhor resultado geral: CNN-LSTM com todas as fontes (SAR + óptico), R² = 0.7405 e RMSE = 26.4314 Mg/ha [p. 15].
- Somente óptico (três sensores) com CNN-LSTM: R² = 0.7289 e RMSE = 26.9166 Mg/ha [p. 15].
- Somente SAR (três sensores) com CNN-LSTM: R² = 0.5882 e RMSE = 30.0384 Mg/ha [p. 15].
- SAR individual com CNN-LSTM: GF-3 R² = 0.4355 e RMSE = 31.5704; ALOS-2 R² = 0.4285 e RMSE = 31.7333; Sentinel-1 R² = 0.4184 e RMSE = 32.7193 Mg/ha [p. 12]. O texto afirma que o ALOS-2 teve maior R², mas a Tabela 11 mostra o GF-3 ligeiramente à frente [p. 12].
- A fusão multissensor melhora a acurácia entre 5% e 10% em relação à fonte única [p. 1].
- CNN-LSTM foi o melhor modelo em 8 dos 9 conjuntos de dados [p. 18].
- AGB de 2018: maioria entre 60 e 90 Mg/ha, média de 64.20 Mg/ha [p. 15].
- Maiores correlações com AGB: H = 0.312 e A = −0.319 no ALOS-2 (decomposição de polarização) [p. 10]; PCA3 = 0.343 (GF-6), 0.420 (Sentinel-2) e −0.406 (Landsat-8) [p. 11].

## 6. Limitações que os próprios autores reconhecem

- Base amostral pequena: 160 parcelas, com bons resultados obtidos "with a small number of samples" [p. 17].
- Subestimação acima de 80 Mg/ha e superestimação abaixo de 30 Mg/ha, por saturação das imagens em alta biomassa e mistura de pixels em baixa cobertura [p. 18].
- Combinar os três SAR não melhorou a acurácia, atribuído ao baixo contraste das feições SAR e ao menor ponto de saturação dos fatores radar [p. 15, p. 17].
- Dados heterogêneos podem introduzir erros [p. 2]; a complexidade dos modelos e a exigência de inventário florestal limitam o uso de deep learning [p. 3].

## 7. O que serve ao projeto e o que não serve

- Serve: o desenho comparativo de três sensores ópticos e três SAR com RF, CNN e CNN-LSTM, incluindo seleção de variáveis por correlação — replicável para silvicultura em Goiás [p. 7–9, p. 17].
- Serve: a evidência de maior sensibilidade da banda L (ALOS-2) à AGB frente à banda C, e de que fusão óptico + SAR é o melhor arranjo [p. 15, p. 17].
- Não serve: o estudo estima apenas AGB (Mg/ha), sem estoque de carbono nem fator de conversão [p. 15]; carbono não é tratado no artigo.
- Não serve: a área é floresta subtropical natural mista [p. 3], não plantios de silvicultura do Cerrado; há uma única partição 130/30 e não se informa validação cruzada nem mapa de incerteza [p. 5].

## 8. Frases citáveis (literais)

- "In contrast with the single source, integrating multisource data can effectively enhance accuracy, with improvements ranging from 5% to 10%." [p. 1]
- "It should also be noted that the models constructed on the basis of different data and methods generally have the phenomena of high underestimation and low overestimation." [p. 18]
