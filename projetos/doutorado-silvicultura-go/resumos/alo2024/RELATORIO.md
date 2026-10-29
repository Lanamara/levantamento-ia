# RELATÓRIO — Lívia Lanzi Aló (2024)

## 1. Referência

Aló, Lívia Lanzi; le Maire, Guerric; Thiersch, Cláudio Roberto; Mota, Thiago Santos; Pinheiro, Rafael Costa; Passos, José Raimundo de Souza (2024). *Mapping stem volume in fast-growing eucalypt plantations: integrating spectral, textural, and temporal remote sensing information with forest inventories and spatial models*. **Annals of Forest Science**, 81:43. DOI: 10.1186/s13595-024-01255-6. O `TEXTO.txt` está completo (16 páginas, do resumo às referências) e corresponde ao DOI indicado.

## 2. Pergunta do estudo

Avaliar se índices de textura de imagem SPOT-6 de alta resolução e integrais temporais de NDVI da série Landsat, usados como variáveis auxiliares em Kriging with External Drift (KED) e em Generalized Additive Model (GAM), melhoram a predição do volume de madeira de plantações de *Eucalyptus* sp. de ciclo curto no Brasil [p. 1, p. 3].

## 3. Área e dados

- Local: talhões de *Eucalyptus* sp. no sul de Mato Grosso do Sul, próximo a Ribas do Rio Pardo (grafado "Ribas do Rio Padro" no texto), altitude média de 374 m, clima tropical Aw, precipitação média de 1241 mm e temperatura média de 24,2 °C [p. 3].
- Inventário florestal: agosto de 2018, 211 parcelas circulares de 500 m² em grade sistemática, uma parcela a cada ~722 m; todos os talhões com menos de 4 anos (classes de 1,5–4,5 anos), com 8, 7 e 1 clones por classe de idade, totalizando 9431,21 ha [p. 3].
- Volume por parcela: mínimo de 1,16, máximo de 249,84, média de 59,79 m³ ha⁻¹, desvio padrão de 58,85 e CV de 0,98 [p. 3].
- Sensores: SPOT-6 (4 bandas espectrais a 6 m + pancromática a 1,5 m, 12 bits, imagem de agosto de 2018, pansharpened para 1,5 m) e série Landsat-5 TM, Landsat-7 ETM+ e Landsat-8 OLI (30 m, janeiro de 2000 a agosto de 2018) [p. 4]. SPOT e Landsat reamostrados para 7,5 m [p. 4].
- Variáveis: 86 preditores extraídos das imagens [p. 5].

## 4. Método

- Extração de 86 variáveis: reflectâncias SPOT-6, 12 razões simples entre bandas, NDVI, SAVI e ARVI, textura GLCM (contraste, correlação, energia, homogeneidade) em janela 3 × 3 pixels e quatro direções, produtos e razões banda × textura, e integrais/mínimos/máximos de NDVI da série Landsat [p. 4–5].
- Seleção de variáveis por oito métodos de regressão múltipla (forward e backward stepwise, sequential replacement, Sparse PLS, Spike and Slab Lasso, Ridge, Lasso e Elastic Net), com divisão 80% treino / 20% validação e métricas RMSE, R² ajustado e AICc [p. 4, p. 6].
- KED com os preditores selecionados como external drift; cinco modelos de variograma testados (exponencial, esférico, Matérn, gaussiano e Matérn de Stein), ajuste por Levenberg–Marquardt e escolha pelo menor RMSE [p. 6–7].
- GAM com spline de regressão penalizada sobre longitude e latitude (pacote `mgcv`, suavização por GCV), sem co-krigagem de resíduos; desempenho avaliado por validação cruzada cinco vezes [p. 6–7].

## 5. Resultados principais

