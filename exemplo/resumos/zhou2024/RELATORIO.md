# RELATÓRIO — Yuchuan Zhou (2024)

## 1. Referência

- Autores: Yuchuan Zhou, David M Taylor e Hao Tang (Department of Geography e Centre for Nature-based Climate Solutions, National University of Singapore).
- Título: *Improved country-wide estimation of above-ground tropical forest biomass using locally calibrated GEDI spaceborne LiDAR data*.
- Revista: *Environmental Research Letters*, v. 20, artigo 014017. Publicado online em 13/12/2024; a citação oficial da própria revista é "2025" (recebido 03/04/2024, aceito 05/12/2024) [p. 2].
- DOI: 10.1088/1748-9326/ad9aba — confere com o DOI do pedido.
- O `TEXTO.txt` está completo: 14 páginas de artigo, com abstract, métodos, resultados, discussão, conclusão, agradecimentos, ORCIDs e referências [p. 2–15].

## 2. Pergunta do estudo

Se a calibração local dos modelos do produto GEDI L4A com o inventário florestal nacional (NFI) de 2019 reduz o viés do produto global e permite estimar o AGBD por classe de floresta natural em escala nacional no Laos.

## 3. Área e dados

- Local: Laos (Lao PDR), Sudeste Asiático; floresta natural em ~57% do território [p. 3], cerca de 130.345 km² [p. 3], dividida em cinco classes: evergreen (EG, 19,7%), mixed deciduous (MD, 69,6%), coniferous (CF, 0,9%), mixed coniferous/broadleaved (MCB, 0,8%) e dry dipterocarp (DD, 9,0%) [p. 4]. Plantações ficam fora do escopo [p. 3].
- NFI 2019: 359 parcelas, cada uma com quatro subparcelas em raio de 300 m, subparcelas a ≥75 m entre si; só subparcelas classificadas como floresta foram medidas [p. 3].
- GEDI L2A e L4A no Google Earth Engine, 1/1/2019 a 31/12/2020, para validação e calibração [p. 3]; pegadas de 25 m entre 51°N e 51°S [p. 2]. O L4A tem 35 estratos de predição e 12 modelos efetivamente implantados [p. 3].
- Auxiliares: SRTM 30 m (elevação, declividade), WorldClim Bio V1 (temperatura e precipitação anuais), mapa de tipos florestais de 2015 e mapa de textura do solo de 2020 (projeto K4D/CDE Bern) [p. 3, 6].
- Amostras efetivamente usadas na calibração: 138 das 359 parcelas do NFI (38,4%) tinham pegadas GEDI de qualidade suficiente [p. 6, 13].

## 4. Método

