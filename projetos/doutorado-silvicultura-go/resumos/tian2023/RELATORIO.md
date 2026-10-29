# RELATÓRIO — Lei Tian (2023)

## 1. Referência
- Tian, L.; Wu, X.; Tao, Y.; Li, M.; Qian, C.; Liao, L.; Fu, W. (2023). Review of Remote Sensing-Based Methods for Forest Aboveground Biomass Estimation: Progress, Challenges, and Prospects. *Forests*, 14(6), 1086. DOI 10.3390/f14061086 [p. 1]
- Artigo de revisão, publicado em 24/05/2023 [p. 1]
- Verificação: o TEXTO.txt traz o texto integral do artigo (páginas 1–21 de conteúdo + referências até a página 31); não está truncado nem há indício de divergência com o DOI.

## 2. Pergunta do estudo
Qual o progresso dos métodos de sensoriamento remoto para estimativa de biomassa florestal acima do solo (AGB), quais suas fontes de dados, limitações, incertezas e direções futuras de melhoria da acurácia?

## 3. Área e dados
- Revisão de literatura, sem área experimental própria; exemplos abrangem escala global: Amazônia, Congo, México, Dinamarca, EUA, Suécia, Tailândia, Austrália, China [p. 5, 8, 10, 13–14, 17–18].
- Período: não informado (não há delimitação temporal própria da revisão).
- Sensores/fontes revisadas: passive optical — MODIS, AVHRR, SPOT Vegetation (250–8000 m), Landsat TM/ETM+/OLI, Sentinel-2 MSI, Terra/Aqua ASTER (~30 m), IKONOS, QuickBird, WorldView-2 (<5 m) [p. 6]; microwave — SAR (bandas X, C, S, L, P; polarizações HH, HV, VH, VV), InSAR, PolInSAR, TomoSAR [p. 7–8]; LiDAR — TLS, ALS, GLAS, LVIS, GEDI, ICESat-2/ATLAS [p. 8–9]; UAVs [p. 3, 10]; SIF — GOME-2, OCO-2, TanSat [p. 4].
- Número de amostras: não informado (revisão sem meta-análise; a comparação de mapas de AGB da China usa seis produtos de estudos anteriores) [p. 18–19].

## 4. Método
- Revisão organizada em quatro objetivos: (1) princípios da estimativa de AGB por sensoriamento remoto, (2) avaliação de fontes de dados e métodos, (3) síntese de fontes de incerteza, (4) direções para melhorar a acurácia [p. 3].
- O sensoriamento remoto estima AGB indiretamente, via parâmetros correlacionados (reflectância, VIs, LAI, cobertura, altura de árvore e de dossel), em vez de medir AGB diretamente [p. 3].
- Classificação das fontes de dados em passive optical, microwave e LiDAR, com síntese de vantagens/limitações por sensor e resolução (Tabela 1) [p. 11–12].
- Classificação dos métodos de estimativa em empirical models (paramétricos e não paramétricos: KNN, ANN, SVM, RF, GB, ME, DL), physical models (radiative transfer, geometric optical), mechanistic models e comprehensive models, com análise comparativa de limitações e vantagens (Tabela 2) [p. 12–16].
- Discussão de incertezas atribuídas a quatro grupos: remote sensing images, sample plot survey data, stand structure e statistical models [p. 16].

