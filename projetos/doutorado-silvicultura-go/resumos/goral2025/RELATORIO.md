# RELATÓRIO — Mathieu Goral (2025)

## 1. Referência

**Atenção: o `TEXTO.txt` não é o artigo do DOI pedido.** O arquivo está íntegro (texto completo, de 18 páginas, até a lista de referências), mas é outro artigo. O texto realmente presente é:

- Rajab Pourrahmati, M.; Le Maire, G.; Baghdadi, N.; Alvares, C. A.; Stape, J. L.; Scolforo, H. F.; Campoe, O. C.; Nouvellon, Y.; Guillemot, J. (2025). "Integrating MODIS-derived indices for eucalyptus stand volume estimation: an evaluation of MODIS gross primary productivity". *Frontiers in Remote Sensing* 6:1588387. DOI 10.3389/frsen.2025.1588387. Publicado em 14/05/2025 [p. 1].

- O artigo efetivamente pedido aparece apenas na lista de referências desse texto: Goral, M.; Maire, G.; Scolforo, H. F.; Stape, J. L.; Miranda, E. N.; Silva, T. C. F. et al. (2025). "Monitoring the early growth of forest plantations with Sentinel-2 satellite time-series". *Int. J. Remote Sens.* 46, 3110–3136. DOI 10.1080/01431161.2025.2466763 [p. 18].

As seções 2 a 8 descrevem, portanto, o artigo que está de fato no arquivo (Rajab Pourrahmati et al., 2025), e não o de Goral.

## 2. Pergunta do estudo

Se a integração de índices derivados de MODIS — em especial GPP e PSN — com a idade e com índices acumulados desde o plantio melhora a estimativa de volume de povoamentos de *Eucalyptus*, frente a modelos apenas baseados em idade ou em índices de vegetação [p. 3].

## 3. Área e dados

- Local: plantações de *Eucalyptus* no Mato Grosso do Sul, sudoeste do Brasil; clima tropical úmido-seco/savana, temperatura média de 20–28 °C [p. 3–4]; altitude de 250–400 m e 1,3 milhão ha plantados, com 1.200 árvores/ha e produtividade média de 40–45 m³ ha⁻¹ ano⁻¹ (80% dos talhões entre 30 e 50) [p. 4].
- Inventário de campo: parcelas de 400 m², cerca de uma a cada 10 ha, com DAP de todas as árvores; mais de 7.000 talhões medidos, em idades variadas e com remedições [p. 4].
- Amostra analítica após filtro de pixels puros (≥90% da área do pixel dentro de um único talhão): 4.130 pixels em 1.303 talhões, idades de 1,6 a 8,4 anos [p. 6]; subgrupos com 2.488 (>3 anos), 1.582 (>4) e 933 (>5 anos) [p. 6].
- Sensores/fontes: MOD17A2HGF v061 (GPP e PSN, 500 m, composições de 8 dias) [p. 5]; MCD43A4 v6.1 (NBAR, 500 m) para NDVI, interpolado e suavizado por Savitzky-Golay [p. 5]; torre de covariância de fluxo (EC) em 22°58′04″S, 48°43′40″W, 750 m, em plantação de 200 ha, com medições contínuas de fevereiro de 2008 a setembro de 2024 [p. 4–5].

## 4. Método

- Avaliação do GPP MODIS contra GPP de torre de fluxo, agregando a torre em períodos de 8 dias e usando um único pixel de 500 m considerado puro [p. 5].
- Cálculo de índices acumulados do plantio até a data de medição (Cgpp, Cpsn, Cndvi_L e Cndvi_S) e de variáveis intermediárias do plantio até 1–5 anos, conforme o grupo de idade [pp. 6–7].
- Três modelagens: MLR com componentes principais (PCA) para conter multicolinearidade, Random Forest (RF) e Stochastic Gradient Boosting (SGB), com validação cruzada de 5 folds e ajuste por RandomizedSearchCV [p. 7].
- Métricas de desempenho: RMSE, rRMSE e R² [p. 8].

## 5. Resultados principais

