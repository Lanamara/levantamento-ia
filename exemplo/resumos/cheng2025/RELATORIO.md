# RELATÓRIO — Xiaofang Cheng (2025)

## 1. Referência

Cheng, X.; Zhou, L.; Liu, S.; He, C.; Teng, Y. (2025). Improving Forest Above-Ground Biomass Estimation Using UAV LiDAR and RGB with Machine Learning Algorithm. *Forests*, 16, 1819. DOI: 10.3390/f16121819. Texto integral, 20 páginas, compatível com o DOI informado [p. 1].

## 2. Pergunta do estudo

Se a fusão de dados UAV LiDAR e RGB, com seleção de variáveis e modelos de machine learning interpretáveis, estima melhor a AGB de árvores individuais de *Larix principis-rupprechtii* em floresta secundária natural do que cada fonte de dados isolada.

## 3. Área e dados

- Local: Reserva Natural de Pangquangou, Lvliang, província de Shanxi, norte da China (111°22′–111°33′ E, 37°45′–37°55′ N; 1.800–2.831 m de altitude) [p. 3].
- Período: voo em julho de 2024 [p. 4]; data do inventário de campo: não informado.
- Sensores: DJI Matrice 300 RTK com plataforma Zenmuse H20T (RGB e LiDAR), altura relativa de 90 m, sobreposição frontal e lateral de 85% [p. 4].
- Amostras: 8 parcelas de 60 × 60 m, árvores com DBH ≥ 5 cm; 1.070 árvores medidas em campo, das quais 936 (87,5%) foram pareadas e usadas na modelagem [p. 3, p. 9]. Imagens RGB recortadas em tiles de 512 × 512 (72 tiles, divisão 7:1:2), com 457 árvores anotadas no conjunto de teste [p. 5].

## 4. Método

1. AGB de referência por equação alométrica específica da espécie: Y = a·(DBH²·H)^b, com a = 0,0275 e b = 0,9576 [p. 3–4].
2. Segmentação de copas por Mask R-CNN (ResNet50 + FPN) nas imagens RGB e por region growing com seed points no point cloud (janela de 5 m, altura mínima de 1,5 m), com pareamento espacial e morfológico entre as duas fontes [p. 4–6].
3. 88 variáveis (23 RGB e 65 LiDAR), normalizadas por Z-score; seleção por RF permutation importance dentro de cada fold de validação; curva de ablação definiu top 20 (RGB), top 15 (LiDAR) e top 30 (combinado) [p. 6–7, p. 11].
4. RF como baseline, LightGBM e XGBoost com otimização bayesiana de hiperparâmetros; validação espacial leave-one-plot-out (8 folds); R², RMSE, MAE, rRMSE e Bias, com IC 95% por 1.000 reamostragens bootstrap; interpretação por SHAP [p. 7–9, p. 12].

## 5. Resultados principais

- Segmentação: recall de 93,07%, precision de 87,5% e F1-score de 90,21%; AP de 0,663 entre IoU 0,50 e 0,95, com 0,905 em IoU 0,50 e 0,844 em IoU 0,75; RMSE da largura média de copa de 0,90 m [p. 9].
- Pareamento: 1.070 árvores medidas, 936 (87,5%) pareadas; 134 (12,5%) excluídas, por omissão (8,4%) e por erro de segmentação (4,1%) [p. 9].
- RGB isolado: R² de 0,495 (RF), 0,457 (LightGBM) e 0,508 (XGBoost); rRMSE acima de 36% [p. 11–12].
- LiDAR isolado: R² de 0,743 (RF), 0,731 (LightGBM) e 0,748 (XGBoost) [p. 11–12].
- Combinado: R² de 0,751 (RF), 0,759 (LightGBM) e 0,770 (XGBoost, melhor modelo), com RMSE de 156,88 kg·árvore⁻¹, MAE de 113,65 kg·árvore⁻¹, Bias de −12,71 kg·árvore⁻¹ e rRMSE de 25,18% [p. 12].
- IC 95% do R² no RF-RGB: [0,3953; 0,5795], a maior incerteza entre os grupos de variáveis [p. 11].
- SHAP: no conjunto combinado, as três variáveis mais influentes foram CV, H e CD; CV e H vêm do LiDAR e CD do RGB [p. 13–14].
- Ganho de 0,093 em R² sobre o método de Li et al. (R² = 0,677) [p. 15].
- Inconsistência interna: a Seção 4.3 atribui ao XGBoost R² de 0,503 (RGB), 0,732 (LiDAR) e 0,760 (combinado) [p. 15], diferentes dos valores da Tabela 4 [p. 12].

## 6. Limitações que os próprios autores reconhecem

- A acurácia da segmentação cai em áreas de copas densas e sobrepostas, o que os autores tratam como limitação do método em estruturas complexas [p. 16–17], com a mesma ressalva na discussão [p. 15].
- Inclinação do terreno na área de voo e tipo de vegetação de sub-bosque podem restringir a segmentação de copas por afetarem a qualidade da imagem [p. 15].
- O erro vertical do DEM calibrado (erro médio de 1,64 m) se propaga para a extração da altura das árvores e entra no orçamento de incerteza da AGB [p. 4, p. 15].
- Incertezas de campo no DBH (±0,5 cm) e na altura (±5%) geram ruído na AGB de referência usada no treino e na avaliação [p. 4].
- Trabalho futuro proposto: avançar na segmentação de copas densas, incluir correção topográfica e validar o modelo em árvores de tamanhos variados e em condições florestais diversas [p. 17].

## 7. O que serve ao projeto e o que não serve

- Serve: o desenho de fusão LiDAR + RGB com seleção de variáveis por permutation importance e ablação, replicável em povoamentos plantados, onde árvores individuais são mais separáveis do que em floresta natural.
- Serve: a evidência de que atributos estruturais (H e CV) superam os espectrais e de que a fusão eleva o R² de 0,508 (RGB) e 0,748 (LiDAR) para 0,770 [p. 12], como argumento quantitativo para incluir LiDAR no projeto; o protocolo leave-one-plot-out e o uso de SHAP também são reaproveitáveis [p. 7, p. 13–14].
- Não serve: o artigo estima apenas AGB por árvore em kg, sem conversão para carbono, sem fração de carbono e sem estimativa por área (Mg/ha), escala de que o projeto precisa para talhão e estado.
- Não serve: espécie (*Larix principis-rupprechtii*), equação alométrica e região temperada da China são específicas, e o DBH da referência é medido em campo, não pelo sensoriamento — a transferência para silvicultura em Goiás exigiria nova calibração [p. 3–4].

## 8. Frases citáveis (literais)

> "The Extreme Gradient Boosting (XGBoost) algorithm achieved the best performance, with an R2 of 0.770 using the combined feature set." [p. 1]

> "Notably, the features assigned the highest importance by the model were derived from point cloud data." [p. 14]
