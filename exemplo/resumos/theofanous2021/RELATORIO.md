# RELATÓRIO — Nikos Theofanous (2021)

## 1. Referência

Theofanous, N.; Chrysafis, I.; Mallinis, G.; Domakinis, C.; Verde, N.; Siahalou, S. **Aboveground Biomass Estimation in Short Rotation Forest Plantations in Northern Greece Using ESA's Sentinel Medium-High Resolution Multispectral and Radar Imaging Missions.** *Forests* 2021, 12(7), 902. DOI: 10.3390/f12070902.

O `TEXTO.txt` está íntegro: 16 páginas, do título às referências [p. 16], e corresponde ao DOI acima (recebido 4 jun. 2021, publicado 11 jul. 2021 [p. 1]).

## 2. Pergunta do estudo

A combinação de séries temporais Sentinel-2 (índices espectrais) e Sentinel-1 (retroespalhamento VV e VH) melhora a modelagem de AGB por random forest em plantios de rotação curta de *Robinia pseudoacacia*, e qual mês do ano produz o modelo mais acurado? [p. 1, 3]

## 3. Área e dados

- Local: norte da unidade regional de Evros, nordeste da Grécia; elevação de 15 a 455 m, média de 99,19 m; cerca de 80% da área é planície [p. 3]. Clima Csa (verão quente mediterrâneo) [p. 4].
- Trabalho de campo: junho a setembro de 2019 [p. 4].
- Amostra: 105 parcelas quadradas de 0,09 ha, selecionadas por amostragem aleatória estratificada (data de plantio e tratamentos silviculturais) [p. 5].
- Sentinel-2 MSI: janeiro de 2019 a dezembro de 2020, produto L2A, 400 tiles (granules TMF e TMG), bandas de 20 m reamostradas para 10 m, 10 índices espectrais [p. 5].
- Sentinel-1: 29 imagens GRD, banda C, modo IW, polarizações VV e VH, janeiro a dezembro de 2020, passagem descendente, órbita relativa 109 [p. 5].
- Estatísticas de campo: 1589 árvores/ha em média (733–3522); altura média 7,64 m (0,5–22); DAP médio 8,71 cm (3–28,7); AGB média 33,43 Mg ha⁻¹ (4,41–98,12), desvio padrão 16,45 Mg ha⁻¹ [p. 5].

## 4. Método

- AGB por árvore obtida por equação alométrica não linear de Annighöfer et al. (ln(BM) = α + β·ln(D²·H), com α = −3,33, b = 0,95 e fator de correção CF = 1,004), aplicada aos dados de DAP e altura [p. 5].
- Compósitos mensais de média no Google Earth Engine para Sentinel-2 (após máscara de nuvem, cirrus, sombra e neve) e Sentinel-1 (calibração para σ⁰, filtro de Lee 5 × 5, correção topográfica SRTM 30, conversão para dB) [p. 5].
- Extração da média por parcela apenas com pixels inteiramente dentro do limite da parcela e análise de correlação de postos de Spearman entre cada variável e a AGB, mês a mês [p. 7].
- Random forest (pacote randomForest) com quatro conjuntos de preditores — S2; S2/S1_VV; S2/S1_VH; S2/S1 —, ntree = 500, nodesize = 5, mtry = 1/3 das variáveis, ajuste com todos os dados e acurácia avaliada por OOB com 10-fold cross-validation (R² e RMSE) [p. 7].

## 5. Resultados principais

- Melhor modelo: Sentinel-2 de agosto, R² = 0,52 e RMSE = 11,26 Mg ha⁻¹ [p. 9].
- Julho e setembro praticamente empatados: R² = 0,37 com RMSE = 12,87 Mg ha⁻¹ e R² = 0,37 com RMSE = 12,99 Mg ha⁻¹ [p. 9].
- Inverno e início de primavera (dezembro a março) com R² negativo nos modelos só ópticos, isto é, pior que prever pela média [p. 9, 11].
- Acrescentar Sentinel-1 piorou levemente o melhor modelo: R² = 0,50 (S2/S1_VV), 0,51 (S2/S1_VH) e 0,50 (S2/S1) em agosto [p. 10]. Entre maio e setembro os modelos com SAR ficaram equivalentes aos só ópticos [p. 10].
- Correlações de Spearman mais altas em julho: NDWI 0,64; NDI45 0,63; WET 0,62 e GEMI 0,62; NDVI 0,60 [p. 8]. Em agosto o maior valor é WET (0,64) e MCARI sobe para 0,52 [p. 8].
- RSR foi o único índice com correlação significativa em quase todos os meses (exceto maio e janeiro); em janeiro nenhum índice se correlacionou com AGB (p > 0,05) [p. 7–8].
- Sentinel-1 VV correlacionou com AGB (p < 0,01) em março, maio, julho e outubro, com máximo em março (R = 0,35) [p. 8]. VH correlacionou em todos os meses exceto junho e outubro, com máximo em janeiro (R = 0,47) [p. 8].
- Nota: na p. 9 o texto traz um parêntese contraditório para agosto ("R² = 0,379, RMSE = 12,825 Mg ha⁻¹"), que conflita com a Tabela 5 e com o resumo (R² = 0,52; 11,26 Mg ha⁻¹).

## 6. Limitações que os próprios autores reconhecem

- O resultado negativo da sinergia é declarado válido apenas "within the geographical and environmental context of our study" [p. 1].
- Durante a estação com folha, a penetração do comprimento de onda C na folhagem é limitada, de modo que o retroespalhamento não acrescentou informação aos índices espectrais [p. 11].
- Na estação sem folha, a umidade do solo introduz variabilidade no retroespalhamento e afeta a robustez da modelagem [p. 13].
- O terreno relativamente plano e a baixa obstrução por nuvens e sombras favoreceram o experimento, o que restringe a extrapolação para áreas com relevo acidentado [p. 13].
- Identificar a data ótima por série temporal de um único índice "is not a trivial task", pois transições rápidas de fenologia e variação interanual por forçamento climático interferem na escolha [p. 12].
- A inclusão de preditores ruidosos pode reduzir a acurácia do RF, o que exige cautela em procedimentos de seleção de variáveis [p. 11, 13].

## 7. O que serve ao projeto e o que não serve

- Serve: o desenho comparativo mensal com quatro conjuntos de preditores (S2, S2/S1_VV, S2/S1_VH, S2/S1), avaliado por OOB e 10-fold cross-validation, é diretamente replicável para silvicultura em Goiás [p. 7].
- Serve: a evidência negativa é útil — SAR C-band não agrega informação na estação com folha, e o pico de folhagem satura os índices (maio e junho com R² ≈ 0,08–0,11) [p. 9, 11]; isso orienta escolher datas de fim de estação seca, antes da senescência.
- Serve com ressalva: a equação alométrica com DAP e altura é uma via para obter AGB de campo sem corte destrutivo, mas foi calibrada para *Robinia pseudoacacia* no norte da Itália [p. 5].
- Não serve: o artigo para na AGB e não converte em estoque de carbono; o contexto (espécie, clima Csa, terreno plano, 105 parcelas de 0,09 ha, R² máximo de 0,52) não transfere para eucalipto ou pinus em Goiás [p. 5, 9, 13].

## 8. Frases citáveis (literais)

- "The synergy of Sentinel-1 and Sentinel-2 data proved to be a non-efficient approach for improving forest biomass RF models throughout the year within the geographical and environmental context of our study." [p. 1]
- "The results of the study indicate that such a monthly modeling approach, based only on Sentinel-2 data, can be transferred across the country for biomass mapping over black locust plantations." [p. 13]
