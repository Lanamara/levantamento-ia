# RELATORIO — Aló et al. (2024)

## 1. Referência

ALÓ, Lívia Lanzi; LE MAIRE, Guerric; THIERSCH, Cláudio Roberto; MOTA, Thiago Santos; PINHEIRO, Rafael Costa; PASSOS, José Raimundo de Souza. **Mapping stem volume in fast-growing eucalypt plantations: integrating spectral, textural, and temporal remote sensing information with forest inventories and spatial models.** *Annals of Forest Science*, v. 81, artigo 43, 2024. DOI: 10.1186/s13595-024-01255-6. Recebido em 22/12/2023, aceito em 29/08/2024 [p. 14].

## 2. Pergunta do estudo

Testar se textura de imagem de alta resolução e informação histórica de série temporal de NDVI (desde o plantio), usadas como covariáveis em modelos geoestatísticos (KED e GAM), melhoram a predição de volume de madeira de plantações de *Eucalyptus* sp. [p. 1, p. 3].

## 3. Área e dados

- **Local:** talhões de *Eucalyptus* sp. no sul do estado de Mato Grosso do Sul, próximo à cidade de Ribas do Rio Pardo; altitude média de 374 m; clima tropical Aw, precipitação média de 1241 mm e temperatura média de 24,2 °C [p. 3].
- **Período:** inventário florestal em agosto de 2018; todos os talhões com menos de 4 anos nessa data [p. 3]. Série temporal Landsat de janeiro de 2000 a agosto de 2018 [p. 4]. Imagem SPOT-6 de agosto de 2018 [p. 4].
- **Amostras:** 211 parcelas circulares de 500 m², distribuídas sistematicamente em malha, uma parcela a cada ~722 m; área total de 9431,21 ha e 11 clones [p. 3]. Volume por parcela: mínimo 1,16, máximo 249,84, média 59,79 m³ ha⁻¹, desvio padrão 58,85 e CV 0,98 [p. 3].
- **Sensores/fontes:** SPOT-6 (4 bandas espectrais a 6 m + pancromática a 1,5 m, pansharpenizada para 1,5 m; reflectância de topo de atmosfera) [p. 4]; série Landsat-5 TM, Landsat-7 ETM+ e Landsat-8 OLI a 30 m, reflectância de superfície (USGS, Collection 1 Tier 1, via Google Earth Engine), intercalibrados segundo Roy et al. (2016) [p. 4]. Bandas SPOT e Landsat reamostradas para 7,5 m [p. 4].

## 4. Método

1. **Extração de variáveis:** 86 variáveis a partir de SPOT-6 e Landsat – reflectâncias das bandas, 12 razões simples entre bandas, NDVI, SAVI e ARVI, índices de textura GLCM (contraste, correlação, energia e homogeneidade, em janela 3×3 pixels e quatro direções, com média omnidirecional) e produtos/razões entre reflectância e textura; integrais da série temporal de NDVI (suavizada por spline cúbica) entre datas de plantio, 1 e 2 anos e data do inventário/máximo/mínimo [p. 4-5, Tabela 2].
2. **Modelo linear:** regressão múltipla com seleção de variáveis por oito métodos (forward, backward, sequential replacement, sPLS, Spike and Slab Lasso, Ridge, Lasso, Elastic Net), separação 80% treino / 20% validação, comparados por RMSE, R² ajustado e AICc [p. 4-6].
3. **Modelos espaciais:** KED usando as variáveis do melhor modelo linear como *drift* externo, com variograma ajustado por mínimos quadrados ponderados (modelos exponencial, esférico, Matérn, gaussiano e Matérn–Stein, escolhido pelo menor RMSE) [p. 6-7]; GAM com spline de regressão penalizado sobre longitude/latitude (pacote `mgcv`, suavização por GCV) [p. 6].
4. **Avaliação:** validação cruzada cinco vezes (fivefold) para linear, KED e GAM, com RMSE, R² ajustado e partição da variância entre variáveis auxiliares e componente espacial [p. 6-7]. Mapas aplicados em escala de pixel de 7,5 m [p. 8].

## 5. Resultados principais

