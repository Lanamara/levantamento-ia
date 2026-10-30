# Mapa de lacunas

72 artigos com resumo de leitura integral. Marcações por palavras-chave nas seções 1 a 4 de cada resumo (referência, pergunta, área e dados, método): é uma triagem, confira no resumo antes de usar. Artigos sem resumo não entram.

## Combinações centrais do projeto

| Combinação | Artigos lidos | Quais |
|---|---:|---|
| Hiperespectral orbital × Eucalipto | 0 | — |
| Hiperespectral orbital × Biomassa | 3 | ceriani2025, cooper2021, vanguri2024 |
| GEDI × Eucalipto | 3 | fayad2021, fayad2021b, pourrahmati2024 |
| GEDI × Savana/Cerrado | 2 | leite2021, toneli2024 |
| ICESat-2 × Eucalipto | 0 | — |
| GEDI × Seringueira | 0 | — |
| Sentinel-2 × Seringueira | 1 | fu2024 |
| Goiás + Biomassa ou Carbono | 0 | — |

## Sensor × variável estimada

| | Biomassa | Carbono | Altura | Volume | Idade | Espécies | Área plantada | Fragilidade/aptidão |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| GEDI | 7 | 0 | 10 | 4 | 1 | 1 | 0 | 0 |
| ICESat-2 | 2 | 0 | 4 | 0 | 0 | 0 | 1 | 0 |
| LiDAR aéreo | 7 | 2 | 11 | 2 | 3 | 3 | 2 | 0 |
| LiDAR/imagem de drone | 6 | 2 | 4 | 1 | 3 | 3 | 0 | 0 |
| LiDAR terrestre | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| Hiperespectral orbital | 3 | 1 | 2 | 1 | 0 | 6 | 1 | 0 |
| Hiperespectral (outro) | 2 | 0 | 2 | 1 | 1 | 3 | 0 | 0 |
| Sentinel-2 | 13 | 3 | 10 | 3 | 2 | 3 | 2 | 0 |
| Landsat | 8 | 4 | 8 | 4 | 5 | 2 | 5 | 4 |
| MODIS | 2 | 1 | 2 | 3 | 4 | 0 | 0 | 0 |
| Radar (SAR) | 9 | 1 | 7 | 1 | 1 | 0 | 3 | 1 |

## Sensor × tipo de plantio ou vegetação

| | Eucalipto | Pinus | Seringueira | Floresta plantada (geral) | Floresta nativa/tropical | Savana/Cerrado |
|---|---:|---:|---:|---:|---:|---:|
| GEDI | 3 | 0 | 0 | 3 | 2 | 2 |
| ICESat-2 | 0 | 0 | 0 | 0 | 2 | 1 |
| LiDAR aéreo | 4 | 2 | 0 | 3 | 1 | 0 |
| LiDAR/imagem de drone | 4 | 1 | 1 | 6 | 1 | 1 |
| LiDAR terrestre | 0 | 0 | 0 | 0 | 1 | 0 |
| Hiperespectral orbital | 0 | 1 | 1 | 1 | 0 | 0 |
| Hiperespectral (outro) | 2 | 1 | 0 | 3 | 1 | 0 |
| Sentinel-2 | 3 | 2 | 1 | 6 | 1 | 2 |
| Landsat | 9 | 2 | 1 | 11 | 1 | 1 |
| MODIS | 4 | 0 | 0 | 4 | 1 | 2 |
| Radar (SAR) | 3 | 2 | 0 | 3 | 2 | 0 |

## Método × variável estimada

| | Biomassa | Carbono | Altura | Volume | Idade | Espécies | Área plantada | Fragilidade/aptidão |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Random Forest | 15 | 6 | 14 | 12 | 9 | 4 | 4 | 1 |
| XGBoost/boosting | 7 | 2 | 4 | 4 | 4 | 1 | 3 | 0 |
| Redes neurais/deep learning | 4 | 0 | 4 | 1 | 1 | 2 | 1 | 0 |
| SVM | 9 | 4 | 6 | 6 | 3 | 2 | 1 | 0 |
| Regressão | 15 | 3 | 14 | 9 | 6 | 4 | 3 | 1 |
| AHP/multicritério | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 7 |
| Máxima verossimilhança | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |

