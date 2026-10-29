# RELATÓRIO — Fengyun Cheng (2024)

## 1. Referência

Cheng, F.; Ou, G.; Wang, M.; Liu, C. (2024). *Remote Sensing Estimation of Forest Carbon Stock Based on Machine Learning Algorithms*. **Forests**, 15(4), 681. DOI: 10.3390/f15040681. Publicado em 10/04/2024 [p. 1]. O `TEXTO.txt` corresponde ao artigo do DOI indicado, mas contém trechos duplicados: partes do PDF em versão de pré-revisão foram coladas junto ao texto final (por exemplo, o trecho "FOR PEER REVIEW" repete o conteúdo das páginas 4–15) [p. 4–15]. Os números citados abaixo foram conferidos na versão final.

## 2. Pergunta do estudo

Verificar se o refinamento da classificação de uso da terra em sete classes, com três tipos florestais, e o uso de algoritmos de aprendizado de máquina sobre dados Landsat 8 no GEE aumentam a precisão da estimativa de estoque de carbono acima do solo em escala provincial [p. 3].

## 3. Área e dados

- **Local:** província de Yunnan, China (21°8′–29°15′ N; 97°31′–106°11′ E), 394,1 mil km², 88,64% de área montanhosa [p. 3].
- **Período:** imagens de junho a dezembro de 2021; inventário florestal contínuo de setembro a dezembro de 2021 [p. 4].
- **Sensores/fontes:** Landsat 8 Level 2, Collection 2, Tier 1 (USGS, via GEE), mediana das imagens de junho a dezembro de 2021 com cobertura de nuvens < 20% [p. 4]; NASADEM 30 m para elevação, declividade e aspecto [p. 4]; inventário florestal contínuo nacional (dados proprietários, não públicos) [p. 20].
- **Amostras:** 1072 parcelas fixas de 800 m² medidas em campo [p. 5]; somadas a 460 pontos não florestais obtidos por interpretação visual em imagens Google Earth de 2021, total de 1532 pontos para classificação: 557 floresta de folhosas, 365 coníferas, 150 mista, 90 corpos d'água, 120 área construída, 120 agricultura, 130 outros [p. 5]. Divisão 70% treino / 30% validação [p. 8].

## 4. Método

- Extração de variáveis no GEE a partir de Landsat 8 e NASADEM: 29 fatores para a classificação (7 bandas, 3 componentes da Tasseled Cap Transformation, 10 índices de vegetação, 9 texturas) e 80 variáveis para modelagem (7 bandas, 10 índices, 3 TCT, 3 topográficas, 56 texturas da matriz de coocorrência; o texto fala em 80 variáveis, embora a soma das feições listadas dê 79) [p. 7, 12].
- Comparação de quatro classificadores do GEE (RF, CART, GBT, SVM) em cinco esquemas de combinação de feições, com ajuste de parâmetros: RF com 150 árvores, CART com 120, GBT com 100 árvores e taxa de aprendizado 0,2, SVM com custo 10 e gama 0,5 [p. 6–7, 9].
- Seleção de variáveis por coeficiente de Pearson (21 das 80 variáveis com p < 0,01) e controle de multicolinearidade por VIF (0 < VIF < 10; tolerância > 0,1) [p. 7, 12].
- Modelagem separada para folhosas, coníferas e mistas por regressão linear múltipla stepwise, regressão RF e árvore de decisão, com validação em 30% das parcelas espacialmente não adjacentes às de treino, usando R², RMSE, rRMSE e MAE [p. 7–8]. O estoque de carbono das parcelas foi obtido por volume × Biomass Expansion Factor (BEF) → biomassa por hectare × teor de carbono específico por espécie (Tabela A1) [p. 5–6].

## 5. Resultados principais

