# RELATÓRIO — Sam Cooper (2021)

## 1. Referência

Cooper, S., Okujeni, A., Pflugmacher, D., van der Linden, S., Hostert, P. (2021). Combining simulated hyperspectral EnMAP and Landsat time series for forest aboveground biomass mapping. *International Journal of Applied Earth Observations and Geoinformation*, 98, 102307. DOI: 10.1016/j.jag.2021.102307 [p. 1].

O `TEXTO.txt` contém o artigo integral (12 páginas, incluindo referências) e corresponde ao DOI informado.

## 2. Pergunta do estudo

Se a informação espectral densa de imagens hiperespectrais EnMAP simuladas melhora o mapeamento de biomassa acima do solo (AGB) de florestas em relação a dados multiespectrais Landsat, e se a combinação de ambas as fontes supera cada uma isoladamente [p. 1–2].

## 3. Área e dados

- **Local:** Sonoma County, norte da Califórnia (EUA), na borda norte da Baía de San Francisco; ~4.100 km², dos quais 1.680 km² (41%) florestados; elevação do nível do mar até 1.300 m [p. 2].
- **Período:** 2013. Aquisições AVIRIS em 10 de abril e 7 de junho de 2013; série Landsat de abril de 2013 a março de 2014 [p. 3].
- **Sensores/fontes:**
  - EnMAP simulado a partir de AVIRIS (simulador EeteS), 195 bandas, 30 m, faixa de 420–2450 nm [p. 3].
  - Landsat 7 ETM+ e Landsat 8 OLI, Collection 1 Level 1 Tier 1, 52 cenas em três órbitas/pontos, processadas no FORCE v2.0 (6 bandas, reflectância Level-2) [p. 3].
  - Mapa de AGB de referência por lidar aerotransportado (campanha CMS/NASA, 2013), 30 m, ~14 pontos/m² em 44 linhas de voo [p. 3].
  - MDE de 30 m (National Elevation Dataset) e mapa de alianças florestais do Sonoma County Vegetation Mapping & Lidar Program [p. 4].
- **Amostras:** 1.100 pixels de treino e 4.400 pixels de validação [p. 4–5]; a seção 3.3 menciona 4.000 pixels de validação [p. 5]. Após mascaramento, 2.053.387 pixels florestais [p. 3].
- **AGB de referência:** média de 200 Mg/ha nos pixels florestais, com 99,9% dos valores abaixo de 750 Mg/ha [p. 3]; nos dados de treino, 0–1162 Mg/ha (média 342 Mg/ha) e, na validação, 0–1170 Mg/ha (média 329 Mg/ha) [p. 5].

## 4. Método

- Simulação das cenas AVIRIS para EnMAP (EeteS), correção de brilho entre faixas, co-registro com Landsat (AROSICS), máscaras de água e nuvem; 42 bandas de absorção atmosférica e 5 bandas de NIR com recuperação ruim foram removidas [p. 3].
- Geração de composições Landsat BAP (Best Available Pixel) para abril e junho, com imagens de ±15 dias das aquisições AVIRIS, e de uma série temporal interpolada de 16 dias para 2013 (filtros de convolução gaussiana com kernel RBF) [p. 3–4].
- Regressão por Processos Gaussianos (Gaussian Process Regression, GPR), com kernel RBF combinado a um kernel de ruído branco, usando todas as bandas; Python 3.7.0, EnMAP-Box 3.5 e scikit-learn 0.20.0 [p. 4].
- Amostragem aleatória estratificada do mapa de AGB lidar (dez estratos de 50 Mg/ha entre 0 e 500 Mg/ha e um estrato >500 Mg/ha), com buffer de 500 m para reduzir autocorrelação espacial; incerteza do mapa lidar incorporada por amostragem de uma normal (média e desvio-padrão por pixel) [p. 4]. Avaliação por RMSE, MAE, RMSE relativo (rRMSE), razão de variância, R² e análise de resíduos contra estrutura florestal, topografia e tipo florestal [p. 5].

## 5. Resultados principais

