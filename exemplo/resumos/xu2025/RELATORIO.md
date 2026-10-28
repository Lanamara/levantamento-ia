# RELATÓRIO — Xu Xu (2025)

## 1. Referência

Xu Xu; Jingyu Yang; Shanze Qi; Yue Ma; Wei Liu; Luanxin Li; Xiaoqiang Lu; Yan Liu (2025). *Estimation of Forest Aboveground Biomass Using Sentinel-1/2 Synergized with Extrapolated Parameters from LiDAR Data and Analysis of Its Ecological Driving Factors*. **Remote Sensing**, 17(14), 2358. DOI: 10.3390/rs17142358 [p. 1]

O `TEXTO.txt` está completo (20 páginas, incluindo referências) e corresponde ao DOI informado.

## 2. Pergunta do estudo

Se a integração de Sentinel-1, Sentinel-2 e LiDAR aerotransportado, com extrapolação espacial dos parâmetros estruturais do LiDAR, produz estimativa acurada de AGB e como origem florestal (plantio/natural), idade do povoamento e grau de mistura de espécies afetam a distribuição e a acumulação de AGB [p. 3].

## 3. Área e dados

- **Local:** província de Guangdong, sudeste da China, ~180.000 km², clima de monção subtropical, elevações de 4 a 1989 m, cobertura florestal acima de 53% e ~580 milhões de m³ de volume de madeira [p. 3].
- **Período:** 2022 (Sentinel-2, Sentinel-1 e inventário florestal do mesmo ano); medições de campo de abril a outubro de 2022 [p. 3, p. 6].
- **Sensores e fontes:** Sentinel-2 MSI (bandas B2–B12, reamostradas a 10 m, 9 tiles, nuvem <50%, composições medianas mensais) [p. 3]; Sentinel-1 VV e VH, 9 tiles, mesmo intervalo temporal [p. 4–5]; LiDAR aerotransportado em UAV DJI Matrice 300 RTK com sensor RIEGL VUX-1 [p. 5]; inventário florestal (FMI) 2022 do Departamento Florestal de Guangdong como referência de AGB [p. 6]; *China Forest Tree Age Dataset* (30 m) para idade [p. 7]; produto de AGB de Yang et al. para comparação espacial [p. 7].
- **Amostras:** 349 rotas de voo e 4.420 footprints de nuvem de pontos com qualidade [p. 5]; 10.350 manchas válidas do FMI após filtros de área, cobertura e sanidade e buffer de 500 m [p. 6]; 3.874 parcelas de campo válidas de 10 × 10 m (de 4.347 medidas) [p. 6]; 1.000 pontos aleatórios para comparar tipos florestais [p. 8].

## 4. Método

- Extração, de cada copa delimitada por CHM + *watershed*, de FRE, LRE, NGRP e TNRP, convertidos em altura média das árvores (MTH) e cobertura média do dossel (MCC) por equações (1) e (2), e reamostragem em grade de 10 m [p. 6–7].
- Extrapolação espacial de MTH e MCC por Random Forest (RF) usando bandas e índices do Sentinel-1/2; separação treino/teste por agrupamento K-Means para evitar vazamento espacial, com grid search e validação cruzada de 10 dobras [p. 7].
- Predição de AGB por RF com bandas Sentinel-1/2, índices de vegetação (PCA com 5 componentes, >96,4% da variância: NDVI, SAVI, NIRV, REIP, EVI) e MTH/MCC extrapolados, além de modelo de controle sem os parâmetros estruturais [p. 4, p. 7].
- Atributos florestais: origem por RF, SVM, XGB e MLC com fusão por janela deslizante e moda; idade a partir do produto Shang et al.; mistura pelo índice de Shannon (H′) predito por RF; coeficientes locais por MGWR em células de 7,5 × 7,5 km [p. 7–8].

## 5. Resultados principais

