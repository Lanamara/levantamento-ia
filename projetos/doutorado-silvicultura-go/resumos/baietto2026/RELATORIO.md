# RELATÓRIO — Andrés Baietto (2026)

## 1. Referência

Andrés Baietto, Andrés Hirigoyen, Mauricio Acuña, Rafael María Navarro-Cerrillo (2026). *Carbon-water trade-off in Eucalyptus dunnii plantations: A bi-objective optimization framework using remote sensing and machine learning models*. Forest Ecosystems 17 (2026) 100528. DOI: 10.1016/j.fecs.2026.100528.

O `TEXTO.txt` corresponde ao artigo completo do DOI (13 páginas, corpo + referências) [p. 1, 13]. Ressalva técnica: no arquivo, os sobrescritos de expoente (ex.: `g·L−1`) aparecem como caracteres nulos, o que não compromete a leitura; nenhum dado foi estimado a partir disso.

## 2. Pergunta do estudo

É possível definir, com um arcabouço de programação linear biobjetivo espacialmente explícito baseado em sensoriamento remoto e aprendizado de máquina, idades de corte por talhão que equilibrem melhor o estoque de carbono e o uso da água do que o regime tradicional de rotação fixa de 8 anos em plantios comerciais de *Eucalyptus dunnii*? [p. 2]

## 3. Área e dados

- Local: 699 ha no oeste do Uruguai, 226 talhões de *E. dunnii* para celulose, solos Aquic Argiudolls e Typic Albaqualfs; clima Cfa, chuva anual de 1200–1400 mm [p. 2].
- Período: 2021–2024, correspondendo a idades de 6, 7, 8 e 9 anos (talhões mais velhos que 9 anos foram excluídos por escassez) [p. 2, 5].
- Sensores/fontes: Sentinel-1 SAR (VV/VH, órbita descendente, composições anuais, 10 m) [p. 2–3]; Sentinel-2 harmonizado (bandas red, blue, red-edge e NIR, composição anual por mediana com <20% de nuvem, 10 m) [p. 3]; SoilGrids 250 m v2.0 (argila, areia, N, CEC, densidade, pH, 0–30 cm) [p. 4]; ETa do geeSEBAL-MODIS a 500 m, soma diária desde o ano de plantio [p. 4].
- Amostras: 226 talhões (n = 226) em toda a modelagem e nas tabelas [p. 6]. Número de parcelas de campo: não informado (os modelos de SA e AGC usados são de Baietto et al., 2025) [p. 4–5].

## 4. Método

1. Empilhamento de Sentinel-1, Sentinel-2 (EVI e red-edge NDVI), SoilGrids e ETa em raster de 10 m; agregação de médias por talhão [p. 2].
2. Random forest para estimar idade do talhão (SA) ao nível de pixel e, em seguida, random forest com SA + solos + índices para estimar AGC (Mg·ha⁻¹); médias por talhão [p. 2, 5].
3. Programação linear inteira biobjetivo (BOP) com soma ponderada: valores padronizados por z-score de AGC (maximizar) e de ETa invertida (multiplicar por −1) [p. 5]; função `Maximize Z = ΣΣ [α × AGCs + (1−α) × inverted-ETas] × xij`, com uma única idade de corte (6, 7, 8 ou 9 anos) por talhão [p. 5].
4. Fronteira de Pareto variando α de 0 a 1 em passos de 0,1 (11 soluções); cenários escolhidos: water-priority (α = 0,25), balanced (α = 0,50) e carbon-priority (α = 0,75), comparados à rotação fixa de 8 anos; análise de sensibilidade com α ±5% e cálculo de WUE = AGC/ETa × 100 [p. 6].

## 5. Resultados principais