- Idade do talhão correlacionada com volume (coeficiente de 0,83); integrais de NDVI do Landsat (INT_0_DM, INT_0_DS e INT_1_DM) entre 0,86 e 0,89; bandas SPOT B1, B2 e B3 com relações negativas de −0,74 a −0,77 [p. 7].
- NDVI e SAVI com correlação de R = 0,49 e R = 0,47, respectivamente [p. 9]; INT_0_DM com R = 0,89 com o volume [p. 10].
- Razão RAT_B3_B2 com correlação direta de 0,52; textura MUL_B1_HOM_B1 com −0,47 e RAT_B2_CON_B2 com 0,19 [p. 7].
- Modelos finais com 3 a 7 variáveis; nenhum selecionou NDVI, SAVI ou ARVI [p. 7].
- Melhor modelo linear: Lasso (`mod_ls`), com RMSE de 14,03 m³ ha⁻¹, R² de 0,94 e AIC de 1399,54 na calibração [p. 7]; na validação, RMSE de 12,44 m³ ha⁻¹ e R² de 0,95 [p. 7].
- As seis variáveis do `mod_ls`: RAT_B1_B2, RAT_B2_B4, RAT_B3_B2, INT_0_DM, INT_0_2 e INT_2_MAX [p. 8, Tabela 4].
- KED: variograma Matérn–Stein com alcance de 2750 m, pepita de 92,5 m³ ha⁻¹ e patamar de 179 m³ ha⁻¹; na validação, R² de 0,96 e RMSE de 10,62 m³ ha⁻¹ [p. 7]; variáveis auxiliares explicaram ~94% da variância e o termo de correlação espacial 5% [p. 8].
- GAM: R² de 0,96 e RMSE de 10,56 m³ ha⁻¹ na validação; variáveis auxiliares ~98% da variância e termo espacial 1,2% [p. 8].
- Comparação externa: Marsden et al. obtiveram RMSE de 24 m³ ha⁻¹ para plantações de *Eucalyptus*, cerca do dobro do resultado deste estudo [p. 11].
- Biomassa e estoque de carbono: **não informado** (o artigo trata apenas de volume de fuste).

## 6. Limitações reconhecidas pelos autores

- A análise de incerteza é preliminar: "further work is required to improve the analysis of the uncertainty associated with model predictions, and its propagation across scales" [p. 10-11].
- A textura teve apenas correlação moderada com o volume e essas relações tendem a ser específicas do local ("site-specific") [p. 9-10].
- Os modelos foram criados para plantações de eucalipto em contexto pedoclimático específico e dependem de calibração local com dados de inventário; a aplicabilidade a outras localidades, sobretudo em talhões com danos e heterogeneidade local de volume, ainda precisa ser confirmada [p. 11].
- A idade do talhão não entrou na seleção de variáveis por sua forte colinearidade com as integrais de NDVI, e substituir as integrais pela idade reduziu a acurácia do modelo [p. 10, p. 11].
- KED exigiu mais recursos computacionais e a escolha de um modelo de variograma [p. 10].
- Os dados não podem ser disponibilizados publicamente por questões de propriedade [p. 14].

## 7. O que serve ao projeto e o que não serve

**Serve:**
1. Estrutura metodológica replicável para silvicultura: razões entre bandas + integrais de NDVI desde o plantio + textura GLCM como covariáveis, com seleção de variáveis e validação cruzada fivefold [p. 4-7].
2. Evidência quantitativa de que integrais temporais de NDVI são o preditor mais forte (R = 0,86-0,89) e de que índices espectrais instantâneos saturam após o fechamento do dossel [p. 7, p. 9] — argumento direto para o uso de séries temporais no Cerrado goiano.
3. Referência de desempenho para comparação: R² de 0,95 e RMSE de 12,44 m³ ha⁻¹ no linear; R² de 0,96 e RMSE de 10,56-10,62 m³ ha⁻¹ com KED/GAM [p. 7-8].
4. Desenho amostral (211 parcelas de 500 m², grade ~722 m, talhões de 1,5 a 4,5 anos) como parâmetro para dimensionar inventário em Goiás [p. 3].

**Não serve:**
1. Não estima biomassa nem estoque de carbono: só volume de fuste, sem fator de expansão ou densidade da madeira [p. 3, p. 11].
2. Área de estudo é Mato Grosso do Sul, não Goiás; contexto pedoclimático distinto do Cerrado goiano e os autores alertam sobre a necessidade de calibração local [p. 3, p. 11].
3. Sensores limitados a SPOT-6 e Landsat óptico (30 m / 7,5 m), sem radar, LiDAR ou Sentinel-2 — o que contraria a proposta "multissensorial" do projeto [p. 4; p. 11].
4. Aplicável a plantios clonais de eucalipto de rotação curta; não cobre vegetação nativa nem outras espécies/idades [p. 3, p. 11].

## 8. Duas frases citáveis (literais)

> "The spatial prediction of the stem volume was slightly improved with KED or GAM, compared to the linear model alone." [p. 10]

> "These spatial models were applied in the forest area, distinguishing regions with different stand ages and estimating the within-stand variability of wood volume." [p. 11]
