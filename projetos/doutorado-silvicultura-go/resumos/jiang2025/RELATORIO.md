# RELATÓRIO — Fugen Jiang (2025)

## 1. Referência

Fu-Gen Jiang, Ming-Dian Li e Si-Wei Chen (2025). *Adaptive Gaussian-PSO XGBoost Model for Alpine Forests Aboveground Biomass Estimation Using Spaceborne PolSAR and LiDAR Data*. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, vol. 18, pp. 10157–10171. DOI: 10.1109/JSTARS.2025.3559233 [p. 1]. O `TEXTO.txt` está íntegro (inclui referências e biografias dos autores) e corresponde ao DOI indicado.

## 2. Pergunta do estudo

Saber se um XGBoost cujos hiperparâmetros são otimizados por um PSO com peso de inércia adaptativo (função gaussiana) e alimentado pela combinação de PolSAR orbital (Sentinel-1 C e ALOS-2 L) com LiDAR orbital ICESat-2 estima com maior acurácia a AGB de florestas naturais alpinas do leste do Planalto Tibetano do que fontes isoladas e modelos clássicos [p. 1–2].

## 3. Área e dados

- Local: área do Natural Forest Resources Protection Project (NFRPP), leste da Região Autônoma do Tibet, China, 97°20′–99°06′E, 28°41′–32°32′N; altitude de 2122 a 5913 m; temperatura média anual de 7,6 °C e precipitação média anual de cerca de 477,7 mm [p. 3].
- Período: dados de 2019 (base FMI 2019, Sentinel-1 2019, ALOS-2 2019, ATL08 2019) [p. 3–4].
- Fontes: Sentinel-1 C-band dual-pol (VV/VH, 10 m) [p. 4]; ALOS-2/PALSAR-2 mosaic L-band (HH/HV, ~25 m) [p. 4]; ICESat-2 ATL08 (pegadas de ~17 m de diâmetro) [p. 4–5]; DEM para fatores topográficos [p. 9].
- Amostras: 841 amostras de AGB (pinheiro-alpino, abeto, larício e pícea) obtidas da base FMI via biomass expansion factor; AGB entre 100 e 250 Mg/ha, média de 143,06 Mg/ha e desvio padrão de 37,91 Mg/ha [p. 4]. Divisão de 80% treino e 20% teste [p. 7].
- Variáveis: 80 feições de textura GLCM por sensor (8 texturas × 5 janelas de 3×3 a 11×11) mais retroespalhamento; 15 variáveis LiDAR [p. 4–5].

## 4. Método

- Extração de feições: coeficientes de retroespalhamento e oito feições de textura GLCM (mean, variance, homogeneity, contrast, dissimilarity, entropy, second moment, correlation) em cinco tamanhos de janela [p. 4].
- Seleção de variáveis: ranking por %IncMSE e stepwise random forest (SRF) para definir os conjuntos Sentinel-1, ALOS-2, ICESat-2 e conjunto conjunto (joint) [p. 5].
- Modelo proposto (AGP-XGBOOST): peso de inércia do PSO dado por ω = (ωmax − ωmin)·e^(−α·(t/tmax)²) + ωmin, com coeficiente adaptativo α, otimizando n_estimators (1–500), max_depth (≤10) e learning_rate (0,01–0,3) [p. 6].
- Validação e comparação: R² e RMSE em treino/teste contra BPNN, kNN, ELM e SVM; mapeamento wall-to-wall acoplando as melhores predições às feições ALOS-2 contínuas e análise por gradientes de elevação, declividade e exposição [p. 7, 9].

## 5. Resultados principais

