# RELATÓRIO — João Victor do Nascimento Lima (2026)

## 1. Referência

- Autores: João Victor do Nascimento Lima (correspondente), Gabriel Fernandes Bueno, Leonardo Ippolito Rodrigues, Tassius Menezes Araújo, Álvaro Augusto Vieira Soares e George Deroco Martins [p. 1].
- Ano: 2026 (recebido em 1 abr. 2026, aceito em 13 abr. 2026, publicado em 21 abr. 2026) [p. 1].
- Título: "Potential Improvement of Forest Growth and Yield Modeling Incorporating Remote Sensing and Machine Learning" [p. 1].
- Revista: o arquivo traz apenas o cabeçalho "IEEE Geoscience and Remote Sensing Society Section", vol. 14, 2026, pp. 63225–63235; o nome da revista não é escrito no texto — **não informado** [p. 1, p. 11].
- DOI: 10.1109/ACCESS.2026.3686127. No PDF o DOI aparece com erro de extração ("10.1 109/ACCESS.2026.3686127") [p. 1], mas corresponde ao DOI deste pedido.
- Estado do arquivo: texto íntegro (11 páginas, com referências e notas biográficas dos autores), sem truncamento.

## 2. Pergunta do estudo

Testar se índices espectrais e de textura derivados de imagens Landsat 8, usados como proxies ecofisiológicos, aumentam a acurácia das projeções de área basal e volume do modelo de Clutter e se algoritmos de machine learning superam esse modelo em plantios clonais de Eucalyptus [p. 2–3].

## 3. Área e dados

- Local: mesorregião do Vale do Rio Doce, Minas Gerais, Brasil (altitude média de 860 m; precipitação média anual de 1.600 mm) — não é Goiás [p. 3].
- Período: inventário florestal contínuo medido entre junho de 2013 e julho de 2019 [p. 3]; imagens de 2013–2019 [p. 4].
- Base dendrométrica: inventário contínuo da Celulose Nipo-Brasileira (CENIBRA), com idade, área basal, altura dominante e volume comercial até dap mínimo de 5 cm, sem casca; idades de ~2 a 8,5 anos e rotação média de 7 anos [p. 3].
- Material genético: 28 genótipos clonais em sete espaçamentos iniciais (3 × 2,5 m a 4 × 2,5 m) [p. 3].
- Sensor/fonte: Landsat 8 OLI (30 m, 16 bits, revisita de 16 dias), imagens Level-2 sem nuvens do USGS; 8 índices espectrais e 8 métricas de textura por GLCM [p. 1, p. 3–5].
- Amostras: 2.854 parcelas em 372 talhões no banco original; após filtro (≥ 3 medições e sobrevivência > 90%), 825 parcelas em 137 talhões, com ~165 parcelas por fold na validação cruzada 5-fold [p. 3].

## 4. Método

- Sistema de Clutter de duas equações (área basal futura e volume futuro), ajustado por two-stage least squares (2SLS); o termo com VI/TI entra apenas na equação de área basal, multiplicado por (1 − I1/I2) para garantir consistência (G2 = G1 quando I2 = I1) [p. 4–5].
- Reflectância Landsat 8 obtida por centróides de pixels dentro do polígono do talhão e média por talhão, associada à medição de inventário com data mais próxima; 16 índices testados (NDVI, GNDVI, SAVI, SR, RVI, DVI, NBRI, EVI, Energy, Entropy, Correlation, IDM, Inertia, CS, CP, HC) [p. 4–5].
- Cinco algoritmos de machine learning (Random Forest, SVM, XGBoost, ELM, KNN) treinados com os mesmos preditores do Clutter (idade atual, idade alvo, área basal atual, índice de sítio) e com combinações de 1, 2, 3, 4 e 8 índices; hiperparâmetros por grid search. Observação: o resumo cita "Artificial Neural Network" [p. 1], mas os métodos descrevem Extreme Learning Machine (ELM) [p. 5].
- Validação cruzada 5-fold com partição aleatória; métricas RMSE%, bias (%), r e R², com máximo, mínimo, média e desvio-padrão entre folds [p. 6].

## 5. Resultados principais

