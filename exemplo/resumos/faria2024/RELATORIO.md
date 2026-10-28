# RELATÓRIO — Luana Duarte de Faria (2024)

## 1. Referência

Faria, L.D.; Matricardi, E.A.T.; Marimon, B.S.; Miguel, E.P.; Marimon Junior, B.H.; Oliveira, E.A.; Prestes, N.C.C.S.; Carvalho, O.L.F. **Biomass Prediction Using Sentinel-2 Imagery and an Artificial Neural Network in the Amazon/Cerrado Transition Region**. *Forests* **2024**, *15*, 1599. DOI: 10.3390/f15091599.

O `TEXTO.txt` está integral (do "Abstract" às referências finais, "20 of 20" [p. 20]) e corresponde ao artigo do DOI informado.

## 2. Pergunta do estudo

É possível estimar a biomassa acima do solo (AGB) de vegetação nativa em uma área de transição Amazônia/Cerrado com dados de campo, índices de vegetação Sentinel-2 e uma rede neural artificial, com acurácia suficiente para monitoramento [p. 2].

## 3. Área e dados

- Área: 18.863,6 km² de ecótono Amazônia/Cerrado, municípios de Gaúcha do Norte, Querência e Ribeirão Cascalheira, Mato Grosso; clima Aw; próximo à Terra Indígena Xingu [p. 3].
- Campo: 12 parcelas permanentes de 100 × 100 m, subdivididas em 60 subparcelas de 100 × 20 m (uma parcela com dimensões diferentes, 180 × 60 m); medições na estação seca (julho a outubro) de 2014, 2018, 2020 e 2021 [p. 3–4]. Distribuição: 1 parcela em 2014, 3 em 2018, 5 em 2020 e 3 em 2021 [p. 4].
- Sensores: 5 cenas Sentinel-2A/MSI, nível 1C (reflectância TOA), todas de agosto (2016 a 2021), processadas no Google Earth Engine [p. 5]. A cena de 2016 foi usada para os dados de campo de 2014 porque não havia imagem Sentinel em 2014 [p. 5].
- Variáveis: 9 índices de vegetação — NDVI, EVI, EVI2, GNDVI, AFRI, MSAVI, NDRE, SAVI e MSAVIaf [p. 5, 8]; AGB de campo por equações alométricas (Chave et al. para fitofisionomia amazônica; Rezende et al. para Cerrado) [p. 4–5].
- Amostragem para modelagem: 40 subparcelas para treino (70% das 60) e 20 para validação/teste [p. 8].

## 4. Método

- Inventário florestal (DAP, altura total, densidade básica da madeira via ForestPlots.net), AGB por equação alométrica e normalização em t·ha⁻¹ [p. 4–5].
- Índices de vegetação calculados no GEE a partir das cenas Sentinel-2; teste de Shapiro–Wilk e matriz de correlação de Spearman (dados não normais), seguida de regressão stepwise para selecionar preditores [p. 5–10].
- Rede neural Multilayer Perceptron (MLP) treinada no Statistica 12 com Intelligent Problem Solver e algoritmo BFGS; entrada = índices + variável categórica de estrato (Floresta Estacional Perenifólia e Cerrado típico); saída = AGB [p. 8].
- Seleção de redes por coeficiente de correlação e RMSE%; validação com teste t de Student e diferença agregada percentual (AD%) [p. 8].

## 5. Resultados principais

