# RELATÓRIO — Sanjiwana Arjasakusuma (2026)

## 1. Referência

Sanjiwana Arjasakusuma, Marzuki Marzuki, Projo Danoedoro, Danang Sri Hadmoko, Wirastuti Widyatmanti, Muhammad Arrafi, Yanuar Vira Febiyanti, Putri Laila Kartika Ningrum, Ratih Solichia Maharani & Agus Justianto (2026). "Comparison of shallow and deep learning methods for LiDAR-based aboveground biomass estimation of eucalyptus plantations in Ibu Kota Nusantara, East Kalimantan Province, Indonesia". *European Journal of Remote Sensing*, 59(1), 2733157. DOI: 10.1080/22797254.2026.2733157.

O `TEXTO.txt` contém o artigo integral (19 páginas, incluindo referências) e o DOI confere com o solicitado [p. 1–2].

## 2. Pergunta do estudo

Comparar modelos de *shallow learning* e de *deep learning* — inclusive arquiteturas CNN com módulos KAN e *squeeze-and-excitation* — na estimativa de AGB por árvore individual a partir de métricas LiDAR (CHM, SHM, IM e LMOM) em plantio de eucalipto [p. 2–3].

## 3. Área e dados

- **Local:** Floresta Ibu Kota Nusantara (gerida pela Universitas Gadjah Mada), cidade de Nusantara, Kalimantan Oriental, Indonésia; 600 hectares de plantio de eucalipto, elevação de 50 a 200 m [p. 3].
- **Período:** datas de aquisição LiDAR e de campo não informadas; apenas submissão em 10/10/2025, revisão em 14/07/2026 e aceite em 10/09/2026 [p. 2].
- **Sensor LiDAR:** DJI Zenmuse L1 (904 nm) em UAV DJI Matrice 300 RTK, 6 missões de voo a 150 m AGL, *side-lap* de 50%, densidade de ~100–200 pontos/m², georreferenciamento por PPK/CORS [p. 4–5].
- **Amostras de campo:** 17 parcelas de 30 × 30 m em amostragem aleatória estratificada (estratos por índices de vegetação de imagem de satélite); DAP medido a 1,3 m para árvores com diâmetro > 10 cm; total de 362 árvores [p. 5]. Imagens PlanetScope citadas apenas como base visual/estratificação [p. 3].
- **Variáveis:** 62 métricas LiDAR em pixel de 1 × 1 m — 44 SHM, 4 LMOM, 13 IM e 1 CHM [p. 6]; após estatística zonal por copa, vetor de 744 dimensões por árvore [p. 7]; RFE reduziu a 100 variáveis no cenário "with variable importance" [p. 11].
- **Referência de AGB:** equação alométrica de eucalipto industrial, AGB = 0,499·D^2,863 + 6,136 (kg/árvore, D em cm) [p. 5].

## 4. Método

- Pré-processamento LiDAR no `lidR`: remoção de ruído por SOR, solo por PMF, DSM/DTM por KNN-IDW, CHM = DSM − DTM; segmentação de copas por máximos locais + MCWS (*ForestTools*) [p. 5–6].
- *Shallow learning*: Random Forest, Extra Trees, Gradient Boosting, XGBoost, LightGBM, SVR e Lasso; *grid search* com validação cruzada 5-fold [p. 7].
- *Deep learning*: MLP, CNN1D, CNN2D e variações com MLP, atenção, SE e módulo KAN (*Efficient-KAN*, B-splines nas arestas); Optuna/TPE para hiperparâmetros (dimensão oculta 64/128/256, grid 3–10, ordem de spline 2–5) [p. 7].
- Protocolo: divisão treino/teste 80:20 fixa, 5-fold, semente 42, alvo em log(1+x), AdamW (lr 0,0001), *batch* 32, perda combinada MSE+MAE, *early stopping*; métricas R² (escala log), MAE e RMSE (escala original) [p. 7–8].

## 5. Resultados principais

