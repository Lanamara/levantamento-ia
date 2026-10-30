# RELATÓRIO — Hantao Li (2024)

## 1. Referência

**Atenção: o `TEXTO.txt` desta pasta não é o artigo do DOI pedido.** O arquivo contém outro artigo, completo e íntegro, sem truncamento:

- Al Saim, A.; Aly, M. H. (2026). *Machine Learning and Multisensor Data Fusion for Forest above Ground Biomass Estimation in Arkansas*. Earth Systems and Environment, 10, 1783–1800. DOI: 10.1007/s41748-025-00713-z.
- O artigo solicitado — Li, H. (2024), *Accuracy assessment of GEDI terrain elevation, canopy height, and aboveground biomass density estimates in Japanese artificial forests*, DOI 10.1016/j.srs.2024.100144 — **não está neste arquivo**.

Como o texto presente é um artigo científico completo e legível, as seções 2 a 8 abaixo resumem **apenas esse documento real**, sem qualquer dado inventado sobre o artigo de Li (2024). Nada foi preenchido com conhecimento externo. As páginas citadas são as marcas `[página N]` do arquivo.

## 2. Pergunta do estudo

É possível estimar a aboveground biomass (AGB) das florestas de Ozark e Ouachita, no Arkansas, em resolução de 10 m, fundindo Sentinel-2, Sentinel-1 e GEDI com regressão Random Forest no Google Earth Engine, e extrapolar essa estimativa para 2015–2023? [p. 1; p. 4]

## 3. Área e dados

- **Local:** Ozark-St. Francis National Forest (~426.000 ha, norte do Arkansas, topografia cárstica, floresta decídua de carvalho-nogueira) e Ouachita National Forest (>1,7 milhão de acres, Arkansas central e Oklahoma oriental, pinheiro/carvalho em relevo de cristas leste-oeste) [p. 4].
- **Período:** Sentinel-2 e Sentinel-1 na estação de crescimento de 2021 (junho–agosto); GEDI L4B com dados de abril de 2019 a agosto de 2021; Landsat 8 de 2015 a 2023, exceto 2021 [p. 4; p. 6].
- **Sensores e fontes:** Sentinel-2 MSI (bandas de 10 m, <5% de nuvem, composição por média) [p. 4]; Sentinel-1 C-band IW GRD, polarizações VV e VH, 10 m, filtro Lee refinado 7×7 [p. 5]; SRTM DEM para correção de terreno [p. 5]; 3DEP 10 m para elevação e declividade [p. 6]; GEDI L2A (RH50, RH70, RH90, RH95, RH100) e GEDI L4B (AGBD em células de 1 km) [p. 6]; Landsat 8 Surface Reflectance Tier 1 [p. 6]; máscara de água JRC Global Surface Water (limiar de 60%, 30 m) [p. 5].
- **Amostras:** 2.000 pontos sorteados do GEDI L4B por amostragem estratificada, divididos em 80% treino e 20% validação [p. 6–7].
- **Variáveis:** 154 preditoras calculadas, das quais 34 selecionadas por importância no Random Forest [p. 7].

## 4. Método

- **Fusão multissensorial no GEE:** composições médias de Sentinel-2 (bandas, NDVI, EVI, LAI) e Sentinel-1 (retroespalhamento calibrado, correção topográfica por SRTM), mais elevação, declividade e métricas de altura do GEDI [p. 4–6].
- **Métricas de altura:** cinco produtos de altura relativa do GEDI (RH50 a RH100) e interpolação por Random Forest a partir do Sentinel-2 para gerar produto de altura em 10 m [p. 6].
- **Textura:** GLCM sobre 22 bandas, janela 3×3, 14 métricas de Haralick (mean, variance, homogeneity, contrast, dissimilarity, entropy, correlation) [p. 7].
- **Modelagem e validação:** Random Forest para regressão, com grid search; numberOfTrees = 350, variablesPerSplit = raiz do número de variáveis, minLeafPopulation = 1, bagFraction = 0,75; avaliação por R² e RMSE no conjunto de validação de 20% [p. 7–8].

## 5. Resultados principais

- **Treino:** R² = 0,95 e RMSE = 18,46 [p. 8].
- **Validação:** R² = 0,75 e RMSE = 34,52 [p. 8].
- **Variável mais importante:** elevação, entre as 34 selecionadas [p. 8]. Em seguida, as métricas de altura relativa, com RH98 > RH95 > RH100 [p. 8].
- **Índices de vegetação:** EVI, NDVI e LAI com importância quase igual [p. 8]. Entre as bandas espectrais, a banda 11 foi a mais influente e a banda 5 a menos [p. 8].
- **Mapa de AGB 2021 em 10 m:** maiores valores no norte do Ozark; menores no oeste do Ouachita; valores baixos ao longo de estradas e em pastagens/áreas nuas [p. 8–9].
- **Série 2015–2023 (Mg/ha):** 2015 = 150,99; 2016 = 100,75; 2017 = 163,36; 2018 = 177,15; 2019 = 168,95; 2020 = 170,18; 2021 = 163,36; 2022 = 191,10; 2023 = 199,84 [p. 12]. A média variou entre 100 e 200 Mg/ha [p. 8]; 2016 foi o menor valor, atribuído à cobertura de nuvens [p. 8]; a tendência geral foi de aumento [p. 9].
- **Corroboração externa:** o levantamento do USDA de 2022 indicou maior biomassa de madeira dura no Ozark do que no Ouachita, coerente com o mapa gerado [p. 14].

## 6. Limitações que os próprios autores reconhecem

- O Random Forest tendeu a **superestimar AGB baixa e subestimar AGB alta**, por causa da natureza de média do algoritmo e das características dos dados de referência [p. 11].
- A **falta de dados históricos de parcelas de campo** impediu a validação confiável das séries temporais de AGB [p. 14].
- A premissa de que a relação entre AGB e imagem de satélite permanece **estável no tempo** pode não ser válida [p. 14].
- Nuvens e sombras de nuvens afetaram a estimativa em alguns anos; sombras de dossel em relevo complexo e interferência de sub-bosque e solo em florestas abertas também são apontadas [p. 14].
- As lacunas de cobertura do GEDI podem ter contribuído para a ausência de valores extremos na amostra [p. 12].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o desenho de fusão Sentinel-2 + Sentinel-1 + GEDI + variáveis topográficas em GEE, com saída em 10 m e validação por R²/RMSE em 20% retido, é diretamente transferível para silvicultura em Goiás [p. 4; p. 7–8].
- **Serve:** a hierarquia de preditores (elevação, RH98/RH95/RH100, EVI/NDVI/LAI) e o uso de amostragem estratificada do GEDI L4B como referência são replicáveis e úteis para priorizar variáveis [p. 6–8].
- **Não serve:** a área é floresta natural temperada dos EUA, não plantio comercial; não há nenhuma análise de silvicultura, rotação ou espécie plantada [p. 4].
- **Não serve:** o trabalho estima apenas AGB, sem conversão para estoque de carbono, e usa GEDI L4B (produto modelado) como referência, não parcelas de campo medidas [p. 6]; além disso, não é uma avaliação de acurácia de elevação, altura de dossel e AGBD do GEDI, que é o tema do artigo de Li (2024) pedido.

## 8. Frases citáveis (literais)

- "For the training dataset, the model achieved an R-squared value of 0.95, demonstrating that 95% of the variation in observed AGB was accounted for by the model." [p. 8]
- "The lack of historical field sample plot data hindered the reliable validation of the long-term time-series AGB maps, which were generated by applying the 2021 AGB prediction models to subsequent years." [p. 14]
