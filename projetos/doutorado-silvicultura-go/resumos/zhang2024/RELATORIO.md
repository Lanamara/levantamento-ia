# RELATÓRIO — Linjing Zhang (2024)

## 1. Referência

- Zhang, L.; Yin, X.; Wang, Y.; Chen, J. (2024). *Aboveground Biomass Mapping in Semiarid Forests by Integrating Airborne LiDAR with Sentinel-1 and Sentinel-2 Time-Series Data*. Remote Sensing, 16, 3241. DOI: 10.3390/rs16173241 [p. 1]
- Nota sobre o arquivo: `TEXTO.txt` corresponde a esse DOI e está completo (24 páginas), mas mistura o layout de revisão por pares com o publicado — há parágrafos e figuras duplicados — e a Tabela 1 traz as fórmulas de textura corrompidas por caracteres inválidos. Nenhum resultado numérico foi perdido.

## 2. Pergunta do estudo

Avaliar, em floresta semiarida, o desempenho de três fontes de dados (séries temporais S1 e S2 e LiDAR aerotransportado de data única) e de sete algoritmos de predição no mapeamento de AGB, identificando a melhor combinação, o melhor modelo e a época de aquisição mais útil.

## 3. Área e dados

- Local: centro de Gansu e nordeste de Qinghai, China, entre 36°38′15″–36°50′50″N e 102°31′19″–102°47′24″E, ~530 km², na transição Planalto de Loess–Planalto Qinghai-Tibete; floresta semiarida de coníferas e folhosas mistas [p. 4].
- Campo: inventário na estação de crescimento (setembro–outubro) de 2019 a 2021, em 804 parcelas de 100 m² (10 m × 10 m), com DAP ≥ 3 cm; AGB por parcela de 16,32 a 186,50 Mg/ha (média 104,16; DP 40,84) [p. 4–5].
- LiDAR: voo de junho de 2019, aeronave Partenavia P68, 850 m acima do solo, 70 kHz, densidade média de 1,5 pulsos/m², CHM de 1 m [p. 5].
- Sentinel-1: 12 imagens S1A de 2019 (uma por mês), banda C, GRD, polarizações VV e VH, modo IW [p. 6].
- Sentinel-2: imagens de 2019–2021; 9 imagens livres de nuvem (jan–abr e ago–dez) e composições de mínimo para mai–jul; 10 bandas a 10 m [p. 6–7].
- Amostras de modelagem: 603 parcelas para treino (75%) e 201 para validação (25%) [p. 11].

## 4. Método

- Variáveis preditoras: 21 métricas LiDAR (percentis Hp10–Hp90, Hmean, Hmax, Hvar, COV, CRR, PD por intervalo de altura), S1 (VV, VH, soma, diferença, quociente e 8 texturas GLCM em janela 3 × 3) e S2 (10 bandas, FAPAR, FCOVER, LAI e 12 índices de vegetação, incluindo MSRren, NDVI, IRECI e STVI) [p. 7–9].
- Cinco experimentos de combinação de dados: A = S1 (156 preditores), B = S2 (300), C = S1+S2 (456), D = S2+LiDAR (321), E = S1+S2+LiDAR (477) [p. 11].
- Sete algoritmos comparados: SGB, RF, XGBoost, GPR, LASSO, CNN e MLP, com hiperparâmetros por grid-search e validação cruzada [p. 9–10].
- Validação em 25% independente, com estratificação em quatro classes de AGB de 50 Mg/ha, usando R², RMSE e RMSEr; importância de variáveis por sequential forward selection (SFS) [p. 11–12].

## 5. Resultados principais

