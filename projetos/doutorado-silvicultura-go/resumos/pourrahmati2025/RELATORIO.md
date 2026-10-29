# RELATÓRIO — Manizheh Rajab Pourrahmati (2025)

## 1. Referência

Rajab Pourrahmati, M.; Le Maire, G.; Baghdadi, N.; Alvares, C. A.; Stape, J. L.; Scolforo, H. F.; Campoe, O. C.; Nouvellon, Y.; Guillemot, J. (2025). Integrating MODIS-derived indices for eucalyptus stand volume estimation: an evaluation of MODIS gross primary productivity. *Frontiers in Remote Sensing*, 6:1588387. DOI: 10.3389/frsen.2025.1588387.

O `TEXTO.txt` corresponde ao artigo do DOI indicado (recebido 05/03/2025, publicado 14/05/2025) e está íntegro: vai da página 1 ao fim das referências, na página 19 [p. 1] [p. 19].

## 2. Pergunta do estudo

Os índices cumulativos derivados de MODIS — GPP, PSN e NDVI — agregam acurácia à estimativa de volume de povoamentos de eucalipto baseada apenas na idade, e o produto MOD17A2HGF é confiável nesse tipo de plantação?

## 3. Área e dados

- Local: plantações de eucalipto no Mato Grosso do Sul, sudoeste do Brasil (clima tropical úmido/seco, 250–400 m de altitude, 1,3 milhão de ha de eucalipto na região); clones de *E. grandis*, *E. urophylla* e híbridos, 1.200 árvores/ha [p. 3–4].
- Torre de fluxo (eddy covariance): 22°58′04″S, 48°43′40″W, 750 m, em plantação homogênea de 200 ha; medições contínuas de fevereiro de 2008 a setembro de 2024, cobrindo o fim de uma rotação, dois cortes (2009 e 2018) e o início da rotação seguinte [p. 4–5].
- Inventário: parcelas de 400 m², cerca de uma a cada 10 ha; mais de 7.000 povoamentos medidos, com idades entre 1,6 e 8,4 anos e medições repetidas em alguns povoamentos [p. 4] [p. 6].
- Sensores: MOD17A2HGF v061 (GPP e PSN, composições de 8 dias, 500 m) e MCD43A4 v6.1 (reflectância NBAR, 500 m, usada para NDVI) [p. 5].
- Amostra efetiva após filtro de pureza do pixel (≥90% de sobreposição com um único povoamento): 4.130 pixels em 1.303 povoamentos; subconjuntos de 2.488 (>3 anos), 1.582 (>4 anos) e 933 (>5 anos) [p. 6].

## 4. Método

- Avaliação do GPP MODIS contra GPP de torre de fluxo, agregando a torre em períodos de 8 dias e comparando com um pixel puro de 500 m (RMSE e R²) [p. 5–6].
- Filtro espacial de povoamentos com ≥90% de sobreposição por pixel MODIS, extração de séries temporais de GPP, PSN e NDVI (NDVI interpolado linearmente e suavizado por Savitzky-Golay) [p. 5–6].
- Construção de variáveis cumulativas da data de plantio até a medição (Cgpp, Cpsn, Cndvi) e até N anos após o plantio (Cgpp1Y…Cgpp5Y, etc.), sempre com a idade (Age) como preditor [p. 6–7].
- Modelagem por MLR (com PCA para colinearidade), random forest (RF) e stochastic gradient boosting (SGB), com validação cruzada de cinco dobras, ajuste por RandomizedSearchCV e métricas RMSE, rRMSE e R² [p. 7–8].

## 5. Resultados principais

