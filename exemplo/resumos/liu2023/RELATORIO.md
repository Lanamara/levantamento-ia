# RELATÓRIO — Yao Liu (2023)

## 1. Referência

Yao Liu, Peng Lei, Qixu You, Xu Tang, Xin Lai, Jianjun Chen e Haotian You (2023). *Individual Tree Aboveground Biomass Estimation Based on UAV Stereo Images in A Eucalyptus Plantation*. **Forests**, 14(9), 1748. DOI: 10.3390/f14091748. Recebido em 19/07/2023, aceito em 28/08/2023, publicado em 29/08/2023 [p. 1].

## 2. Pergunta do estudo

Até que ponto imagens estéreo obtidas por UAV com câmera de consumo permitem estimar a AGB de árvores individuais de eucalipto, e como os diferentes atributos derivados dessas imagens (espectrais, textura, altura, área de copa) e os algoritmos de modelagem afetam essa estimativa [p. 4].

## 3. Área e dados

- **Local:** condado de Luzhai, cidade de Liuzhou, região autônoma de Guangxi Zhuang, China (108°28′–110°12′ E, 24°14′–24°50′ N); relevo baixo e plano, altitude de 99,1 m a 242,6 m; clima de monção subtropical, ~20 °C de média anual, ~1500 mm de chuva e ~1600 h de sol por ano [p. 4].
- **Período:** medições de campo em julho de 2022; voos adicionais em outubro de 2022 e março de 2023 com os mesmos parâmetros de voo [p. 4–5].
- **Sensor:** DJI Phantom 4 RTK, voo em cinco direções, altitude de 70 m, velocidade média de 5,6 m/s, superposição longitudinal de 80% e lateral de 70% [p. 5]; resolução espacial das imagens de 0,02 m × 0,02 m, processadas no Pix4D V4.7.5 [p. 7].
- **Amostras:** 5 classes de idade — 1, 11, 15, 22 e 36 meses — com 85, 52, 85, 70 e 57 árvores medidas (349 no total) [p. 5]. DBH médio de 2,38 cm (1 mês) a 13,17 cm (36 meses); altura média de 1,59 m a 15,84 m [p. 5]. Para a segmentação, 345 amostras de pontos (145 de eucalipto e 200 de outros alvos), ampliadas para 2070 e divididas em 7:3 entre treino e validação [p. 7].

## 4. Método

1. AGB de referência calculada por equação alométrica oficial de eucalipto (LY/T 2253-2014) a partir de DBH e altura medidos em campo [p. 6].
2. Processamento fotogramétrico (DSM, DOM, nuvem de pontos), filtragem gaussiana, normalização pelo DEM e geração do CHM; segmentação de árvores individuais com a rede neural PointNet++ seguida de agrupamento por nuvem de pontos [p. 5–8].
3. Extração de 19 atributos espectrais (bandas RGB e 16 índices de vegetação), 24 atributos de textura (MEA, VAR, HOM, CON, DIS, ENT, SEM, COR), altura (TH), área de copa e idade do povoamento [p. 8–9, p. 13].
4. Modelagem com ridge regression, random forest e CatBoost, validação cruzada de dez dobras (R², RMSE, NRMSE, Bias) e otimização de atributos por SHAP [p. 10–11, p. 15].

## 5. Resultados principais

