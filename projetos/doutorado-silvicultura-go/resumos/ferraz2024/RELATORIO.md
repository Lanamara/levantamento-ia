# RELATÓRIO — Debora Da Paz Gomes Brandão Ferraz (2024)

## 1. Referência

- Autores: Debora da Paz Gomes Brandão Ferraz e Raúl Sánchez Vicens (Department of Geography, Fluminense Federal University, Niterói, RJ).
- Ano: 2024 (disponível online em 27/12/2024); número da revista datado de 2025.
- Título: Comparison between machine learning classification and trajectory-based change detection for identifying eucalyptus areas in Landsat time series.
- Revista: Remote Sensing Applications: Society and Environment, v. 37, art. 101444 [p. 1].
- DOI: 10.1016/j.rsase.2024.101444 [p. 1].
- O `TEXTO.txt` corresponde ao artigo do DOI informado e está íntegro (páginas 1 a 17, incluindo referências).

## 2. Pergunta do estudo

Comparar o desempenho de dois métodos de classificação de áreas de eucalipto — GEOBIA sobre produtos do LandTrendr e Random Forest ano a ano — na detecção dessas áreas e do ano inicial de plantio em uma série temporal Landsat de resolução anual [p. 4].

## 3. Área e dados

- Local: subconjunto de 13.721,8 km² no sudeste do Brasil, cobrindo o centro-norte do estado do Rio de Janeiro e uma porção menor do sul de Minas Gerais, em duas cenas Landsat path/row 217/75 e 217/76 [p. 4].
- Período: série temporal de 1985 a 2020 [p. 5].
- Sensores/fontes: Landsat TM, ETM+ e OLI, composições anuais de refletância de superfície a 30 m, geradas no Google Earth Engine por seleção de medoid (uma observação por pixel por ano) [p. 5].
- Bandas e índices: 6 bandas (blue, green, red, NIR, SWIR 1 e 2) e índices NDVI, BSI, SAVI, EVI, NBR, NDWI e Tasseled Cap [p. 5, 8].
- Amostras: 600 amostras para treinamento do Random Forest (200 "eucalyptus", 400 "non-eucalyptus") [p. 8]; 240 pontos de validação estratificada por classificação (40 de eucalipto e 200 de não eucalipto) [p. 9]; 61 talhões comuns aos dois métodos para validar o ano inicial de plantio [p. 9].
- Segmentação multitemporal feita sobre 28 bandas dos anos 1986, 1995, 2005 e 2015 [p. 5].

## 4. Método

- Composições anuais Landsat 1985–2020 no GEE (medoid, 30 m) e segmentação multirresolução no eCognition (escala 70, shape 0,3, compactness 0,2) para gerar geo-objetos temporalmente homogêneos [p. 5].
- LandTrendr (LT-GEE) aplicado a SWIR e NDVI para segmentar a trajetória de cada pixel, com parâmetros definidos por validação visual (max segments 15; spike 0,2; p-value 0,05; recovery threshold 0,75; min observations 6) e filtros de magnitude >200 para perda (duração <2 anos) e ganho (duração >2 anos) [p. 5–7].
- Classificação GEOBIA hierárquica fuzzy em dois níveis: nível 1 separa "green"/"non-green" por NDVI (0,4–0,8); nível 2 classifica eucalipto pelas taxas de mudança (magnitude/duração) de ganho e perda em NDVI e SWIR [p. 8].
- Random Forest no GEE (ntree = 500, mtry ≈ 11) com 120 bandas anuais (15 bandas/índices × 8 métricas: mediana, desvio padrão e percentis 5, 10, 30, 70, 90, 98), treinado em 2019 e replicado aos demais anos por transfer learning; validação pelo método Area2 (Olofsson et al., 2014), IoU e teste de McNemar [p. 8–9].

## 5. Resultados principais

- GEOBIA/LandTrendr (2019): 145 fragmentos de eucalipto, 3.609 ha, 26,3% da área total, tamanho médio de 44,3 ha e máximo de 609,7 ha [p. 10].
- GEOBIA/LandTrendr: acurácia global 0,988, F-Score 0,975, acurácia do produtor 0,975 e do usuário 0,951; 2 falsos positivos e 1 omissão em 240 pontos [p. 10].
- Random Forest (2019): 189 talhões, 4.136 ha (527,1 ha a mais que o método por trajetória), tamanho médio de 19,8 ha e máximo de 338 ha; acurácia global 0,954, F-score 0,849, produtor 0,816 e usuário 0,886; 229 dos 240 pontos corretos [p. 11].
- Série anual do RF validada em 1989, 1999 e 2009: acurácia global 0,898 / 0,923 / 0,957 e F-score 0,632 / 0,754 / 0,823 [p. 12].
- IoU entre os dois mapeamentos: 0,898 para a classe eucalipto [p. 12].
- Aplicação em todo o estado do Rio de Janeiro: GEOBIA/LandTrendr com acurácia global 0,963 e F-Score 0,892; Random Forest com 0,942 e 0,820 [p. 13].
- Ano inicial de plantio: a maioria das áreas surge entre 2007 e 2012 pelo LT, com pico em 2009 (idade média de 15 anos); pelo RF o pico é em 2010 [p. 13].
- McNemar (n = 61): 47 acertos e 14 erros com LandTrendr contra 37 acertos e 24 erros com Random Forest; qui-quadrado 2,7 e p-valor 0,1003 (α = 0,05), sem diferença significativa [p. 13].

## 6. Limitações que os próprios autores reconhecem

- Número pequeno de talhões de eucalipto na área de estudo, que não é a atividade econômica principal da região, o que limitou a validação a 240 pontos, dos quais 40 para a classe-alvo [p. 13].
- A validação do primeiro ano de rotação depende apenas da interpretação visual das curvas temporais de bandas e índices, pela ausência de imagens de alta resolução espacial na série, que começa em meados dos anos 1980 [p. 13].
- O desempenho do Random Forest piora conforme o ano se afasta do ano-base (2019) [p. 13, 15].
- O LandTrendr não permite análise das áreas dos fragmentos ano a ano, pois exige o conhecimento do ciclo de crescimento e corte [p. 14, 15].

## 7. O que serve ao projeto e o que não serve

- Serve: o uso dos produtos do LandTrendr (taxas de mudança magnitude/duração em NDVI e SWIR) como atributos para separar eucalipto e estimar a idade do talhão — variável de entrada direta em modelos de biomassa e carbono [p. 8, 13].
- Serve: o protocolo de validação comparável (amostragem estratificada Area2/Olofsson, IoU e McNemar) e a cadeia Landsat 30 m anual no GEE de 1985 a 2020, replicável para Goiás [p. 5, 9].
- Não serve: a área de estudo é o Rio de Janeiro e o sul de Minas Gerais, não Goiás, e o artigo não trata de biomassa nem de estoque de carbono — só de classificação de uso e ano de plantio [p. 4].
- Não serve: o número reduzido de talhões e a validação por interpretação visual limitam a transferência dos valores de acurácia (0,988 / 0,954) para outro estado [p. 10, 13].

## 8. Frases citáveis (literais)

- "The mapping (Fig. 6) achieved a global accuracy of 0.988 and an F-Score of 0.975, indicating a satisfactory result." [p. 10]
- "The main limitation of the approach used is the small number of Eucalyptus stands in the study area." [p. 13]
