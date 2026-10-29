# RELATÓRIO — Shashika Himandi Gardeye Lamahewage (2025)

## 1. Referência

Lamahewage, S.H.G.; Witharana, C.; Riemann, R.; Fahey, R.; Worthley, T. **Comparing Machine Learning and Statistical Models for Remote Sensing-Based Forest Aboveground Biomass Estimations.** *Forests* **2025**, 16, 1430. Publicado em 7 de setembro de 2025. DOI: 10.3390/f16091430.

## 2. Pergunta do estudo

Comparar sistematicamente a acurácia de estimativa de AGB de algoritmos de machine learning (RF e SVM) com a de métodos estatísticos convencionais (MLR) usando variáveis multissensoriais de sensoriamento remoto e dados de um único ano do inventário FIA [p. 1].

## 3. Área e dados

- Local: área florestal do estado de Connecticut, EUA (41,6° N, 72,7° W); ~58% do território é floresta sob definição FIA e ~1,8 milhão de acres de floresta [p. 3].
- Período: 2016, ano único, escolhido para alinhar com a missão LiDAR estadual [p. 3].
- Fontes: LiDAR aerotransportado leaf-off de 2016 com densidade de 2 pontos/m² [p. 4]; imagens NAIP leaf-on de 2016 [p. 4]; imagens Sentinel-2 da primavera de 2016 com cobertura de nuvens ≤10% [p. 4]; dados de campo do FIA (USFS), com AGB calculada pelo *component ratio method* (CRM) e apenas árvores com dbh ≥12 cm [p. 4].
- Amostras: 320 parcelas FIA existentes em CT, das quais 42 parcelas medidas em 2016, gerando 168 subparcelas; após remoção de outliers, 142 subparcelas [p. 3–4]. O teste final usou 20% dos dados (n = 28) [p. 9].
- Preditores: 65 variáveis raster (LiDAR, NAIP, Sentinel-2) [p. 5–6].

## 4. Método

- Geração de 65 preditores em buffer de 2,4 km (1,5 milha) das parcelas FIA públicas; cientistas do FIA extraíram os valores nas coordenadas reais das subparcelas [p. 4].
- Seleção de variáveis por critério distinto em cada modelo: IncNodePurity para RF, *recursive feature elimination* (RFE) para SVM, e VIF < 10 seguido de *stepwise regression* por AIC e *best subset* para MLR [p. 5, 8–9].
- Divisão 80:20 (treino/teste), validação por *k-fold cross-validation* (5 folds no ajuste, 10 folds na seleção de variáveis do SVM) e *grid search* de hiperparâmetros; LOOCV para o ensemble [p. 6, 13].
- Ensemble linear empilhado (MLRE) por mínimos quadrados ordinários sobre as predições de RF, SVM e MLR, com termos de interação [p. 9].

## 5. Resultados principais

- RF ajustado (grupo com as 65 variáveis): RMSE 27,19 Mg ha⁻¹, MSE 739,46 (Mg ha⁻¹)², R² 0,41, com 28 variáveis [p. 10, 15].
- Das 28 variáveis do RF, 68% foram derivadas de LiDAR, 18% de NAIP e 14% de Sentinel-2; as três mais importantes foram P95th, P90th e sen_swir [p. 10].
- SVM: RFE retornou 44 variáveis com RMSE 20,51 Mg ha⁻¹, MAE 16,69 Mg ha⁻¹ e R² 0,25 no reamostragem [p. 10]; o modelo final (kernel linear, C = 0,01, γ = 0,0154, ε = 0,1, 108 vetores de suporte) teve MSE 1034,59 (Mg ha⁻¹)², RMSE 32,17 Mg ha⁻¹, MAE 22,36 Mg ha⁻¹ e R² 0,10 [p. 10, 15].
- MLR por *stepwise*: 5 variáveis, AIC 728,06, F = 9,41, p = 1,77 × 10⁻⁷, R² de teste 0,15 e RMSE 23,53 Mg ha⁻¹ [p. 12].
- MLR por *best subset*: 8 variáveis, R² de teste 0,22, RMSE 22,59 Mg ha⁻¹, RSE 21,12 Mg ha⁻¹, F = 6,982, p = 2,296 × 10⁻⁷ [p. 13, 15].
- Ensemble linear: R² 0,79, RMSE 7,12 Mg ha⁻¹ e MSE 142,41 (Mg ha⁻¹)² em LOOCV [p. 13–14]; a Tabela 6 registra RMSE 11,13 Mg ha⁻¹ e MSE 123,85 (Mg ha⁻¹)² para o mesmo ensemble [p. 15].
- ANOVA unifatorial: RF difere do MLR (p = 1,28 × 10⁻⁹) [p. 14]; SVM marginalmente significativo frente ao RF (p = 0,0509); RF e ensemble não diferem estatisticamente (p = 0,6210) [p. 15].
- O RF apresentou o maior R², mas o MLR apresentou menor RMSE (22,59 contra 27,19 Mg ha⁻¹) [p. 14].

