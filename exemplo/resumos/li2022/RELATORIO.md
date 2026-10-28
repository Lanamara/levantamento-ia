# RELATÓRIO — Yiran Li (2022)

## 1. Referência

Li, Y.; Wang, R.; Shi, W.; Yu, Q.; Li, X.; Chen, X. **Research on Accurate Estimation Method of Eucalyptus Biomass Based on Airborne LiDAR Data and Aerial Images.** *Sustainability*, 2022, 14(17), 10576. DOI: 10.3390/su141710576. Recebido 14/06/2022, publicado 25/08/2022 [p. 1].

O `TEXTO.txt` está íntegro (18 páginas, incluindo referências) e corresponde ao DOI indicado. Observação: nas páginas 3–15 o arquivo traz, intercalado, o texto duplicado da versão em revisão (marcas "FOR PEER REVIEW"), o que gera repetições e pequenas divergências de números; nos pontos em que isso ocorre, o relatório usa a versão final.

## 2. Pergunta do estudo

Qual combinação de dados (LiDAR aerotransportado + imagens aéreas multiespectrais) e qual método (regressão múltipla stepwise, random forest, SVM ou árvore de decisão) estima com maior acurácia a biomassa acima do solo de eucalipto em escala de árvore individual [p. 2].

## 3. Área e dados

- **Local:** Zengcheng Forestry Field, Guangzhou, Guangdong, China (23,292°–23,369° N; 113,681°–113,815° E). Floresta estadual de 2.777,55 hm²; subárea de eucalipto de 11,11 hm² [p. 3].
- **Período:** voo em 18 e 19/11/2019; amostragem de campo em novembro de 2019 [p. 3–4].
- **Sensores:** helicóptero Bell a 500 m, com câmera Feith RGB de 100 MP (3 bandas, mais de 2.900 imagens, mais de 850 G, ortofoto de 0,07 m) e sensor LiDAR Galaxy Prime (1064 nm, 180 pts/m² em média, 50–1000 kHz) [p. 3–4].
- **Amostras:** 100 árvores medidas em campo (altura média 13,19 m; DAP médio 12,63 cm) + 100 árvores interpretadas na ortofoto, totalizando 200 [p. 4–5]; divididas em 140 para treino e 60 para teste (7:3) [p. 8].
- **Referência de biomassa:** equação alométrica para eucalipto em Guangdong, Wa = 0,1882·D^2,1916 (R² = 0,953), aplicada ao DAP [p. 4]; para as 100 árvores não medidas, o DAP foi estimado pela relação copa–DAP C = 0,51539 + 0,17531·D [p. 4].

## 4. Método

- CHM obtido por DSM − DEM, otimizado por preenchimento de depressões (median filtering escolhido entre três filtros) e segmentação de copas por watershed, com altura mínima de 2 m, fator de suavização 1 e raio de 5 pixels [p. 5–6].
- 32 variáveis candidatas (bandas RGB, texturas GLCM, altura e largura de copa do segmento, VFC, DEM, slope, aspect), reduzidas a 10 por importância IncNodePurity do random forest [p. 7, 12].
- Quatro modelos comparados: regressão múltipla stepwise [p. 7]; RF com ntree = 400 e mtry = 11 [p. 8]; SVM com kernel linear, C = 1 e ε = 0,09 [p. 9]; árvore de decisão CART com cp = 0,1 [p. 9].
- Avaliação por R² e RMSE em treino e teste, com validação cruzada de 10 folds [p. 10, 13].

## 5. Resultados principais

- Segmentação: 4.533 árvores identificadas, 1.741 árvores reais não detectadas e 963 mal segmentadas, acurácia de 77% [p. 11].
- Variáveis selecionadas (10): DEM, Slope, Aspect, CD, rmean, bmean, bcor, VFC, rDN, bDN [p. 12].
- Modelo linear: AGB = 2,0418·rmean − 2,8189·bmean − 0,0095·bdis − 0,2651·DEM + 0,5486·VFC + 25,1370·Slope [p. 13].
- Treino — RF: R² = 0,9375 e RMSE = 9,8024; SVR: 0,7173 e 14,1331; CART: 0,5722 e 16,7032; MLR: 0,4132 e 19,4161 [p. 14].
- Teste — RF: R² = 0,7855 e RMSE = 13,0377; SVR: 0,4822 e 17,1953; MLR: 0,3490 e 20,2352; CART: 0,2856 e 22,3906 [p. 14–15].
- O abstract traz outros valores para o RF: treino R² = 0,9346 e RMSE = 8,8399; teste R² = 0,8670 e RMSE = 15,0377 [p. 1]. Esses números não coincidem com os da Tabela 3 [p. 15]; a série consistente é a de resultados/conclusão.
- Mapa de biomassa de eucalipto com resolução espacial de 0,05 m [p. 16].

## 6. Limitações que os próprios autores reconhecem

- Em dossel denso, não se sabe determinar se existem árvores pequenas sob as copas, nem como identificá-las e segmentá-las; sugerem acrescentar dados como radar de solo para melhorar estrutura e localização [p. 16].
- Idade das árvores e volume de madeira ("storage volume") não foram usados; deveriam entrar em estudos futuros [p. 16].
- Sugerem testar algoritmos de deep learning para estimativa em grandes áreas [p. 16].
- A acurácia da segmentação foi menor que em áreas de menor densidade, atribuída à vegetação densa e à sobreposição de copas [p. 11].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o desenho completo em escala de árvore individual — fusão de LiDAR (estrutura vertical) com imagem multiespectral (estrutura horizontal), segmentação por CHM + watershed e comparação de quatro estimadores — é replicável para silvicultura em Goiás.
- **Serve:** o conjunto de preditores e o critério de seleção por importância no RF (de 32 para 10 variáveis) fornecem um ponto de partida concreto; ressalva: as imagens são apenas RGB, sem NIR ou red-edge, o que limita o contraste espectral entre espécies e idades.
- **Não serve diretamente:** clima, espécies e escala são de Guangdong (200 árvores em 11,11 hm², nov/2019); não há nenhum dado de Goiás. O artigo estima só AGB de eucalipto — estoque de carbono não é calculado, nem informado fator de conversão.
- **Não serve como validação de campo:** a biomassa de referência vem de equação alométrica aplicada ao DAP, e metade dos DAPs foi derivada da largura de copa — há circularidade entre preditor e alvo, além da acurácia de segmentação de 77%, que limita o ganho real de precisão.

## 8. Frases citáveis (literais)

- "In areas with dense vegetation, high densities and overlapping tree canopies, the optimised CHM watershed segmentation algorithm could effectively achieve a large area extraction of single trees with an accuracy of 77% for single tree segmentation." [p. 17]
- "In terms of single wood segmentation in dense vegetation cover areas, how to determine whether there are small trees below the dense canopy and how to identify and segment these small trees are issues that need to be studied in depth in the next step." [p. 16]
