# RELATÓRIO — Rodolfo Ceriani (2025)

## 1. Referência

Ceriani, R.; Brocco, S.; Pepe, M.; Oggioni, S.; Vacchiano, G.; Motta, R.; Berretti, R.; Ascoli, D.; Garbarino, M.; Morresi, D.; Bassi, F.; Fava, F. (2025). *Hyperspectral and LiDAR space-borne data for assessing mountain forest volume and biomass*. International Journal of Applied Earth Observation and Geoinformation, 141, 104614. DOI: 10.1016/j.jag.2025.104614. Texto integral lido (11 páginas, com referências); confere com o DOI informado.

## 2. Pergunta do estudo

Dados hiperspectrais orbitais (EMIT) superam o multiespectral Sentinel-2 — e o ganho se mantém quando se acrescenta a altura de dossel do LiDAR orbital GEDI — na estimativa de volume de madeira (SV) e biomassa acima do solo (AGB) de florestas montanas mistas?

## 3. Área e dados

- Duas áreas na Itália: "Alpine" (Valcamonica, Brescia, e Alta Valtellina, Sondrio; altitude média 1926 m, 190–3824 m; floresta em 906 km², 41,8% do território) e "Apennine" (Berceto, Parma; altitude média 746 m, 228–1349 m; floresta em 99 km², 75,4%) [p. 3].
- Campo: 82 parcelas na área alpina em 2020 + 19 em 2023; 56 parcelas nos Apeninos em 2024; 157 no total, das quais 130 retidas após controle de qualidade (NDVI ≥ 0,3) [p. 3]. Parcelas circulares de raio 14 m (~615 m²) [p. 3].
- Sensores: Sentinel-2B (13 bandas; 10, 20 e 50 m), imagens de 05/04/2024 (Alpine) e 12/04/2024 (Apennine) [p. 3]; EMIT (285 bandas, 380–2500 nm, resolução espectral ≤10 nm, FWHM ≤13 nm, 60 m), cenas de 13/04/2024 (Alpine) e 12/04/2024 (Apennine) [p. 3–4]; produto global de altura de dossel (CH) derivado de GEDI (30 m, reamostrado para 60 m), baseado em dados GEDI de abril a outubro de 2019 [p. 4].
- Modelagem: 286 variáveis de entrada (285 bandas EMIT + 1 métrica GEDI) contra 130 observações de campo [p. 4].

## 4. Método

- Amostragem estratificada aleatória por espécie, com cobertura de declive (DEM) e densidade; DAP de todas as árvores e altura de 15 árvores por parcela; relações altura–diâmetro específicas por espécie; SV e AGB por equações alométricas do Inventário Florestal Nacional italiano, convertidos para m³ ha⁻¹ e Mg ha⁻¹ [p. 3].
- Quatro combinações de entrada (S2; S2+GEDI CH; EMIT; EMIT+GEDI CH) × cinco algoritmos (PLSR, BTR, SVM, ANN, GPR) em MATLAB R2024a, com PCA prévio (20 componentes; 10 para PLSR) [p. 4].
- Otimização bayesiana de hiperparâmetros e validação cruzada de 5 folds; métricas R²cv e RMSEcv [p. 4].
- Aplicação espacial do melhor modelo por combinação, restrita a máscara de floresta, com checagem de artefatos, faixas ecologicamente plausíveis e coerência com histórico de cortes (2011–2025) e mapas de espécies [p. 4].

## 5. Resultados principais

