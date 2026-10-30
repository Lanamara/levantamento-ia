# RELATÓRIO — Vítězslav Moudrý (2024)

## 1. Referência

Moudrý, V., Prošek, J., Marselis, S., Marešová, J., Šárovcová, E., Gdulová, K., Kozhoridze, G., Torresani, M., Rocchini, D., Eltner, A., Liu, X., Potůčková, M., Šedová, A., Crespo-Peremarch, P., Torralba, J., Ruiz, L. A., Perrone, M., Špatenková, O., & Wild, J. (2024). How to Find Accurate Terrain and Canopy Height GEDI Footprints in Temperate Forests and Grasslands? *Earth and Space Science*, 11, e2024EA003709. DOI: 10.1029/2024EA003709. Texto integral conferido (26 páginas); recebido em 26/04/2024, aceito em 16/09/2024 [p. 1].

## 2. Pergunta do estudo

Qual é a forma mais eficaz de filtrar footprints do GEDI para reter observações acuradas de terreno e de altura de dossel em florestas temperadas e campos, e como características de aquisição (número de modos, *sensitivity*, *quality flag*, *degrade flag*, feixe, horário) e ambientais (cobertura da terra, declividade) controlam essa acurácia?

## 3. Área e dados

- **Local:** três áreas no bioma temperado — Cantabrian Mountain Range, Espanha (4.200 km², 0–2.648 m), Marlborough Richmond Range, Nova Zelândia (4.900 km², 0–1.760 m) e Trinity Alps Wilderness, Califórnia/EUA (2.400 km², 600–2.750 m) [p. 6].
- **Período:** ALS de referência adquirido entre 2018 e 2021 [p. 6]; footprints GEDI L2A versão 2 de abril/2019 a setembro/2022, baixados em setembro/2022 [p. 9].
- **Sensores/fontes:** GEDI L2A (*elev_lowestmode*, *num_detectedmodes*, *sensitivity*, *quality_flag*, *degrade_flag*, RH98) [p. 7]; ALS discreto (densidade 1–2, 9 e 8 pontos/m²) para DTM e CHM a 2 m [p. 6]; TanDEM-X DEM; ESA WorldCover 10 m de 2020 [p. 7].
- **Amostras:** 2.081.108 footprints não filtrados declarados no resumo [p. 1]; após restringir a floresta e campo, 740.779 (Cantabria), 695.023 (Marlborough) e 645.306 (Trinity) [p. 9].

## 4. Método

- Workflow em quatro etapas: (a) filtragem de ruído por número de modos e *sensitivity*; (b) filtragem de baixa qualidade por *quality flag* (QF), diferença para TanDEM-X (TDX, limiares de 50 e 100 m) e concordância entre os seis *algorithm setting groups* (ASG, ≤2 m); (c) filtros adicionais (*degrade flag*, potência do feixe, dia/noite, declividade); (d) mitigação do erro de geolocalização [p. 7–9].
- Erro vertical definido como desvio entre o GEDI e o DTM/CHM de ALS (média em buffer de 25 m), resumido por ME e RMSE e por distribuições (densidade e boxplots) estratificadas por cobertura e declividade [p. 10].
- Observação "de alta qualidade" definida como erro absoluto de terreno <3 m, baseada na acurácia vertical teórica de 2–3 m do GEDI; avaliou-se tanto a remoção de erros quanto a retenção de acertos [p. 10].
- Teste de geolocalização: deslocamento de 10 e 5 m em oito direções, gerando 17 posições por footprint, escolhendo-se a de menor erro [p. 9].

## 5. Resultados principais

