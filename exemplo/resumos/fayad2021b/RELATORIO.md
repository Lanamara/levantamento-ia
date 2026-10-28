# RELATÓRIO — Ibrahim Fayad (2021)

## 1. Referência

Ibrahim Fayad, Nicolas N. Baghdadi, Clayton Alcarde Alvares, Jose Luiz Stape, Jean Stéphane Bailly, Henrique Ferraço Scolforo, Mehrez Zribi e Guerric Le Maire (2021). "Assessment of GEDI's LiDAR Data for the Estimation of Canopy Heights and Wood Volume of Eucalyptus Plantations in Brazil". *IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing*, vol. 14, p. 7095–7110. DOI 10.1109/JSTARS.2021.3092836.

`TEXTO.txt` está completo (16 páginas, do resumo às referências e biografias) e corresponde ao DOI informado.

## 2. Pergunta do estudo

Com que precisão os dados LiDAR do GEDI, combinados em diferentes modelos de regressão, estimam a altura dominante (Hdom) e o volume de madeira (V) de plantações de eucalipto em escala de talhão, e quanto dessa precisão depende da escolha do algoritmo de processamento da forma de onda [p. 2].

## 3. Área e dados

- Local: quatro regiões do Brasil — Bahia/Espírito Santo, Mato Grosso do Sul, São Paulo e Maranhão; não inclui Goiás [p. 2].
- Período: pegadas GEDI adquiridas entre 20/04/2019 e 04/09/2019; inventários de campo com diferença máxima de dois meses em relação à passagem do satélite [p. 6].
- Sensores e fontes: GEDI (LiDAR espacial, 1064 nm, pegada de 25 m de diâmetro, 242 Hz, 8 feixes, grade de 60 m ao longo da órbita), produtos L1B e L2A do LP DAAC/NASA, e DEM SRTM de 30 m para declividade, Terrain Index e rugosidade [p. 3, p. 6–7].
- Amostras: 6.166 pegadas adquiridas, das quais 92,15% aproveitáveis [p. 6]; 566 talhões de eucalipto selecionados, com parcelas permanentes de ~400 m² (30 a 100 árvores, média de 58) na densidade de uma parcela por 10 ha [p. 6–7]; 5.517 disparos GEDI efetivamente analisados [p. 14].

## 4. Método

- Extração de métricas da forma de onda (RH10 a RH100, `toploc`, `botloc`, `Wext`, `Leadext`, `Trailext`) nas seis configurações de algoritmo do L2A (a1 a a6), mais dois critérios de posição do retorno do solo: o modo `SM` do L2A (último modo não ruidoso) e o modo de maior amplitude entre os dois últimos [p. 4–5].
- Estimativa de Hdom por sete modelos lineares da literatura ICESat/GLAS (equações 3 a 8) e por dois modelos que selecionam variáveis automaticamente — regressão stepwise (SRH) e random forest (RFH, 100 árvores) [p. 7–8].
- Estimativa de V por quatro vias: duas funções potência calibradas com Hdom de campo (equações 9 e 10) e os modelos stepwise (SRV) e random forest (RFV) aplicados diretamente às métricas GEDI [p. 8].
- Validação por validação cruzada de cinco dobras, com as dobras separadas por talhão para evitar que pegadas do mesmo talhão caíssem em treino e validação ao mesmo tempo; métricas de desempenho R², bias, RMSE, RMSPE e AIC [p. 8].

## 5. Resultados principais

