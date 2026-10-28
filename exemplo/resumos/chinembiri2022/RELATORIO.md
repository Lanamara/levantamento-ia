# RELATÓRIO — Tsikai Solomon Chinembiri (2022)

## 1. Referência

Chinembiri, T.S.; Mutanga, O.; Dube, T. (2022). *Landsat-8 and Sentinel-2 Based Prediction of Forest Plantation C Stock Using Spatially Varying Coefficient Bayesian Hierarchical Models*. **Remote Sensing**, 14, 5676. DOI: 10.3390/rs14225676 [p. 1]. O `TEXTO.txt` está íntegro (18 páginas, do resumo às referências) e corresponde ao DOI indicado.

## 2. Pergunta do estudo

Avaliar se modelos Bayesian hierarchical com coeficientes espacialmente variáveis (SVC), alimentados por índices de vegetação de Landsat-8 e de Sentinel-2, superam modelos sem estrutura espacial na predição do estoque de carbono (C) de florestas plantadas, num ambiente submetido a perturbação antrópica desde a reforma agrária de 2000 [p. 1, p. 4].

## 3. Área e dados

- Local: lote 75 A de Nyanga Downs, distrito de Nyanga, Eastern Highlands, província de Manicaland, Zimbábue; cerca de 2.766 ha, entre 32°40′E–32°54′E e 18°10′12″S–18°25′4″S [p. 4].
- Espécies dominantes: *Eucalyptus grandis*, *Eucalyptus camaldulensis* e *Pinus patula* [p. 4].
- Período: inventário de campo de 19/09/2021 a 24/10/2021 [p. 4]; imagens de Landsat-8 OLI e Sentinel-2 MSI de 20/09/2020, com cobertura de nuvem inferior a 10% [p. 9].
- Sensores: Landsat-8 OLI (16 dias de revisita, 30 m nas bandas 1–7 e 9, 15 m na banda 8) e Sentinel-2 MSI (13 bandas: 4 a 10 m, 6 a 20 m, 3 a 60 m), Sentinel-2 em nível 1C, reflectância TOA [p. 8–9].
- Amostras: 191 parcelas circulares de 500 m², árvores com DBH > 10 cm (1,3 m) [p. 4]. Distância mínima entre amostras de aproximadamente 8 m e máxima de 2.500 m [p. 4].
- Preditores: NDVI, SAVI e EVI derivados dos dois sensores [p. 9].

## 4. Método

- Amostragem por cobertura espacial com Mean Squared Shortest Distance (MSSD) e k-means para cobertura de área igual [p. 4]. AGB por equações alométricas (Pinus e Eucalyptus) e conversão para C pelo fator IPCC de 0,47 [p. 5].
- Modelo `y(s) = x(s)′β + x̃(s)′w(s) + ε(s)`, com efeitos aleatórios espaciais `w(s)` vindos de processos gaussianos independentes e função de correlação exponencial; priors normal multivariada para β, inverse-Gamma para as variâncias e uniforme para os decaimentos espaciais [p. 6–7].
- Cinco modelos candidatos por sensor: não espacial, SVI (só o intercepto varia), SVC completo, SVC−β1 (intercepto + NDVI) e SVC−β2 (intercepto + DIST) [p. 8].
- Inferência por MCMC em `spBayes` 0.4.3: três cadeias de 20.000 iterações, convergência (Gelman–Rubin) em 10.000 iterações, inferência sobre 15.000 iterações pós-burn-in [p. 8]. Avaliação por DIC e validação cruzada 10-fold com RMSPE, além de 95% credible interval widths (CIW) [p. 8–9].

Observação de leitura: o texto anuncia cinco modelos [p. 8], mas as tabelas 2 e 3 trazem apenas quatro (não espacial, SVI, SVC−NDVI e SVC) [p. 10], e a variável DIST não é definida em nenhum ponto do artigo.

## 5. Resultados principais

