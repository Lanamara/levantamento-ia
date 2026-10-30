# RELATÓRIO — Aliny Aparecida dos Reis (2018)

## 1. Referência

- Reis, Aliny Aparecida dos; Carvalho, Mônica Canaan; Mello, José Marcio de; Gomide, Lucas Rezende; Ferraz Filho, Antônio Carlos; Acerbi Junior, Fausto Weimar (2018). "Spatial prediction of basal area and volume in Eucalyptus stands using Landsat TM data: an assessment of prediction methods". *New Zealand Journal of Forestry Science*, 48:1. DOI: 10.1186/s40490-017-0108-0.
- `TEXTO.txt` contém o artigo integral (17 páginas, de "Received: 3 February 2017" a "Page 17 of 17"), compatível com o DOI indicado; não está truncado.

## 2. Pergunta do estudo

Estimar e mapear área basal e volume de povoamentos de Eucalyptus integrando inventário florestal e dados espectrais do Landsat 5 TM por métodos paramétricos e não paramétricos, comparando MLR, RF, SVM e ANN e verificando se a krigagem ordinária dos resíduos melhora essas estimativas [p. 2].

## 3. Área e dados

- Local: Lagoa Grande, noroeste de Minas Gerais, Brasil (17°43′–17°44′ S; 46°32′–46°33′ W; 560 m), clima Aw [p. 3].
- Povoamento: 20 talhões clonais de *Eucalyptus urophylla* × *E. camaldulensis*, 362,2 ha, plantados em abril e maio de 2004, espaçamento 3 × 2 m ou 3 × 3 m, com cerca de 5 anos na medição [p. 1, p. 3].
- Inventário: junho e julho de 2009; 35 parcelas georreferenciadas de 400 m² em amostragem sistemática (cerca de 1 parcela por 10 ha), com DAP e altura [p. 3].
- Sensoriamento: imagem Landsat 5 TM de 25/06/2009, 30 m, órbita 220 ponto 072, reflectância de superfície (LEDAPS/USGS); bandas TM1–TM5 e TM7 mais 8 índices (NDVI, ND53, ND54, ND57, SAVI, MSAVI, EVI, GEMI), totalizando 14 variáveis [p. 3–4].
- Amostras: 35 parcelas divididas em 25 para ajuste (70%) e 10 para validação (30%) [p. 4].

## 4. Método

- MLR com eliminação stepwise e AIC, diagnóstico de multicolinearidade por VIF (corte 10) [p. 4].
- RF no WEKA 3.8 (20 árvores e 10 atributos por nó para área basal; 80 árvores e 11 atributos para volume), SVM com kernel RBF/SMO (C e σ de 10 e 0,1 para área basal; 100 e 0,01 para volume) e ANN multilayer perceptron com backpropagation (14–1–1; taxa de aprendizado 0,3, momento 0,5 e 500 iterações para área basal; 0,2, 0,7 e 500 para volume) [p. 5].
- Krigagem ordinária dos resíduos de cada método (modelos esférico, exponencial e gaussiano ajustados por mínimos quadrados ponderados, selecionados por RAE e SRE), somando os resíduos interpolados às estimativas [p. 5–6].
- Avaliação por ME, MAE e RMSE nas bases de ajuste e validação, melhoria relativa (RI) pela Eq. 4 e teste t de Student entre as bases [p. 6, p. 8].

## 5. Resultados principais

- Área basal: 10,07 a 21,63 m² ha⁻¹, média 16,86 m² ha⁻¹, desvio-padrão 2,4 m² ha⁻¹, CV 14,26% [p. 6].
- Volume: 95,80 a 213,85 m³ ha⁻¹, média 169,34 m³ ha⁻¹, desvio-padrão 29,66 m³ ha⁻¹, CV 17,51% [p. 6].
- Correlação: ND54 com r = −0,91 para área basal e r = −0,52 para volume; as faixas entre todas as variáveis espectrais foram de −0,91 a 0,15 (área basal) e de −0,52 a −0,02 (volume) [p. 6, p. 11].
- MLR: área basal explicada apenas por ND54, R²aj = 0,81 e erro-padrão residual de 5,76%; volume por NDVI e TM1, R²aj = 0,37 e erro de 13,08% [p. 7].
- Validação (RMSE em %): área basal MLR 9,42, RF 9,54, SVM 9,39, ANN 8,52; volume MLR 16,72, RF 14,91, SVM 13,58, ANN 13,82; no volume o SVM foi o melhor e o MLR o pior [p. 8–9].
- Ajuste (RMSE em %): RF com 2,48 para área basal e 4,77 para volume, os menores erros entre os métodos [p. 9].
- Estrutura de dependência espacial nos resíduos em 6 de 8 situações; resíduos de volume de MLR e ANN tiveram efeito pepita puro [p. 8].
- Krigagem de resíduos: RI de 25,23% para área basal com ANN (RMSE de 8,52% para 6,37%) e de −5,66% com RF (9,54% para 10,08%, aumento de 5,7% no erro); RI de 30,93% (ajuste) e 13,70% (validação) para volume com SVM [p. 9, p. 11].
- Mapas: ANN subestimou área basal (total 5715,3, fora do IC 5807,9–6405,0 do inventário) e volume (total 56.223,8 m³) [p. 11].

## 6. Limitações que os próprios autores reconhecem

- Resultados limitados a uma área de estudo homogênea e relativamente pequena, com pequeno número de parcelas [p. 14].
- Uso de sensor relativamente antigo, o Landsat 5 TM [p. 14].
- ANN sensível à variação dos parâmetros de entrada e com desempenho ruim em razão do conjunto restrito de dados [p. 14].
- Métodos de machine learning com baixa transparência e interpretação biológica limitada [p. 14].
- Métodos híbridos com krigagem podem ser menos precisos em regiões com dados de campo esparsos [p. 14].

## 7. O que serve ao projeto e o que não serve

- Serve: o desenho de comparação MLR/RF/SVM/ANN com bandas e índices de sensor óptico multiespectral para área basal e volume é diretamente replicável para biomassa e estoque de carbono [p. 15].
- Serve: os achados operacionais — RF com menores erros e melhor mapeamento, ND54 como variável de maior importância e recomendação de testar RF, SVM e MLR antes de escolher o método [p. 8, p. 15].
- Serve (com cautela): krigagem ordinária de resíduos como correção de tendência, com ganho apenas em parte dos métodos e dependência da estrutura espacial dos resíduos [p. 9, p. 15].
- Não serve: o artigo não estima biomassa nem estoque de carbono, não usa RADAR ou LiDAR (apenas os aponta como necessidade futura) e não é em Goiás — a área é em Minas Gerais, com data e sensor únicos [p. 3, p. 14–15].

## 8. Frases citáveis (literais)

- "The ND54 index was the spectral variable that had the best correlation values with basal area (r = − 0.91) and volume (r = − 0.52) and was also the variable that most contributed to basal area and volume estimates by the MLR and RF methods." [p. 1]
- "The combination of spatial prediction methods with residual kriging should be used with caution, since the relative improvement of spatial prediction accuracy of basal area and volume did not occur in all methods, and there is not always a spatial dependency structure in the residuals of a spatial prediction method." [p. 15]
