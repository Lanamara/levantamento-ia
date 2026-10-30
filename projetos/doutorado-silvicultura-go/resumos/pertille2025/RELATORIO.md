# RELATÓRIO — Carla Talita Pertille (2025)

## 1. Referência

Pertille, C. T.; Behling, A.; Sanquetta, C. R.; Campoe, O. C.; Le Maire, G.; Guillemot, J.; Barros, G. M.; Schoeninger, E. R.; Dalla Corte, A. P. (2025). *Biomass and Carbon of Eucalyptus spp. Genotypes Estimated With UAV-LIDAR Using Area-Based Approach and Machine Learning*. International Journal of Forestry Research, v. 2025, Article ID 5516907, 16 p. DOI: 10.1155/ijfr/5516907. Recebido em 12/06/2025; aceito em 19/09/2025 [p. 1].

O `TEXTO.txt` está íntegro (16 páginas, do resumo às referências) e corresponde ao DOI informado.

## 2. Pergunta do estudo

Estimar, por unidade de área e por compartimento (total, tronco e copa), a biomassa acima do solo e o estoque de carbono acima do solo de genótipos de *Eucalyptus* spp. a partir de métricas de UAV-LiDAR com abordagem por área (*area-based approach*, ABA), comparando regressão stepwise e cinco algoritmos de machine learning [p. 2].

## 3. Área e dados

- Local: Itatinga, São Paulo, Brasil; área experimental de 192,54 ha ligada ao programa EUCFLUX (IPEF/CIRAD), em talhões de empresa de celulose e papel [p. 2].
- Clima Cfa, altitude 845 m, temperatura média anual 19,4 °C, precipitação média anual 1319 mm [p. 2].
- Povoamento: 5 blocos, 25 genótipos de *Eucalyptus* spp., plantio no fim de 2018, espaçamento 3 × 2 m (6 m² por árvore; 1666 árvores·ha⁻¹), sistema de alto fuste; idade de ~4,5 anos na avaliação [p. 2, p. 8].
- Parcelas: 125 no total, 124 usadas (genótipo 23 no bloco 10 excluído por alta mortalidade); parcela útil de 30 × 20 m (600 m² = 0,06 ha) [p. 2–3].
- Inventário florestal e amostragem destrutiva: maio de 2023; 150 árvores abatidas (6 por genótipo) [p. 1, p. 3].
- Sensor: LiDAR aerotransportado em UAV DJI Matrice 300 com Zenmuse L1, voo em maio de 2023 [p. 4].
- Amostras para modelagem: 124 (88 para treino, 70%; 36 para validação, 30%) [p. 4].

## 4. Método

- Inventário (DAP, altura por clinômetro e modelo hipsométrico de Trorey, R²aj 0,724; Syx 2,36 m) e cubagem pelo método de Smalian; volume por Schumacher–Hall (R²aj 0,985; Syx 6,47%); pesagem dos componentes (madeira, casca, galhos vivos, galhos mortos, folhas) e secagem a 65 °C para obter biomassa seca [p. 3].
- AGB por compartimento estimada por Schumacher–Hall com o genótipo como variável *dummy* (equações 5–7) e convertida para t·ha⁻¹ pelo fator 16,67 (10.000/600 m²); carbono pelo teor médio de 46,08% [p. 4].
- Voo LiDAR a 80 m, 9 m·s⁻¹, faixa de 450 m, 905 nm, até 3 retornos, ângulo de varredura de 45°, densidade média de 389,30 pontos·m⁻²; processamento em R 4.2.0 com pacote lidR (CSF para solo, DTM por kNN/IDW, DSM e CHM por p2r em resolução de 0,5 m, normalização) e extração de 36 métricas [p. 4].
- Seleção de métricas por PCA e stepwise; modelagem por stepwise, ANN, kNN, RF, SVR e XGB com ajuste de hiperparâmetros via `caret`; avaliação por R²aj, Syx, RMSE, índices de concordância (A, p, CC2, λ) e gráficos de Bland–Altman [p. 4–5, p. 7].

## 5. Resultados principais