- Só o NDVI foi preditor significativo de C; os intervalos de 95% de SAVI e EVI continham zero e esses índices foram excluídos da predição e do mapeamento finais [p. 9].
- Coeficientes do NDVI (média; IC 95%): 2,47 (0,78–4,62) no modelo Landsat-8 e 4,90 (4,52–5,38) no Sentinel-2 [p. 10].
- RMSPE (Mg C ha⁻¹), Landsat-8: 8 no não espacial, 7,77 no SVI e 6,42 no SVC [p. 1, p. 10]. Sentinel-2: 7,85, 7,69 e 6,23, respectivamente [p. 1, p. 10].
- DIC, Landsat-8: 207 (não espacial), 105,6 (SVI) e 29,0 (SVC); Sentinel-2: 207,6, 112,5 e −177,3 [p. 10].
- Ganho de 10% no RMSPE do modelo Landsat-8 ao passar do erro-independente para o SVC, e de 12% no modelo Sentinel-2 ao passar do SVI para o SVC [p. 13].
- 95% CIW: [1,17–1,60] Mg C ha⁻¹ no SVC Sentinel-2 contra [1,13–1,62] Mg C ha⁻¹ no SVC Landsat-8 [p. 1]. O texto atribui ao Sentinel-2 intervalos "marginalmente mais estreitos" [p. 1].
- C stock observado entre log (0,2–6) Mg C ha⁻¹ [p. 13]; variabilidade da incerteza aproximadamente constante na área estudada para os dois sensores [p. 13].
- O SVC completo teve o menor DIC, D e RMSPE nos dois sensores [p. 13]; β0 do SVC ficou em −3,5 (−5,3 a −1,7) no Landsat-8 e −3,5 (−5,4 a −1,6) no Sentinel-2 [p. 10].
- Contradição interna: a discussão afirma que o RMSPE é "marginalmente maior" no SVC Sentinel-2 que no Landsat-8 [p. 15], enquanto as tabelas registram 6,23 contra 6,42 Mg C ha⁻¹ [p. 10].

## 6. Limitações que os próprios autores reconhecem

- Uso apenas de índices de vegetação como preditores, sem variáveis climáticas e topográficas, o que "pode não ser representativo" da dinâmica geral de C na região; recomendam integrar fatores topo-climáticos em pesquisas futuras [p. 16].
- Estimativas precisas dos parâmetros de covariância são difíceis com amostras pequenas de inventário, com possível impacto na acurácia das predições [p. 15].
- Predições com pouca informação a "emprestar" devido à esparsidade das observações de C, agravada pela redução da amostra na validação cruzada [p. 16].
- A variabilidade quase idêntica entre os dois sensores é atribuída à inadequação das covariáveis no arcabouço de modelagem [p. 14].
- O tamanho amostral pequeno viabilizou o custo computacional; amostras maiores exigiriam operações matriciais de grandes dimensões, inviáveis em PCs comuns [p. 16–17].

## 7. O que serve ao projeto e o que não serve

- Serve: a estrutura SVC bayesiana hierárquica com efeitos aleatórios espaciais trata explicitamente não estacionariedade e dependência residual — exatamente o problema de extrapolar relações empíricas entre índices espectrais e biomassa por todo o estado de Goiás [p. 3, p. 6].
- Serve: o protocolo de avaliação combinado (DIC + 10-fold CV com RMSPE + 95% CIW) é reaproveitável para comparar sensores e conjuntos de preditores, e o achado de que o NDVI carrega quase toda a informação preditiva é um ponto de partida para o desenho de covariáveis [p. 9–10].
- Serve com ressalva: a comparação Landsat-8 (30 m) × Sentinel-2 (10 m) sugere vantagem pequena e estável do Sentinel-2, útil para justificar a escolha de sensor-base antes de acoplar LiDAR ou radar [p. 1, p. 13].
- Não serve: é comparação de dois sensores ópticos usados separadamente, não fusão multissensorial; são apenas três VIs, 191 parcelas, nenhuma métrica de estrutura vertical e nenhuma variável topo-climática, o que não cobre o escopo "multissensorial" nem a escala de Goiás [p. 8–9, p. 16]. Os valores de RMSPE e os coeficientes são locais e não transferíveis.

## 8. Frases citáveis (literais)

- "The Sentinel-2-based SVC model was preferred for prediction in the plantation forest ecosystems as its model provided tighter credible intervals compared to the Landsat-8-based C stock SVC model." [p. 16]
- "As such, the limitation of our study is the application of vegetation indices as predictors of C stock, and this may, therefore, not be representative of the general C stock dynamics in the studied region." [p. 16]