- Apenas 19,5% (Cantabria), 24,5% (Marlborough) e 30,8% (Trinity) das observações do conjunto não filtrado tiveram erro absoluto de terreno <3 m; o resumo arredonda para 20%–30% [p. 1, p. 12].
- O critério "número de modos ≥1" removeu menos de 1% das observações de alta qualidade, enquanto o critério de *sensitivity* removeu 9%–15% delas; os dois critérios concordaram em mais de 85% dos casos [p. 10, p. 12–13].
- Após a filtragem de ruído restaram 1.195.259 footprints; após QF+TDX, 991.932; após excluir *degrade flag* 5, 50 e 85, 963.709 [p. 11, p. 14, p. 16].
- ASG+TDX foi a combinação mais acurada (RMSE de 6,3 a 11,1 m), mas ASG removeu 75%–80% das observações e 60%–65% das de alta qualidade; QF+TDX teve RMSE de 11,2 a 13,2 m, removeu apenas 10%–30% do total e menos de 1% das de alta qualidade [p. 12, p. 14].
- Somente 4%–25% das observações foram classificadas como de baixa qualidade por todos os métodos, indicando baixa concordância entre eles [p. 12].
- Ruído identificado: 51,5% (Cantabria), 44,2% (Marlborough) e 30,5% (Trinity); baixa qualidade: 14,7%, 8,0% e 6,0%; retenção final de 33,8%, 47,8% e 63,5% [p. 16]. Feixes de potência perderam sinal em 20,0% (floresta) e 19,6% (campo) contra 31,0% e 33,2% dos feixes de cobertura [p. 14].
- Número ótimo de modos para altura de dossel: 2–4 em Cantabria, 9–12 em Marlborough e 13–20 em Trinity, acompanhando a altura da vegetação; em campos houve superestimativa crescente com o número de modos [p. 14, p. 17].
- Em declividades >45° observou-se subestimativa mediana do terreno e superestimativa correspondente da altura de dossel de até 10 m [p. 17].
- O *degrade flag* reduziu o número de observações em 19,5% adicionais; horário (dia/noite) e tipo de feixe não afetaram a acurácia [p. 21].
- Deslocamento de 10 m melhorou a acurácia em 70% dos footprints e de 5 m em outros 26% (4% sem melhora); o RMSE de terreno caiu, por exemplo, de 12,7 para 9,4 m em Marlborough, mas o RMSE de dossel praticamente não mudou (8,3 para 8,2 m) [p. 16, p. 20].

## 6. Limitações que os próprios autores reconhecem

- O teste de filtragem cobriu apenas florestas temperadas e campos; os autores afirmam que a filtragem pode precisar de ajuste por cobertura e que seria importante testá-la em outros biomas e tipos de cobertura, inclusive florestas tropicais [p. 23].
- Avaliaram apenas terreno e altura do topo do dossel (RH98), sem tratar da estrutura vertical intermediária entre topo e solo [p. 23].
- Não propagaram os erros de altura de dossel para aplicações posteriores (índices de estrutura, área foliar, biomassa acima do solo) [p. 23].
- A mitigação do erro de geolocalização por DTM de alta resolução parece insuficiente e perde eficácia com o aumento do número de modos; abordagens com formas de onda simuladas poderiam ser mais adequadas [p. 22–23]. O teste de deslocamento limitou-se a 5 e 10 m em oito direções [p. 9].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o protocolo sequencial (excluir 0 modos → QF + TDX <100 m → remover *degrade flag* 5, 50 e 85) é replicável como etapa de garantia de qualidade antes de qualquer modelagem de biomassa ou carbono com GEDI L2A [p. 7–9, p. 21].
- **Serve:** o achado de que a acurácia do terreno condiciona a altura de dossel — em campos, tanto super quanto subestimativa do terreno geram superestimativa da altura, e o próprio artigo liga isso a superestimar carbono [p. 1, p. 14]; justifica relatar a retenção (aqui 33,8%–63,5%) e não apenas o RMSE final [p. 16].
- **Não serve diretamente:** os limiares numéricos foram calibrados em florestas temperadas; os autores indicam que em florestas tropicais a filtragem ótima pode diferir (apenas feixes de potência e *sensitivity* >0,98) [p. 23].
- **Não serve:** o artigo não avalia biomassa nem estoque de carbono e não há número de AGB transferível; a correção de geolocalização melhorou o terreno mas não a altura da vegetação [p. 16, p. 23].

## 8. Frases citáveis (literais)

- "In dense forests, a minimum sensitivity of 0.9 was required, while in areas with sparse vegetation, sensitivity of 0.5 sufficed." [p. 1]
- "We found that the most effective strategy for filtering low‐quality observations was to combine the quality flag and difference from TanDEM‐X, striking an optimal balance between eliminating poor‐quality data and preserving a maximum number of high‐quality observations." [p. 1]
