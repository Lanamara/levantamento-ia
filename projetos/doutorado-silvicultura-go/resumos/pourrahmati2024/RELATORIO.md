# RELATÓRIO — Manizheh Rajab Pourrahmati (2024)

## 1. Referência

**Atenção: o `TEXTO.txt` não é o artigo do DOI indicado no pedido.**

- DOI pedido: 10.1080/01431161.2024.2354072 ("Effects of Eucalyptus plantation characteristics and environmental factors on GEDI waveform metrics", 2024) — **não está no arquivo**.
- Artigo efetivamente presente no `TEXTO.txt`: Rajab Pourrahmati, M.; Le Maire, G.; Baghdadi, N.; Alvares, C. A.; Stape, J. L.; Scolforo, H. F.; Campoe, O. C.; Nouvellon, Y.; Guillemot, J. (2025). "Integrating MODIS-derived indices for eucalyptus stand volume estimation: an evaluation of MODIS gross primary productivity". *Frontiers in Remote Sensing* 6:1588387. DOI 10.3389/frsen.2025.1588387.
- Mesma primeira autora, tema próximo (Eucalyptus, sensoriamento remoto), mas outro artigo, outra revista, outro ano e outro DOI. O arquivo está íntegro (19 páginas, corpo completo + referências), apenas não corresponde ao DOI solicitado.
- As seções 2 a 8 abaixo descrevem **somente** o artigo que está no `TEXTO.txt`. Nada foi preenchido com conhecimento externo sobre o artigo de GEDI.

## 2. Pergunta do estudo

Avaliar se o GPP do produto MODIS MOD17A2HGF v061, após validação contra torre de fluxo, agrega precisão a modelos de volume de povoamentos de Eucalyptus baseados em idade e em índices de vegetação.

## 3. Área e dados

- Local: plantios de Eucalyptus no Mato Grosso do Sul, sudoeste do Brasil (1,3 milhão de ha de plantios; altitude 250–400 m) [p. 4].
- Inventário: parcelas de 400 m², ~1 parcela a cada 10 ha, mais de 7.000 povoamentos medidos, em idades variadas e com remedições [p. 4].
- Torre de fluxo (eddy covariance, projeto EucFlux): 22°58′04″S; 48°43′40″W, 750 m, plantio de 200 ha; medidas contínuas de fevereiro de 2008 a setembro de 2024 [p. 4–5].
- Sensores: MOD17A2HGF v061 (GPP e PSN, composto de 8 dias, 500 m) e MCD43A4 v061 NBAR (NDVI, 500 m, interpolado e suavizado por Savitzky-Golay) [p. 5].
- Amostra após filtro de pixels com ≥90% de sobreposição a um único povoamento: 4.130 pixels em 1.303 povoamentos [p. 6].
- Idades de 1,6 a 8,4 anos; subgrupos com n = 4.130 (todas), 2.488 (>3 anos), 1.582 (>4 anos) e 933 (>5 anos) [p. 6].

## 4. Método

- Validação do GPP MODIS contra GPP da torre de fluxo, agregando dados de meia hora em períodos de 8 dias, com RMSE e R² [p. 5–6].
- Cálculo de índices cumulativos por povoamento, do plantio até a data de medição (Cgpp, Cpsn, Cndvi_L, Cndvi_S) e até 1–5 anos após o plantio (CgppNY, CpsnNY, CndviNY), sempre com a variável Age [p. 6–7].
- Três modelos: multiple linear regression (MLR) com PCA para colinearidade, random forest (RF) e stochastic gradient boosting (SGB), com ajuste de hiperparâmetros por RandomizedSearchCV [p. 7].
- Validação cruzada de cinco folds e métricas RMSE, rRMSE e R² [p. 7–8].

## 5. Resultados principais