- GPP MODIS vs. torre de fluxo: R² = 0,38 e RMSE = 19,65 g C m⁻² 8 dia⁻¹ [p. 8]; rRMSE = 30,64% [p. 14]. Viés sistemático: subestima os picos de produtividade e superestima os períodos de baixo GPP [p. 8], com superestimativa no primeiro ano após colheita [p. 8].
- Correlação do volume com variáveis isoladas: Cndvi R² = 0,81; idade 0,78; Cgpp 0,74; Cpsn 0,52 [p. 8].
- Melhor RF do conjunto completo (n = 4.130, Cgpp, Cpsn, Cndvi_L e Age): RMSE = 27,90 m³ ha⁻¹, rRMSE = 21,15%, R² = 0,85 [p. 9].
- Melhor MLR (quatro componentes principais): RMSE = 29,59 m³ ha⁻¹, rRMSE = 22,43%, R² = 0,83 [p. 9]; VIF originais de 38,66 (Cgpp), 11,83 (Cpsn), 101,32 (Cndvi) e 77,29 (Age) [p. 9].
- Melhor modelo global: SGB com índices acumulados do primeiro ano — RMSE = 22,63 m³ ha⁻¹, rRMSE = 17,15%, R² = 0,90, ganho de 19,67% em rRMSE sobre o modelo de quatro variáveis [p. 12]; o RF equivalente deu RMSE = 25,42 m³ ha⁻¹, rRMSE = 19,27% e R² = 0,87 [p. 12].
- Talhões com mais de 3 anos (n = 2.488): SGB com índices até o 3º ano, RMSE = 23,55 m³ ha⁻¹, rRMSE = 13,52%, R² = 0,84 [p. 12]; ganhos sucessivos de 20,35%, 7,83% e 5,12% ao acrescentar os anos 1, 2 e 3 [p. 16].
- Talhões com mais de 4 anos (n = 1.582): SGB, RMSE = 27,38 m³ ha⁻¹, rRMSE = 13,62%, R² = 0,73 [p. 13]. Com mais de 5 anos (n = 933): SGB, RMSE = 31,82 m³ ha⁻¹, rRMSE = 14,30%, R² = 0,61 [p. 15].
- Efeito do ajuste de hiperparâmetros: no SGB o RMSE caiu de 26,00 para 22,63 m³ ha⁻¹ (13%) e o R² subiu de 0,87 para 0,90; no RF a mudança foi de 25,71 para 25,42 m³ ha⁻¹ (1,1%) [p. 9].

## 6. Limitações que os próprios autores reconhecem

- O GPP do MODIS tem desempenho fraco no contexto estudado (R² = 0,38, rRMSE = 30,64%), atribuído sobretudo ao FPAR, que "permanece um gargalo crítico" [p. 14]; o produto é ruidoso e pouco acurado no primeiro ano de crescimento [p. 8].
- Mais de 90% das plantações estão em terrenos planos a suavemente inclinados no Mato Grosso do Sul [p. 4], o que restringe a extrapolação a topografias mais acidentadas.
- A análise não foi estendida a talhões com mais de 6 anos porque o número de amostras cai muito com cada filtro adicional de idade [p. 7].
- O número de amostras diminui com a idade (4.130 → 2.488 → 1.582 → 933), o que "pode afetar a robustez e a generalização" dos modelos para povoamentos mais velhos [p. 16].
- Não há análise de incerteza do produto GPP neste contexto, apontada como trabalho necessário para quantificar erros sistemáticos e ruído [p. 17].
- EVI, LAI e variáveis ambientais externas (temperatura, precipitação) não foram incluídos por delimitação de escopo [p. 6].

## 7. O que serve ao projeto e o que não serve

- **Serve — protocolo de validação:** comparar produto de produtividade (GPP) com torre de fluxo antes de usá-lo em modelos, quantificando viés por estádio de crescimento [pp. 8, 14]; é replicável para silvicultura em Goiás.
- **Serve — variáveis cumulativas:** índices integrados desde o plantio mais idade, e sobretudo os dois primeiros anos, elevam o rRMSE em 19,67% (R² de 0,85 para 0,90) [p. 12]; é o achado mais transferível para modelagem de biomassa.
- **Serve — referência de desempenho:** rRMSE de 13,52% a 21,15% e R² de 0,61 a 0,90 conforme a classe de idade [pp. 9, 12, 13, 15], útil como benchmark.
- **Não serve diretamente:** o alvo é volume de madeira (m³ ha⁻¹), não biomassa ou estoque de carbono — o texto não traz fator de conversão nem teor de carbono; a área é o Mato Grosso do Sul com *Eucalyptus* clonal, e o sensoriamento é só MODIS a 500 m, sem o caráter multissensorial previsto no projeto [pp. 4, 5].

## 8. Frases citáveis (literais)

- "The scatter plot comparing MODIS and flux tower GPP demonstrates a moderate level of agreement, with an R2 value of 0.38 and an RMSE of 19.65 g C m−2 8 day−1." [p. 8]
- "Our results confirm that the early-growth stage of Eucalyptus plantations provides valuable information to predict the stand volume in the subsequent years, even at the end of the rotation." [p. 16]