## 6. Limitações que os próprios autores reconhecem

- Falta de dados de teste impediu comparar e generalizar o ensemble frente aos três modelos: "due to a lack of data testing, we were not able to compare and generalize the linear ensemble method with the other three models" [p. 14].
- O ensemble foi treinado, direta ou indiretamente, sobre todo o conjunto disponível; generalização estadual exigiria dados independentes do treinamento dos quatro modelos [p. 9].
- Tamanho amostral pequeno e dados FIA de um único ano limitam a generalização do ensemble a outras regiões ou tipos florestais [p. 18–19].
- Construção do ensemble é complexa e computacionalmente intensiva, e requer um conjunto separado de parcelas FIA independentes para comparação justa [p. 17].
- Coordenadas FIA públicas são deslocadas em até 1,6 km e até 20% das parcelas privadas são trocadas; por isso recomendam 30 m e não 15 m de resolução, dado erro de geolocalização de 8 m (±2 m) [p. 17].
- Usaram VIF de 10, embora a recomendação geral seja abaixo de 5, por limitação do tamanho do conjunto [p. 17].
- Variáveis ruidosas podem distorcer o hiperplano do SVM e explicar seu baixo desempenho frente ao RF [p. 16].
- Os dados de treinamento não podem ser compartilhados por política de proteção dos proprietários FIA [p. 19].

## 7. O que serve ao projeto e o que não serve

- Serve: o protocolo de seleção de variáveis e ajuste de hiperparâmetros (IncNodePurity + CV + grid search) é diretamente transferível a modelos de AGB em povoamentos de Goiás, sobretudo com poucas parcelas [p. 7, 16].
- Serve: a evidência de que métricas de altura LiDAR dominam a predição (68% das 28 variáveis; P95th e P90th no topo) sustenta a prioridade de LiDAR aerotransportado no desenho amostral do projeto [p. 10, 16].
- Serve: a recomendação de 30 m como menor pixel viável dado erro de geolocalização de 8 m (±2 m) é referência útil para definir a resolução dos mapas de estoque de carbono [p. 17].
- Não serve: o contexto é floresta temperada mista de Connecticut, com FIA/CRM, sem qualquer dado de Goiás, de silvicultura plantada ou de eucalipto; o artigo não usa Sentinel-1/SAR nem GEDI, e a comparação SVM/MLR tem baixo poder estatístico (n = 28 no teste), o que limita transpor os rankings de modelo [p. 3–4, 9].

## 8. Frases citáveis (literais)

- "The hyperparameter-tuned RF model produced a root mean square error (RMSE) of 27.19 Mgha−1 and an R2 of 0.41, which outperformed the evaluation metrics of SVM and MLR models." [p. 1]
- "But we recommend estimations for 30 m resolution since the 2016 FIA dataset can potentially have a geolocation error of 8 m (±2 m)." [p. 17]