- MODIS vs. torre de fluxo: R² = 0,38 e RMSE = 19,65 gC m⁻² 8 dia⁻¹; subestimativa nos picos de produtividade e superestimativa no início do ciclo [p. 8]; rRMSE = 30,64% [p. 14].
- Correlação do volume com variáveis isoladas: Cndvi R² = 0,81; Age R² = 0,78; Cgpp R² = 0,74; Cpsn R² = 0,52 [p. 8].
- Melhor modelo com variáveis só na data de medição (n = 4.130): RF com RMSE 27,90 m³ ha⁻¹, rRMSE 21,15% e R² = 0,85 [p. 9].
- Melhor MLR (quatro componentes principais): RMSE 29,59 m³ ha⁻¹, rRMSE 22,43%, R² = 0,83; o PCA reduziu o VIF a 1 (VIF originais: 38,66 para Cgpp, 11,83 para Cpsn, 101,32 para Cndvi e 77,29 para Age) [p. 9].
- Acrescentar índices cumulativos do 1º ano elevou o SGB a RMSE 22,63 m³ ha⁻¹, rRMSE 17,15% e R² = 0,90, ganho de 19,67% em rRMSE; o RF ficou em RMSE 25,42 m³ ha⁻¹ e R² = 0,87 [p. 9; Tabela 3, p. 12].
- Ajuste de hiperparâmetros no SGB: RMSE de 26,00 para 22,63 m³ ha⁻¹ (13%) e R² de 0,87 para 0,90 [p. 9].
- Povoamentos >3 anos: SGB com RMSE 23,55 m³ ha⁻¹, rRMSE 13,52% e R² = 0,84 [p. 10]; ganhos de 20,35%, 7,83% e 5,12% ao somar índices até 1, 2 e 3 anos [p. 16].
- Povoamentos >4 anos: SGB com RMSE 27,38 m³ ha⁻¹, rRMSE 13,62% e R² = 0,73 [p. 13].
- Povoamentos >5 anos: melhor SGB com RMSE 31,82 m³ ha⁻¹, rRMSE 14,30% e R² = 0,61 [p. 15].
- LUE usada pelo MODIS para florestas latifoliadas perenes: ~0,57 gC MJ⁻¹, contra 1,59–1,97 gC MJ⁻¹ medidos em plantios brasileiros de eucalipto [p. 14].

## 6. Limitações que os próprios autores reconhecem

- A análise não foi estendida a povoamentos com mais de 6 anos porque o número de amostras cai muito e compromete a confiabilidade [p. 7].
- A redução amostral com a idade (4.130 → 2.488 → 1.582 → 933) pode afetar a robustez e a generalização dos modelos para povoamentos mais velhos [p. 16].
- O GPP do MODIS é ruidoso e pouco acurado no primeiro ano após a colheita, por causa de dossel esparso e mudanças fisiológicas rápidas [p. 17]; o FPAR é apontado como o gargalo da estimativa de GPP [p. 14].
- Não foi feita análise de incerteza; os autores afirmam que ela seria necessária para quantificar erros sistemáticos e ruído aleatório do produto [p. 17].
- Os dados não podem ser compartilhados pelos autores (declaração de disponibilidade de dados) [p. 17].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o desenho de usar séries temporais cumulativas de índices MODIS somadas à idade, com RF e SGB e validação cruzada de cinco folds, é diretamente replicável para volume de eucalipto em Goiás.
- **Serve:** o achado de que os índices cumulativos dos dois primeiros anos carregam a maior parte do ganho preditivo (19,67% de redução de rRMSE) orienta a janela temporal mínima de aquisição de dados.
- **Serve (com cautela):** o GPP MODIS não deve entrar como proxy direto de carbono estocado; o viés de LUE (0,57 vs. 1,59–1,97 gC MJ⁻¹) exige calibração local com torre de fluxo antes de qualquer uso em estoque de carbono.
- **Não serve:** o estudo é no Mato Grosso do Sul (não em Goiás), estima volume de madeira e não biomassa/estoque de carbono, não usa GEDI nem LiDAR, e a resolução de 500 m limita a aplicação a talhões grandes e homogêneos [p. 6].

## 8. Frases citáveis (literais)

- "These results highlight the importance of cumulative indices from earlier growth stages in improving the overall prediction accuracy." [p. 9]
- "This difference in LUE values contributes to the MODIS underestimation of GPP, especially in Eucalyptus plantations when canopy photosynthesis is at its maximum." [p. 14]