- GPP MODIS vs. torre: R² = 0,38 e RMSE = 19,65 g C m⁻² 8 dia⁻¹; subestimação nos picos de produtividade e superestimação nos períodos de baixa produtividade [p. 1] [p. 8].
- O produto MOD17A2HGF teve desempenho fraco, com R² = 0,38 e rRMSE = 30,64%, atribuído sobretudo ao FPAR [p. 14].
- Correlações do volume com variáveis individuais: Cndvi R² = 0,81; idade R² = 0,78; Cgpp R² = 0,74; Cpsn R² = 0,52 [p. 8].
- Melhor modelo com variáveis só na data de medição (n = 4.130): RF com RMSE = 27,90 m³ ha⁻¹, rRMSE = 21,15% e R² = 0,85 [p. 9].
- MLR com os quatro componentes principais (Cgpp, Cpsn, Cndvi, Age): RMSE = 29,59 m³ ha⁻¹, rRMSE = 22,43%, R² = 0,83; VIF originais de 38,66 (Cgpp), 11,83 (Cpsn), 101,32 (Cndvi) e 77,29 (Age) caíram para 1 após PCA [p. 9].
- Melhor resultado geral, incluindo índices do primeiro ano (n = 4.130): SGB com RMSE = 22,63 m³ ha⁻¹, rRMSE = 17,15% e R² = 0,90, melhora de 19,67% em rRMSE sobre o melhor modelo da Tabela 2 [p. 9] [p. 12].
- Povoamentos >3 anos (n = 2.488): melhor SGB com índices até o 3º ano, RMSE = 23,55 m³ ha⁻¹, rRMSE = 13,52%, R² = 0,84 [p. 10] [p. 12].
- Povoamentos >4 anos (n = 1.582): melhor SGB com índices até o 4º ano, RMSE = 27,38 m³ ha⁻¹, rRMSE = 13,62%, R² = 0,73 [p. 13].
- Povoamentos >5 anos (n = 933): melhor SGB com índices até o 5º ano, RMSE = 31,82 m³ ha⁻¹, rRMSE = 14,30%, R² = 0,61 [p. 15].
- A inclusão de índices dos dois primeiros anos foi o principal ganho; ganhos adicionais dos anos 3 a 5 foram menores [p. 13] [p. 16].

## 6. Limitações que os próprios autores reconhecem

- O GPP do MOD17A2HGF foi impreciso neste contexto (R² = 0,38; rRMSE = 30,64%), com o FPAR como gargalo; defendem comparação sítio-específica antes do uso operacional [p. 14].
- Viés sistemático: subestimação nos picos de produtividade e superestimação no primeiro ano após o plantio/corte, quando o dossel é esparso [p. 8] [p. 17].
- A incerteza do GPP MODIS nos estágios iniciais reduz a eficiência do modelo, o que torna o NDVI necessário como contrapeso [p. 17].
- Redução do tamanho amostral com a idade (4.130 → 2.488 → 1.582 → 933), o que pode afetar a robustez e a generalização para povoamentos mais velhos; por isso a análise não foi estendida além de 6 anos [p. 7] [p. 16].
- A resolução de 500 m limita os pixels inteiramente contidos em um povoamento, exigindo o filtro de 90% (1.303 povoamentos aproveitados de mais de 7.000) [p. 6].
- Não foi feita análise formal de incerteza; os autores a apontam como etapa necessária para quantificar erros sistemáticos e ruído [p. 17].

## 7. O que serve ao projeto e o que não serve

- Serve: a arquitetura metodológica (índices cumulativos + idade, RF/SGB com validação cruzada de cinco dobras e rRMSE) é diretamente transponível para volume/biomassa de silvicultura em Goiás [p. 7–8].
- Serve: a evidência de que índices cumulativos, sobretudo dos dois primeiros anos, carregam a maior parte da informação preditiva, e de que o NDVI cumulativo é o preditor individual mais forte (R² = 0,81) [p. 8] [p. 16].
- Serve com cautela: o artigo trata de volume de fuste, não de biomassa nem de estoque de carbono; não há qualquer valor de biomassa ou carbono no texto, e a conversão exigiria densidade da madeira e teor de carbono, não informados.
- Não serve: a área é o Mato Grosso do Sul, não Goiás, e a escala de 500 m com filtro de pureza restringiu a amostra a 1.303 povoamentos; não há transferência validada para Goiás nem para plantios fragmentados [p. 3] [p. 6].

## 8. Frases citáveis (literais)

- "But it can be important at early growth stages, but then at mid-age to late rotation the information of GPP really brings important new information." [p. 16]
- "The use of cumulative values helps to mitigate this short-term variability, but this underline the challenge of addressing biases in MODIS GPP and ensuring accuracy during early growth stages." [p. 17]