- Melhor *shallow learning*: LightGBM com seleção de variáveis, test R² = 0,63 e RMSE = 43,83 kg/árvore [p. 12]; sem seleção, R² = 0,59 e RMSE = 43,89 kg/árvore [p. 12].
- XGBoost: test R² = 0,62 e RMSE = 44,28 kg/árvore; GradientBoosting 0,61 e 44,46; RandomForest 0,61 e 44,78; ExtraTrees 0,56 e 44,99 [p. 12]. Faixa dos ensembles: R² de 0,56 a 0,63 com RMSE ≈ 44 kg/árvore [p. 15].
- Modelos lineares/kernel fracos: SVR test R² = 0,10 sem seleção e −0,03 com seleção; Lasso test R² = 0,06 e RMSE = 100,80 kg/árvore sem seleção, passando a R² = 0,62 e RMSE = 43,98 com seleção [p. 12].
- CNNs convencionais: test R² de 0,19 a 0,46 e RMSE de 45,65 a 50,56 kg/árvore, com R² de treino negativo em vários casos (CNN1D: treino −0,86; teste 0,39) [p. 13; p. 17].
- KAN sem seleção: CNN1D+KAN test R² = 0,52 (RMSE 45,78) e CNN2D+KAN 0,44 (RMSE 45,13); com SE, CNN1D+KAN+SE 0,59 (RMSE 45,02) e CNN2D+KAN+SE 0,55 (RMSE 45,69); faixa consolidada de R² 0,44–0,59 com RMSE de 45,02 a 45,78 kg/árvore [p. 13; p. 17].
- Melhor resultado geral: CNN1D+KAN+SE com seleção de variáveis, test R² = 0,65, MAE = 27,14 e RMSE = 42,13 kg/árvore — porém com treino instável (R² de treino −5,69 ± 5,42) [p. 13].
- Seleção por importância degradou quase todo o *deep learning*: CNN1D caiu de 0,39 para −0,12; CNN2D+KAN chegou a test R² = −9,9 [p. 13].
- Optuna: CNN2D+KAN e CNN2D+KAN+SE atingiram R² = 0,56 (RMSE 44,96 e 44,68); CNN1D+KAN caiu de 0,52 para 0,40 e CNN1D+KAN+SE de 0,59 para 0,44 [p. 14].
- Custo computacional: CNN1D+KAN 1.284–1.294 s de treino; CNN2D+KAN 133–172 s; LightGBM 175 s; CNNs convencionais 30–211 s [p. 14; p. 17].
- Importância de variáveis: métricas de intensidade (IM) dominam, com `ipcumzq10_sum`, `ipground_sum` e `pground_sum` no topo; SHM vêm depois e LMOM contribuem pouco [p. 11].
- Produtos intermediários: DTM/DSM de 50 a 131 m e CHM com máximo de 69 m; copas acima de 2 m segmentadas [p. 10–11].

## 6. Limitações que os próprios autores reconhecem

- Base de 362 árvores de um único plantio de eucalipto, o que limita a generalização para florestas tropicais estruturalmente mais complexas; recomendam conjuntos mais diversos e validação entre sítios [p. 17].
- AGB de referência derivada de uma única equação alométrica, o que introduz incerteza nos rótulos e pode limitar a acurácia, sobretudo em modelos de *deep learning* mais sensíveis a ruído de rótulo [p. 17].
- Seleção de variáveis avaliada por eliminação, não por transformação; sugerem testar PCA ou *embeddings* não lineares [p. 17].
- O KAN exige ajuste cuidadoso e apresentou instabilidade de treino (R² de treino negativo), além de custo computacional dependente da dimensionalidade da entrada no spline; o Optuna adiciona custo único elevado [p. 14; p. 15; p. 17].
- O modelo CNN2D+KAN gerou previsões extremas acima de 1000 kg/árvore, associadas a incerteza na segmentação de copas e à escassez de amostras de alta biomassa [p. 15].
- Modelos de *deep learning* mostraram-se menos robustos que os ensembles, exigindo estimativa de incerteza, restrições de predição e regularização [p. 15; p. 17].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o desenho de comparar *shallow* vs *deep learning* sobre o mesmo conjunto de métricas e mesma partição 80:20 é replicável para eucalipto em Goiás e dá linha de base (ensembles com test R² 0,56–0,63 e RMSE ≈ 44 kg/árvore) [p. 12; p. 15].
- **Serve:** a constatação de que métricas de intensidade LiDAR superam SHM e LMOM em importância é transferível ao desenho de atributos para silvicultura, assim como o uso de CHM/SHM/LMOM/IM combinados (62 métricas, 744 dimensões por copa) [p. 6–7; p. 11].
- **Serve (com cautela):** o fluxo de segmentação individual de copas (máximos locais + MCWS) e a equação alométrica DAP→AGB fornecem estrutura metodológica, mas ambos precisam de recalibração local, pois a equação usada é de outra região e a segmentação é fonte declarada de erro [p. 5; p. 15].
- **Não serve:** a hierarquia de modelos não se transfere automaticamente — o *deep learning* só competiu após seleção agressiva de variáveis e mesmo assim com treino instável; para o projeto, o ganho de R² (0,65 vs 0,63) é marginal frente ao custo (até ~1.294 s de treino) e ao risco de extrapolação [p. 13; p. 14; p. 15].

## 8. Frases citáveis (literais)

- "LightGBM provides greater prediction stability and controlled extrapolation, making it highly reliable for operational applications with limited training samples." [p. 15]
- "The analysis was based on 362 field-measured trees from a single Eucalyptus plantation, which may limit the generalizability of the findings to more structurally complex tropical forests." [p. 17]
