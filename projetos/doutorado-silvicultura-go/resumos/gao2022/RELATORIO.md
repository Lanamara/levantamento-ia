# RELATÓRIO — Linghan Gao (2022)

## 1. Referência

Gao, Linghan; Chai, Guoqi; Zhang, Xiaoli (2022). *Above-Ground Biomass Estimation of Plantation with Different Tree Species Using Airborne LiDAR and Hyperspectral Data*. **Remote Sensing**, 14(11), 2568. DOI: 10.3390/rs14112568. Recebido em 25/04/2022, aceito em 24/05/2022, publicado em 27/05/2022 [p. 1]. O `TEXTO.txt` contém o artigo integral, da primeira página às referências, com marcas de página legíveis e sem truncamento; o DOI confere.

## 2. Pergunta do estudo

A fusão de dados LiDAR aerotransportado e hiperespectrais melhora a acurácia da estimativa de AGB em plantios com diferentes espécies arbóreas, em comparação ao uso de uma única fonte de dados? [p. 1, p. 3]

## 3. Área e dados

- Local: fazenda florestal de Gaofeng, Nanning, província de Guangxi, China; 108°19′30″–108°23′30″E e 22°56′–23°1′N; altitude 70–875 m, declividade 25–35°, clima de monção tropical, cobertura florestal próxima de 90% [p. 3].
- Período: inventário de campo em janeiro de 2018; aquisição remota em fevereiro de 2018 [p. 4–5].
- Sensores: UAV de asa fixa Yun-12 com sistema de varredura a laser RIEGL LMS-Q680i e sensor hiperespectral AISA Eagle II (400–1000 nm, resolução espectral 3,3 nm, 125 bandas) [p. 5].
- Amostras: 98 parcelas — 27 de Chinese fir (*Cunninghamia lanceolata*), 15 de pinus, 35 de eucalipto e 21 de outras folhosas [p. 4].
- Densidade do LiDAR: 3,35 pontos/m² [p. 5].

## 4. Método

- Extração de atributos hiperespectrais: reflectância, 1ª e 2ª derivadas das 125 bandas; índices de vegetação (NDVI, EVI, NDVI705, NDVI1, NDVI2, SAVI, PRI, TCARI, OSAVI, MCARI, SARVI); textura GLCM de 2ª ordem nas bandas 482, 550 e 645 nm (24 atributos); textura por wavelet transform (espectral, horizontal, vertical, aproximada, diagonal) e bordas por morfologia matemática [p. 6–7].
- Extração de atributos LiDAR: estrutura do dossel (densidade de copa, LAI), estrutura do ponto (percentis de altura, máximo e mínimo), densidade de pontos em estratos de altura e terreno (declividade, aspecto); CHM obtido por DSM − DEM [p. 6–7].
- Seleção de atributos por random forest (RF) em três níveis: triagem por conjunto de atributos, triagem dos atributos hiperespectrais ótimos e triagem após fusão dos dois conjuntos; modelagem por multiple stepwise regression (MSR), com proporção treino/validação de 4:1 [p. 8].
- Avaliação por R², RMSE e MAE, com modelos construídos separadamente por espécie [p. 8].

## 5. Resultados principais

- A triagem hiperespectral reteve 4, 4, 6 e 3 atributos para Chinese fir, pinus, eucalipto e outras folhosas, respectivamente [p. 9].
- Somente hiperespectral (Tabela 7): R² de treino 0,89 (Chinese fir), 0,84 (pinus), 0,78 (eucalipto) e 0,89 (outras folhosas); R² de validação 0,38, 0,79, 0,03 e 0,13; RMSE 9,67, 20,02, 350,14 e 128,47 t/hm²; MAE 7,43, 14,37, 194,55 e 94,53 t/hm² [p. 10].
- Fusão LiDAR + hiperespectral (Tabela 8): R² de treino 0,78 (Chinese fir), 0,95 (pinus), 0,72 (eucalipto) e 0,89 (outras folhosas); R² de validação 0,44, 0,91, 0,71 e 0,13; RMSE 11,02, 12,94, 50,75 e 128,47 t/hm²; MAE 9,15, 8,95, 25,48 e 94,53 t/hm² [p. 12].
- O resumo cita 0,78, 0,95, 0,72 e 0,89 como "acurácia dos modelos ótimos", valores que correspondem ao R² de treino da fusão e não ao de validação [p. 1, p. 12].
- Ganho da fusão: pinus passou de 0,84/0,79 (treino/validação, hiperespectral) para 0,95/0,91; Chinese fir, de 0,89/0,38 para 0,78/0,44; eucalipto teve validação de 0,03 para 0,71 e treino reduzido em 0,06 [p. 12].
- Para eucalipto, os atributos importantes vieram apenas de métricas de altura do LiDAR; para outras folhosas, apenas da textura por wavelet transform do hiperespectral; Chinese fir e pinus combinaram altura, espectro e textura wavelet [p. 11–12].
- Mapeamento: mínimo de AGB de Chinese fir de 11,5 t/hm² (hiperespectral) e 77,5 t/hm² (fusão), contra mínimo medido de 59,2 t/hm²; pinus com máximo/mínimo de 160/95 t/hm² (hiperespectral) e 170/91 t/hm² (fusão); eucalipto com máximo de 700 t/hm² (hiperespectral) e 150 t/hm² (fusão), contra máximo medido de 338,8 t/hm² — saturação severa no hiperespectral [p. 13–14].

## 6. Limitações que os próprios autores reconhecem

- O estudo se restringe ao modelo de AGB da fazenda de Gaofeng, Nanning, Guangxi, sem análise comparativa sobre a aplicação do modelo às mesmas espécies em outras áreas; a extensão fica para trabalho futuro [p. 15].
- Usa apenas fusão por atributos (*feature fusion*); outros métodos de fusão de fontes de dados não foram testados [p. 15].
- A divergência entre acurácia de treino e de validação pode decorrer de parcelas de modelagem e de validação mal distribuídas [p. 11].
- O modelo de eucalipto baseado só em hiperespectral apresenta sobressaturação e "over fitting" (validação 0,03); apenas 3 atributos foram selecionados para outras folhosas, cujo modelo não melhorou com a fusão [p. 12, p. 15].

## 7. O que serve ao projeto e o que não serve

- Serve: a estratificação por espécie na modelagem (modelos separados por grupo) e a lógica de triagem de atributos em níveis com RF + MSR são diretamente replicáveis em povoamentos de eucalipto e pinus em Goiás, sobretudo com poucas parcelas [p. 8, p. 14–15].
- Serve: a evidência de que textura por wavelet transform do hiperespectral e métricas de altura do LiDAR carregam sinal de AGB, com o eucalipto (espécie alta) dependendo essencialmente de atributos de altura [p. 11–12].
- Não serve: o artigo entrega AGB, não estoque de carbono — não há fator de conversão, fração de carbono, biomassa subterrânea nem incerteza propagada; qualquer uso em carbono exige etapa adicional [p. 1, p. 15].
- Não serve como referência climática/espacial: área de monção tropical no sul da China, com LiDAR de UAV a 3,35 pontos/m² e 98 parcelas — a transferência para o Cerrado goiano e para sensores orbitais não foi testada nem autorizada pelos autores [p. 3–5, p. 15].

## 8. Frases citáveis (literais)

- "This shows that the optimal features of different tree species are different due to the specific vertical and canopy structure, and the texture features extracted by wavelet transform can be used for forest AGB modeling." [p. 14]
- "The reason for the deviation between training accuracy and verification accuracy may be that the selected modeling and verification sample plots are uneven, and many attempts can be made in subsequent research." [p. 11]