## Por artigo

| Artigo | Sensores | Variáveis | Plantio | Região | Método | Métrica (trecho do resumo) |
|---|---|---|---|---|---|---|
| [Jamshid Ali (2025)](resumos/ali2025/RELATORIO.md) | Sentinel-2, Landsat | Biomassa, Carbono, Altura | Floresta plantada (geral) | — | Random Forest, XGBoost/boosting, SVM | XGBoost foi o melhor modelo: Sentinel-2 com R² = 0,82, RMSE = 0,73 Mg/ha e MAE = 0,60 Mg/ha; Landsat-9 com R² = 0,80, RMSE = 0,71 Mg/ha e MAE = 0,58 Mg/ha [p. 9]. |
| [Danilo Roberti Alves de Almeida (2021)](resumos/almeida2021/RELATORIO.md) | LiDAR/imagem de drone, Hiperespectral (outro) | Biomassa, Altura, Idade, Espécies | Floresta plantada (geral), Floresta nativa/tropical | Brasil | Regressão | Após remover um outlier, o melhor preditor de AGB foi CH (r² = 0,82; RMSE = 7,62; RMSE relativo = 9,0%), seguido por RVSI (r² = 0,75; RMSE = 8,98; RMSE relativo = 10,1%) [p. 8]. |
| [Lívia Lanzi Aló (2024)](resumos/alo2024/RELATORIO.md) | Landsat | Volume, Idade | Eucalipto, Floresta plantada (geral) | Brasil | Regressão | Melhor modelo: Lasso (`mod_ls`), com RAT_B1_B2, RAT_B2_B4, RAT_B3_B2, INT_0_DM, INT_0_2 e INT_2_MAX [p. 8]. Calibração: RMSE 14,03 m³ ha⁻¹, R² 0,94, AICc 1399,54 [p. 7]; validação: RMSE 12,44 m³ ha⁻¹ e R² 0,95 [p. 7]. |
| [Sanjiwana Arjasakusuma (2026)](resumos/arjasakusuma2026/RELATORIO.md) | LiDAR/imagem de drone | Biomassa | Eucalipto, Floresta plantada (geral) | — | Random Forest, XGBoost/boosting, Redes neurais/deep learning, SVM, Regressão | Melhor *shallow learning*: LightGBM com seleção de variáveis, test R² = 0,63 e RMSE = 43,83 kg/árvore [p. 12]; sem seleção, R² = 0,59 e RMSE = 43,89 kg/árvore [p. 12]. |
| [Fathin Ayuni Azizan (2021)](resumos/azizan2021/RELATORIO.md) | Hiperespectral orbital, Landsat | — | Seringueira, Floresta plantada (geral) | — | — | 55 de 68 documentos usaram dados de campo como referência (mais de 80%); 32 apresentaram Kappa junto à matriz de erro e 12 usaram R² e/ou RMSE; seis não informaram validação [p. 8–9]. |
| [Andrés Baietto (2026)](resumos/baietto2026/RELATORIO.md) | Sentinel-2, MODIS, Radar (SAR) | Carbono, Idade | Eucalipto, Floresta plantada (geral) | — | Random Forest | Desempenho dos modelos herdados: SA com R² = 77,7% e RMSE = 1,1 ano; AGC com R² = 84,7% e RMSE = 8,42 Mg·ha⁻¹ [p. 5]. |
| [Jamis M. Bruening (2023)](resumos/bruening2023/RELATORIO.md) | GEDI, Radar (SAR) | Biomassa, Altura | — | — | Regressão | — |
| [Escleide Gomes Cabral (2019)](resumos/cabral2019/RELATORIO.md) | Landsat | Área plantada | Eucalipto, Floresta plantada (geral), Savana/Cerrado | Goiás, Cerrado, Brasil | Máxima verossimilhança | Acurácia:** coeficiente Kappa de 0,79, classificado como "muito boa" [p. 8, p. 11]. |
| [Derblai Casaroli (2018)](resumos/casaroli2018/RELATORIO.md) | — | Fragilidade/aptidão | — | Brasil | Regressão | Ajuste da estimativa de temperatura: r = 0,81, R² = 0,78 e d de Willmott = 0,86 [p. 4]. |
| [Rodolfo Ceriani (2025)](resumos/ceriani2025/RELATORIO.md) | GEDI, Hiperespectral orbital, Sentinel-2 | Biomassa, Altura, Volume, Espécies | — | — | SVM | SV só com S2: BTR R² = 0,30, RMSE = 98,08 m³ ha⁻¹; só com EMIT: ANN R² = 0,47, RMSE = 93,34 m³ ha⁻¹ [p. 5]. |
| [Fengyun Cheng (2024)](resumos/cheng2024/RELATORIO.md) | Landsat | Biomassa, Carbono, Volume | — | — | Random Forest, SVM, Regressão | Classificação com apenas as 7 bandas espectrais: acurácia global de 0,7165 (RF), 0,6813 (CART), 0,7130 (GBT) e 0,6127 (SVM); Kappa de 0,6147, 0,5672, 0,6068 e 0,4781 [p. 9]. |
| [Sam Cooper (2021)](resumos/cooper2021/RELATORIO.md) | LiDAR aéreo, Hiperespectral orbital, Landsat | Biomassa, Área plantada | — | — | Regressão | Modelos apenas com EnMAP: RMSE de 109,7 Mg/ha (abril), 108,2 Mg/ha (junho) e 97,5 Mg/ha (duas datas, o melhor modelo EnMAP-only; R² = 0,83) [p. 5]. |
| [Gabriele Delogu (2024)](resumos/delogu2024/RELATORIO.md) | Hiperespectral orbital | Espécies | — | — | Redes neurais/deep learning | Validação:** OA média de 0,927 (Cube_R1_M), 0,924 (Cube_R2_M) e 0,923 (Cube_R3_M); a maior acurácia isolada foi 0,973, com Cube_R3_M [p. 12–13]. |
| [Ralph Dubayah (2022)](resumos/dubayah2022/RELATORIO.md) | GEDI | Biomassa | Floresta nativa/tropical | — | Regressão | Comparação com a FAO: **r² = 0,86**, **RMSD = 3,2 Pg**, diferença média (FAO−GEDI) de **−0,63 Pg** [p. 7]; China **27,7 Pg** e Indonésia **23,3 Pg** acima do reportado [p. 8]. |
| [Ibrahim Fayad (2021)](resumos/fayad2021/RELATORIO.md) | GEDI | Altura, Volume | Eucalipto, Floresta plantada (geral) | Brasil | Random Forest, Regressão | Hdom, declividade 0–10%: MH1 com o pior desempenho, RMSE de 2.06 m; os demais modelos com RMSE entre 1.34 m e 1.42 m e R² entre 0.93 e 0.94 [p. 12, p. 14]. |
| [Ibrahim Fayad (2021)](resumos/fayad2021b/RELATORIO.md) | GEDI | Altura, Volume | Eucalipto, Floresta plantada (geral) | Brasil | Random Forest, Regressão | Modelos lineares (eq. 3–8), algoritmo a1: RMSE de 1,70 a 2,31 m e R² de 0,80 a 0,89; o melhor foi a eq. 8 (RMSE = 1,70 m, R² = 0,89) [p. 9]. Terreno (TI, S) não trouxe ganho significativo [p. 9]. |
| [Juan Carlos Fernández-Diaz (2022)](resumos/fernandezdiaz2022/RELATORIO.md) | ICESat-2, LiDAR aéreo | Altura | — | — | — | Erro normalizado de h_canopy: IQR entre −33,5% e 7,0%, mediana em torno de −16,5% e RMSE% de 67,0% [p. 8]. |
| [Debora Da Paz Gomes Brandão Ferraz (2024)](resumos/ferraz2024/RELATORIO.md) | Landsat | — | Eucalipto, Floresta plantada (geral) | Brasil | Random Forest | GEOBIA/LandTrendr: acurácia global 0,988, F-Score 0,975, acurácia do produtor 0,975 e do usuário 0,951; 2 falsos positivos e 1 omissão em 240 pontos [p. 10]. |
| [Micael de Souza Fraga (2018)](resumos/fraga2018/RELATORIO.md) | Radar (SAR) | Fragilidade/aptidão | Eucalipto | Brasil | AHP/multicritério | — |
| [Luciano Cavalcante de Jesus França (2020)](resumos/franca2020/RELATORIO.md) | — | Área plantada, Fragilidade/aptidão | — | Brasil | Random Forest, AHP/multicritério | — |
| [Luciano Cavalcante de Jesus França (2022)](resumos/franca2022/RELATORIO.md) | — | Fragilidade/aptidão | — | Brasil | AHP/multicritério | — |
| [Yanglimin Fu (2024)](resumos/fu2024/RELATORIO.md) | Sentinel-2 | Biomassa | Seringueira, Floresta plantada (geral) | — | Random Forest, SVM | Melhor modelo: RF + variáveis selecionadas por Boruta (G5), com R² = 0,86, RMSE = 15,77 Mg/ha e MAE = 13,18 [p. 13–14]. |
| [Omid Reisi Gahrouei (2026)](resumos/gahrouei2026/RELATORIO.md) | LiDAR aéreo, Hiperespectral orbital, Landsat | Altura, Espécies | Pinus | — | Redes neurais/deep learning | O modelo multimodal PRISMA+ALS obteve OA de 76,5%, Kappa de 67,2% e F1 médio de 76,6% nas 285 parcelas de campo [p. 9]. |
| [Linghan Gao (2022)](resumos/gao2022/RELATORIO.md) | LiDAR aéreo, LiDAR/imagem de drone, Hiperespectral (outro) | Biomassa, Altura, Espécies | Eucalipto, Pinus, Floresta plantada (geral) | — | Random Forest, Regressão | Somente hiperespectral (Tabela 7): R² de treino 0,89 (Chinese fir), 0,84 (pinus), 0,78 (eucalipto) e 0,89 (outras folhosas); R² de validação 0,38, 0,79, 0,03 e 0,13; RMSE 9,67, 20,02, 350,14 e 128,47 t/hm²; MAE 7,43, 14,37, 194,55 e 94,53 t/hm² [p. 10]. |
| [Mathieu Goral (2025)](resumos/goral2025/RELATORIO.md) | Sentinel-2, MODIS | Volume, Idade | Eucalipto, Floresta plantada (geral), Savana/Cerrado | Brasil | Random Forest, XGBoost/boosting | GPP MODIS vs. torre de fluxo: R² = 0,38 e RMSE = 19,65 g C m⁻² 8 dia⁻¹ [p. 8]; rRMSE = 30,64% [p. 14]. Viés sistemático: subestima os picos de produtividade e superestima os períodos de baixo GPP [p. 8], com superestimativa no primeiro ano após colheita [p. 8]. |
| [ELIZA EMANOELLE SILVA GUIMARÃES (2023)](resumos/guimaraes2023/RELATORIO.md) | — | Fragilidade/aptidão | — | Goiás, Brasil | — | — |
| [Rosana Márcia da Costa Silva Herculano (2023)](resumos/herculano2023/RELATORIO.md) | Landsat | Fragilidade/aptidão | — | Goiás | AHP/multicritério | Uso e cobertura: pastagem 1.471,10 km² (38,0%) e agricultura 1.048,38 km² (27,1%), somando 65,10% [p. 8–9]; Cerrado florestal e hidrografia 482,97 km² (12,5%); savânica 575,83 km² (14,9%), 27,40% juntas [p. 9]; solo exposto e área urbana 290,63 km² (7,5%) [p. 9]. Kappa 0,81 e exatidão global de 85,4 |
| [Xiandie Jiang (2023)](resumos/jiang2023/RELATORIO.md) | LiDAR aéreo, Landsat | Carbono, Altura, Idade | Eucalipto | — | Regressão | Sítios típicos (LiDAR):** R²v = 0,84, RMSE 9,53 t·ha⁻¹ e RMSEr 16,93% em Yunxiao; R²v = 0,90, RMSE 7,01 t·ha⁻¹ e RMSEr 14,56% em Gaofeng [p. 6–7]. HME (altura média) e H55 foram os preditores mais importantes [p. 6]. |
| [Fugen Jiang (2025)](resumos/jiang2025/RELATORIO.md) | ICESat-2, Radar (SAR) | Biomassa, Área plantada | Floresta nativa/tropical | — | Random Forest, XGBoost/boosting, SVM | Na otimização de hiperparâmetros do conjunto joint, as PSOs lineares, exponencial e parabólica reduziram o RMSE em 7,7% e 9% frente ao XGBoost com hiperparâmetros padrão; a PSO gaussiana obteve os menores RMSEs e, com α = 5, o mínimo em apenas 12 iterações [p. 9]. |
| [James R. Kellner (2022)](resumos/kellner2022/RELATORIO.md) | GEDI, LiDAR aéreo, Landsat, MODIS | Biomassa | — | — | — | — |
| [Venkata Shashank Konduri (2023)](resumos/konduri2023/RELATORIO.md) | ICESat-2, MODIS | Altura | Savana/Cerrado | Cerrado, Brasil | — | — |
| [Shashika Himandi Gardeye Lamahewage (2025)](resumos/lamahewage2025/RELATORIO.md) | LiDAR aéreo, Sentinel-2 | Biomassa | — | — | Random Forest, SVM, Regressão | RF ajustado (grupo com as 65 variáveis): RMSE 27,19 Mg ha⁻¹, MSE 739,46 (Mg ha⁻¹)², R² 0,41, com 28 variáveis [p. 10, 15]. |
| [Nico Lang (2023)](resumos/lang2023/RELATORIO.md) | GEDI, LiDAR aéreo, Sentinel-2 | Altura | — | — | Redes neurais/deep learning, Regressão | Erro balanceado: aRMSE de 7,3 m e aME de −1,8 m; sem balanceamento, RMSE de 6,0 m, MAE de 4,0 m e viés de 1,3 m [p. 2]. |
| [Rodrigo Vieira Leite (2020)](resumos/leite2020/RELATORIO.md) | LiDAR aéreo | Altura, Volume, Idade | Eucalipto, Floresta plantada (geral) | Brasil | Random Forest, SVM, Regressão | ABA com ANN foi o melhor resultado de volume por talhão: r = 0,95, RMSE = 14,41% e bias = −1,59% [p. 14]. |
| [Rodrigo Vieira Leite (2021)](resumos/leite2021/RELATORIO.md) | GEDI, LiDAR/imagem de drone | — | Savana/Cerrado | Cerrado | Random Forest | Desempenho em validação: WDfuels R² = 0,88 ± 0,029 (RMSE 13,07 Mg ha⁻¹; 40,6%); TFfuels R² = 0,71 ± 0,052 (RMSE 23,01 Mg ha⁻¹; 40,78%) [p. 10]. |
| [Dengqiu Li (2022)](resumos/li2022/RELATORIO.md) | Landsat | Idade | Eucalipto, Floresta plantada (geral) | — | Random Forest | Detecção de mudanças: random localization obteve PA/UA/OA de 89,8%/89,0%/84,9% para cortes e 89,3%/87,0%/84,7% para estabilidade; a segmentação global obteve 35,2%/59,4%/36,8% e 30,7%/60,5%/43,2% [p. 13]. |
| [Hantao Li (2024)](resumos/li2024/RELATORIO.md) | GEDI, Sentinel-2, Landsat, Radar (SAR) | Biomassa, Altura | — | — | Random Forest, Regressão | Treino:** R² = 0,95 e RMSE = 18,46 [p. 8]. |
| [Yiman Li (2024)](resumos/li2024b/RELATORIO.md) | Landsat | — | Eucalipto, Floresta plantada (geral) | — | — | Acurácia global da identificação de eucalipto: 90,08% no resumo [p. 1] e OA = 90,87% na avaliação (PA 90,75%, UA 89,32%, matriz com 28.613 pixels) [p. 12]. Os dois valores diferem no próprio artigo. |
| [João Victor do Nascimento Lima (2026)](resumos/lima2026/RELATORIO.md) | Landsat | Altura, Volume, Idade | Eucalipto, Floresta plantada (geral) | Brasil | Random Forest, XGBoost/boosting, Redes neurais/deep learning, SVM | Clutter tradicional, área basal (médias entre folds): RMSE% = 6,33; bias = 0,08 m² ha⁻¹; r = 0,96; R² = 0,91 [p. 7]. |
| [Karen Carrilho da Silva Lira (2022)](resumos/lira2022/RELATORIO.md) | — | Fragilidade/aptidão | — | Brasil | AHP/multicritério | — |
| [Aobo Liu (2021)](resumos/liu2021/RELATORIO.md) | GEDI, ICESat-2, LiDAR aéreo | Altura | — | — | Random Forest, Regressão | Terreno, latitudes médias/baixas:** RMSE 2,24 m (ICESat-2) e 4,03 m (GEDI); MAE 0,91 m e 1,80 m [p. 7]. |
| [Isáira Leite e Lopes (2025)](resumos/lopes2025/RELATORIO.md) | — | Biomassa | Eucalipto, Pinus | Brasil | Regressão | LMM de BEF: FI de 0,81 e 0,80; RMSE de 0,059 e 0,064; RMSE% de 5,035 e 5,277; MAE de 0,041 e 0,051; AIC de −4591,26 e −379,44 (Eucalyptus e Pinus) [p. 8]. |
| [Selma Regina Maggiotto (2014)](resumos/maggiotto2014/RELATORIO.md) | — | Biomassa, Carbono, Idade | Seringueira, Floresta plantada (geral) | Brasil | — | — |
| [Vítězslav Moudrý (2024)](resumos/moudry2024/RELATORIO.md) | GEDI, LiDAR aéreo | Altura | — | — | — | ASG+TDX foi a combinação mais acurada (RMSE de 6,3 a 11,1 m), mas ASG removeu 75%–80% das observações e 60%–65% das de alta qualidade; QF+TDX teve RMSE de 11,2 a 13,2 m, removeu apenas 10%–30% do total e menos de 1% das de alta qualidade [p. 12, p. 14]. |
| [Guilherme Resende Oliveira (2021)](resumos/oliveira2021/RELATORIO.md) | Landsat | Área plantada | Floresta plantada (geral) | Goiás, Brasil | Random Forest | Desmatamento de 2013 a 2015: 195.369 ha, contra variação de 37.544 ha (MapBiomas) e 16.067 ha (PEVS) de área plantada; correlação baixa (r² = −0,023 e 0,032) [p. 7]. |
| [Luiz Gustavo de Souza Paula (2022)](resumos/paula2022/RELATORIO.md) | Landsat | Fragilidade/aptidão | Floresta plantada (geral) | Brasil | AHP/multicritério | — |
| [Valeria La Pegna (2026)](resumos/pegna2026/RELATORIO.md) | Hiperespectral orbital | — | — | — | — | Correlação global entre reflectâncias médias dos dois sensores com R² = 0.981 [p. 9]; exceções Madrid e Sevilla, com RMSE de 0.238 e 0.263 para solo exposto [p. 9]. |
| [Carla Talita Pertille (2025)](resumos/pertille2025/RELATORIO.md) | LiDAR aéreo, LiDAR/imagem de drone | Biomassa, Carbono, Altura, Volume, Idade | Eucalipto, Floresta plantada (geral) | Brasil | Random Forest, SVM, Regressão | Ajuste do modelo de campo (Schumacher–Hall com *dummy* de genótipo): total R²aj 0,960 e Syx 10,64%; tronco 0,961 e 10,31%; copa 0,808 e 33,72% [p. 7]. |
| [Manizheh Rajab Pourrahmati (2024)](resumos/pourrahmati2024/RELATORIO.md) | GEDI, MODIS | Volume, Idade | Eucalipto, Floresta plantada (geral) | Brasil | Random Forest, XGBoost/boosting, Regressão | MODIS vs. torre de fluxo: R² = 0,38 e RMSE = 19,65 gC m⁻² 8 dia⁻¹; subestimativa nos picos de produtividade e superestimativa no início do ciclo [p. 8]; rRMSE = 30,64% [p. 14]. |
| [Manizheh Rajab Pourrahmati (2025)](resumos/pourrahmati2025/RELATORIO.md) | MODIS | Volume, Idade | Eucalipto, Floresta plantada (geral) | Brasil | Random Forest, XGBoost/boosting | GPP MODIS vs. torre: R² = 0,38 e RMSE = 19,65 g C m⁻² 8 dia⁻¹; subestimação nos picos de produtividade e superestimação nos períodos de baixa produtividade [p. 1] [p. 8]. |
| [Aliny Aparecida dos Reis (2018)](resumos/reis2018/RELATORIO.md) | Landsat | Altura, Volume | Eucalipto | Brasil | Random Forest, SVM | MLR: área basal explicada apenas por ND54, R²aj = 0,81 e erro-padrão residual de 5,76%; volume por NDVI e TM1, R²aj = 0,37 e erro de 13,08% [p. 7]. |
| [Fabiana Piontekowski Ribeiro (2024)](resumos/ribeiro2024/RELATORIO.md) | — | Carbono, Altura, Idade | Eucalipto, Floresta plantada (geral), Savana/Cerrado | Cerrado, Brasil | — | Modelo 1 (Schumacher–Hall adaptado): r = 0.99, RMSE% = 9.65, AIC = 258; modelo 2: r = 0.98, RMSE% = 12.86, AIC = 279; modelo 3: r = 0.98, RMSE% = 12.83, AIC = 278 [p. 7]. |
| [Lizza Adrielle Nascimento Santos (2020)](resumos/santos2020/RELATORIO.md) | Landsat | Área plantada, Fragilidade/aptidão | — | — | AHP/multicritério | — |
| [Raiany Cristina Ribeiro Santos (2023)](resumos/santos2023/RELATORIO.md) | — | Fragilidade/aptidão | Savana/Cerrado | Goiás, Cerrado, Brasil | — | — |
| [Flávio José Simioni (2017)](resumos/simioni2017/RELATORIO.md) | — | — | Floresta plantada (geral) | Brasil | — | — |
| [Cleonice Batista Regis Soares (2021)](resumos/soares2021/RELATORIO.md) | Landsat | Área plantada, Fragilidade/aptidão | — | Goiás | — | — |
| [Roneide dos Santos Sousa (2024)](resumos/sousa2024/RELATORIO.md) | — | Fragilidade/aptidão | — | Brasil | — | — |
| [Hongjian Tan (2025)](resumos/tan2025/RELATORIO.md) | LiDAR/imagem de drone | Biomassa | Seringueira, Floresta plantada (geral) | — | XGBoost/boosting, Redes neurais/deep learning, Regressão | Sem seleção de variáveis, o melhor modelo foi CatBoost com VIs+TFs: R² = 0,71, RMSE = 14,60 t/ha, MAE = 11,54 t/ha [p. 11; tabela p. 12]. |
| [Iyán Teijido-Murias (2025)](resumos/teijidomurias2025/RELATORIO.md) | Sentinel-2, Radar (SAR) | Biomassa, Altura, Volume | Eucalipto, Pinus, Floresta plantada (geral) | — | Random Forest, Regressão | Piores ajustes: N, com R² de 0,12 a 0,27 e RMSE% de 51,5% a 68,6%; em seguida H0, com R² de 0,33 a 0,38 e RMSE% de 22,9% a 30,4% [p. 7]. |
| [Thiara Messias de Almeida Teixeira (2024)](resumos/teixeira2024/RELATORIO.md) | — | Fragilidade/aptidão | Floresta plantada (geral), Savana/Cerrado | Cerrado | — | — |
| [Larissa Pereira Ribeiro Teodoro (2023)](resumos/teodoro2023/RELATORIO.md) | Hiperespectral (outro) | Volume, Espécies | Eucalipto, Floresta plantada (geral) | Brasil | Random Forest, Regressão | — |
| [Nikos Theofanous (2021)](resumos/theofanous2021/RELATORIO.md) | Sentinel-2, Radar (SAR) | Biomassa, Altura | Floresta plantada (geral) | — | Random Forest | Melhor modelo: Sentinel-2 de agosto, R² = 0,52 e RMSE = 11,26 Mg ha⁻¹ [p. 9]. Julho e setembro praticamente empatados: R² = 0,37 com RMSE = 12,87 e 12,99 Mg ha⁻¹, respectivamente [p. 9]. |
| [Lei Tian (2023)](resumos/tian2023/RELATORIO.md) | GEDI, ICESat-2, LiDAR aéreo, LiDAR terrestre, Sentinel-2, Landsat, MODIS, Radar (SAR) | Biomassa, Altura | Floresta nativa/tropical | — | — | Combinação de dados L- e P-band teve maior acurácia do que banda única, por ser sensível a biomassa baixa (L) e alta (P) [p. 8]. |
| [Xin Li Tian (2024)](resumos/tian2024/RELATORIO.md) | Sentinel-2, Landsat, Radar (SAR) | Biomassa | Pinus | — | Random Forest, Redes neurais/deep learning | Melhor resultado geral: CNN-LSTM com todas as fontes (SAR + óptico), R² = 0.7405 e RMSE = 26.4314 Mg/ha [p. 15]. |
| [Carlos Augusto Zangrando Toneli (2024)](resumos/toneli2024/RELATORIO.md) | GEDI, Sentinel-2 | Biomassa, Altura | Savana/Cerrado | Cerrado, Brasil | — | Equação ajustada (de Bispo et al., 2020) com R² de 0,89, RMSE de 8,12 Mg·ha⁻¹ e bias de 0,43 Mg·ha⁻¹; alturas LIDAR de 1,7 a 38 m e biomassa aérea de 19 a 104 Mg·ha⁻¹ [p. 6]. |
| [Michele Torresani (2025)](resumos/torresani2025/RELATORIO.md) | LiDAR aéreo, Hiperespectral orbital | Espécies | — | — | Regressão | Bandas individuais: R2 máximo de 0,38 com a abordagem weighted CC >70%; correlações maiores no NIR, intermediárias no VIS e baixas ou negativas no SWIR [p. 8]. |
| [Marco Bruno Xavier Valadão (2020)](resumos/valadao2020/RELATORIO.md) | — | Biomassa, Altura, Volume, Idade | Eucalipto, Savana/Cerrado | Cerrado, Brasil | — | — |
| [Elia Vangi (2021)](resumos/vangi2021/RELATORIO.md) | Hiperespectral orbital, Sentinel-2 | Espécies | — | — | — | — |
| [Rajesh Vanguri (2024)](resumos/vanguri2024/RELATORIO.md) | Hiperespectral orbital, Sentinel-2 | Biomassa, Carbono, Espécies | — | — | Random Forest, XGBoost/boosting, SVM | Acurácia global entre 85 % e 93 % para o mapeamento de espécies [p. 1]; F1 global de 0,91 para o mapa combinado [p. 12]. |
| [Dejun Wang (2025)](resumos/wang2025/RELATORIO.md) | Sentinel-2, Radar (SAR) | Biomassa, Altura, Área plantada | — | — | XGBoost/boosting, Regressão | Modelo final (TS1S2D, 13 atributos): R² = 0,71 e RMSE = 18,11 Mg/ha no conjunto de teste [p. 10]; na validação cruzada, R² = 0,60 e RMSE = 21,28 Mg/ha [p. 10]. |
| [Yi Zhang (2022)](resumos/zhang2022/RELATORIO.md) | LiDAR/imagem de drone, Landsat | Biomassa, Carbono, Altura, Idade, Espécies | Eucalipto, Floresta plantada (geral) | — | Random Forest | Escala SP com idade de inventário: R² de 0,80 a 0,93 para DBH, H e ACS [p. 9]; considerar o desbaste elevou o R² de ACS, DBH e H em 0,09, 0,06 e 0,07 e reduziu o RRMSE em 8,54%, 6,75% e 4,2% [p. 9]. |
| [Linjing Zhang (2024)](resumos/zhang2024/RELATORIO.md) | LiDAR aéreo, Sentinel-2, Radar (SAR) | Biomassa, Altura, Área plantada | — | — | Random Forest, XGBoost/boosting, Redes neurais/deep learning, Regressão | S1 sozinho: R² 0,24–0,45 e RMSE 47,36–56,51 Mg/ha; S2 sozinho: R² 0,62–0,75 e RMSE 30,08–38,83 Mg/ha; S1+S2: R² 0,65–0,78 e RMSE 28,68–35,92 Mg/ha [p. 1]. |
