# RELATÓRIO — Juan Carlos Fernández-Diaz (2022)

## 1. Referência

Juan Carlos Fernandez-Diaz, Mariya Velikova e Craig L. Glennie (2022). "Validation of ICESat-2 ATL08 Terrain and Canopy Height Retrievals in Tropical Mesoamerican Forests". *IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing*, vol. 15, pp. 2956–2970. DOI: 10.1109/JSTARS.2022.3163208. `TEXTO.txt` está completo (15 páginas, incluindo referências e biografias); corresponde ao DOI indicado.

## 2. Pergunta do estudo

Quão acurados são os produtos ATL08 do ICESat-2 (elevação interpolada do terreno, topo do dossel e altura de dossel) em florestas tropicais densas da Mesoamérica, tomando como referência lidar aerotransportado de alta densidade?

## 3. Área e dados

- **Local:** sete sítios em florestas tropicais — três na península de Yucatán, México (Puuc, Coba, Calakmul), dois na Guatemala (Reserva da Biosfera Maia, Lacandón), um em Belize (Rio Bravo) e um na região de Mosquitia, Honduras (Rio Plátano) [p. 3].
- **Período:** ATLAS de 24/10/2018 a 28/10/2020 (ciclos orbitais 1–9); o período das aquisições HDL não é informado, mas as diferenças temporais entre voo e satélite vão de poucas semanas a 8,3 anos, sendo < 4,5 anos em 97,9% das amostras [p. 3].
- **Sensores/fontes:** ICESat-2/ATLAS, produto ATL08 versão 3; referência de lidar aerotransportado de alta densidade (HDL) com > 15 pulsos/m² e > 20 retornos/m², 97,9% coletado com Teledyne Optech Titan e um sítio com Optech Gemini [p. 3].
- **Amostras:** cerca de 30 000 segmentos ATL08 de 100 m e 3 742 km² de área validada [p. 1]; 29 484 segmentos no conjunto, 7 sítios e 20 trilhas de referência [p. 3]; segmentos válidos por parâmetro: 29 145 (h_te_interp), 28 137 (h_canopy_abs) e 28 230 (h_canopy) [p. 6].

## 4. Método

- Comparação ponto a ponto entre segmentos ATL08 de 100 m e rasters HDL de 20 m derivados de nuvens de pontos classificadas; cinco pontos amostrais por segmento (−40, −20, 0, 20 e 40 m) com interpolação bilinear [p. 5–6].
- Erro por amostra = valor ATL08 − valor HDL de referência; também erro normalizado de altura de dossel em relação à altura de referência (rCH) [p. 6].
- Métricas agregadas (RMSE, MAE, R², mínimo, máximo, mediana, percentis 5 e 95, IQR) para o conjunto total e estratificadas por faixa de rCH de 5 m, sítio, passe/feixe, iluminação (dia/noite) e força do feixe (forte/fraca) [p. 6].
- Protocolo tipo ASPRS: sem remoção de outliers e sem deslocamento horizontal dos dados ATL08; ajuste de geolocalização testado com PhoREAL em ~25% dos segmentos apenas como análise auxiliar [p. 4–5].

## 5. Resultados principais

