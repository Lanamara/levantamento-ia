# RELATÓRIO — Yanglimin Fu (2024)

## 1. Referência

- Fu, Y.; Tan, H.; Kou, W.; Xu, W.; Wang, H.; Lu, N. (2024). *Estimation of Rubber Plantation Biomass Based on Variable Optimization from Sentinel-2 Remote Sensing Imagery*. **Forests**, 15, 900. DOI: 10.3390/f15060900.
- O `TEXTO.txt` está íntegro (20 páginas, incluindo referências) e corresponde ao DOI informado.

## 2. Pergunta do estudo

Qual combinação de variáveis derivadas do Sentinel-2 — bandas espectrais, índices de vegetação, texturas GLCM, NDTI e componentes principais — e qual algoritmo de machine learning (RF, XGBR, KNNR, SVR), após seleção de variáveis, estimam com maior acurácia a AGB de plantações de seringueira [p. 3]?

## 3. Área e dados

- Local: plantações de seringueira no condado de Jinghong, prefeitura autônoma de Xishuangbanna, província de Yunnan, China [p. 4].
- Amostras: 64 parcelas de 20 × 25 m², sendo 24 de campanhas de 2021 e 40 de 2023 [p. 4].
- Sensores/fontes: Sentinel-2 Level 2A (Harmonized Sentinel-2 MSI, refletância de superfície, correção Sen2Cor) via Google Earth Engine; composição mediana a 20 m, cobertura de nuvem < 20% [p. 5–6].
- Período das imagens: 1º de março a 1º de junho de 2021 e de 2023, para coincidir com os levantamentos de campo [p. 5].
- Variáveis: 170 no total — 9 bandas espectrais, 7 índices de vegetação, 153 parâmetros de textura e 1 índice de textura [p. 14].
- AGB de referência: equação alométrica (AE) de Tang et al., com R² > 0,99, aplicada a DBH e H medidos em campo, pois o corte de árvores não era viável [p. 5].

## 4. Método

- Extração de bandas, 7 VIs (NDVI, EVI, RVI, NDWI, LSWI, NDRE, MSAVI) e 17 métricas de textura GLCM por banda, mais NDTI construído com CORRG e SAVGRE1 [p. 6–7].
- Redução/seleção de variáveis por quatro vias: correlação de Spearman, PCA sobre texturas (variância explicada de 98%, 10 componentes), ranking de importância por Random Forest e seleção Boruta [p. 7–8].
- Comparação de 11 combinações multivariadas (V1–V11) e 5 grupos por importância (G1–G5, sendo G5 o conjunto Boruta + NDTI) [p. 11, 13].
- Validação: 80% treino / 20% teste por amostragem estratificada aleatória, com reamostragem repetida e validação cruzada de 10 folds; métricas R², RMSE e MAE; hiperparâmetros fixados (RF e XGBR com 500 árvores, seed 54; KNN com k = 5; SVR com kernel poly, C = 2, epsilon = 0,01) [p. 7–8].

## 5. Resultados principais

- Melhor modelo: RF + variáveis selecionadas por Boruta (G5), com R² = 0,86, RMSE = 15,77 Mg/ha e MAE = 13,18 [p. 13–14].
- No mesmo grupo G5: XGBR com R² = 0,83, RMSE = 16,95 e MAE = 13,87; KNNR com R² = 0,66, RMSE = 24,10 e MAE = 20,56; SVR com R² = 0,35, RMSE = 33,38 e MAE = 24,31 [p. 13].
- Modelos univariados: GLCM com R² = 0,74 (RMSE = 21,09; MAE = 15,73); PCAGLCM com R² = 0,58 (RMSE = 26,82; MAE = 21,81); bandas espectrais com R² = 0,56 (RMSE = 27,67; MAE = 22,17); VIs com R² = 0,25 (RMSE = 36,06; MAE = 29,20); NDTI com R² = 0,18 (RMSE = 37,51; MAE = 25,08) [p. 11]. Observação: o texto afirma R² = 0,55 para bandas espectrais, valor divergente do 0,56 da Tabela 5 [p. 11].
- Melhor combinação multivariada sem seleção: KNNR em V8 (NDTI + PCAGLCM + bandas), com R² = 0,73, RMSE = 21,48 t/ha e MAE = 17,25; RF e XGBR atingiram R² = 0,70 em V4 (PCAGLCM + VIs) [p. 11].
- Correlações com AGB: RE1 com r = 0,42; NDWI com r = 0,28 e NDRE com r = −0,28; PC5GLCM e PC8GLCM com r = 0,50 [p. 9–10].
- Entre bandas: NIR vs. RE3 com r = 0,98 e NIR vs. vermelho com r = −0,58 [p. 9].
- Ganho da seleção: de R² = 0,67 (G4, RF) para R² = 0,86 (G5, RF) [p. 13].

## 6. Limitações que os próprios autores reconhecem

- Não avaliaram a combinação de informação espectral e de textura com dados PALSAR (HH e HV), cujo efeito sobre a acurácia permanece incerto [p. 15].
- Fatores de terreno (elevação, aspecto, declividade) e idade do povoamento não foram incluídos, e devem ser testados em trabalhos futuros [p. 15].
- Tamanho amostral limitado (64 parcelas), com 24 de 2021 e 40 de 2023 agrupadas por diferenças e desequilíbrio entre amostras; o artigo cita que ao menos 100 pontos seriam necessários para um modelo de biomassa de espécie única [p. 15].
- Falta teste independente dos efeitos de variedade e idade, apesar de o modelo abranger diferentes variedades e anos de plantio [p. 15].

## 7. O que serve ao projeto e o que não serve

- Serve: o desenho de otimização de variáveis (Spearman + PCA + importância + Boruta) como protocolo replicável para reduzir um conjunto grande de preditores Sentinel-2 antes de modelar AGB, com ganho documentado de R² 0,67 → 0,86 [p. 13–14].
- Serve: a evidência de que texturas GLCM carregam mais informação sobre AGB do que VIs isolados (R² = 0,74 vs. 0,25), útil contra a saturação espectral em dosséis densos [p. 11, 14].
- Serve com cautela: RF como baseline e o esquema 80/20 com validação cruzada de 10 folds; porém 64 parcelas são insuficientes para generalizar ao cerrado/goiano, e os autores recomendam ≥ 100 pontos [p. 15].
- Não serve: os valores absolutos de AGB e a equação alométrica de seringueira em Xishuangbanna, o recorte tropical úmido e a fenologia decídua da seringueira — nada disso é transferível à silvicultura de Goiás; o artigo também não usa dados multissensoriais (SAR/LiDAR), foco do projeto [p. 4–5, 15].

## 8. Frases citáveis (literais)

- "This study extracted a total of 170 variables from Sentinel-2 satellite imagery, including 9 spectral bands, 7 vegetation indices, 153 texture parameters, and 1 texture index using the GEE platform." [p. 14]
- "Even though a repeated resampling method of 10-fold cross-validation was employed to enhance the model's robustness, the limited sample size (64 samples) may result in instability in model fitting accuracy for variable optimization, due to insufficient sample points." [p. 15]
