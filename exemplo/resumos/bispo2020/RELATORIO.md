# Relatório — Bispo et al. (2020)

## 1. Referência

BISPO, P. da C.; RODRÍGUEZ-VEIGA, P.; ZIMBRES, B.; MIRANDA, S. do C. de; CEZARE, C. H. G.; FLEMING, S.; BALDACCHINO, F.; LOUIS, V.; RAINS, D.; GARCIA, M.; ESPÍRITO-SANTO, F. D. B.; ROITMAN, I.; PACHECO-PASCAGAZA, A. M.; GOU, Y.; ROBERTS, J.; BARRETT, K.; FERREIRA, L. G.; SHIMBO, J. Z.; ALENCAR, A.; BUSTAMANTE, M.; WOODHOUSE, I. H.; SANO, E. E.; OMETTO, J. P.; TANSEY, K.; BALZTER, H. **Woody Aboveground Biomass Mapping of the Brazilian Savanna with a Multi-Sensor and Machine Learning Approach**. *Remote Sensing*, v. 12, n. 17, art. 2685, 2020. DOI: 10.3390/rs12172685. Recebido em 16/07/2020, publicado em 19/08/2020 [p. 1].

## 2. Pergunta do estudo

Qual é a distribuição espacial da biomassa acima do solo (AGB) lenhosa em uma bacia do Cerrado central, em resolução de 30 m, combinando parcelas de campo, LiDAR aerotransportado e imagens Landsat 8 e ALOS-2/PALSAR-2 com aprendizado de máquina [p. 3]?

## 3. Área e dados

- **Local:** bacia hidrográfica do Rio Vermelho, afluente do Araguaia, estado de Goiás, Brasil; área de 1.082.460 ha; clima Aw, inverno seco (maio–setembro) e verão chuvoso (outubro–abril) [p. 3]. Pastagens ocupam mais de 57% da área e, em 2018, restavam cerca de 33% de vegetação nativa [p. 4].
- **Período:** parcelas de campo estabelecidas em 2014 [p. 5]; LiDAR voado entre 20/06/2015 e 07/07/2015 [p. 7]; composto mediano Landsat 8 de 2015–2017 [p. 7]; mosaicos PALSAR-2 de 2015, 2016 e 2017 [p. 8]; Sentinel-1 de 2016–2018 usado só como referência de geolocalização [p. 8].
- **Sensores/fontes:** 15 parcelas de campo de 20 × 50 m em cerradão (10 em Itapirapuã, 5 em Goiás) [p. 5–6]; 60 tiles de LiDAR aerotransportado (Optech Orion M300 e Optech ALTM 09SEN243), 1.009,01 ha, ~45 pontos/m² [p. 7]; Landsat 8 OLI (30 m), 244 cenas [p. 7]; mosaicos ALOS/PALSAR-2 L-band de 25 m (γ⁰HV, γ⁰HH, RFDI, CpR) [p. 7–8].
- **Número de amostras:** 15 parcelas de campo [p. 5]; AGB das parcelas entre 19 e 104 Mg ha⁻¹ [p. 6]; 2.973 pixels de AGB-LiDAR usados como treino/teste no random forest [p. 8].

## 4. Método

1. **Upscaling em duas etapas** (campo → LiDAR → sensoriamento remoto orbital), aplicado pela primeira vez no bioma [p. 3, p. 8].
2. **AGB das parcelas** por equação alométrica de espécies misturadas para cerradão (N = 87, R² = 0,94, RSE = 0,13 Mg), com dbh ≥ 5 cm e só árvores vivas [p. 6].
3. **Modelo LiDAR:** métricas derivadas da nuvem de pontos (CHM, CC, CD, percentis, DSM, DTM) em pixel de 1 m, média por parcela; seleção de modelo linear generalizado por AICc entre combinações de CHM, CC e CD; extrapolação para 30 m sobre toda a pegada LiDAR [p. 7–8].
4. **Random forest** (regressão, Google Earth Engine) com validação cruzada k-fold, preditores = 4 variáveis SAR + 6 bandas e 5 índices Landsat 8; importância por jackknife; incerteza propagada de 5 componentes (medição 10%, LiDAR 1,5%, alometria 49,83%, amostragem 12,39%, predição) [p. 8–9].

## 5. Resultados principais