- **Segmentação (PointNet++)**: F-score acima de 0,89 em todas as idades; F = 1 no povoamento de 1 mês; F = 0,89 aos 11 e aos 36 meses; precisão de 0,80 aos 36 meses e 0,87 aos 11 e 22 meses [p. 11].
- **Extração de copa e altura**: R² superior a 0,91 para as duas variáveis, com a área de copa um pouco abaixo da altura [p. 13].
- **Correlações com AGB**: idade 0,84; TH 0,80; VAR-G −0,69; área de copa 0,55; banda b 0,52 [p. 13]. Atributos com |r| > 0,5: b, RBRI, IKAW e GBRI (espectrais); HOM-G, HOM-R, HOM-B, VAR-G, CON-G e DIS-G (textura) [p. 13].
- **Todos os atributos, CatBoost**: R² 0,90, RMSE 7,85 kg/árvore, NRMSE 0,08, Bias −0,09; ridge regression: R² 0,82, RMSE 10,79 kg/árvore, NRMSE 0,11 [p. 14].
- **Apenas espectrais**: CatBoost R² 0,65, RMSE 14,49 kg/árvore, NRMSE 0,15; ridge regression R² 0,34, RMSE 20,65 kg/árvore, NRMSE 0,21 [p. 15]. Espectrais + TH: R² 0,86 (CatBoost) e 0,62 (ridge) [p. 14–15].
- **Modelo otimizado (idade, TH, área de copa e HOM-B, CatBoost)**: R² 0,90 e NRMSE 0,08 com quatro variáveis, sem ganho ao acrescentar mais [p. 16]; contra a AGB de campo, R² 0,90, RMSE 7,93 kg/árvore, NRMSE 0,08 e Bias 0,04 [p. 16].
- **Faixas por algoritmo**: CatBoost R² 0,65–0,90, NRMSE 0,08–0,15 e Bias −0,39 a 0,01; random forest R² 0,59–0,88, NRMSE 0,09–0,16 e Bias −0,82 a −0,19; ridge regression R² 0,34–0,82, NRMSE 0,11–0,21 e Bias −0,07 a 0,03 [p. 19].
- **Ganho da altura**: incluir TH elevou o R² em 0,28 em relação ao modelo só espectral [p. 1].
- **Mapas multitemporais**: AGB cresceu de julho/2022 a março/2023, com queda local em parte das parcelas [p. 17].
- *Observação:* o número de árvores por classe difere entre a Tabela 1 (campo: 85, 52, 85, 70, 57) [p. 5] e a Tabela 4 (segmentação: 85, 25, 91, 79, 20) [p. 11]; o texto não explica a diferença.

## 6. Limitações que os próprios autores reconhecem

- Relevo das parcelas relativamente plano, faixa de idade estreita e uso exclusivo de algoritmos de machine learning (sem deep learning), o que limita a validade dos resultados em situações mais complexas [p. 19–20].
- Erros de sobre e subsegmentação de copas, visíveis nas áreas marcadas nas figuras, exigiram correção manual dos limites vetoriais [p. 11–12].
- A extração da área de copa foi menos precisa que a da altura, porque copas adjacentes aparecem conectadas na segmentação [p. 13].
- Crescimento negativo de AGB em parte das parcelas atribuído a tombamento por vento e chuva e ao desbaste de brotações em povoamentos de segunda ou terceira geração [p. 17].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o desenho multitemporal com o mesmo UAV e os mesmos parâmetros de voo em três datas, com cinco idades e AGB por árvore individual — estrutura diretamente transplantável para talhões de eucalipto em Goiás [p. 4–5].
- **Serve:** a hierarquia de atributos (TH e idade dominam; textura e espectrais agregam pouco) e o teto de quatro variáveis, que reduz custo de campo e de processamento sem perder acurácia [p. 13, p. 16].
- **Serve com cautela:** CatBoost superou random forest e ridge regression em todas as combinações, e os autores recomendam CatBoost por causa do Bias menor do que o do random forest [p. 15].
- **Não serve:** a AGB de referência vem de equação alométrica nacional chinesa aplicada a *Eucalyptus robusta*, não de corte e pesagem; para Goiás seria preciso equação local e validação destrutiva. O estudo também não trata de estoque de carbono, de dossel fechado ou de terreno acidentado [p. 6, p. 19–20].

## 8. Frases citáveis (literais)

> "The AGB model that we established with forest age, TH, crown area, and HOM-B feature variables using the CatBoost algorithm had the best estimation accuracy, with an R2 of 0.90 and an NRMSE of 0.08." [p. 1]

> "However, given the relatively flat terrain of the sample plots we used, the small forest age range, and the fact that all three algorithms were machine learning algorithms, the practicality of the results in more complex situations needs further verification." [p. 19]