- Na otimização de hiperparâmetros do conjunto joint, as PSOs lineares, exponencial e parabólica reduziram o RMSE em 7,7% e 9% frente ao XGBoost com hiperparâmetros padrão; a PSO gaussiana obteve os menores RMSEs e, com α = 5, o mínimo em apenas 12 iterações [p. 9].
- Sentinel-1: RMSE de 29,95 a 36,01 Mg/ha; o AGP-XGBOOST com VV+VH reduziu o RMSE em 13,1% e 9,7% frente a VH e VV isolados; BPNN, kNN e ELM ficaram com R² abaixo de 0,1 [p. 9].
- ALOS-2: HH+HV reduziu o RMSE em 14,7% e 13,4% frente às polarizações simples; melhor resultado com R² = 0,47 e RMSE = 27,43 Mg/ha; os RMSEs de BPNN, kNN, ELM, SVM e AGP-XGBOOST caíram 4%, 11,2%, 11,3%, 7,3% e 8,4% em relação ao Sentinel-1 [p. 9].
- ICESat-2 isolado: RMSEs entre 20 e 25 Mg/ha; o AGP-XGBOOST reduziu o RMSE em 30,8% e 24,4% e o erro absoluto médio em 30,7% e 23,7% frente a Sentinel-1 e ALOS-2 [p. 8–9].
- Conjunto ALOS-2 + ICESat-2: R² = 0,76 e RMSE = 18,64 Mg/ha, com redução de 10,1% no RMSE e 9,0% no erro absoluto médio frente ao ICESat-2 isolado; a maioria dos RMSEs ficou abaixo de 20 Mg/ha [p. 8–9].
- Frente a estudo anterior com Sentinel-2 + ICESat-2 (RMSE = 25,14 Mg/ha), a combinação ALOS-2 + ICESat-2 reduziu o erro em 25,9% [p. 11].
- `Height_98th` foi a variável mais importante e apresentou correlação de 0,72 com a AGB [p. 8, 12].
- Mapeamento: maiores AGB no leste e sudoeste, menores no oeste e centro; os fatores topográficos tiveram correlação significativa (P < 0,01), mas com coeficientes baixos [p. 9]. A AGB concentrou-se entre 3500 e 4500 m, com máximo em 3900–4100 m, e a maioria entre 25° e 35° de declividade [p. 11].

## 6. Limitações que os próprios autores reconhecem

- O formato de mosaico anual do PALSAR-2 pode perder mudanças florestais causadas por desastres naturais ou atividades humanas dentro do ano [p. 13].
- O conjunto de dados contém apenas amplitude, sem fase, o que impede extrair feições de decomposição polarimétrica mais sensíveis aos parâmetros florestais [p. 13].
- Com α = 1 o PSO não percorre toda a faixa de pesos de inércia, podendo cair em ótimo local; recomendam testar mais valores de α [p. 13].
- As flutuações locais de elevação introduzem incerteza nas métricas de altura do ICESat-2, sendo necessário corrigir a deformação das pegadas [p. 14].
- A cobertura de produtos SAR de onda longa em larga escala ainda é limitada [p. 13].

## 7. O que serve ao projeto e o que não serve

- Serve: o pipeline é replicável e barato — texturas GLCM em múltiplas janelas, seleção por %IncMSE/SRF e ajuste de hiperparâmetros por PSO gaussiano, implementado nos pacotes R `xgboost` e `psoptim` [p. 6] — e pode ser aplicado a povoamentos de silvicultura em Goiás com ICESat-2/GEDI e SAR.
- Serve: a hierarquia empírica de acurácia (LiDAR de dossel 18,64 Mg/ha > L-band 27,43 Mg/ha > C-band ~30–36 Mg/ha) [p. 8–9] justifica priorizar métricas de altura do dossel na modelagem do projeto.
- Serve: o uso de textura de polarização cruzada como variável dominante em SAR, mais informativa que o retroespalhamento puro [p. 8], é transferível ao mapeamento de plantios.
- Não serve: o objeto é floresta natural alpina mista sob clima temperado subúmido, com AGB de 100 a 250 Mg/ha [p. 3–4], sem talhadia, idade, espaçamento ou manejo silvicultural; o artigo trata só de AGB, sem estoque de carbono, densidade da madeira ou fatores de expansão detalhados, e não usa GEDI nem dados ópticos.

## 8. Frases citáveis (literais)

- "The longer wavelengths of ALOS-2 provide stronger penetration capabilities, capturing richer internal forest structure information." [p. 11]
- "Spaceborne LiDAR can provide metrics highly correlated with the vertical structure of forests, enhancing forest AGB estimation." [p. 9]