- Modelo LiDAR escolhido, AGB = f(CHM, CC): R² ajustado = 0,93 e RMSE = 6,74 Mg ha⁻¹ (13% da média), contra RMSE = 24,70 Mg ha⁻¹ do modelo nulo [p. 10].
- Validação final mapa-EO vs. referência LiDAR: R² = 0,89, RMSE = 7,58 Mg ha⁻¹, RMSE relativo = 43%, viés = 0,43 Mg ha⁻¹ [p. 10].
- AGB do mapa variou de 0 a 90 Mg ha⁻¹ por pixel; a incerteza por pixel, de 0 a 49 Mg ha⁻¹ [p. 10].
- Por faixa de AGB: RMSE = 6,39 Mg ha⁻¹ (rel. 61%) para AGB < 50 Mg ha⁻¹ e RMSE = 13,41 Mg ha⁻¹ (rel. 19%) para AGB > 50 Mg ha⁻¹ [p. 10].
- Faixa > 80 Mg ha⁻¹ (71 pixels): referência 89,2 Mg ha⁻¹, mapa 72,3 Mg ha⁻¹, viés −17,0 Mg ha⁻¹, RMSE 20,0 Mg ha⁻¹ [p. 11]. Faixa 0–20 Mg ha⁻¹ (2.084 pixels): viés +1,3 e RMSE relativo de 109% [p. 11].
- Importância de variáveis: Landsat 8 reflectância sozinha R² = 0,84; backscatter ALOS-2 sozinho R² = 0,79; índices ALOS sozinhos R² = 0,51, mas sua exclusão derruba o R² em 0,07 — o maior efeito entre os conjuntos [p. 16].
- Média de AGB na bacia: 18,66 Mg ha⁻¹ neste estudo, contra 16,25 (Avitabile), 33,89 (Santoro), 31,12 (Saatchi) e 58,59 Mg ha⁻¹ (Baccini) [p. 15]. Valor de referência independente para o Cerrado central: 20,4 ± 6,0 Mg ha⁻¹ [p. 15].
- O mapa atende aos requisitos da missão BIOMASS (RMSE < 10 Mg ha⁻¹ para AGB < 50 e rel. RMSE < 20% para AGB > 50) [p. 15].

## 6. Limitações reconhecidas pelos autores

- Estimativas de AGB < 19 Mg ha⁻¹ são incertas, pois as parcelas de campo cobriram apenas vegetação lenhosa (não pastagem, agricultura ou solo exposto) [p. 15].
- Subestimação das faixas altas de AGB (> 80 Mg ha⁻¹, viés −17,0 Mg ha⁻¹), porque o random forest fica limitado ao intervalo de valores do treino [p. 15].
- O erro alométrico assumido é de 49,83%, a maior componente da incerteza propagada [p. 9].
- Erro de geolocalização de ~80 m nos mosaicos PALSAR-2, corrigido por corregistro SAR-SAR com Sentinel-1 [p. 8].
- Trabalho de campo no Cerrado é caro e demorado, e os conjuntos de campo existentes não representam toda a extensão do bioma [p. 14].
- O viés espacial do mapa é similar ao de outros mapas de AGB, ou seja, o problema não é exclusivo do método [p. 17].

## 7. O que serve ao projeto e o que não serve

**Serve:**
- O desenho de upscaling em duas etapas (campo → LiDAR → orbital) com validação k-fold e propagação explícita de incerteza — replicável para silvicultura em Goiás [p. 8–9].
- A combinação Landsat 8 + PALSAR-2 L-band com random forest, com ganho de acurácia sobre o uso isolado de cada sensor (R² = 0,89 no conjunto completo vs. 0,84 e 0,79 isolados) [p. 10, p. 16].
- Referências regionais de AGB para o Cerrado goiano (19–104 Mg ha⁻¹ nas parcelas; média de 18,66 Mg ha⁻¹ na bacia) úteis como contraste com povoamentos plantados [p. 6, p. 15].
- O arcabouço de comparação com produtos globais/pantropicais e a checagem contra requisitos da missão BIOMASS servem de critério de acurácia [p. 9, p. 15].

**Não serve:**
- Não trata de silvicultura: a vegetação é cerradão nativo, sem informação de espécie plantada, clone, espaçamento, idade ou rotação [p. 4–5].
- Não estima estoque de carbono: entrega apenas AGB (Mg ha⁻¹), sem fator de conversão para carbono [p. 10].
- O intervalo de AGB é estreito (19–104 Mg ha⁻¹ nas parcelas) e o modelo satura acima de 80 Mg ha⁻¹, faixa em que povoamentos comerciais frequentemente se encontram [p. 6, p. 11, p. 15].
- A resolução de 30 m e a dependência de LiDAR aerotransportado caro limitam a repetição em escala operacional [p. 3, p. 7].

## 8. Frases citáveis

1. "The accuracy assessment showed that our map underestimates high AGB levels and slightly overestimates low AGB levels (Table 4)." [p. 15]
2. "Our study highlights the need to use remote sensing in combination with local field inventories to effectively quantify the spatial variation of AGB in the ecosystems of the Brazilian Savanna." [p. 17]
