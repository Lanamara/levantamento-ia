# RELATÓRIO — Nikos Theofanous (2021)

## 1. Referência

Theofanous, N.; Chrysafis, I.; Mallinis, G.; Domakinis, C.; Verde, N.; Siahalou, S. "Aboveground Biomass Estimation in Short Rotation Forest Plantations in Northern Greece Using ESA's Sentinel Medium-High Resolution Multispectral and Radar Imaging Missions". *Forests* 2021, 12, 902. DOI: 10.3390/f12070902. Recebido em 4/6/2021, aceito em 9/7/2021, publicado em 11/7/2021 [p. 1]. O `TEXTO.txt` está completo (16 páginas, incluindo referências) e corresponde ao DOI indicado.

## 2. Pergunta do estudo

A combinação sinérgica de séries temporais Sentinel-2 (óptico) e Sentinel-1 (radar) melhora a modelagem de AGB em plantios de rotação curta de *Robinia pseudoacacia*, e quais datas e sensores são ótimos para isso?

## 3. Área e dados

- Local: norte da unidade regional de Evros, nordeste da Grécia; elevação de 15 a 455 m, média de 99,19 m; cerca de 80% da área é planície, com declives suaves [p. 3]; clima Csa (Mediterrâneo de verão quente) [p. 4].
- Campo: medições de junho a setembro de 2019 em 105 parcelas quadradas de 0,09 ha, selecionadas por amostragem aleatória estratificada (data de plantio e tratamentos silviculturais); medidos número de árvores, DAP (d1,3) e altura [p. 4–5].
- Sentinel-2 MSI: imagens de janeiro de 2019 a dezembro de 2020, 400 tiles (granulos TMF e TMG), reflectância de superfície L2A, composições mensais e 10 índices espectrais (NDVI, NDWI, NDI45, MCARI, PSSRa, GEMI, WET, RSR, EVI, GNDVI); bandas de 20 m reamostradas para 10 m [p. 5].
- Sentinel-1: 29 imagens GRD C-band, modo IW, dupla polarização VV/VH, de janeiro a dezembro de 2020, órbita relativa 109, passe descendente; filtro Lee 5×5, correção de terreno com SRTM 30, conversão para dB [p. 5–6].

## 4. Método

- AGB por árvore obtida por equação alométrica de Annighöfer et al. (ln(BM) = α + β·ln(D²·H), com α = −3,33, b = 0,95 e CF = 1,004) [p. 5].
- Correlação de Spearman entre cada índice espectral ou coeficiente de retroespalhamento (VV, VH) e a AGB, mês a mês [p. 7–8].
- Modelos Random Forest (RF) mensais em quatro conjuntos de variáveis: S2 (só índices), S2/S1_VV, S2/S1_VH e S2/S1 (VV e VH) [p. 7].
- Ajuste com ntree = 500, nodesize = 5 e mtry = 1/3 dos preditores; acurácia avaliada por out-of-bag (OOB) e validação cruzada de 10 folds, com R² e RMSE [p. 7].

## 5. Resultados principais

- AGB média das 105 parcelas: 33,43 Mg ha⁻¹; amplitude de 4,41 a 98,12 Mg ha⁻¹; desvio padrão de 16,45 Mg ha⁻¹ [p. 5]. Densidade média de 1.589 árvores ha⁻¹ (733–3.522), altura média de 7,64 m (0,5–22) e DAP médio de 8,71 cm (3–28,7) [p. 5].
- Melhor modelo: Sentinel-2 de agosto, R² = 0,52 e RMSE = 11,26 Mg ha⁻¹ [p. 9]. Julho e setembro praticamente empatados: R² = 0,37 com RMSE = 12,87 e 12,99 Mg ha⁻¹, respectivamente [p. 9].
- Inverno e início de primavera com desempenho pior que a média: R² negativo em dezembro (−0,08), janeiro (−0,17), fevereiro (−0,23) e março (−0,16) para os modelos S2 [p. 9].
- Ao acrescentar Sentinel-1 em agosto, a acurácia caiu: R² = 0,50 (S2/S1_VV), 0,51 (S2/S1_VH) e 0,50 (S2/S1) [p. 10]. Em meses de baixo desempenho (janeiro a abril e outubro a dezembro) houve ganho pequeno [p. 10].
- Correlações de Spearman mais altas em julho: NDWI = 0,64, NDI45 = 0,63, NDVI/PSSRa/GEMI/WET = 0,60–0,62 [p. 8]. WET e MCARI tiveram correlação máxima em agosto (0,64 e 0,52) [p. 8]. Em janeiro nenhum índice se correlacionou com AGB (p > 0,05) [p. 8].
- Sentinel-1: VV correlacionado (p < 0,01) em março, maio, julho e outubro, com máximo em março (R = 0,35) [p. 8]; VH significativo em todos os meses exceto junho e outubro, com máximo em janeiro (R = 0,47) [p. 9].
- RSR manteve correlação significativa em todos os meses exceto maio e janeiro [p. 7]; MCARI teve a menor correlação ao longo do ano [p. 13].

## 6. Limitações que os próprios autores reconhecem

- A penetração do C-band na folhagem do *Robinia* é limitada, de modo que o retroespalhamento não acrescentou informação à resposta espectral no período com folhas [p. 11].
- A inclusão das bandas Sentinel-1 reduziu levemente a acurácia dos modelos no período folhado; preditores ruidosos ou irrelevantes podem reduzir a acurácia do RF [p. 11], e o impacto negativo das bandas Sentinel-1 é destacado nas conclusões [p. 13].
- A umidade do solo no período sem folhas introduz variabilidade no retroespalhamento e afeta a robustez da modelagem [p. 13].
- Variação interanual das respostas espectrais por forçamento climático, cobertura do piso florestal e diferenças sazonais de sombreamento dificultam identificar a data ótima de modelagem a partir de um único índice [p. 12].
- A acurácia é baixa em maio e junho, atribuída à saturação de índices no pico de biomassa verde [p. 11]; o melhor resultado é descrito apenas como "rather satisfactory" (R² = 0,52) [p. 13].

## 7. O que serve ao projeto e o que não serve

- Serve: o desenho de comparar séries mensais ópticas e SAR com RF e correlação de Spearman por fenofase é diretamente replicável para silvicultura em Goiás, inclusive a lógica de escolher a data ótima de imageamento [p. 7–9].
- Serve: o conjunto de 10 índices espectrais Sentinel-2 (NDVI, NDWI, NDI45, MCARI, PSSRa, GEMI, WET, RSR, EVI, GNDVI) e o uso de composições mensais no Google Earth Engine são um ponto de partida barato para AGB [p. 5].
- Serve com cautela: o achado de que Sentinel-1 C-band não agrega no período folhado é um alerta metodológico, mas é específico de folhosas decíduas e terreno plano na Grécia [p. 11]; em Cerrado e em plantios de eucalipto o comportamento do C-band pode diferir.
- Não serve: o artigo estima apenas AGB, sem estoque de carbono, e a extrapolação para Goiás é limitada por espécie (*Robinia pseudoacacia*), clima Csa, 105 parcelas de 0,09 ha e R² máximo de 0,52 [p. 5, 9].

## 8. Frases citáveis (literais)

- "The synergy of Sentinel-1 and Sentinel-2 data proved to be a non-efficient approach for improving forest biomass RF models throughout the year within the geographical and environmental context of our study." [p. 1]
- "The results of the study indicate that such a monthly modeling approach, based only on Sentinel-2 data, can be transferred across the country for biomass mapping over black locust plantations." [p. 13]