- S1 sozinho: R² 0,24–0,45 e RMSE 47,36–56,51 Mg/ha; S2 sozinho: R² 0,62–0,75 e RMSE 30,08–38,83 Mg/ha; S1+S2: R² 0,65–0,78 e RMSE 28,68–35,92 Mg/ha [p. 1].
- S2 superou S1 em todos os modelos: R² +0,30 a +0,42 e RMSE −17,28 a −21,16 Mg/ha [p. 12].
- Somar S1 ao S2 trouxe ganho pequeno: R² +0,01 a +0,03 e RMSE −0,21 a −2,91 Mg/ha [p. 12].
- Com LiDAR (experimentos D e E), os três modelos de árvore ficaram com R² > 0,84 e RMSE < 24 Mg/ha [p. 12].
- Melhor resultado: XGBoost com S1+S2+LiDAR, R² 0,87, RMSE 21,63 Mg/ha e RMSEr 14,45% [p. 12]; o mesmo valor é repetido nas conclusões [p. 19–20].
- Passar de S1+S2 (C) para S1+S2+LiDAR (E) elevou R² de 0,71 para 0,87 e reduziu RMSE de 33,35 para 21,63 Mg/ha [p. 12].
- CNN foi o melhor modelo nos experimentos A–C (R² 0,45; 0,75; 0,78 e RMSE 47,36; 30,08; 28,68 Mg/ha), mas perdeu para os modelos de árvore com LiDAR [p. 12].
- Mapa final: AGB de 19,63 a 189,42 Mg/ha, média 97,24 Mg/ha; ~60% da área entre 70 e 140 Mg/ha [p. 15].
- Variáveis mais importantes: em C, Jan_MSRren (1ª) e Nov_NDVI (2ª); a soma VV+VH foi a 3ª em C e E; em D e E, Hp90 foi a 2ª e a 1ª, respectivamente [p. 14–15].
- Época: as variáveis mais importantes vieram da estação seca (outubro–março); no top 10 de C, só duas eram da estação chuvosa [p. 15–16].
- Erros: todos os modelos subestimaram AGB alta e superestimaram AGB baixa, com XGBoost mais próximo da linha 1:1 [p. 12].

## 6. Limitações que os próprios autores reconhecem

- Não houve etapa de seleção de variáveis, que "é conhecida por melhorar a acurácia"; será incorporada em estudos futuros [p. 18].
- GPR teve o pior desempenho em S1 (R² 0,24; RMSE 56,51 Mg/ha), possivelmente por escolha inadequada da função de kernel, que precisa ser testada em outras formas [p. 12; p. 18].
- MLP foi sensível a ruído e outliers; o mecanismo de penalização do LASSO explicaria o ganho limitado ao receber variáveis LiDAR [p. 18].
- A banda C do S1 tem baixa penetração no dossel; os autores recomendam combinar SAR de onda longa (bandas P e L) em trabalho futuro [p. 16–17].
- S2 é insensível a biomassa alta em florestas além do fechamento do dossel [p. 17].
- A área tem biomassa relativamente baixa, "insuficiente para causar saturação", o que limita testar o comportamento do LiDAR em biomassa alta [p. 17].
- Ocorrem superestimações e subestimações em regiões de floresta esparsa ou densa [p. 15].
- O RF depende de superfícies de decisão lineares suaves, o que pode ser pouco eficaz com amostras pequenas [p. 18].

## 7. O que serve ao projeto e o que não serve

- Serve: o desenho de ablação em cinco experimentos (A–E) isola o ganho de cada fonte (S1, S2, LiDAR) com o mesmo conjunto de parcelas e o mesmo protocolo de validação — estrutura diretamente replicável para plantios de Goiás [p. 11–12].
- Serve: a evidência de que modelos de árvore (XGBoost, RF, SGB) superam CNN, GPR, MLP e LASSO nesse tipo de dado, e o shortlist de variáveis — percentis de altura LiDAR (Hp90), índices de borda vermelha (MSRren), FCOVER/LAI e a soma VV+VH [p. 12; p. 14–15].
- Não serve: o contexto e a escala — floresta natural semiarida de ~530 km², dossel que perde folhas de outubro a março, AGB média de 97,24 Mg/ha e uso de equação de volume/biomassa genérica por falta de equações alométricas locais; não há calibração para silvicultura tropical úmida nem conversão de AGB em estoque de carbono [p. 4–5; p. 15].
- Não serve: a recomendação de época seca e o LiDAR de data única (junho de 2019) — o ganho do LiDAR é medido contra um único voo, sem repetição temporal, e a vantagem da estação seca decorre da queda de folhas do ambiente semiarido, condição diferente de plantios perenes em Goiás [p. 5; p. 16].

## 8. Frases citáveis (literais)

- "Compared to adding multiple temporal S1 variables, the addition of a single-temporal LiDAR variable to S2 increased the R2 by 0.14 and reduced the RMSE by 10.61 Mg/ha (experiments C and D)." [p. 12]
- "Compared with other tested machine-learning algorithms, XGBoost produced the best performance with the optimal combination of data sources (S1, S2, and LiDAR)" [p. 19–20]
