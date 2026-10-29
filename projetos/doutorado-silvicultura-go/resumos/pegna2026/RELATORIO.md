# RELATÓRIO — Valeria La Pegna (2026)

## 1. Referência

La Pegna, V.; Seo, S.; De Santis, D.; Del Frate, F.; Loyola, D. (2026). *Comparative analysis on spectral characteristics of PRISMA and EnMAP hyperspectral missions*. Frontiers in Remote Sensing, 7:1856867. DOI: 10.3389/frsen.2026.1856867. Publicado em 24/07/2026.

O `TEXTO.txt` contém o artigo integral (17 páginas, incluindo referências); o DOI no cabeçalho confere com o solicitado.

## 2. Pergunta do estudo

Até que ponto as medidas hiperespectrais de PRISMA e EnMAP são intercambiáveis no VNIR e em que faixas espectrais essa intercambialidade é confiável?

## 3. Área e dados

- Região Euro-Mediterrânea, com pares co-localizados em Rieti (IT), Valencia (ES), Opava (CZ), Aix-en-Provence (FR), Almeria (ES), Madrid (ES), Toulouse (FR), Sevilla (ES), Ceuta (ES), Toledo (ES) e Zealand (DK) [p. 4].
- Período: pares de 22/01/2024 a 20/08/2025 segundo a Tabela 2 [p. 4]; o texto afirma que a coleta "begins from January 2023" [p. 4], o que não coincide com a primeira data tabulada.
- Sensores: PRISMA (ASI, lançado em 22/03/2019) e EnMAP (DLR, lançado em 01/04/2022) [p. 3].
- Produtos Level-1 (radiance no topo da atmosfera, TOA), sem correção atmosférica [p. 4]; faixa analisada de 400 a 1.000 nm (VNIR) [p. 6].
- Amostras: 11 pares de imagens co-localizadas [p. 1]; 25 pixels contíguos por classe, em quatro classes (solo exposto, área urbana, vegetação e água) [p. 7]; cobertura das quatro classes em 8 cenas [p. 7].

## 4. Método

- Seleção por coincidência geográfica e temporal, com intervalo entre aquisições inferior a 1 h e descarte de cenas com nuvem, névoa, poeira, fumaça ou sombra [p. 4].
- Uso de Level-1 TOA para evitar divergências entre os esquemas de correção atmosférica das agências; superfícies tratadas como lambertianas ideais [p. 4–5].
- Correção geométrica pelo *air mass factor* (AMFG) aplicada apenas ao cubo PRISMA, reescalado para a geometria do EnMAP (Eq. 5) [p. 6–7]; reflectância obtida com *Instrumental Spectral Response Function* gaussiana e espectros de irradiância solares específicos de cada missão (SOLSPEC para PRISMA; Fontenla 2011/MODTRAN 6.0 para EnMAP) [p. 6].
- Comparação estatística por *Standard Deviation* (STD) difference e *Spectral Angle Mapper* (SAM), com interpolação linear do EnMAP para a grade de bandas do PRISMA, no VNIR completo e nas janelas de CHL (400–480 e 600–700 nm), NO2 (420–500 nm) e NDVI (750–940 nm) [p. 4, p. 8].

## 5. Resultados principais

- SAM no VNIR completo entre 0.0463 rad (Toledo) e 0.0774 rad (Valencia), sempre abaixo de 0.1 rad [p. 12].
- Correlação global entre reflectâncias médias dos dois sensores com R² = 0.981 [p. 9]; exceções Madrid e Sevilla, com RMSE de 0.238 e 0.263 para solo exposto [p. 9].
- Não há tendência sazonal ou geográfica clara; os menores SAM, cerca de 0.04 rad, ocorrem em áreas de latitudes e datas distintas [p. 12].
- Janela NDVI (750–940 nm): a menos consistente, com STD de 0.067 e SAM de 0.097 [p. 1], diferenças de STD de até 0.334 [p. 10] e SAM máximo de 0.0969 em Rieti [p. 13].
- Janela NO2 (420–500 nm): SAM de 0.048 e STD de 0.045 [p. 1]; SAM por cena entre 0.0354 (Sevilla) e 0.0478 (Almeria) [p. 13].
- Bandas de absorção de clorofila: STD de aproximadamente 0.051 [p. 13].
- Água: menor diferença de STD entre os sensores em todas as quatro subfaixas [p. 10].
- Configuração espectral: 63 bandas VNIR no PRISMA contra 91 no EnMAP; primeira banda em 402 nm contra 418 nm; última antes do SWIR em 972 nm contra 993 nm; 171 bandas SWIR contra 133 [p. 3].

## 6. Limitações que os próprios autores reconhecem

- Ausência de correção atmosférica: só o AMFG geométrico foi aplicado, sem Rayleigh/Mie nem modelo de transferência radiativa; a hipótese de superfície lambertiana é simplificadora [p. 5–6].
- Consistência em TOA não implica desempenho equivalente em produtos de superfície ou em estimativas de clorofila em água, pois a radiance de saída da água é fração pequena do sinal [p. 5].
- Correção geométrica aplicada apenas ao PRISMA, mantendo-se o EnMAP na forma original [p. 6–7].
- Análise restrita ao VNIR (400–1.000 nm); o SWIR (1.000–2.500 nm), com feições de CO2 e CH4, fica para trabalho futuro [p. 14].
- Recomendam um algoritmo de correção atmosférica comum e padronizado para reduzir espalhamento e absorção, e ampliação multi-temporal [p. 13–14].
- Sem reamostragem espectral; as diferenças de resolução e de número de bandas afetam a comparabilidade em janelas estreitas [p. 3, p. 10].
- Nem todas as cenas contêm as quatro classes de cobertura [p. 7].

## 7. O que serve ao projeto e o que não serve

- Serve: fornece base quantitativa de interoperabilidade PRISMA–EnMAP no VNIR (GSD de 30 m em ambos, FWHM VNIR de 9–13 nm e 8,1 ± 1,0 nm) para justificar uso combinado dos dois sensores [p. 3].
- Serve: o protocolo SAM + diferença de STD, com interpolação de bandas e pareamento em menos de 1 h, é reaproveitável na harmonização de cenas multissensor [p. 4, p. 12].
- Serve: alerta operacional de que 750–940 nm é a faixa menos consistente, justamente a região de red/NIR usada em índices de vegetação, exigindo harmonização no nível do índice e não só da reflectância [p. 13].
- Não serve: não há biomassa, estoque de carbono, silvicultura, trópico ou Goiás; os dados são TOA sem reflectância de superfície e sem SWIR, que são insumos usuais em modelos de biomassa — esses elementos não são tratados no artigo.

## 8. Frases citáveis (literais)

- "Overall, the quantitative and qualitative assessments confirm a strong correspondence between the PRISMA and EnMAP hyperspectral measurements across the VNIR spectrum, with SAM always below 0.1 rad." [p. 1]
- "The closer look at wavelengths sensitive to vegetative environments within the VNIR domain (750–940 nm) shows largest discrepancies also in terms of standard deviation." [p. 13]