- Modelos apenas com EnMAP: RMSE de 109,7 Mg/ha (abril), 108,2 Mg/ha (junho) e 97,5 Mg/ha (duas datas, o melhor modelo EnMAP-only; R² = 0,83) [p. 5].
- Modelos apenas com Landsat BAP: RMSE de 123,7 Mg/ha (abril), 112,0 Mg/ha (junho) e 108,8 Mg/ha (duas datas) — todos piores que os modelos EnMAP correspondentes [p. 5].
- Série temporal Landsat de 2013: RMSE de 102,3 Mg/ha, melhor que os BAP e que os modelos EnMAP de data única, mas pior que o EnMAP de duas datas [p. 5].
- Modelo combinado (EnMAP duas datas + série temporal Landsat 2013): RMSE de 86,0 Mg/ha, MAE de 64,2 Mg/ha, rRMSE de 0,27, R² = 0,87 e razão de variância de 1,15 — o melhor resultado geral [p. 5].
- Ganho do modelo combinado: redução de 11,8% no RMSE em relação ao EnMAP de duas datas e de 15,9% em relação à série temporal Landsat [p. 5].
- Saturação observada em aproximadamente 800 Mg/ha, algo reduzida no modelo combinado [p. 5].
- Espacialmente, 95% das diferenças entre o mapa combinado e o mapa lidar ficaram entre 160 Mg/ha de subestimação e 131 Mg/ha de superestimação [p. 5].
- Resíduos do modelo combinado: superestimação em florestas com altura média abaixo de 20 m e subestimação acima de 50 m; cobertura moderada (50–80%) modelada com maior acurácia [p. 6].
- Sem relação clara dos resíduos com elevação até ~700 m; acima disso, superestimação crescente, chegando a ~175 Mg/ha em média [p. 6].
- Por tipo florestal: superestimação mais marcada em pínus, sequoia e madrone; resíduos médios próximos de zero em carvalho, loureiro-da-Califórnia, ripário e florestas não nativas [p. 6].
- Erro do mapa lidar de referência: subestimação em áreas de alta biomassa, atribuída à sub-representação dessas áreas nos dados de campo [p. 3].

## 6. Limitações que os próprios autores reconhecem

- As imagens EnMAP são **simuladas** a partir de AVIRIS; o valor real de aquisições hiperespectrais só poderá ser verificado com séries temporais densas de sensores hiperespectrais orbitais [p. 7].
- Aquisições hiperespectrais são limitadas a campanhas únicas ou intermitentes, o que impede derivar informação fenológica de longo prazo apenas do hiperespectral [p. 7].
- Correção topográfica aplicada às imagens Landsat, mas não às imagens EnMAP, o que pode introduzir confusão no modelo combinado em áreas de variação de declividade e orientação [p. 9].
- Ausência de dados de campo: a incerteza do mapa lidar foi incorporada apenas via desvios-padrão por pixel, e uma análise de incerteza mais rigorosa "não foi viável" [p. 10].
- O mapa lidar de referência subestima AGB em áreas de alta biomassa quando comparado a dados de campo independentes [p. 10].
- Sentinel-2 não foi avaliado, pois a aquisição óptica é anterior ao seu lançamento [p. 9].
- Cobertura hiperespectral incompleta em abril de 2013: ~130 km² (costa noroeste e duas seções da borda nordeste) excluídos; a aquisição de novembro foi descartada por cobertura de nuvens [p. 3].
- Covariáveis auxiliares (topografia, clima, cobertura da terra, métricas lidar) não foram incluídas como preditoras porque algumas já foram usadas na construção do mapa lidar de referência [p. 10].

## 7. O que serve ao projeto e o que não serve

- **Serve:** a lógica de combinar informação espectral densa com informação temporal densa (aqui EnMAP + série Landsat) como estratégia para AGB — ganho de RMSE de 86,0 contra 97,5 e 102,3 Mg/ha [p. 5]; transponível para a silvicultura goiana, onde há séries Landsat/Sentinel-2 disponíveis.
- **Serve:** o desenho metodológico — amostragem estratificada por classes de AGB, buffer de 500 m, propagação da incerteza da referência, GPR com todas as bandas e análise de resíduos por tipo florestal, estrutura e topografia [p. 4–6].
- **Serve:** o alerta de saturação em alto valor de biomassa (~800 Mg/ha) e a superestimação em dosséis abertos e em maiores elevações [p. 5–6] — pontos a testar em povoamentos plantados.
- **Não serve:** o ambiente é floresta temperada/mediterrânea nativa da Califórnia (sequoia, abeto Douglas, carvalho), não silvicultura tropical plantada em Goiás; os dados hiperespectrais são **simulados** de AVIRIS de 2013, não de sensor orbital real, e o estudo não usa Sentinel-2, não usa dados de campo e não trata de estoque de carbono [p. 1–3, p. 9].

## 8. Frases citáveis (literais)

- "Combining the two datasets further improved AGB mapping efforts, with 2-date EnMAP + 2013 Landsat TS providing the best overall AGB maps (RMSE = 86.0 Mg/ha)." [p. 1]
- "This study demonstrates that such a combination of spectral and temporal information can improve the assessment of forest AGB beyond what either is capable of modeling separately." [p. 9]