- Erros de h_te_interp (percentis 5–95) crescem com a rCH: de ±2,5 m para rCH de 5–10 m até −10 a 24 m para rCH de 40–45 m [p. 6].
- A mediana do erro de h_te_interp cresce com a rCH e superestima sistematicamente o terreno de referência; mínimo de −108,381 m e máximo de 108,37 m [p. 6].
- h_canopy_abs: IQR dos erros entre −5,5 e 6,0 m; mediana praticamente constante e subestimada em −0,5 a −2,0 m [p. 7].
- h_canopy: percentis 5–95 entre −25 e 30 m; extremos de −30,15 m e 123,26 m [p. 8].
- Erro normalizado de h_canopy: IQR entre −33,5% e 7,0%, mediana em torno de −16,5% e RMSE% de 67,0% [p. 8].
- RMSE global: 10,58 m (h_te_interp), 17,18 m (h_canopy_abs) e 13,35 m (h_canopy); %MAE de h_canopy = 30,9% [p. 8].
- Distribuição dos segmentos por condição: noite/feixe forte 42,9%, noite/feixe fraco 2,3%, dia/feixe forte 37,6%, dia/feixe fraco 17,2% [p. 9].
- RMSE de h_te_interp por condição: dia forte 6,04 m, dia fraco 5,91 m, noite fraco 6,67 m, noite forte 14,59 m [p. 9].
- RMSE de h_canopy_abs: dia forte 4,87 m, dia fraco 5,72 m, noite fraco 11,2 m, noite forte 25,5 m [p. 9].
- RMSE de h_canopy: dia forte 7,19 m, dia fraco 7,56 m, noite fraco 7,24 m, noite forte 18,6 m [p. 9].
- Viés de h_canopy menor à noite (0,43 m) que de dia (−3,03 m), mas %MAE de 42,4% à noite contra 21,6% de dia [p. 10].
- Ajuste de geolocalização não melhorou o conjunto: ganho mínimo em h_te_interp em alguns perfis, degradação de h_canopy_abs e sem mudança significativa em h_canopy [p. 5].

## 6. Limitações que os próprios autores reconhecem

- Quatro limitações principais: diferença temporal entre ATLAS e HDL; diâmetro de pegada e incerteza de geolocalização do ATLAS; cobertura geográfica limitada frente ao alcance global do ICESat-2; e topo do dossel definido pelo percentil 98 dos eventos de fótons no ATL08 contra o retorno mais alto no HDL [p. 2].
- A acurácia posicional vertical absoluta do HDL sob dossel não foi avaliada em campo em larga escala; é estimada em melhor que 15 cm, com precisão tipicamente melhor que 8 cm RMSE [p. 3–4].
- O sítio de Honduras representa apenas 2,1% das amostras, usou sensor de geração anterior (Gemini) e tem a maior diferença temporal (6,5–8,3 anos) [p. 4].
- As ferramentas de ajuste de geolocalização (PhoREAL) produziram deslocamentos inconsistentes e não confiáveis sob dossel denso [p. 4–5].
- Nenhum outlier foi removido dos dados ATL08, o que eleva as métricas de erro [p. 5].
- Não houve correlação significativa entre as incertezas internas reportadas no ATL08 e os erros validados externamente [p. 10].
- A condição noite/feixe fraco tem apenas cerca de 665 segmentos (2,3%), insuficientes para conclusões gerais [p. 9].
- A separação dia/noite é uma simplificação da iluminação; o efeito de inclinação do terreno e abertura do dossel ficou fora do escopo [p. 7], [p. 10].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o desenho de validação (comparação com lidar de alta densidade, sem remoção de outliers e sem deslocamento horizontal) é replicável para quantificar o erro do ATL08 antes de usá-lo em modelos de biomassa em Goiás.
- **Serve:** a estabilidade do erro normalizado de altura de dossel (mediana −16,5%, IQR −33,5% a 7,0%) fornece um termo de incerteza propagável a modelos de estoque de carbono baseados em altura de dossel [p. 8].
- **Serve:** a recomendação de usar valores agregados, e não segmentos individuais, além de filtros de qualidade (terrain_flg, cloud_flag_atm) e comparação com modelos GEDI/GLAS para sinalizar outliers [p. 10].
- **Não serve:** não há biomassa, estoque de carbono, equações alométricas nem silvicultura; a área é floresta tropical natural madura da Mesoamérica, não plantios de Goiás, e os autores apenas sugerem extrapolação cautelosa para outros trópicos [p. 2].

## 8. Frases citáveis (literais)

- "These derived geophysical or biophysical parameters for individual ATL08 segments have to be utilized with reasonable caution." [p. 10]
- "However, the results are also encouraging in that the top of canopy elevations can be retrieved with a fair degree of accuracy and the median of the relative errors of canopy heights seems to exhibit a uniform behavior that can be used to propagate uncertainty to models and algorithms that leverage canopy data." [p. 10]
