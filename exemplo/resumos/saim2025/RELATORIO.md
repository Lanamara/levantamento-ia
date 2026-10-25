# Relatório de leitura — Saim & Aly (2026)

*Observação sobre paginação: as páginas entre colchetes seguem as marcas `[página N]` do TEXTO.txt (p. 1 = p. 1783 da revista).*

## 1. Referência

SAIM, Abdullah Al; ALY, Mohamed H. **Machine Learning and Multisensor Data Fusion for Forest above Ground Biomass Estimation in Arkansas**. *Earth Systems and Environment*, v. 10, p. 1783–1800, 2026. DOI: 10.1007/s41748-025-00713-z. (Recebido em 11/11/2024; aceito em 25/06/2025; publicado online em 11/07/2025.) [p. 1]

## 2. Pergunta do estudo

É possível estimar a biomassa acima do solo (AGB) em resolução de 10 m nas florestas nacionais de Ozark e Ouachita (Arkansas), fundindo Sentinel-2, Sentinel-1 e GEDI com regressão por Random Forest no Google Earth Engine, e extrapolar essa AGB para 2015–2023 com Landsat 8? [p. 1, p. 4]

## 3. Área e dados

- **Local:** Ozark National Forest (≈ 426.000 ha, norte do Arkansas) e Ouachita National Forest (> 1,7 milhão de acres, centro do Arkansas e leste de Oklahoma), EUA. [p. 4]
- **Período:** Sentinel-2 e Sentinel-1 da estação de crescimento de 2021 (junho a agosto); GEDI L4B com dados de abril de 2019 a agosto de 2021; Landsat 8 de 2015 a 2023, exceto 2021, sempre de junho a agosto. [p. 4, p. 6]
- **Sensores/fontes:** Sentinel-2 MSI (bandas de 10 m, < 5% de nuvens, índices NDVI, EVI e LAI), Sentinel-1 C-band IW GRD em VV/VH (10 m), GEDI L2A (RH50, RH70, RH90, RH95, RH100) e GEDI L4B (AGBD em células de 1 km), Landsat 8 SR, DEM 3DEP de 10 m (elevação e declividade), máscara de água JRC. [p. 4, p. 5, p. 6]
- **Amostras:** 2.000 pontos sorteados do GEDI L4B por amostragem estratificada; 80% para treino e 20% para validação independente. [p. 6, p. 7]

## 4. Método

1. **Fusão de variáveis em 10 m:** bandas espectrais, índices de vegetação, cinco métricas de altura relativa do GEDI interpoladas para 10 m por Random Forest com Sentinel-2, elevação e declividade do 3DEP e texturas GLCM (janela 3 × 3, 22 bandas de entrada) — 154 variáveis no total, reduzidas a 34 por importância no RF. [p. 5, p. 6, p. 7]
2. **Random Forest no GEE:** regressão com busca em grade; melhores hiperparâmetros `numberOfTrees` = 350, `variablesPerSplit` = raiz do número de variáveis, `minLeafPopulation` = 1 e `bagFraction` = 0,75. [p. 7]
3. **Validação:** 80/20 sobre os pontos GEDI, com R² e RMSE como métricas. [p. 7, p. 8]
4. **Extrapolação temporal:** normalização radiométrica relativa das imagens Landsat 8 de 2015–2023 tendo 2021 como ano-base, aplicando o modelo linear resultante aos anos-alvo. [p. 7, p. 8]

## 5. Resultados principais

- O RF reteve **34 das 154 variáveis** (topografia, espectrais e texturais). [p. 1, p. 7]
- **Treino:** R² = **0,95** e RMSE = **18,46**. [p. 1, p. 8]
- **Validação:** R² = **0,75** e RMSE = **34,52**. [p. 1, p. 8]
- AGB mapeada em **10 m** de resolução, com todos os preditores nessa mesma resolução. [p. 1, p. 8]
- **Elevação** foi a variável mais importante; entre as alturas, **RH98**, seguida de **RH95** e **RH100**; EVI, NDVI e LAI com importância quase igual; entre as bandas, a 11 foi a mais influente e a 5 a menos. [p. 8]
- Padrão espacial: AGB mais alta no norte do Ozark e nas porções sudeste/noroeste do Ouachita; mais baixa no oeste do Ouachita, perto de estradas e do rio Ouachita, e em pastagens e áreas estéreis. [p. 8, p. 9]
- Série histórica: média anual entre **100 e 200 Mg/ha** em 2015–2023. [p. 1, p. 8]
- Valores anuais da Tabela 1: 2015 = **150,99**; 2016 = **100,75** (o menor, atribuído a nuvens); 2017 = **163,36**; 2018 = **177,15**; 2019 = **168,95**; 2020 = **170,18**; 2021 = **163,36**; 2022 = **191,10**; 2023 = **199,84** Mg/ha — com tendência geral de aumento no período. [p. 12, p. 9]
- *Inconsistência interna a registrar:* o texto diz usar RH50, RH70, RH90, RH95 e RH100 [p. 6], mas os resultados destacam o RH98 como mais importante [p. 8] e o resumo cita RH100, RH98 e RH95 [p. 1].

## 6. Limitações que os próprios autores reconhecem

- O RF **superestima AGB baixa e subestima AGB alta**, com viés em direção à média, sobretudo quando o dado de referência não cobre valores extremos. [p. 11]
- A cobertura do GEDI **não é wall-to-wall** e tem lacunas, o que pode explicar a falta de amostragem de valores extremos na área. [p. 12]
- **Falta de dados históricos de campo** impediu validar de forma confiável as séries temporais de AGB; a premissa de relação estável entre AGB e sensoriamento ao longo do tempo pode não valer. [p. 14]
- Em Landsat, **nuvens e sombras de nuvem**, sombras de dossel em relevo complexo e interferência de sub-bosque e solo em formações abertas afetam a estimativa; perturbações naturais ou antrópicas podem quebrar a relação satélite–AGB. [p. 14]
- As predições fora de 2021 são **difíceis de validar** por falta de modelos históricos de AGB. [p. 8]
- As lacunas do GEDI L4B vêm de nuvens persistentes e da dinâmica orbital da ISS. [p. 6]

## 7. O que serve ao projeto e o que não serve

- **Serve:** o desenho de fusão multissensorial (óptico + SAR + LiDAR + topografia + textura) inteiramente em nuvem, que os autores apresentam explicitamente como estrutura transferível para outras regiões. [p. 1, p. 4]
- **Serve:** a hierarquia de preditores (elevação, alturas relativas de dossel, EVI/NDVI/LAI) e o par de hiperparâmetros do RF como ponto de partida para seleção de variáveis em Goiás. [p. 7, p. 8]
- **Não serve:** o alvo é apenas **AGB (Mg/ha)**; não há conversão para estoque de carbono, CO₂ ou fatores de expansão — o tema do projeto (carbono) não é quantificado. [p. 2, p. 12]
- **Não serve:** a área é floresta natural temperada (carvalho-nogueira, pinheiro-carvalho), não silvicultura plantada, e a validação é contra o próprio GEDI, sem parcelas de campo — não fornece allometria nem calibração local utilizável para plantios em Goiás, onde a cobertura GEDI também é limitada. [p. 3, p. 4, p. 8]

## 8. Duas frases citáveis

> "The RF model showed strong performance with R-squared and RMSE values of 0.95 and 18.46 for the training dataset and 0.75 and 34.52 for the validation dataset, respectively." [p. 1]

> "The lack of historical field sample plot data hindered the reliable validation of the long-term time-series AGB maps, which were generated by applying the 2021 AGB prediction models to subsequent years." [p. 14]