- **Avaliação de viés:** subconjunto de pegadas L4A com `l4_quality_flag` = 1, `degrade_flag` = 0, máscara de floresta (cobertura de copa >20%), e filtro de qualidade (QF) com sensibilidade >0,98 e erro padrão relativo <50%; declividade >30° excluída; pegadas agregadas em raio de 300 m de cada parcela, exigindo ≥4 pegadas por parcela; teste de Wilcoxon para amostras pareadas contra o NFI [p. 3–4, 5].
- **Configuração do modelo:** teste dos 12 modelos do GEDI L4A para cada classe, ranqueados por MAE e, em caso de diferença <5%, por %RMSE [p. 6, 8].
- **Calibração local:** regressões OLS do AGBD do NFI sobre o AGBD GEDI configurado (modelos #1–#5) e sobre métricas RH médias com transformação de raiz quadrada e fator de correção de viés (modelos #6–#9), incluindo variáveis auxiliares (classe, desvio-padrão do AGBD por parcela, elevação, declividade, temperatura, precipitação, tipo de solo); validação cruzada 10-fold e seleção por correlação e VIF [p. 6–7].
- **Expansão e estimativa:** aplicação do melhor modelo a todas as pegadas L2A de 25/03/2019 a 01/03/2023, agregação em células hexagonais de 600 m de diâmetro (mínimo de 4 pegadas QF por célula), correção pelo resíduo médio de cada classe e estimador GREG com IC 95%, comparado ao estimador por delineamento do NFI [p. 7–8, 11].

## 5. Resultados principais

- O produto L4A original difere significativamente do NFI (Wilcoxon p = 0,01125) e o filtrado também (p = 0,01708) [p. 9].
- Viés do L4A original, por classe: EG +129,05; DD +44,63; MD −5,43; CF −12,19; MCB −17,38; total +12,89 Mg ha⁻¹ [p. 9].
- Viés após filtro de qualidade: EG +106,23; DD +12,59; MD −41,63; CF −54,24; MCB −40,90; total −15,59 Mg ha⁻¹ — o filtro piorou o viés em CF, MCB e MD [p. 9]. O abstract resume a faixa de viés absoluto em −54,24 a 106,23 Mg ha⁻¹ [p. 2].
- Melhor configuração por classe: modelo ENT da Austrália para CF, MCB e MD; DBT da Europa para DD; DBT global para EG [p. 8]. Ganho nas métricas de desempenho: 9,78% a 33,03% [p. 8].
- Calibração final (10-fold CV): EG com R² ajustado 0,11, MAE 78,88, %RMSE 25,63 e viés 13,33; MD com R² ajustado 0,14, MAE 37,25, %RMSE 29,18 e viés −0,13; CF/DD/MCB com modelo comum de R² ajustado 0,38, MAE 35,61 e %RMSE 29,33, vieses de −13,64 (CF), 13,55 (DD) e 6,83 (MCB) [p. 10].
- Redução média de viés somando todas as classes: 42,2 Mg ha⁻¹, com a maior redução no EG [p. 2].
- Mapa nacional: 3.239.372 tiros GEDI QF agregados em 312.661 células hexagonais com floresta natural [p. 10].
- Parcelas pareadas por classe: CF 15/40 (37,5%), DD 3/62 (4,8%), EG 20/34 (58,9%), MCB 24/38 (63,1%), MD 76/185 (41,1%), total 138/359 (38,4%) [p. 13].
- Os IC 95% de GREG e NFI se sobrepõem em todas as classes; em CF e DD a incerteza do GREG é bem maior, e em MCB o GREG foi ligeiramente mais preciso que o NFI com 63% da amostra [p. 11].

## 6. Limitações que os próprios autores reconhecem

- Erro de geolocalização do GEDI maior que 10 m, o que dificulta calibrar pegadas com parcelas pequenas e dispersas [p. 12].
- Discrepância de resolução entre parcelas do NFI e pegadas GEDI: a calibração pode valer apenas para a grade hexagonal, não para pegadas individuais; testes em nível de subparcela ficam para o futuro [p. 13].
- Descompasso entre pegadas disponíveis e parcelas do NFI impede incluir todas as parcelas na calibração, reduzindo o desempenho; o caso do DD é pouco confiável porque há só três parcelas [p. 13].
- A célula hexagonal de 600 m pode mascarar a variabilidade interna da floresta, com incerteza sobre a representatividade em paisagens heterogêneas [p. 14].
- Áreas em branco onde não há pegadas GEDI (limitação orbital): a suposição de pesos iguais do GREG pode não valer, pode haver viés adicional, um mapa contínuo do país é inviável no momento e "the mean AGBD estimates by forest type reported in this study must be viewed with caution" [p. 14].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o desenho de calibração local — produto global (GEDI L4A) confrontado com inventário de campo, reconfiguração por classe e regressão OLS com variáveis auxiliares, tudo validado por 10-fold CV — é replicável para povoamentos de eucalipto em Goiás, desde que exista inventário com coordenadas confiáveis.
- **Serve:** o estimador GREG e a agregação em células hexagonais de 600 m como ponte entre pegadas de 25 m, parcelas de ~300 m e o mapa contínuo; a lógica de comparar estimativa assistida por modelo com estimativa por delineamento é diretamente transferível.
- **Serve:** a evidência de que o modelo global padrão pode ser enviesado por tipo de floresta e de que outro estrato (ENT_Au) pode superá-lo — argumento para calibrar por classe/estrato em vez de usar o produto pronto.
- **Não serve:** não há fusão multissensorial (só GEDI + rasters auxiliares de topografia, clima e solo), não há silvicultura nem plantações (explicitamente fora do escopo [p. 3]), não há dados de idade, espaçamento ou crescimento, e a área é floresta natural tropical no Laos; os valores de viés e MAE não são transferíveis para o Cerrado goiano.

## 8. Frases citáveis (literais)

- "Our findings thus illustrate how the availability of plot data affects accuracy and highlight the need for more field-based surveys for currently sparsely surveyed forest classes to improve estimation accuracy." [p. 13]
- "In other words, despite the GREG estimator being designed to be unbiased, the limited distribution of hexagonally-plotted data across the natural forest estate in Laos may have introduced additional biases." [p. 14]