- Biometria média: DAP 12,86 cm, altura total 20,63 m, volume 261,34 m³·ha⁻¹; maior volume no bloco 10 (282,21 m³·ha⁻¹) e menor no bloco 2 (236,65 m³·ha⁻¹) [p. 5–6].
- Partição da biomassa (árvores abatidas): madeira 64,20 kg·árvore⁻¹ (78,96%), casca 8,17 (10,05%), galhos vivos 4,74 (5,83%), folhas 2,80 (3,45%), galhos mortos 1,39 (1,71%) [p. 5].
- Ajuste do modelo de campo (Schumacher–Hall com *dummy* de genótipo): total R²aj 0,960 e Syx 10,64%; tronco 0,961 e 10,31%; copa 0,808 e 33,72% [p. 7].
- Estoques médios (campo): AGB total 111,22 t·ha⁻¹ e carbono total 51,25 t·ha⁻¹; tronco 100,01 e 46,09 t·ha⁻¹; copa 10,79 e 4,97 t·ha⁻¹; desvio-padrão da AGB total 25,40 t·ha⁻¹ [p. 8].
- Genótipo 21 com maior AGB e carbono (137,61 t·ha⁻¹ e 63,41 t·ha⁻¹) e genótipo 25 com os menores (32,31 t·ha⁻¹ e 14,89 t·ha⁻¹) [p. 8].
- O tronco (madeira + casca) representou 89% da AGB total [p. 8].
- Seleção de métricas: 36 métricas extraídas, 8 excluídas por valor zero; os dois primeiros componentes principais explicaram 81% da variação; ao final, 5 métricas (percentis de altura de 70%, 75%, 80%, 85% e 90%) [p. 5–6].
- RF, ajuste: AGB total R²aj 0,952 e RMSE 5,42%; AGB do tronco 0,959 e 4,59%; carbono total 0,952 e 5,38%; carbono do tronco 0,961 e 4,54% [p. 9].
- RF em validação (30%): RMSE de 10,47% (AGB total), 10,81% (tronco), 10,17% (carbono total) e 10,84% (carbono do tronco) [p. 9].
- Copa: a Tabela 5 traz RF com R²aj 0,844 (biomassa) e 0,924 (carbono) e XGB com 0,765 e 0,707, com RMSE de 13,49% e 15,06% [p. 9].
- Atenção: o texto e o resumo atribuem o melhor ajuste da copa ao XGB, mas informam 0,844/0,924 como sendo do XGB e 0,765/0,707 como sendo do RF [p. 1, p. 6] — o oposto do que consta na Tabela 5 [p. 9].
- stepwise: R²aj entre 0,61 e 0,78 e RMSE entre 10,18% e 18,73% [p. 6]; kNN e SVR com R²aj abaixo de 0,782 e o menor valor na biomassa da copa (0,285), com erros entre 9,94% e 27,06% [p. 6].
- Conclusão: RF eleito para total e tronco (AGB média 110,97 t·ha⁻¹ e carbono 51,16 t·ha⁻¹, a 4,5 anos) e XGB para a copa (10,72 t·ha⁻¹ de biomassa e 4,96 t·ha⁻¹ de carbono) [p. 13].
- Concordância: RF com as melhores medidas (A, p, CC2, λ próximos de 1) em total e tronco; XGB na copa [p. 7].

## 6. Limitações que os próprios autores reconhecem

- Número, tamanho, forma e exatidão da geolocalização das parcelas: foram usadas apenas 124 parcelas de 0,06 ha, retangulares, e os autores citam recomendação de mais parcelas e de maiores dimensões para reduzir erros de geolocalização [p. 8].
- Sensor Zenmuse L1: tipo de sensor, taxa de pulsos e tipo de retorno afetam penetração no dossel, densidade de pontos e altitude de voo, com possível impacto em copas muito densas ou heterogêneas [p. 13].
- Heterogeneidade espacial das parcelas e quantidade limitada de dados [p. 13].
- Métodos convencionais de ML (RF, XGB, ANN, SVR, kNN) foram adequados a este experimento com poucas parcelas, mas a literatura recente indica deep learning mais eficiente em cenários complexos e com dados multimodais [p. 13].
- A ABA fica limitada ao uso de métricas derivadas da distribuição vertical dos retornos LiDAR [p. 8].
- O uso de ML para AGB e carbono em multicompartimentos de plantios clonais de *Eucalyptus* no Brasil com UAV-LiDAR "is still in its infancy" [p. 9].
- Heteroscedasticidade dos resíduos em todos os algoritmos testados [p. 7].
- Dados de pesquisa não são compartilhados [p. 14].

## 7. O que serve ao projeto e o que não serve

- Serve: valores de referência para *Eucalyptus* a ~4,5 anos (AGB total 111,22 t·ha⁻¹, carbono 51,25 t·ha⁻¹, tronco 100,01/46,09, copa 10,79/4,97 e desvio-padrão de 25,40 t·ha⁻¹), úteis para comparar com a silvicultura goiana, ressalvadas as diferenças de sítio e clima [p. 8].
- Serve: o desenho operacional — ABA com poucas métricas (5 percentis de altura, 70%–90%) e RF para total/tronco e XGB para copa, com RMSE de ajuste de ~4,5%–5,4% [p. 6, p. 9] — e o protocolo de amostragem destrutiva com teor de carbono de 46,08% [p. 3–4].
- Não serve como referência de sensoriamento multissensorial: há apenas LiDAR, sem óptico, SAR ou fusão de sensores nos resultados [p. 4].
- Não serve direto para Goiás nem para escala regional: um único sítio, uma idade (~4,5 anos), genótipos clonais e 124 parcelas de 0,06 ha [p. 2–3]; além disso, os números da copa se contradizem entre texto e Tabela 5 [p. 6, p. 9] e os dados não são disponibilizados [p. 14].

## 8. Frases citáveis (literais)

- "Only 124 plots were used in this study—plots of 0.06 ha and rectangular shape." [p. 8]
- "However, the application of the ML algorithms for estimating aerial biomass and aerial carbon in multicompartments (as in this research) of clonal plantations of Eucalyptus spp. in Brazil using UAV-LiDAR data is still in its infancy." [p. 9]

*Observação: citações transcritas como no `TEXTO.txt`; quebras de linha foram unidas.*