- AGB média: 146,86 t·ha⁻¹ nas parcelas de floresta e 18,38 t·ha⁻¹ nas de Cerrado — cerca de oito vezes maior na floresta; DAP médio 19,12 cm vs. 13,81 cm e altura média 13,99 m vs. 6,64 m; densidade da madeira semelhante (0,67 vs. 0,66 g·cm³) [p. 9].
- Em um fragmento florestal na borda sul da área, a AGB variou de 155 a 195 t·ha⁻¹ [p. 9].
- Shapiro–Wilk indicou não normalidade de biomassa e índices; Spearman mostrou correlações positivas e significativas (α < 0,05) entre AGB e todos os índices, com destaque para GNDVI (0,621), SAVI (0,594) e MSAVIaf (0,555); as menores foram MSAVI (0,404) e EVI (0,443) [p. 9–10].
- A stepwise selecionou AFRI, EVI e GNDVI como preditores (α < 0,05) [p. 10].
- Cinco redes tiveram r > 0,90 e erro de validação < 16%; a ANN-1 (MLP 3-12-1, 860 ciclos, ativação tangente nas camadas oculta e de saída) obteve RMSE% de 18,09 (ajuste), 15,76 (validação) e 15,92 (teste), com R = 0,94 no teste [p. 10, 12].
- Teste t de Student: p = 0,952, sem diferença significativa entre observados e estimados [p. 12]. Diferença agregada AD = −0,1637%, indicando leve superestimação [p. 14].
- Biomassa total da vegetação nativa na área de estudo estimada em 109.118.121 t; classes mais frequentes de 0 a 50 t·ha⁻¹, seguidas de 100 a 150 t·ha⁻¹ [p. 14].
- A discussão relata R² de 0,94 e RMSE% de 10,76 para a rede 1, valor que não coincide com os 15,92% da Tabela 5 [p. 12, 16]; afirma também RMSE abaixo de 14% [p. 16].
- Erros da ANN concentrados entre −1,5% e −12% e entre 0% e 10%; erros acima de ±16% pouco frequentes [p. 17].
- Pastagens ocupam quase 16% da área de estudo [p. 15].

## 6. Limitações que os próprios autores reconhecem

- O artigo não tem seção formal de limitações; os reconhecimentos estão dispersos no texto.
- Modelos de aprendizado de máquina "são mais difíceis de interpretar e exigem dados de campo acurados como entrada" [p. 2].
- Descompasso temporal entre campo e imagem: a cena de 2016 foi associada aos dados de 2014 por falta de imagem Sentinel no ano do inventário [p. 5].
- Sugerem que abordagens alternativas, como deep learning e outras técnicas de machine learning, "poderiam ser eficazes" e "deveriam ser exploradas em pesquisas futuras", o que implica que o método aplicado não esgota o problema [p. 17].
- Os dados só estão disponíveis "sob solicitação direta ao autor correspondente" [p. 17].

## 7. O que serve ao projeto e o que não serve

- Serve: o desenho completo de validação para AGB com Sentinel-2 gratuito no GEE — correlação de Spearman para triagem de índices, stepwise para reduzir preditores, MLP com BFGS e validação por t de Student + AD% — replicável para silvicultura em Goiás [p. 8–10, 12].
- Serve: a lista de índices com correlações medidas (GNDVI 0,621; SAVI 0,594; AFRI 0,469; NDVI 0,466) como ponto de partida para seleção de variáveis em plantios [p. 10].
- Serve como referência de ordem de grandeza e de estratificação: floresta ≈ 147 t·ha⁻¹ e Cerrado ≈ 18 t·ha⁻¹, com AGB total de 109.118.121 t na área [p. 9, 14].
- Não serve: o estudo trata só de AGB de vegetação nativa, sem estoque de carbono (fração de carbono, raízes, solo) nem floresta plantada; a amostra é pequena (12 parcelas, 60 subparcelas, 40 para treino) e a área de treino cobre um único ecótono, com inconsistência interna entre RMSE% de 15,92% e 10,76% [p. 8, 12, 16].

## 8. Frases citáveis (literais)

- "Our study results can support the definition of environmental conservation priorities and help set parameters for payment for ecosystem services in environmentally sensitive tropical regions." [p. 1]
- "Moreover, it was determined that a training dataset size of approximately 60 subplots or fewer was sufficient to achieve a good fit with the linear functional model." [p. 17]