- Correlação de Spearman com o volume: idade 0,83; integrais INT_0_DM, INT_0_DS e INT_1_DM entre 0,86 e 0,89; bandas SPOT B1, B2 e B3 negativas, de −0,74 a −0,77 [p. 7]. NDVI R = 0,49 e SAVI R = 0,47 [p. 9].
- Modelos lineares retiveram de 3 a 7 variáveis; nenhum selecionou NDVI, SAVI ou ARVI; RAT_B3_B2 apareceu em metade dos modelos [p. 7].
- Melhor modelo: Lasso (`mod_ls`), com RAT_B1_B2, RAT_B2_B4, RAT_B3_B2, INT_0_DM, INT_0_2 e INT_2_MAX [p. 8]. Calibração: RMSE 14,03 m³ ha⁻¹, R² 0,94, AICc 1399,54 [p. 7]; validação: RMSE 12,44 m³ ha⁻¹ e R² 0,95 [p. 7].
- KED: variograma Matérn de Stein, range de 2750 m, nugget de 92,5 m³ ha⁻¹ e sill de 179 m³ ha⁻¹; na validação, R² 0,96 e RMSE 10,62 m³ ha⁻¹; variáveis auxiliares explicaram ~94% da variância e o termo espacial 5% [p. 7–8].
- GAM: R² 0,96 e RMSE 10,56 m³ ha⁻¹; variáveis auxiliares ~98% da variância e termo espacial 1,2% [p. 8].
- O mapa final de volume foi gerado com GAM em pixels de 7,5 m; diferenças visuais entre linear, KED e GAM foram pequenas [p. 8–9, p. 10].
- Crescimento médio citado para esses plantios: 40 m³ ha⁻¹ ano⁻¹, com altura de dossel acima de 20 m no corte aos ~7 anos [p. 3]. RMSE de 24 m³ ha⁻¹ em estudo anterior comparável (Marsden et al.) [p. 11].

## 6. Limitações que os próprios autores reconhecem

- A incerteza das predições não foi analisada em profundidade nem propagada entre escalas (árvore, parcela, interpolação) [p. 10].
- Os modelos foram criados para eucalipto em contexto pedoclimático específico e dependem de calibração local com inventário; aplicabilidade em outras regiões, sobretudo em talhões com danos e heterogeneidade local de volume, ainda precisa ser confirmada [p. 11].
- Apenas uma imagem SPOT-6 foi usada, com reflectância top-of-atmosphere aplicada diretamente, sem correção atmosférica [p. 4].
- A textura mostrou correlação apenas moderada com o volume, com relações dependentes do sítio, e não entrou no melhor modelo [p. 9–10].
- A idade dos talhões veio do gestor florestal, não do sensoriamento remoto [p. 10].
- KED exigiu mais recursos computacionais e a escolha de um modelo de variograma [p. 10].
- Os dados não podem ser disponibilizados publicamente por questões de propriedade [p. 14].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o desenho de variáveis temporais — integrais de NDVI desde o plantio (INT_0_DM, INT_0_2, INT_2_MAX), que foram as mais correlacionadas com o volume (0,86–0,89) e sobrevivem à seleção por Lasso [p. 7–8] — é diretamente transponível para biomassa e estoque de carbono em plantios de Goiás, desde que se aplique fator de expansão e densidade da madeira.
- **Serve:** a combinação de razões de bandas e textura GLCM como auxiliares em KED/GAM, com validação 80/20 e validação cruzada cinco vezes, oferece um protocolo de comparação entre modelo linear e modelos espaciais [p. 4–8].
- **Serve com cautela:** o ganho dos modelos espaciais é pequeno (RMSE de 12,44 para 10,6 m³ ha⁻¹; R² de 0,95 para 0,96) e quase todo o poder preditivo vem das variáveis auxiliares, não da autocorrelação espacial [p. 7–8].
- **Não serve:** o artigo estima volume do fuste, não biomassa ou carbono; não há dados de Goiás (o estudo é no Mato Grosso do Sul), nem radar ou LiDAR, e a abordagem depende de data de plantio e de equações de volume calibradas pela empresa [p. 3, p. 4, p. 11].

## 8. Frases citáveis (literais)

- "The best linear model of stem volume using remotely sensed predictors gave an R-squared value of 0.95 and a Root Mean Square Error (RMSE) of 12.44 m3/ha." [p. 1]
- "The models were created for eucalypt plantations in a specific pedoclimatic context." [p. 11]