## 5. Resultados principais
- Relação constante AGB–altura (BPS) em florestas fechadas: média global de 9,9 Mg/(hm²·m), com variação regional de 9,4–10,5 Mg/(hm²·m) [p. 4].
- Saturação por banda SAR: C-band satura em ~60–70 Mg/ha; L-band e P-band satura em ~100 Mg/ha em florestas tropicais complexas, subindo a ~250 Mg/ha em povoamentos de estrutura simples [p. 8].
- L-band com polarização cruzada (HV), em ângulos de incidência ≥45°, foi a mais adequada para AGB, com saturação de 80–85 Mg/ha (Lucas et al., Queensland, Austrália) [p. 8].
- Combinação de dados L- e P-band teve maior acurácia do que banda única, por ser sensível a biomassa baixa (L) e alta (P) [p. 8].
- Métrica de waveform adaptada à declividade (GLAS) alcançou R² = 0,92 na estimativa de AGB florestal [p. 9].
- Densidade de pontos LiDAR acima de 5 points/m² faz modelos baseados em CHM e em waveform performarem de forma semelhante [p. 9].
- Fusão SAR + óptico: modelo com backscatter/textura ALOS-2 e NDVI de Landsat 8 obteve R² = 0,66 em floresta mista (Califórnia e Alpes), com estimativas de baixo custo e ampla cobertura em escala regional [p. 10].
- UAV + Sentinel-1 + Sentinel-2 superou o uso de sensor único na estimativa de AGB de mangue no Senegal, em nível de amostra [p. 10].
- No México (algoritmo ME), a maior contribuição relativa para AGB foi de ALOS/PALSAR (50,9%), seguida por MODIS VI (32,9%) e SRTM DEM (menor contribuição) [p. 14].
- Incerteza de 20% no carbono total estimado para a bacia Amazônica (regressão de Saatchi et al.), correlacionada ao comprimento da estação seca [p. 16].
- Erros de localização de parcelas reduzem a acurácia do carbono florestal estimado; o upscaling espacial atenua esse efeito (Landsat TM + inventário nacional) [p. 16–17].
- Tipo de sensor é o fator mais importante para a acurácia (LiDAR supera hyperspectral); hyperspectral + LiDAR não melhorou a predição; modelos afetam mais que o tamanho de amostra [p. 17].
- Para a China, seis produtos apresentaram AGB médio de 69,88–120,00 Mg/ha, com valores individuais entre 61,80 (Du et al., ~5600 m) e 120,00 Mg/ha (Su et al., 1000 m); Huang et al. deu 69,88 Mg/ha a 30 m [p. 18–19].
- Perspectiva: dados HLS (Landsat 8 + Sentinel-2) com intervalo de até 5 dias e 30 m permitem estimativa consistente do local ao global [p. 19].

## 6. Limitações que os próprios autores reconhecem
- Saturação do sinal em óptico e radar em AGB alto, limitando estimativas em florestas tropicais/subtropicais densas [p. 2–3].
- Óptico tem baixa penetração e registra sobretudo estrutura horizontal, dificultando deduzir tree height e DBH; satura em florestas muito densas [p. 7].
- SAR não distingue tipos de vegetação e é sensível a vento, umidade e temperatura; a saturação do sinal também reduz a acurácia [p. 8].
- LiDAR: alto custo de aquisição, cobertura descontínua e pequena área; a acurácia de inversão é afetada pelo terreno [p. 9].
- Escolher sensor adequado conforme disponibilidade de dados, orçamento do projeto e exigência técnica permanece um desafio prático; dados de campo adicionais continuam indispensáveis para construção e validação de modelos [p. 11].
- Physical models têm cálculo complicado e só se aplicam a pequenas áreas; mechanistic e comprehensive models exigem muitos parâmetros difíceis de obter, e os comprehensive dependem de informação detalhada por espécie [p. 12, 15–16].
- Cada fonte de incerteza — imagens, dados de parcelas, stand structure e modelos estatísticos — gera subestimação de valores altos e superestimação de valores baixos de AGB [p. 16].
- Faltam, ainda, dados AGB medidos com acurácia em escala regional e global para treinar modelos empíricos e de machine learning [p. 19].

## 7. O que serve ao projeto e o que não serve
- Serve: fundamenta a escolha de dados gratuitos de resolução média (Landsat/Sentinel-2, 10–30 m) para estimativa de AGB em escala local/regional, situação típica de um levantamento de silvicultura em Goiás [p. 6, 11].
- Serve: alerta quantitativamente sobre o limite de saturação das bandas (~60–70 Mg/ha em C-band; ~100–250 Mg/ha em L/P-band), crítico para povoamentos de alta biomassa, e indica LiDAR (GEDI, ICESat-2) e fusão multissensorial como caminhos para contorná-lo [p. 8–9, 19].
- Serve: dá base para decidir o modelo — MR é útil em escala local/regional, enquanto machine learning (RF, XGBoost, SVM) tem vantagem em projetos regionais/globais, com destaque para seleção de variáveis e modelagem por tipo florestal [p. 14, 20–21].
- Não serve: não traz equações alométricas, fatores de conversão ou resultados específicos para espécies de silvicultura brasileira ou para o Cerrado/Goiás; é revisão sem experimento original, então não fornece valores de AGB diretamente aplicáveis ao nosso inventário.

## 8. Frases citáveis (literais)
- "However, optical and radar data generally suffer from signal saturation at high AGB, which limits their ability to estimate AGB in dense tropical and subtropical forests [40,67]." [p. 3]
- "Combining remotely sensed data from multiple sources is the most promising strategy for AGB estimation." [p. 21]
