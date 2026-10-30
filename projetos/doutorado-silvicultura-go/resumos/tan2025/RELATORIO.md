# RELATÓRIO — Hongjian Tan (2025)

## 1. Referência

Tan, H.; Kou, W.; Xu, W.; Wang, L.; Wang, H.; Lu, N. (2025). *Improved Estimation of Aboveground Biomass in Rubber Plantations Using Deep Learning on UAV Multispectral Imagery*. **Drones**, 9(1), 32. DOI: 10.3390/drones9010032. Publicado em 6 de janeiro de 2025 [p. 1]. O `TEXTO.txt` está íntegro (23 páginas) e corresponde ao DOI informado.

## 2. Pergunta do estudo

Testar se um DCNN aplicado diretamente a imagens multiespectrais de UAV supera algoritmos de ML combinados com seleção de variáveis (PCA, importância por RFR, VSURF) na estimativa de AGB de plantações de seringueira [p. 1, p. 4].

## 3. Área e dados

- Local: Jinghong, prefeitura de Xishuangbanna, sul de Yunnan, China; clima de monção tropical, 1200–1700 mm/ano, temperatura média de 23,5 °C; plantações entre 500 e 1000 m de altitude [p. 4].
- Período: campanhas de campo e voo em maio de 2023 e maio de 2024 [p. 4, p. 6].
- Amostras: 80 parcelas de 20 × 25 m (40 em 2023 e 40 em 2024), com quatro cultivares (GT1, RRIM600, Yunyan 77-4, Yunyan 74-72) e altitudes de 600 a 900 m; divididas em 56 para treino e 24 para teste (7:3) [p. 4, p. 6, p. 9].
- Sensor: DJI Mavic 3 M com câmera multiespectral (G 560 nm, R 650 nm, RE 730 nm, NIR 860 nm) e câmera RGB, voo a 100 m, resolução espacial de ~3 cm [p. 6].
- AGB de referência: não destrutiva; equações alométricas de Tang et al. para Xishuangbanna a partir do DBH (R² > 0,97), com AGB = 0,136·DBH^2,437 − 0,108·DBH^1,948 [p. 5–6]. AGB observada nas parcelas: 69,69 a 184,02 t/ha; médias por cultivar de 101,81 a 123,59 t/ha [p. 6].
- Preditores: 20 índices de vegetação (VIs) e 17 métricas de textura (TFs) GLCM (orientação 135°, 2 deslocamentos, janela 7 × 7) [p. 7].

## 4. Método

- Comparação de três regressores de ML (RFR, XGBR, CatBoost) sobre três conjuntos de preditores: VIs, TFs e VIs+TFs, sem e com seleção de variáveis [p. 10, p. 11].
- Seleção de variáveis por três vias: PCA (componentes com variância > 1%), análise de importância por RFR (features que somam 98% da importância) e VSURF [p. 9, p. 12].
- DCNN baseada em AlexNet (5 camadas convolucionais, 3 de max-pooling, 3 totalmente conectadas, ReLU), entrada 224 × 224 × 3, usando reflectância bruta em cinco combinações de bandas (RGB; G-R-NIR; G-R-RE; R-NIR-RE; G-NIR-RE) [p. 8, p. 9, p. 16].
- Validação: 5-fold cross-validation, grid search; RFR e XGBR com 150 árvores e profundidade 16, CatBoost com 300 iterações, taxa 0,01 e profundidade 10; métricas R², RMSE e MAE; Python 3.8 [p. 10].

## 5. Resultados principais

- Sem seleção de variáveis, o melhor modelo foi CatBoost com VIs+TFs: R² = 0,71, RMSE = 14,60 t/ha, MAE = 11,54 t/ha [p. 11; tabela p. 12].
- TFs isoladas foram o pior conjunto: RFR com R² = 0,34 e RMSE = 23,05 t/ha [p. 12].
- Importância por RFR: TVI (0,33) e DVI (0,14) entre os VIs; contrast (0,31), corr (0,21) e var (0,12) entre as TFs [p. 12].
- Com variáveis selecionadas por importância (RFR), o melhor resultado foi RFR: R² = 0,73, RMSE = 13,90 t/ha, MAE = 11,01 t/ha; VSURF foi inferior (R² = 0,70, RMSE = 14,69 t/ha) [p. 13; tabela p. 14].
- PCA gerou 5 componentes dos VIs, 3 das TFs e 6 da combinação [p. 14]; o melhor modelo ML foi RFR sobre VIs+TFs via PCA: R² = 0,81, RMSE = 11,63 t/ha, MAE = 9,27 t/ha [p. 15].
- DCNN com RGB: R² = 0,50, RMSE = 12,78 t/ha, MAE = 10,78 t/ha [p. 16]; melhor combinação, G-R-NIR: R² = 0,89, RMSE = 6,44 t/ha, MAE = 5,72 t/ha; pior, G-NIR-RE: R² = 0,75, RMSE = 9,53 t/ha, MAE = 7,90 t/ha [p. 16].
- Ganho do DCNN sobre o melhor ML: RMSE de 11,63 para 6,44 t/ha (redução de 5,19 t/ha) [p. 15–16].
- Inconsistência interna: a Discussão atribui ao RFR "R² of 0.75, RMSE of 9.53, MAE of 7.90" [p. 17], valores que não coincidem com a Tabela 5 (R² = 0,81; RMSE = 11,63; MAE = 9,27) [p. 15].

## 6. Limitações que os próprios autores reconhecem

- A generalização de DCNNs depende de bases grandes e representativas; as 80 amostras são "relatively few", o que pode enfraquecer a generalização do modelo a outros ambientes e condições [p. 19].
- As bandas do sensor multiespectral são largas e podem não capturar informações sensíveis à AGB; os autores propõem testar hyperspectral de banda estreita no futuro [p. 19].
- DCNN exige mais recursos computacionais e tempo de treinamento que o ML [p. 19].
- Não testaram outras arquiteturas de DL (YOLO, VGG, ResNet) [p. 19].

## 7. O que serve ao projeto e o que não serve

- Serve: o desenho comparativo ML (RFR, XGBR, CatBoost) versus DCNN e o protocolo de seleção de variáveis (PCA, importância por RFR, VSURF) são replicáveis para eucalipto/pinus em Goiás [p. 9–10].
- Serve: evidência quantitativa de que reflectância bruta em 3 bandas (G, R, NIR) em cubos 224 × 224 pode superar VIs+TFs (RMSE 6,44 vs 11,63 t/ha), útil para desenhar entradas de redes neurais [p. 15–16].
- Serve parcialmente: o uso de equação alométrica de DBH em vez de corte destrutivo é o caminho viável em plantios comerciais, mas o modelo é específico para seringueira em Xishuangbanna e não é transferível sem calibração local [p. 5–6].
- Não serve: o artigo estima apenas AGB (t/ha), sem conversão para estoque de carbono, sem LiDAR ou fusão multissensorial, com apenas 4 bandas e 80 parcelas em uma única região tropical — não cobre a escala, a espécie nem a multi-sensoriedade previstas no projeto goiano [p. 6, p. 19].

## 8. Frases citáveis (literais)

- "The results indicate that the RFR combined with a principal component analysis (PCA) for feature selection yielded the best performance (R2 = 0.81, RMSE = 11.63 t/ha, MAE = 9.27 t/ha) between the three ML algorithms." [p. 1]
- "Although this study selected rubber tree samples from different varieties, altitudes, and stand ages, the 80 samples obtained were relatively few." [p. 19]