- AGC e ETa cresceram com a idade; máximos aos 9 anos: 63,76 Mg·ha⁻¹ e 10.396 mm [p. 6].
- WUE média teve pico aos 7 anos (0,724 g·L⁻¹) e caiu para 0,617 g·L⁻¹ aos 9 anos [p. 6]. Médias por idade (desvio-padrão entre parênteses): 6 anos 49,26 (3,04) Mg·ha⁻¹, 7.288 (606) mm, 0,681; 7 anos 60,25 (2,20), 8.386 (670), 0,724; 8 anos 61,38 (1,92), 9.401 (756), 0,658; 9 anos 63,76 (2,20), 10.396 (804), 0,617 [p. 6].
- Cenário balanced (α = 0,50): rotação média de 7 ± 0 anos, AGC 60,35 ± 2,22 Mg·ha⁻¹, ETa 8.407 ± 701 mm, WUE 0,723 ± 0,072 g·L⁻¹ — a maior WUE entre os cenários [p. 6].
- Comparação com a rotação fixa de 8 anos: WUE 0,723 vs. 0,658 g·L⁻¹, ETa 8.407 vs. 9.401 mm (−994 mm) e AGC 60,35 vs. 61,38 Mg·ha⁻¹ (−1,03 Mg·ha⁻¹, ≈1,7%) [p. 1, 6].
- Cenário water-priority (α = 0,25): 207 dos 226 talhões aos 6 anos, 19 aos 7 anos; AGC 50,53 ± 3,89 Mg·ha⁻¹ e ETa 7.373 ± 619 mm [p. 6, 9]; cenário carbon-priority (α = 0,75): rotação média 8 ± 1 anos, AGC 63,04 ± 2,51 Mg·ha⁻¹, ETa 9.670 ± 1.072 mm, WUE 0,659 ± 0,071 g·L⁻¹ [p. 6].
- Talhões colhidos aos 7 anos concentram as maiores WUE (0,725–0,772 g·L⁻¹); aos 9 anos, ETa acima de 10.000 mm e WUE de 0,630 g·L⁻¹ [p. 6].
- Sensibilidade ±5% em α: balanced permaneceu em 7 anos; water-priority em 6 anos; carbon-priority migrou de 8 para 9 anos com α +5% (0,75 → 0,7875) [p. 7, 11].
- Desempenho dos modelos herdados: SA com R² = 77,7% e RMSE = 1,1 ano; AGC com R² = 84,7% e RMSE = 8,42 Mg·ha⁻¹ [p. 5].
- Contexto hídrico: ETa média anual de 1.155–1.215 mm·ano⁻¹, com déficit de 101 mm·ano⁻¹ (precipitação média 1.085 vs. demanda 1.186 mm·ano⁻¹) [p. 8]; WUE de 0,617–0,724 g·L⁻¹ equivale a 1,313–1,540 g·L⁻¹ em matéria seca (fator 0,47) [p. 8].

## 6. Limitações que os próprios autores reconhecem

- Resolução grosseira das entradas de ETa (geeSEBAL-MODIS, 500 m) e de solo (SoilGrids, 250 m) gera efeito de pixel misto dado o tamanho médio pequeno dos talhões e limita a representação da heterogeneidade interna; a otimização vale na escala do talhão, não para análises finas dentro dele [p. 11]. Os pixels de 10 m herdam o valor do pixel de 500 m/250 m, o que pode subestimar a variação entre talhões [p. 4].
- Composições temporais (anuais) podem atenuar o efeito da variabilidade sazonal e fenológica sobre SA e AGC [p. 11, 2].
- Ausência de variáveis LiDAR, que costumam dar predições mais acuradas [p. 11]; ETa não validada localmente com torres de Eddy Covariance [p. 11].
- Encurtar rotações pode elevar a exportação de nutrientes, reduzindo fertilidade, carbono orgânico e atributos biológicos do solo [p. 11].
- O arcabouço não é um sistema de planejamento tático/operacional: talhões tratados como unidades independentes, sem restrições de adjacência, agrupamento ou acessibilidade, e sem análise formal de incerteza [p. 11].
- Comparações de WUE com a literatura exigem cautela porque a métrica é ecossistêmica e média da rotação, baseada em ETa total (inclui evaporação do solo e interceptação), e não em transpiração [p. 9].

## 7. O que serve ao projeto e o que não serve

- Serve: o desenho de pipeline — SAR Sentinel-1 + óptico Sentinel-2 + solos + composições anuais em grade comum de 10 m, com random forest em dois estágios (idade → AGC) e agregação por talhão — é diretamente replicável para silvicultura em Goiás [p. 2, 5].
- Serve: a arquitetura de validação relatada (R² = 84,7%, RMSE = 8,42 Mg·ha⁻¹) e o uso exclusivo de dados abertos e gratuitos (Sentinel, SoilGrids, geeSEBAL-MODIS), que dá base para um argumento de custo-efetividade e escalabilidade [p. 5, 11].
- Não serve: os modelos de SA e AGC são calibrados para *E. dunnii* no Uruguai, em solos e manejo específicos; não há qualquer dado de Goiás, do Cerrado, de biomassa de campo ou de outras espécies/clones, e os autores condicionam a transferência a condições semelhantes de pressão sobre recursos [p. 2, 5, 11].
- Não serve: o produto final do artigo é escala de rotação de corte (6–9 anos) e WUE, não estoque de carbono/biomassa em si; o alvo é carbono aéreo (AGC), sem biomassa total, sem carbono de solo e sem componente econômico, o que limita o uso direto como referência de estoque para o projeto [p. 5, 11].

## 8. Frases citáveis (literais)

1. "The balanced scenario emerges as the best management compromise (mean rotation length of 7 ± 0 years)." [p. 6]
2. "Furthermore, the methodological strategy is highly replicable and transferable to other plantation species and regions under similar resource pressures." [p. 11]
