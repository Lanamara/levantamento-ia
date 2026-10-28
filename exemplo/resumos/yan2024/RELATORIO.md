# RELATÓRIO — Yan Yan (2024)

## 1. Referência

Yan Yan, Jingjing Lei e Yuqing Huang (2024). "Forest Aboveground Biomass Estimation Based on Unmanned Aerial Vehicle–Light Detection and Ranging and Machine Learning". *Sensors*, 24(21), 7071. DOI: 10.3390/s24217071. Publicado em 2/11/2024 [p. 1]. O `TEXTO.txt` está íntegro (páginas 1–19, incluindo referências) e o DOI confere com o pedido.

## 2. Pergunta do estudo

Qual combinação de parâmetros derivados de LiDAR de UAV e de modelo (regressão ou machine learning) estima com maior acurácia a AGB de plantios de *Eucalyptus*, nas escalas de árvore individual e de povoamento [p. 3].

## 3. Área e dados

- **Local:** oeste de Laibin, região autônoma Zhuang de Guangxi, China (108°59′59″ E, 23°46′36″ N), área de 0,49985 km², relevo cárstico, altitude de 208 a 301 m [p. 3].
- **Período:** voo LiDAR e medições de campo em outubro de 2019 [p. 4].
- **Sensores:** LiDAR aerotransportado em UAV (sensor LiDA1350), a 60 m de altura, 3,2 m/s, sobreposição longitudinal de 80% e lateral de 40% [p. 3]; ortofoto de alta resolução [p. 4]. Sem sensor multiespectral e sem SAR.
- **Densidade de pontos:** o texto informa "mais de 40 pontos/m²" [p. 3] e, em outro trecho, "aproximadamente 300 pontos/m²" [p. 4] — inconsistência interna do artigo.
- **Amostras:** 22 parcelas, 20 m × 20 m, exceto a parcela 4 (20 m × 40 m); as parcelas 1–10 foram usadas na segmentação de árvores individuais [p. 3]. Número total de árvores medidas: não informado.
- **Estatística descritiva:** DBH médio de 7,76 cm (parcelas 1–10) e 8,56 cm (11–22); altura média de 10,17 m e 11,82 m; copa média de 2,10 m e 2,05 m [p. 4].
- **Variáveis:** 35 métricas LiDAR candidatas, das quais 29 selecionadas [p. 6, 11].

## 4. Método

- Segmentação de árvores individuais comparando watershed algorithm (WA) e Euclidean distance clustering algorithm (EDCA); WA adotado por ter menos falsos positivos [p. 5].
- Escala de árvore individual: regressão linear entre AGB medida e os parâmetros AvgHA, LorCHA e CE, com e sem transformação logarítmica natural [p. 5–7, 9–10].
- Escala de povoamento: 35 métricas calculadas em grades de 10 m × 10 m, seleção por PLSR com variable importance in projection (VIP, limiar 0,8) e três modelos — MLSR, SVR com quatro kernels e KNN com k de 1 a 11 [p. 6, 11–13].
- Validação: leave-one-out cross-validation (LOOCV), com R², RMSE e RRMSE [p. 8].

## 5. Resultados principais

- Melhor modelo de árvore individual, ln(AGB) = 1,99 × ln AvgHA − 1,341: R = 0,873, R² ajustado = 0,867, R² = 0,851, RMSE = 0,312 t/ha, RRMSE = 0,0091 [p. 10]. O abstract cita "R2 = 0,873, RMSE = 0,312 t/ha, RRMSE = 0,0091" [p. 1], mas 0,873 é o R da Tabela 4, não o R².
- Incluir CE não melhorou a predição: RMSE de 0,318 t/ha e RRMSE de 0,0092 no modelo com AvgHA e CE [p. 10].
- Sem transformação logarítmica, o RMSE ficou entre 10,298 e 11,076 t/ha [p. 9].
- Seleção por VIP: 29 das 35 variáveis com VIP ≥ 0,8; H10 com o maior valor (VIP = 1,15) e d0 no limite (VIP = 0,80); percentis de altura somam 51,7% das variáveis importantes [p. 11].
- MLSR 2 (H10 e LAI): R² = 0,822, RMSE = 8,547 t/ha, RRMSE = 0,249; equação AGB = −16,324 + 4,134 × H10 + 27,143 × LAI [p. 11–12].
- SVR: kernel polinomial foi o melhor, com R² de 0,807 para 0,824 e RMSE de 9,614 para 9,139 t/ha após a seleção de variáveis [p. 12]. No confronto final: R² = 0,868, RMSE = 7,932 t/ha, RRMSE = 0,231 [p. 13].
- KNN: melhor resultado com k = 7 (RMSE = 11,191 t/ha) [p. 13]; na comparação final, R² = 0,807, RMSE = 9,664 t/ha, RRMSE = 0,282, com a maior superestimativa [p. 13].
- Mapa de AGB pelo SVR: valores de 28,407 a 91,473 t/ha, em cerca de 70% da área de estudo [p. 13].
- Ordem de acurácia: SVR > MLSR > KNN [p. 14].

## 6. Limitações que os próprios autores reconhecem

- O estudo "não é suficiente para discutir a adaptabilidade de uma única espécie florestal" e não considera a correlação entre variáveis de terreno e AGB [p. 16].
- Previu a AGB de apenas uma espécie e em área pequena, e a segmentação de árvores individuais afeta a acurácia da estimativa [p. 16].
- O DBH não pode ser obtido diretamente do LiDAR de UAV, e os parâmetros de copa sofrem com sobre e subsegmentação [p. 15].
- O número restrito de parcelas (22) motivou o uso de LOOCV, método indicado para conjuntos pequenos [p. 8].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o desenho comparativo — regressão versus MLSR, SVR e KNN, com seleção de variáveis por VIP e validação por LOOCV — é diretamente replicável em povoamentos de eucalipto em Goiás [p. 8, 11].
- **Serve:** a evidência de que variáveis de altura (H10 e percentis) concentram a explicação da AGB em eucalipto, com correlação mais fraca para métricas de copa [p. 11, 15].
- **Serve com cautela:** o SVR como modelo de referência [p. 13], desde que revalidado — a área tem 0,5 km², uma única espécie e nenhuma variação de terreno no modelo [p. 3, 16].
- **Não serve:** o artigo termina em AGB e não calcula estoque de carbono (fração de carbono e razão raiz/parte aérea não informadas); e não é multissensorial — usa só LiDAR e ortofoto, sem dados ópticos multiespectrais ou SAR [p. 4].

## 8. Frases citáveis (literais)

- "The study applied three machine learning methods, MLSR, SVR, and KNN, to predict AGB, respectively. The results concluded that the SVR model had the best estimation, followed by the MLSR model, and the KNN model was the worst." [p. 15]
- "It is worth noting that the study only predicted the AGB of a single tree species in a small area, and the data of single tree segmentation would affect the estimation accuracy of forest biomass." [p. 16]