- Extrapolação de MTH: R² = 0,798 e RMSE = 1,595 [p. 9]; de MCC: R² = 0,738 e RMSE = 0,077 [p. 9]. Faixa extrapolada de altura de 2,88 a 24,67 m [p. 8] e de cobertura de 0,177 a 0,924 [p. 9].
- AGB sem parâmetros do LiDAR: R² = 0,724, RMSE = 15,59 e coeficiente de regressão 0,6899, com subajuste acima de 130 Mg/ha [p. 9]. Com os parâmetros: R² = 0,811, RMSE = 10,64 e coeficiente 0,8603, ampliando o teto de 159,8 Mg/ha para mais de 180 Mg/ha [p. 10].
- Concordância com o produto de referência: 80% da área dentro de ±20% e 20% acima desse limiar [p. 10].
- Classificação origem: XGB 93% de acurácia global e Kappa 0,85; RF 89%/0,77; MLC 82%/0,64; SVM 79%/0,57 [p. 12]. Naturais ~54% e plantios 46% da área [p. 12].
- Idade: 20–40 anos em 35,25%, 40–60 anos em 33,92%, <20 anos em 29,28% e >60 anos em 1,55% [p. 12].
- Shannon H′ predito com R² = 0,791 e RMSE = 0,272; média ~1,17, com 0,83–2,3 em áreas naturais e 0–0,4 em plantios [p. 13].
- MGWR: idade positiva em 95,4% das células florestais, coeficientes acima de 0,75 no norte, sudoeste e sudeste, chegando a 1,23; apenas 4,6% com efeito mínimo ou negativo [p. 14]. Mistura positiva em 87,7% da área, com coeficientes acima de 0,88 no norte e parte do sul [p. 14].
- AGB mediana: 113,68 Mg/ha em florestas naturais contra 87,37 Mg/ha em plantios, diferença de 26,31 Mg/ha; quartil superior ~140 contra ~120 Mg/ha [p. 14].
- Aos 55–60 anos, naturais de todos os níveis de mistura superam 100 Mg/ha e plantios ficam abaixo de 100 Mg/ha [p. 15]. Aos 20 anos, plantio puro ~80 Mg/ha e plantio pouco misturado ~85 Mg/ha, contra ~60–70 Mg/ha nas naturais; plantios estabilizam por volta de 95 Mg/ha aos 40 anos [p. 15].

## 6. Limitações que os próprios autores reconhecem

- A extrapolação de altura e cobertura é sensível à heterogeneidade da paisagem; em relevo complexo, bordas abruptas e composições diversas os erros se acumulam e enviesam a AGB localmente, faltando validação com dados de campo independentes [p. 16].
- A idade florestal veio de produto nacional de 30 m não validado na região de estudo, com risco de viés sistemático onde o histórico de distúrbio é incerto [p. 16].
- O H′ mede riqueza e equitabilidade, mas ignora estratificação vertical, camadas de dossel e distribuição de tamanhos, simplificando a diversidade em florestas maduras [p. 16].
- Foram avaliados apenas efeitos independentes dos atributos; interações entre si e com clima, topografia e solo não foram incorporadas [p. 17]. A transferência para outras zonas climáticas exige recalibração e validação regionais [p. 17].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o desenho central — extrair MTH e MCC de LiDAR discreto, extrapolar para grades contínuas de 10 m por RF e fundir com Sentinel-1/2 — é diretamente replicável em Goiás, onde o LiDAR é escasso; o ganho medido (R² de 0,724 para 0,811; RMSE de 15,59 para 10,64 Mg/ha) serve como referência de expectativa [p. 10].
- **Serve:** o esquema de validação — modelo de controle sem variáveis estruturais, separação treino/teste por clusters K-Means, buffer de 500 m e inventário florestal como referência [p. 6–7] — é apropriado para talhões homogêneos de silvicultura, sujeitos a autocorrelação espacial.
- **Não serve:** a parte de MGWR e de atributos ecológicos foi calibrada para florestas de até mais de 60 anos e para o contraste natural/plantio de Guangdong [p. 12, p. 15]; em rotações curtas de eucalipto em Goiás a escala temporal e o contraste de origem são outros.
- **Não serve:** o artigo entrega AGB, não estoque de carbono (sem fração de carbono, raízes ou necromassa), e os coeficientes não são transferíveis sem recalibração para o Cerrado [p. 17].

## 8. Frases citáveis (literais)

> "The inclusion of these parameters addressed the saturation issue, expanding the AGB range from 159.8 Mg/ha to over 180 Mg/ha." [p. 10]

> "The median AGB of natural forests is 113.68 Mg/ha, compared to only 87.37 Mg/ha for planted forests, representing a statistically significant difference of 26.31 Mg/ha." [p. 14]
