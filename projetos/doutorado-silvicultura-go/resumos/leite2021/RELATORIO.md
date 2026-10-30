# RELATÓRIO — Rodrigo Vieira Leite (2021)

## 1. Referência

LEITE, R. V.; SILVA, C. A.; BROADBENT, E. N.; AMARAL, C. H.; LIESENBERG, V.; ALMEIDA, D. R. A.; MOHAN, M.; GODINHO, S.; CARDIL, A.; HAMAMURA, C.; FARIA, B. L.; BRANCALION, P. H. S.; HIRSCH, A.; MARCATTI, G. E.; DALLA CORTE, A. P.; ALMEYDA ZAMBRANO, A. M.; COSTA, M. B. T.; MATRICARDI, E. A. T.; SILVA, A. L.; GOYA, L. R. R. Y.; VALBUENA, R.; MENDONÇA, B. A. F.; SILVA JUNIOR, C. H. L.; ARAGÃO, L. E. O. C.; GARCÍA, M.; LIANG, J.; MERRICK, T.; HUDAK, A. T.; XIAO, J.; HANCOCK, S.; DUNCANSON, L.; FERREIRA, M. P.; VALLE, D.; SAATCHI, S.; KLAUBERG, C. **Large scale multi-layer fuel load characterization in tropical savanna using GEDI spaceborne lidar data**. *Remote Sensing of Environment*, v. 268, art. 112764, 2022 (disponível online em 30 out. 2021). DOI: 10.1016/j.rse.2021.112764 [p. 1]

Observação: o texto integral está completo (corpo do artigo e referências), sem truncamento, e corresponde ao DOI indicado.

## 2. Pergunta do estudo

Avaliar se o sensor lidar orbital GEDI é capaz de estimar, em escala de bioma, o combustível vegetal (fuel load) em múltiplas camadas — superfície, herbáceo, arbustivo, arbóreo e total — nas formações de Cerrado [p. 3].

## 3. Área e dados

- Local: Cerrado brasileiro; quatro sítios — Parque Nacional da Serra do Cipó, Parque Nacional da Chapada dos Veadeiros, Floresta Nacional de Paraopeba e Floresta da Universidade Federal de São João del-Rei [p. 3].
- Período: inventário de campo em junho–julho de 2019 [p. 4]; voos UAV-lidar em julho de 2019 [p. 5]; dados GEDI em órbita de 18 abr. 2019 a 29 out. 2020 [p. 7].
- Sensores/fontes: UAV-lidar GatorEye Gen 1 (hexacóptero DJI M600 Pro + Velodyne VLP-32c, ~600.000 pulsos/s) [p. 5]; produtos GEDI L2A e L2B versão 2 [p. 7]; classificação de cobertura MapBiomas para mascarar [p. 7].
- Amostras: 50 parcelas de 30 × 30 m (900 m²) — 5 em grassland, 30 em savanna e 15 em forest —, com 4 subparcelas de 1 m² e 2 de 1 × 5 m por parcela [p. 4–5].
- Número de footprints GEDI usados: não informado.

## 4. Método

1. Medição destrutiva do combustível por estrato (duff, litter, galhos caídos, herbáceas, arbustos e árvores com dbh < 10 cm), com secagem a 65 °C e fatores de expansão para Mg ha⁻¹ [p. 4].
2. Simulação de formas de onda GEDI a partir das nuvens de pontos UAV-lidar (gediWFSimulator, pacote rGEDI), com ruído realista para sensibilidade de feixe de 0,98 [p. 5].
3. Cálculo de quatro métricas (RH98, CCF, PAI, FHD) e ajuste de Random Forest com 500 árvores, mtry de 2 a 4, validação cruzada 5-fold e 500 repetições por camada [p. 6].
4. Aplicação dos modelos aos footprints GEDI de ~25 m em todo o Cerrado, agregação para células de 1 km² e partição da incerteza (variabilidade interna, falta de ajuste e aleatoriedade do RF) [p. 7].