- SV de campo: 64,96 a 1298,68 m³ ha⁻¹, média 298,74 m³ ha⁻¹, distribuição assimétrica à direita (Shapiro-Wilk p = 0,041); média alpina 328 vs. 287 m³ ha⁻¹ nos Apeninos, mas o máximo (1298 m³ ha⁻¹) é apenino [p. 5].
- AGB de campo: 31,51 a 682,48 Mg ha⁻¹, média 160,83 Mg ha⁻¹ (p = 0,048); nos Apeninos média 208 vs. 142 Mg ha⁻¹, máximo 682 vs. 312 Mg ha⁻¹ e IQR 115 vs. 80 Mg ha⁻¹ [p. 5].
- SV só com S2: BTR R² = 0,30, RMSE = 98,08 m³ ha⁻¹; só com EMIT: ANN R² = 0,47, RMSE = 93,34 m³ ha⁻¹ [p. 5].
- SV com S2+GEDI: ANN R² = 0,69, RMSE = 79,56 m³ ha⁻¹; com EMIT+GEDI: GPR R² = 0,75, RMSE = 75,48 m³ ha⁻¹ (melhor resultado do estudo) [p. 5].
- AGB só com S2: BTR R² = 0,18, RMSE = 69,16 Mg ha⁻¹; só com EMIT: PLSR R² = 0,17, RMSE = 60,40 Mg ha⁻¹ [p. 5].
- AGB com GEDI: S2+GEDI/GPR R² = 0,67, RMSE = 44,24 Mg ha⁻¹; EMIT+GEDI/BTR R² = 0,45, RMSE = 47,92 Mg ha⁻¹ — o multiespectral superou o hiperespectral [p. 5].
- Reamostrar o S2 para 60 m derrubou a AGB para R² = 0,55 e RMSE = 51,83 Mg ha⁻¹, valor próximo ao do EMIT+GEDI [p. 7].
- 11 pixels EMIT (60 m) continham mudança de espécie dominante dentro do pixel e todos tiveram erro alto de AGB (MAE > 70 Mg ha⁻¹); as 4 parcelas de maior erro correspondiam a esses pixels [p. 7].
- Mapas de SV: área alpina 14,44–594,87 m³ ha⁻¹ (média 295,54; DP 122,54), sem artefatos [p. 5]; Apeninos 0,02–708,37 m³ ha⁻¹ (média 326,82; DP 152,97), com 34 pixels abaixo de 5 m³ ha⁻¹ em áreas de solo/rocha/construção [p. 5].
- Nota: o resumo cita S2-GEDI como ANN com RMSE = 84,48 m³ ha⁻¹ [p. 1], mas a Tabela 1 traz ANN com 79,56 e BTR com 84,48 m³ ha⁻¹ [p. 5] — inconsistência interna do artigo.

## 6. Limitações que os próprios autores reconhecem

- A AGB recuperada é inferior à de estudos com dados hiperspectrais aerotransportados, que reportam R² de 0,60 a 0,91 e RMSE de 41,03 a 64,9 Mg ha⁻¹ [p. 6].
- O pixel de 60 m do EMIT mistura espécies e limita a AGB, que é sensível à densidade da madeira (0,37–0,70 Mg m⁻³); os trade-offs entre resolução espacial e espectral precisam de mais investigação (EnMAP, PRISMA, 30 m) [p. 7].
- A PCA aplicada a priori impede avaliar a importância das variáveis pelos pesos do modelo, aceito como trade-off para ganhar robustez [p. 4].
- Razão variável/amostra de 286 para 130 exige ampliar o conjunto de campo para confirmar os achados [p. 4, p. 8].
- Erros do CH do GEDI tendem a crescer para dosséis acima de 20 m [p. 4].
- O tempo de revisita não regular das missões hiperspectrais operacionais (EMIT, EnMAP, PRISMA) limita o monitoramento de mudanças; CHIME é apontada como alternativa futura [p. 8].
- Os estoques de carbono subterrâneos não são avaliados e seguem como desafio crítico [p. 8].
- O intervalo entre campo (2020/2023) e imagem (2024) foi corrigido apenas por taxas médias de incremento do inventário nacional (0,6 e 2,4 m³ ha⁻¹), consideradas de efeito mínimo [p. 3].
- A transferibilidade do arcabouço para outros contextos geográficos ainda não foi testada [p. 8]; os autores também declaram não ter permissão para compartilhar os dados [p. 9].

## 7. O que serve ao projeto e o que não serve

- Serve: o desenho de comparação controlada (óptico × óptico+LiDAR, quatro combinações × cinco algoritmos, validação cruzada de 5 folds, R² e RMSE) é diretamente replicável para silvicultura em Goiás.
- Serve: a evidência de que a altura de dossel LiDAR é o insumo decisivo (ganho de R² de 0,47 para 0,75 em SV) e de que GPR foi o algoritmo mais consistente [p. 5, p. 8]; e a constatação de que SV é mais robusto que AGB em florestas heterogêneas [p. 7].
- Serve: a etapa de espacialização como controle de qualidade (artefatos, faixas plausíveis, coerência com cortes e tipos florestais), útil para validar mapas de biomassa antes de usar em carbono [p. 4, p. 8].
- Não serve: o contexto é floresta natural montana mista na Itália, com alometria do inventário italiano e densidade de madeira espécie-específica [p. 3, p. 7]; não há plantio, eucalipto/pinus, estoque de carbono (fração de carbono, raízes) nem Cerrado ou Goiás. Também não serve como referência de acurácia para AGB: o melhor R² foi 0,67 e o hiperespectral orbital perdeu para o multiespectral de 10 m [p. 5], e o CH do GEDI é de 2019, com pixel de 60 m incompatível com talhões estreitos [p. 4].

## 8. Frases citáveis (literais)

- "This study shows that, regardless of what data modelling approach is considered, the integration of CH data from GEDI is essential to improve SV and AGB retrieval performance" [p. 7].
- "However, trade-offs between sensor spatial and spectral resolutions were observed for AGB retrieval, with S2 outperforming EMIT when combined with GEDI data." [p. 8].
