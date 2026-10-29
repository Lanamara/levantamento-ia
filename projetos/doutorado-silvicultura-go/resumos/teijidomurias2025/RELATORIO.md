# RELATÓRIO — Iyán Teijido-Murias (2025)

## 1. Referência

Teijido-Murias, I.; Barrio-Anta, M.; López-Sánchez, C.A. (2025). Sentinel-1 and Sentinel-2 data for predicting forest stand variables in GEE: A case study of timber plantations in northern Spain. *Forest Systems*, 34(3), 20986. DOI: 10.5424/fs/2025343-20986. Recebido em 04/12/2024, aceito em 14/05/2025, publicado em 27/11/2025 [p. 2].

O `TEXTO.txt` está íntegro — vai da Introdução às Referências [p. 1–12] — e corresponde ao DOI informado. Há apenas um bloco de parágrafos repetido por falha de extração [p. 5], sem perda aparente de conteúdo.

## 2. Pergunta do estudo

Construir modelos de machine learning, no Google Earth Engine, com dados Sentinel-1 (radar), Sentinel-2 (óptico) e variáveis auxiliares de terreno e clima, para estimar biomassa aérea (AGB), área basimétrica (G), altura dominante (H0), número de árvores por hectare (N) e volume total com casca (TV) em plantações de *Eucalyptus globulus*, *Pinus pinaster* e *Pinus radiata* no norte da Espanha [p. 3].

## 3. Área e dados

- **Local:** norte da Espanha (Asturias, Cantabria, País Basco e Galiza), 52.821 km², clima temperado, altitude de 0 a 2.650 m [p. 3].
- **Período:** parcelas do Inventário Florestal Nacional espanhol (SNFI-4.5) medidas em meados de 2018; imagens Sentinel selecionadas para 2018 [p. 3, 5].
- **Fontes:** Sentinel-1 SAR GRD (banda C) e Sentinel-2 MSI Level 1C harmonizado, ambos no repositório do GEE [p. 3]; DEM de 5 m (CNIG) e 5 variáveis climáticas do Atlas Climático Digital da Península Ibérica, a 200 m [p. 3]; todas as variáveis reamostradas a 10 m [p. 4].
- **Amostras:** 1.471 parcelas puras (≥80% da área basimétrica da espécie-alvo): 589 de *E. globulus*, 474 de *P. pinaster* e 408 de *P. radiata* [p. 3]; após filtragem, os modelos usaram 544, 415 e 381 parcelas, respectivamente [p. 7].

## 4. Método

1. Pré-processamento no GEE: S1 com correção de ruído de borda, filtro de speckle e normalização radiométrica de terreno (Mullissa et al., 2021) [p. 5]; S2 com correções atmosférica, topográfica e BRDF (Teijido-Murias et al., 2024) [p. 5].
2. Variáveis derivadas: 2 índices SAR (RVI, VDDPI) e 4 operações entre bandas VV/VH [p. 4–5]; 21 índices espectrais e 18 variáveis de textura baseadas em NDVI [p. 5]; estatísticas zonais por parcela [p. 5].
3. Redução de dimensionalidade por métodos Wrapper no Weka 3.8, ajuste de `mtry` e `Nvar` no pacote `caret` do R 4.4.2 e ajuste final dos Random Forest no GEE [p. 5].
4. Validação: 10-fold cross-validation repetido 10 vezes (100 iterações de modelo), com R² para regressão não linear (Ryan, 1997), Bias, Bias%, RMSE, RMSE% e importância relativa de variáveis (VIMR) [p. 5].

## 5. Resultados principais

- Piores ajustes: N, com R² de 0,12 a 0,27 e RMSE% de 51,5% a 68,6%; em seguida H0, com R² de 0,33 a 0,38 e RMSE% de 22,9% a 30,4% [p. 7].
- Melhores ajustes: TV, AGB e G, com R² acima de 0,39, exceto G de *P. radiata* (R² 0,37); R² máximo de 0,45 e RMSE% de 38,1% a 62,0% [p. 7].
- TV: R² 0,445 (*E. globulus*), 0,415 (*P. pinaster*) e 0,398 (*P. radiata*) [p. 7].
- AGB: R² 0,434 com RMSE% 62,03% (*E. globulus*), 0,394 com 58,15% (*P. pinaster*) e 0,37 com 47,24% (*P. radiata*, `mtry` = 2 e `Nvar` = 2) [p. 7].
- Viés: Bias% entre -0,017% e 0,001%, média de -0,005%, modelos considerados não viesados [p. 7].
- Importância relativa média (VIMR): bandas espectrais 39,11%; índices espectrais 25,69%; textura 11,69%; terreno 10,63%; clima 7,62%; índices radar 3,55%; bandas radar 1,71% [p. 7].
- O Sentinel-2 acumula de 58,96% a 73,70% da VIMR por espécie [p. 8]; o conjunto radar acumula 5,26%, com máximo de 9% (banda radar no modelo de AGB de *E. globulus*) [p. 8–9].
- Valores médios observados (Tabela 2): AGB de 99,44 Mg ha⁻¹ (*E. globulus*), 92,26 (*P. pinaster*) e 127,43 (*P. radiata*); TV de 148,42, 164,05 e 246,23 m³ ha⁻¹ [p. 4].

## 6. Limitações que os próprios autores reconhecem

- A principal limitação declarada é a dificuldade de obter imagens sem nuvens [p. 10].
- O GEE não aceita imagens Single Look Complex (SLC), o que impede análises interferométricas, polarimétricas e de tomografia na plataforma [p. 10].
- A inclusão das bandas radar não melhorou os modelos em relação ao estudo anterior apenas com óptico (Novo-Fernández et al., 2024) [p. 9].
- A banda C do Sentinel-1 não é a usual para estrutura florestal; as bandas L e X permitiriam obter biomassa e alturas interferométricas, respectivamente [p. 9].
- Topografia acidentada (layover e foreshortening) e o efeito speckle degradam a informação radar na área de estudo [p. 3, 9].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o desenho de validação (10-fold repetido 10 vezes, 100 iterações, Bias% e RMSE% reportados junto ao R²) e o uso de VIMR para justificar a seleção de preditores [p. 5, 7].
- **Serve:** o fluxo reprodutível em GEE (assets próprios + estatísticas zonais a 10 m), replicável para povoamentos de eucalipto e pinus em Goiás [p. 4–5].
- **Serve como evidência negativa:** o SAR C-band GRD não agrega informação a variáveis de rodal (5,26% da VIMR acumulada; conclusão explícita dos autores), o que sustenta priorizar Sentinel-2/LiDAR em Goiás e tratar radar como teste exploratório [p. 8, 10].
- **Não serve:** transpor os R² e RMSE% como desempenho esperado em Goiás — o estudo é de clima temperado, relevo complexo, inventário de 2018 e apenas validação cruzada, sem conjunto de validação independente descrito no texto [p. 3, 5, 7].

## 8. Frases citáveis (literais)

> "Optical bands yielded the highest VIMR in all cases, and the contribution of radar bands was less important." [p. 9]

> "Sentinel-1 GRD radar variables do not provide further information about forest state variables in forest plantations in northern Spain." [p. 10]
