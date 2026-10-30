# RELATÓRIO — Dejun Wang (2025)

## 1. Referência

Wang, D.; Xing, Y.; Fu, A.; Tang, J.; Chang, X.; Yang, H.; Yang, S.; Li, Y. (2025). *Mapping Forest Aboveground Biomass Using Multi-Source Remote Sensing Data Based on the XGBoost Algorithm*. **Forests**, 16(2), 347. DOI: 10.3390/f16020347. O `TEXTO.txt` corresponde ao artigo completo do DOI (20 páginas, incluindo referências).

## 2. Pergunta do estudo

Verificar se a combinação de altura contínua de árvores (TH) derivada de imagens estereoscópicas GF-7 com atributos espectrais de Sentinel-1 e Sentinel-2 e topográficos do ALOS DEM, após seleção por RFE, melhora a estimativa de AGB florestal por XGBoost em relação a fontes isoladas.

## 3. Área e dados

- Local: Genhe City, nordeste da China, Grandes Montanhas Khingan (~20.010 km²; 120,196–122,90° E, 50,414–52,517° N; 700–1.300 m de altitude; 91,92% de cobertura florestal, dominada por lariço-da-dauria — 82,77%) [p. 3].
- Período: coletas de campo em agosto de 2012, fevereiro de 2022 e agosto de 2024 [p. 3]; Sentinel-2 de outubro de 2022 [p. 5]; Sentinel-1 de 9 de agosto de 2021 [p. 6]; ALOS DEM de 30 de agosto de 2010 [p. 6].
- Sensores/fontes: 37 imagens GF-7 DLC (0,65 m retro / 0,8 m frontal), 11 imagens S2 (10 bandas, 24 índices de vegetação e 5 variáveis biofísicas), 2 imagens S1 IW (VV e VH) e 3 imagens ALOS DEM (5 atributos topográficos), todas reamostradas a 30 m [p. 4–6].
- Amostras: 186 parcelas (53 de 40 × 40 m em 2012; 83 e 50 de 25 × 25 m em 2022 e 2024), sendo 112 de coníferas e 74 de folhosas [p. 3]; AGB observada de 21,16 a 156,40 Mg/ha, média de 85,42 Mg/ha [p. 4].

## 4. Método

- Geração de TH contínua por `TH = DSM(GF-7) − DEM(ALOS)` (Equação 1), com DSM extraído no OrthoEngine/Geomatica 2018 e reamostragem para 30 m [p. 7].
- Construção de 15 combinações de atributos a partir de quatro grupos (TH, S1, S2 e DEM), totalizando até 50 variáveis na combinação completa [p. 6, p. 10].
- Seleção de atributos por RFE usando XGBoost como estimador externo e validação cruzada de cinco folds, com escolha do subconjunto por R² e RMSE [p. 8].
- Regressão por XGBoost (n_estimators = 500; max_depth = 6; learning_rate = 0,1; subsample e colsample_bytree = 0,8; gamma = 1,0; lambda = 1,0; alpha = 0,5), divisão 80% treino / 20% teste e mapeamento final a 30 m [p. 8–9].

## 5. Resultados principais

- Modelo final (TS1S2D, 13 atributos): R² = 0,71 e RMSE = 18,11 Mg/ha no conjunto de teste [p. 10]; na validação cruzada, R² = 0,60 e RMSE = 21,28 Mg/ha [p. 10].
- TS2D: R² = 0,60 e RMSE = 21,32 Mg/ha na validação cruzada, com 16 atributos [p. 10]; no teste, R² = 0,67 e RMSE = 20,88 Mg/ha [p. 11]. TS1S2: R² = 0,65 e RMSE = 20,66 Mg/ha [p. 11].
- Fonte única: TH foi a mais precisa (R² = 0,43; RMSE = 28,72 Mg/ha), seguida de S2 (R² = 0,33; RMSE = 30,88), DEM (R² = 0,19; RMSE = 44,79) e S1 (R² = 0,09; RMSE = 49,32) [p. 10].
- Importância dos atributos no modelo TS1S2D: TH = 19,8%; B5 = 7,9%; B12 = 6,5%; SPI = 4,3%; NDI45 = 3,5%; NDRE1 = 2,8%; VV/VH = 0,4% e VV+VH = 0,2% [p. 11].
- Mapa de AGB: 18,0 a 181,2 Mg/ha; média de 89,4 Mg/ha; AGB total de 0,87 × 10^8 Mg e estoque de carbono de 0,43 × 10^8 MgC (fator de conversão 0,5) [p. 11].
- Por tipo florestal: coníferas R² = 0,72 e RMSE = 18,02 Mg/ha; folhosas R² = 0,71 e RMSE = 18,09 Mg/ha [p. 13–14]; TH com 20,5% (coníferas) e 18,9% (folhosas) de importância [p. 14].
- Comparação com mapas publicados: mediana de 90,145 Mg/ha neste estudo contra 82,236, 80,041 e 77,867 Mg/ha; médias de 89,41 contra 81,729, 82,301 e 81,437 Mg/ha [p. 16].

## 6. Limitações que os próprios autores reconhecem

- O método de TH "depends highly on high-precision DEM data", com proposta de usar no futuro DEM de radar de maior comprimento de onda (banda P) [p. 12].
- O S1 é banda C e mostrou-se sensível ao conteúdo de água do dossel e à umidade do solo, sobretudo por usar imagens da estação de crescimento; os autores recomendam testar SAR de comprimento de onda maior (bandas L e P) [p. 13].
- A contribuição do S1 foi baixa (0,4% e 0,2%), e os autores sugerem investigar sua aplicabilidade em diferentes regiões, sobretudo em terreno complexo ou alta densidade florestal [p. 11, p. 16].
- Nas conclusões, propõem modelos mais avançados (deep learning) e validação das combinações em outras regiões e tipos florestais [p. 17].

## 7. O que serve ao projeto e o que não serve

- Serve: o desenho experimental de 15 combinações de atributos + RFE + XGBoost é diretamente replicável para as plantações de Goiás, inclusive para comparar TH, óptico, radar e topografia.
- Serve: a evidência de que TH contínua é o preditor mais importante (19,8%) e que sua remoção reduz a acurácia [p. 11–12] reforça a necessidade de dados de altura do dossel no projeto.
- Não serve: a geometria de sensores (GF-7, ALOS DEM de 2010), a espécie (lariço) e os modelos alométricos de lariço, bétula e álamo [p. 4], além do fator de carbono fixo de 0,5 [p. 11] — inadequados para silvicultura tropical/subtropical.
- Não serve: a baixa contribuição do Sentinel-1 (banda C) neste sítio [p. 11] não deve ser extrapolada para Goiás; o próprio artigo sugere testar bandas L e P [p. 13].

## 8. Frases citáveis (literais)

- "TH was found to be the most important predictive feature, followed by S2 optical features, topographic features, and S1 radar features." [p. 1]
- "However, the method depends highly on high-precision DEM data, and in the future, DEMs with higher precision will be generated using SAR data with longer wavelengths (e.g., P-band)." [p. 12]