## 5. Resultados principais

- Desempenho em validação: WDfuels R² = 0,88 ± 0,029 (RMSE 13,07 Mg ha⁻¹; 40,6%); TFfuels R² = 0,71 ± 0,052 (RMSE 23,01 Mg ha⁻¹; 40,78%) [p. 10].
- Camadas inferiores: SUfuels R² = 0,31 (RMSE 5,22 Mg ha⁻¹), HBfuels R² = 0,46 (RMSE 2,81 Mg ha⁻¹), SHfuels R² = 0,17 (RMSE 6,22 Mg ha⁻¹) e SSfuels R² = 0,15 (RMSE 10,55 Mg ha⁻¹) [p. 10].
- Treinamento: todos os modelos com R² > 0,78, RMSE < 10,83 Mg ha⁻¹ e MD < 0,17 Mg ha⁻¹ [p. 9].
- PCA: dois primeiros componentes explicaram 75,7% da variância; RH98 e FHD correlacionados entre si (r = 0,94) e com WDfuels (r > 0,85) e TFfuels (r > 0,82) [p. 7].
- Médias estimadas para o bioma: SUfuels 7,63 ± 1,63; HBfuels 7,87 ± 1,78; SHfuels 14,74 ± 1,87; SSfuels 7,58 ± 1,64; WDfuels 10,29 ± 9,97; TFfuels 28,55 ± 11,4 Mg ha⁻¹ [p. 10].
- Valores de campo (média) por formação: grassland TFfuels 17,2 Mg ha⁻¹; savanna 40,4 Mg ha⁻¹; forest 104,2 Mg ha⁻¹ [p. 5].
- Extensão: mapas para todo o Cerrado (~1,9 milhão de km²) em grade de 1 km [p. 3].

## 6. Limitações que os próprios autores reconhecem

- Incerteza maior justamente nos combustíveis de superfície e de vegetação baixa; os componentes de superfície dificilmente são recuperados diretamente por lidar [p. 14–15].
- Baixa sensibilidade do GEDI a herbáceas e arbustos baixos; a utilidade do sensor para dossel curto, esparso e sub-bosque "ainda não foi estabelecida" [p. 13].
- Missão GEDI planejada apenas até 2023, limitando a aplicação dos modelos a esse período [p. 15].
- Natureza amostral do GEDI: células de 1 km² ainda sem cobertura, por órbita ou perda por nuvens [p. 15].
- Efeito do terreno (declividade) na detecção do solo e nas métricas não foi tratado no estudo [p. 15].

## 7. O que serve ao projeto e o que não serve

- Serve: o framework multiescala campo → UAV-lidar → simulação GEDI → Random Forest é diretamente replicável para povoamentos de silvicultura, inclusive com as métricas RH98, CCF, PAI e FHD [p. 6].
- Serve: o protocolo de aplicação de GEDI L2A/L2B em órbita (filtro quality_flag = 1, agregação a 1 km²) e a partição da incerteza em três componentes são aproveitáveis para estimativas de biomassa e carbono [p. 7].
- Não serve: a área é Cerrado nativo; o texto não indica sítios em Goiás nem povoamentos plantados; os resultados não transferem valores para silvicultura [p. 3].
- Não serve: a variável resposta é fuel load (Mg ha⁻¹), não biomassa aérea nem estoque de carbono; o artigo não apresenta teor de carbono nem estimativas de carbono [p. 4].

## 8. Frases citáveis (literais)

- "Overall, the models had better performance for woody fuels and total fuel loads (R2 = 0.88 and 0.71, respectively)." [p. 2]
- "GEDI's utility for mapping short, sparse canopies and understory has yet to be established, and while the accuracies seen here are likely lower than for closed-canopy forests, or canopy fuels, our results suggest that GEDI data are still useful for this more challenging application." [p. 13]
