# RELATÓRIO — Jamshid Ali (2025)

## 1. Referência

Ali, J.; Haoran, W.; Mehmood, K.; Hussain, W.; Iftikhar, F.; Shahzad, F.; Hussain, K.; Qun, Y.; Zhongkui, J. (2025). *Remote sensing and integration of machine learning algorithms for above-ground biomass estimation in Larix principis-rupprechtii Mayr plantations: a case study using Sentinel-2 and Landsat-9 data in northern China.* Frontiers in Environmental Science, 13:1577298. DOI: 10.3389/fenvs.2025.1577298. Publicado em 02/04/2025 [p. 1]. O `TEXTO.txt` corresponde ao artigo do DOI indicado e está completo (15 páginas, incluindo referências).

## 2. Pergunta do estudo

Qual dos sensores (Sentinel-2 ou Landsat-9) e qual dos algoritmos (XGBoost, SVM ou RF) estima com maior acurácia a AGB de plantios de *Larix principis-rupprechtii*, e quais bandas espectrais e índices de vegetação mais contribuem para essa estimativa [p. 3].

## 3. Área e dados

- Local: Saihanba Mechanical Forest Farm, Chengde, província de Hebei, norte da China (41°22′–42°58′N, 116°53′–118°3′; o texto grafa "W" para a longitude) [p. 3].
- Clima/altitude: zona de monção continental temperada quente; 1.010–1.940 m; temperatura média anual −1,2 °C; precipitação anual 452,2 mm; evaporação 1.388 mm [p. 3].
- Período do inventário de campo: agosto de 2023 [p. 4]; data das imagens de satélite: não informado.
- Sensores: Sentinel-2A (bandas 2, 3, 4 e 8; 10 m) e Landsat-9 OLI (bandas 2, 3, 4 e 5; 30 m), processados no Google Earth Engine; imagens com cobertura de nuvens > 5% descartadas [p. 4–5].
- Amostras: 45 parcelas em plantio de 50 anos de *L. principis-rupprechtii*; divisão 70% treino / 30% validação [p. 4–5].
- Estatísticas de campo: DBH médio 25,43 cm (22,61–29,05); altura média 19,42 m (17,10–21,64); densidade 677 árvores/ha (450–1.000); AGB média 7,57 Mg/ha (5,07–10,29; DP 1,44) [p. 7].

## 4. Método

- Inventário florestal com 45 parcelas, coordenadas por RTK, DBH a 1,3 m, altura por relascópio e carbono orgânico do solo (0–20 cm); AGB por equações alométricas e carbono assumindo 50% da biomassa [p. 4].
- Extração de preditores por buffers circulares de 10 m (Sentinel-2) e 30 m (Landsat-9) em torno do centro de cada parcela, usando a média dos pixels [p. 5].
- Seleção de variáveis por correlação de Pearson e VIF, removendo preditores com |r| ≥ 0,8 e VIF ≥ 10 [p. 6].
- Modelagem com XGBoost, SVM (SVR) e Random Forest, ajustados por grid search (ex.: XGBoost com 75 estimadores, profundidade 9, learning rate 0,1; SVM kernel rbf, C = 4, gamma = 1,5; RF com 350 árvores) e avaliação por r, R², RMSE, RMAE, MAE e ME [p. 6–7].

## 5. Resultados principais

- Sentinel-2 superou Landsat-9 em todas as correlações: coeficientes de 0,32–0,58 no Sentinel-2 e de 0,30–0,56 no Landsat-9 [p. 7–8].
- Sentinel-2: TNDVI e NDI45 com r = 0,58; NDVI 0,56; GNDVI 0,52; banda NIR 0,54; WDVI 0,32 (mais fraca) [p. 7].
- Landsat-9: TNDVI 0,56; NDI45 0,55; NDVI 0,53; B5 0,50; B4 0,42; B2 0,30 e B3 0,35; WDVI 0,30 [p. 8].
- XGBoost foi o melhor modelo: Sentinel-2 com R² = 0,82, RMSE = 0,73 Mg/ha e MAE = 0,60 Mg/ha; Landsat-9 com R² = 0,80, RMSE = 0,71 Mg/ha e MAE = 0,58 Mg/ha [p. 9].
- SVM: Sentinel-2 com R² = 0,79, RMSE = 0,73 Mg/ha, MAE = 0,63 Mg/ha; Landsat-9 com R² = 0,76, RMSE = 0,80 Mg/ha, MAE = 0,66 Mg/ha [p. 9].
- Random Forest foi o mais fraco: Sentinel-2 com R² = 0,74, RMSE = 0,93 Mg/ha, MAE = 0,76 Mg/ha; Landsat-9 com R² = 0,72, RMSE = 0,88 Mg/ha, MAE = 0,74 Mg/ha [p. 9].
- Importância de variáveis: GNDVI foi o preditor mais importante no Sentinel-2 (0,183 no XGBoost) e NDI45 no Landsat-9; WDVI 0,026 (Sentinel-2) e 0,045 (Landsat-9); PSSRa 0,030 e 0,045 [p. 8].
- Mapas de AGB: Sentinel-2 com valores de 5,39–9,15 Mg/ha; as previsões do RF variaram de 4,71 a 10,15 Mg/ha, com mais ruído espacial [p. 9, p. 11].
- Inconsistência interna: a discussão cita RMSE de 0,69 Mg/ha para XGBoost com Sentinel-2 [p. 12], valor diferente dos 0,73 Mg/ha da seção de resultados [p. 9].

## 6. Limitações que os próprios autores reconhecem

- Permanecem pequenos desalinhamentos espaciais entre a grade de pixels e os limites das parcelas, devidos a distorção geométrica, resolução do sensor e variabilidade do terreno; os buffers adotados reduzem, mas não eliminam, essa incerteza residual [p. 5–6].
- O Landsat-9 tem resolução espacial e espectral inferior, o que limita a captura de variações finas da estrutura da vegetação, sobretudo para o Random Forest [p. 9].
- Não há seção formal de limitações; as recomendações indicam necessidade de integrar LiDAR e imageamento hiperespectral, análises multitemporais (variações sazonais e fenológicas) e métodos de ensemble [p. 12].

## 7. O que serve ao projeto e o que não serve

- Serve: o desenho comparativo Sentinel-2 (10 m) vs. Landsat-9 (30 m) com validação de campo e métricas explícitas (R², RMSE, MAE, RMAE) é diretamente replicável em plantios de Goiás [p. 5, p. 9].
- Serve: a hierarquia de modelos (XGBoost > SVM > RF) e o uso de índices de vegetação (TNDVI, NDI45, NDVI, GNDVI) como preditores fornecem hipóteses de trabalho e baseline de acurácia para silvicultura tropical/subtropical [p. 7–9].
- Serve parcialmente: a conversão AGB→carbono por fator fixo de 0,5 [p. 4] é simplificada e precisaria de fatores específicos para as espécies e condições de Goiás.
- Não serve: a área de estudo (plantio homogêneo de 50 anos, clima temperado continental, 45 parcelas, AGB média de apenas 7,57 Mg/ha) não representa a heterogeneidade, a produtividade nem a estrutura etária da silvicultura goiana; não há validação independente nem transferência espacial dos modelos [p. 3, p. 7].

## 8. Frases citáveis (literais)

- "Even though Landsat-9 has lower spatial and spectral resolution than Sentinel-2, both datasets helped estimate biomass, but Sentinel-2 consistently did better than Landsat-9." [p. 9]
- "Future research should further integrate complementary datasets, such as LiDAR and hyperspectral imagery, to improve biomass prediction accuracy." [p. 12]