- Classificação com apenas as 7 bandas espectrais: acurácia global de 0,7165 (RF), 0,6813 (CART), 0,7130 (GBT) e 0,6127 (SVM); Kappa de 0,6147, 0,5672, 0,6068 e 0,4781 [p. 9].
- Com as cinco famílias de feições (bandas, índices de vegetação, textura, componentes principais e terreno): acurácia global de 0,8496 (RF), 0,8133 (CART), 0,8273 (GBT) e 0,7315 (SVM); Kappa de 0,7646, 0,7186, 0,7320 e 0,6388 [p. 9].
- O RF foi o melhor classificador: acurácia global de 84,96% e Kappa de 76,46% [p. 1, 9].
- A inclusão de texturas reduziu a acurácia global e o Kappa dos quatro algoritmos; índices de vegetação, componentes principais e terreno elevaram ambos [p. 9].
- 21 das 80 variáveis independentes tiveram correlação muito significativa (0 < p < 0,01) com o carbono; o carbono correlacionou-se negativamente com as bandas b1–b7 e positivamente com densidade de copa e elevação [p. 12].
- Regressão linear múltipla stepwise para folhosas: R² = 0,23, RMSE = 35,471, rRMSE = 32,881, MAE = 24,442; R² < 0,4 nos três tipos florestais [p. 13].
- Regressão RF para folhosas: R² = 0,663, RMSE = 24,722, rRMSE = 27,46, MAE = 17,64 [p. 13]; R² de 0,636 para coníferas e 0,638 para mistas [p. 1]; R² > 0,6 nos três tipos tanto em RF quanto em árvore de decisão [p. 13].
- Estoques estimados: folhosas ~100–200 t·hm⁻² no sul de Yunnan (Puer, Xishuangbanna, Dehong, vale do Nujiang); coníferas 100–250 t·hm⁻² no noroeste; mistas ~50–150 t·hm⁻² [p. 14–15].
- Folhosas concentradas entre 1500 e 2000 m (32,47% do carbono total das folhosas); mistas acima de 2500 m (42,60% do total das mistas); declividades de 10–30° concentram 60,95% do carbono florestal [p. 15].
- Ordem do estoque: folhosas > coníferas > mistas [p. 19].

## 6. Limitações que os próprios autores reconhecem

- Erros de classificação por "distinct spectra for the same object" e "the same spectra for different objects", e viés introduzido pelas limitações dos algoritmos; apenas quatro algoritmos testados e persistência de erros de pixels mistos [p. 18–19].
- O estoque de carbono acima do solo inclui apenas árvores vivas, excluindo arbustos, herbáceas, serapilheira e solo [p. 19].
- Não houve análise dinâmica nem previsão de tendência temporal do carbono [p. 19].
- Na região de Puer, a estimativa para coníferas foi prejudicada por escassez de dados de campo e por erros de classificação [p. 14].
- Subestimação de valores altos e superestimação de valores baixos não foi eliminada, e há problema de saturação dos dados [p. 17].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o desenho em duas etapas — classificação de tipos florestais seguida de regressão RF por tipo — com validação espacialmente independente e métricas R², RMSE, rRMSE e MAE, é diretamente replicável para talhões de silvicultura em Goiás [p. 7–8].
- **Serve:** a combinação de bandas, índices de vegetação, Tasseled Cap, texturas e terreno como entrada de RF, e o achado de que texturas podem piorar a acurácia, orientam a seleção de variáveis em um arranjo multissensorial [p. 7, 9].
- **Serve parcialmente:** a cadeia volume → BEF → biomassa → teor de carbono específico por espécie é o caminho para estoque de carbono em plantios, mas os coeficientes usados são de espécies de Yunnan (Tabela A1) e não são transferíveis [p. 5–6, 20].
- **Não serve:** o artigo usa apenas Landsat 8 de resolução média (30 m), sem SAR ou LiDAR, em floresta natural heterogênea de escala provincial; não há dados de plantios, idade, espaçamento ou manejo, e o inventário de campo é proprietário, o que impede reprodução direta do desenho amostral [p. 4, 20].

## 8. Frases citáveis (literais)

- "The results indicate that among the four classification algorithms, the RF classifier demonstrates superior performance, with an overall accuracy of 84.96% and a Kappa coefficient of 76.46%." [p. 1]
- "In this study, forest above-ground carbon storage includes only the carbon stored in live trees and does not encompass the estimation of carbon storage in other components of the forest, such as shrubs, herbaceous vegetation, the litter layer, and the soil layer." [p. 19]