- Modelos lineares (equações 3 a 8) para Hdom: RMSE entre 1,70 e 2,31 m e R² entre 0,80 e 0,89; o melhor foi a equação 8, com RMSE de 1,70 m e R² de 0,89 [p. 9].
- SRH foi o modelo mais preciso para Hdom: RMSE de 1,44 m e R² de 0,93 [p. 9]; com as estimativas médias por talhão, RMSE de 1,33 m e R² de 0,93 [p. 12].
- RH90 sozinho estimou Hdom com RMSE de 1,63 m e R² de 0,90; acrescentar RH10 elevado a 1,8 levou a RMSE de 1,5 m e R² de 0,91 [p. 9].
- RH90 foi a variável mais importante, explicando mais de 87% da variabilidade de Hdom e mais de 84% da de V [p. 12]; no SRH vieram depois RH10, RH80 e RH100, e no SRV, RH10, RH30, RH80 e RH20 [p. 13].
- Volume: os quatro modelos ficaram entre RMSE de 24,39 e 27,45 m³.ha⁻¹ e R² entre 0,87 e 0,90 [p. 11]; o melhor foi o SRV, com RMSE de 24,39 m³.ha⁻¹ e R² de 0,90 [p. 12].
- RMSPE de 7,1% para Hdom e 20,4% para V [p. 12].
- Subestimativa de V acima de 250 m³.ha⁻¹: o RMSE relativo sobe de ~18% (V < 250) para ~40% (V > 250) e o bias médio passa de 2,2 para 26,5 m³.ha⁻¹ [p. 12].
- Algoritmos: com métricas de a2 a a6, os modelos lineares pioraram, com RMSE de 2,40 m (R² de 0,78, a3) a 5,06 m (R² de 0,02, a5) [p. 10]; usando só `Wext`, a5 deu RMSE de 4,38 m e R² de 0,26 [p. 11]; no SRH e no RFH, a5 ficou em 1,6 m (R² de 0,90) e 1,80 m (R² de 0,88) [p. 11]. O aumento de RMSE com a5 frente a a1 foi de ~16% para Hdom e V [p. 14].
- Retorno do solo: escolher o modo mais forte entre os dois últimos melhorou Hdom em 12 a 20 cm, sem efeito sobre V [p. 11, p. 14].
- Idade do talhão como preditor extra: RMSE de Hdom caiu de 1,33 para 1,18 m (~13%) e o de V de 24,39 para 22,77 m³.ha⁻¹ (~7%) [p. 13].
- Feixes: melhores resultados nos feixes 8, 3 e 4 e pior no feixe 5, com diferença de 46 cm em Hdom e 9 m³.ha⁻¹ em V [p. 14].
- `quality_flag` 0 ou 1 não alterou a acurácia após a filtragem aplicada [p. 14].

## 6. Limitações que os próprios autores reconhecem

- Os resultados valem para terrenos planos a levemente inclinados (declividade média de 4,7 ± 3%) e para plantações de eucalipto, não podendo ser generalizados para florestas naturais [p. 10, p. 13].
- A defasagem de até dois meses entre inventário e aquisição pode gerar até 50 cm de diferença em Hdom e 10 m³.ha⁻¹ em V [p. 7, p. 13].
- Em terreno inclinado o pico do solo alarga e se mistura com a vegetação, dificultando identificar o retorno do solo [p. 7].
- A comparação usa médias por talhão obtidas de 1 a 10 parcelas, e a variabilidade interna chega a mais de 6 m em alguns talhões [p. 14].
- Um único modelo global foi aplicado a todas as regiões; modelos locais de random forest reduziram o RMSE de Hdom em até 16 cm e o erro de V em até 12,8 m³.ha⁻¹ [p. 14].
- Persiste subestimativa de V acima de 250 m³.ha⁻¹, e as relações alométricas variam entre regiões [p. 14].

## 7. O que serve ao projeto e o que não serve

- Serve como referência de precisão alcançável com GEDI em silvicultura homogênea de eucalipto: RMSE de 1,33 m para Hdom e 24,39 m³.ha⁻¹ (R² de 0,93 e 0,90) [p. 12].
- Serve o desenho metodológico: RH90 como métrica central, seleção de variáveis por stepwise e random forest, validação cruzada separada por talhão e checagem do campo `selected_algorithm` (a1 em mais de 99% das pegadas) [p. 8, p. 13].
- Serve o alerta de que a escolha do algoritmo de processamento muda o resultado em ~16% de RMSE e de que a idade do talhão agrega ~13% de ganho em Hdom — ambos controláveis no fluxo de Goiás [p. 13, p. 14].
- Não serve como evidência local nem para carbono: a área não é Goiás (BA/ES, MS, SP, MA) e o artigo estima altura dominante e volume madeireiro, sem biomassa, estoque de carbono ou sensoriamento multissensorial [p. 2, p. 6].

## 8. Frases citáveis (literais)

- "The most important GEDI variable for the estimation of Hdom and V is RH90, which explained respectively more than 87% and 84% of the variability of Hdom and V." [p. 12]
- "Not all the variability on Hdom and V could be explained by GEDI alone." [p. 14]