- Clutter tradicional, área basal (médias entre folds): RMSE% = 6,33; bias = 0,08 m² ha⁻¹; r = 0,96; R² = 0,91 [p. 7].
- Clutter tradicional, volume (médias entre folds): RMSE% = 8,51; bias = 1,06 m³ ha⁻¹; r = 0,97; R² = 0,93 [p. 7].
- Ganho máximo ao inserir VI/TI no Clutter: 0,01% (RMSE%), 0,01 m² ha⁻¹, 0,001 (r) e 0,002 (R²) na área basal; 0,08%, 0,01 m³ ha⁻¹, 0,0004 e 0,0009 no volume [p. 7]. O resumo reporta redução de RMSE de ~0,05% [p. 1].
- Os coeficientes dos termos VI/TI foram significativos, exceto CShude, CProminence e HC [p. 7].
- Machine learning só com preditores dendrométricos: ordem de desempenho SVM > XGBoost > ELM > RF > KNN, com RMSE% de 7,91 a 10,55; bias de 0,79 a 1,74 m³ ha⁻¹; r de 0,95 a 0,97; R² de 0,90 a 0,95 [p. 7].
- Melhor SVM (com HC como preditor extra): RMSE% = 7,76; bias = 0,59; r = 0,97; R² = 0,95. Melhor XGBoost (Energy + Entropy + Correlation + IDM): RMSE% = 8,77; bias = 0,16; r = 0,97; R² = 0,93 [p. 7].
- Resumo: machine learning melhorou a acurácia em até 0,7% [p. 1]. Nenhum VI, TI ou combinação melhorou as estimativas de forma consistente; no KNN a inclusão de índices chegou a piorar o desempenho [p. 7].
- Índices mais influentes: SR, NBRI e Haralick correlation (HC) [p. 1, p. 7–8].
- Ganho operacional: passar de RMSE ~8,5% para ~7,8% equivale a 1,5–2,5 m³ ha⁻¹ em talhões de 250–300 m³ ha⁻¹ [p. 9].
- Não foi feito teste formal de significância entre modelos [p. 7].

## 6. Limitações que os próprios autores reconhecem

- Partição 5-fold aleatória, sem estratificação espacial ou temporal, com possível autocorrelação espacial e temporal; as métricas devem ser interpretadas com essa ressalva [p. 6].
- Uso de médias espectrais por talhão e ausência de parcelas georreferenciadas, o que suprime a variabilidade interna dos talhões [p. 8, p. 9].
- Resolução espacial e temporal limitada do Landsat 8, que restringe a detecção de dinâmicas finas de crescimento; o período 2013–2019 limitou a oferta de sensores melhores [p. 8–9].
- Os ganhos podem ser considerados modestos do ponto de vista operacional e não justificar o custo de adquirir, processar e integrar imagens ao inventário contínuo, nem a substituição de sistemas de prognóstico já consolidados [p. 9].
- Ausência de teste estatístico formal de diferença entre modelos [p. 7, p. 8].

## 7. O que serve ao projeto e o que não serve

- Serve: o desenho comparativo (mesma base, mesmos preditores, Clutter versus cinco algoritmos, validação 5-fold, RMSE%/bias/r/R²) é replicável para biomassa e estoque de carbono na silvicultura goiana [p. 6–7].
- Serve: a triagem de variáveis — SR, NBRI e métricas de textura GLCM (HC, Energy, Entropy) como candidatas, com o alerta de saturação do NDVI em dossel fechado [p. 7–8].
- Não serve: a variável resposta é volume comercial de madeira (dap ≥ 5 cm, sem casca) [p. 3]; o artigo não trata de biomassa, carbono, equações alométricas ou teor de carbono, não havendo valores transferíveis sem nova modelagem.
- Não serve como referência geográfica nem de multissensorialidade: área no Vale do Rio Doce (MG) [p. 3] e apenas Landsat 8 óptico [p. 3–4]; radar e LiDAR aparecem somente como pesquisa futura [p. 9].

## 8. Frases citáveis (literais)

- "Its primary predictors, basal area and site index, are outcomes of the growth process rather than its causes." [p. 2]
- "No single VI, TI, or combination of VI/TI consistently improved model estimates." [p. 7]
