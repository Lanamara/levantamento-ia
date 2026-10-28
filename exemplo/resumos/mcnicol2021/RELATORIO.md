# RELATÓRIO — Iain M. McNicol (2021)

## 1. Referência

McNicol, I. M.; Mitchard, E. T. A.; Aquino, C.; Burt, A.; Carstairs, H.; Dassi, C.; Modinga Dikongo, A.; Disney, M. I. (2021). *To What Extent Can UAV Photogrammetry Replicate UAV LiDAR to Determine Forest Structure? A Test in Two Contrasting Tropical Forests*. Journal of Geophysical Research: Biogeosciences, 126, e2021JG006586. DOI: 10.1029/2021JG006586 [p. 1].

O `TEXTO.txt` está completo: 17 páginas, do resumo até a lista de referências [p. 1–17].

## 2. Pergunta do estudo

Em que medida nuvens de pontos de SfM-DAP obtidas com UAV conseguem replicar as métricas de estrutura florestal medidas simultaneamente por LiDAR de UAV, em duas florestas tropicais contrastantes? [p. 1, 3]

## 3. Área e dados

- Peru: Comunidad Nativa Bélgica, ~40 km a oeste de Iñapari, Madre de Dios; área de ~20 km² em mosaico de agricultura, pastagem, floresta secundária e madura; 500–600 stems/ha; coleta em julho de 2019 [p. 3].
- Gabão: concessão de exploração da Rougier Gabon, 10 km², quase toda floresta madura com aberturas junto à rede de estradas; 200–300 stems/ha; coleta em janeiro de 2020 [p. 3].
- Sensores: UAV de asa fixa DELAIR DT26X com LiDAR RIEGL miniVUX-1DL (905 nm, FOV de ±23°, até 5 retornos) e câmera RGB de 36 MP, com Applanix APX-15 IMU e GNSS L1/L2 para correção PPK [p. 3].
- Voos: 15 missões em 10 dias de campo (7 no Peru, 3 no Gabão), a 100–130 m de altitude, 17 m/s, GSD de 3 cm, sobreposição lateral de 70% e frontal de 75% [p. 6].
- Área útil após filtro de densidade (<10 pts/m² excluídos): 1.100 ha no Peru e 655 ha no Gabão; densidade final LiDAR de 220 e 240 pts/m², DAP de 210 e 140 pts/m² [p. 6–7].
- Unidade amostral: grades de 20 m (0,04 ha) [p. 8]. Número de células analisadas: não informado.

## 4. Método

1. Coleta simultânea de LiDAR e imagens no mesmo UAV; trajetórias em POSPac, nuvens em RiPROCESS e Pix4DMapper 4.4.12, filtragem de outliers e rarefação em voxels de 10 cm; processamento das métricas no pacote lidR [p. 6].
2. Métricas de dossel: TCH e rugosidade (desvio-padrão das alturas na célula), tree fractional cover e canopy closure com limiar fixo de 10 m, gap fraction fixa e variável (esta com limiar de 50% da altura máxima em janela de 50 × 50 m) [p. 8].
3. Estrutura vertical: perfis em bins de 1 m, VCI/entropy (índice de Shannon normalizado, 0–1), percentis RH5–RH95 e Canopy Ratio = (RH95–RH25)/RH95 [p. 9].
4. Validação célula a célula por CCC, Bias/Mean Error e RMSE (absoluto e relativo ao LiDAR), repetindo o cálculo com o DTM do LiDAR no lugar do DTM do DAP [p. 8, 10–11].

## 5. Resultados principais

- Superfície e rugosidade concordam bem (CCC 0,99; diferença máxima de 1–2 m) [p. 10]. Retornos de solo têm CCC 0,42 e pioram acima de 70% de cobertura de dossel [p. 10].
- TCH subestimado em média 6 m no Gabão (RMSE 11,6 m; −18%, SD 36%) e 8 m no Peru (RMSE 10,0 m; −40%, SD 26%) [p. 10].
- O erro cresce acima de 80%–90% de canopy closure, com estimativas caindo a <50% do valor LiDAR no Peru [p. 10]; mesmo em áreas abertas o RMSE fica em 40%–50% e as diferenças são inconsistentes [p. 14].
- Gap fraction variável superestimada (%Bias de 40% no Gabão e 37% no Peru) e tamanho de clareiras superestimado em 200% e 91%; fractional cover subestimada (−15% e −40%) e canopy closure (−7% e −29%) [p. 10].
- Métricas verticais com viés relativo de 10%–20% [p. 10]; percentis RH ficam dentro de 5% do LiDAR [p. 15]. Com DTM do LiDAR, o viés de fractional cover, canopy closure e gap fraction cai, mas RH e VCI praticamente não mudam [p. 11].
- Contexto LiDAR: TCH de 35–50 m no Gabão e 25–40 m no Peru; clareiras pelo método variável em 7% da área no Gabão (91 m²) e 20% no Peru (113 m²); clareiras por limiar fixo <5% nos dois sítios [p. 9].
- Densidade de retornos junto ao solo no LiDAR de apenas 1–10 pts/m², ainda assim suficiente para a elevação do terreno [p. 15].
- Acurácia geométrica final da nuvem LiDAR: 1,8 cm [p. 6].

## 6. Limitações que os próprios autores reconhecem

- Condições de iluminação não controladas: voos de 45–75 min e distâncias de 1–7 km geraram diferenças dentro e entre missões [p. 6].
- Sobreposição de 70%/75% e GSD de 3 cm devem ser tratados como mínimo para vegetação densa [p. 6].
- Os dados são "ótimos" graças à correção PPK; plataformas e sensores mais baratos podem produzir DSMs piores, e os GCPs exigem GNSS de precisão e são difíceis de instalar em floresta densa [p. 15].
- Métricas de perfil vertical são sensíveis ao sensor e à plataforma LiDAR e ao software de SfM, cujos algoritmos são proprietários e uma "black box"; a transferência para modelos existentes só vale onde a correspondência já foi demonstrada [p. 15].
- A necessidade de um DTM acurado anula boa parte das vantagens originais do SfM-DAP sobre o LiDAR [p. 14].
- Voos além da linha de visada exigiram autorização especial, o que pode não ser possível em outros contextos [p. 6].

## 7. O que serve ao projeto e o que não serve

- Serve: o desenho de validação (CCC, bias, RMSE em grades de 20 m) e o conjunto de métricas (TCH, rugosidade, fractional cover, gap fraction, VCI, RH, Canopy Ratio) são diretamente reaproveitáveis para comparar DAP e LiDAR em povoamentos plantados [p. 8–9].
- Serve: demonstra que, havendo DTM, o DAP entrega altura, heterogeneidade e cobertura de copa próximas do LiDAR, e que as métricas verticais independem do DTM [p. 11, 14].
- Não serve: o artigo não estima biomassa nem estoque de carbono; as métricas são discutidas como preditoras, sem ajuste de modelo de AGB [p. 8, 12].
- Não serve: o contexto é floresta tropical natural no Gabão e no Peru, não silvicultura, e o DAP isolado erra a altura em 18%–40% [p. 10].

## 8. Frases citáveis (literais)

- "We show that SfM-DAP data cannot be used in isolation to measure key aspects of forest structure, including canopy height (%Bias: 40%–50%), fractional cover, and gap fraction, due to difficulties measuring ground elevation, even under low tree cover." [p. 1]
- "However, even in more open areas, there still exists large, and, inconsistent differences (40%–50% RMSE) between the SfM-DAP and LiDAR-derived estimates of tree height, even in areas with low to, non-existent tree cover, or in areas with larger canopy gaps." [p. 14]
