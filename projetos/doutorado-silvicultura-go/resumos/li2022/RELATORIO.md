# RELATÓRIO — Dengqiu Li (2022)

## 1. Referência

Dengqiu Li, Dengsheng Lu, Yunzhong Wu & Kunfa Luo (2022). "Retrieval of eucalyptus planting history and stand age using random localization segmentation and continuous land-cover classification based on Landsat time-series data". *GIScience & Remote Sensing*, 59(1), 1426–1445. DOI: 10.1080/15481603.2022.2118440. O `TEXTO.txt` contém o artigo completo (páginas 1–21, incluindo referências e apêndice) e corresponde ao DOI indicado.

## 2. Pergunta do estudo

O método proposto — random localization segmentation combinada ao teste de Chow sobre séries temporais de NDVI Landsat — detecta com mais robustez os pontos de mudança frequentes e próximos de plantios de eucalipto do que a segmentação global, permitindo reconstruir histórico de corte, geração, ciclo de rotação e idade do povoamento? [p. 4]

## 3. Área e dados

- Local: condado de Yunxiao, sudeste da província de Fujian, China; 583 km² de área florestal (40,1% do condado), clima de monção marítima subtropical [p. 4].
- Período: agosto de 1986 a janeiro de 2021 [p. 5].
- Sensores: NDVI Landsat (TM, ETM+ SLC-off, ETM+ SLC-on e OLI), 593 imagens com cobertura de nuvem inferior a 80% (TM 259, ETM+ SLC-off 203, ETM+ SLC-on 32, OLI 99); média de 17 imagens por ano [p. 5].
- Amostras: 4.172 amostras de cobertura da terra (eucalipto 851, floresta não-eucalipto 601, agricultura 633, pomar 670, não-vegetação 1288, logging slash 129), 70% para treino e 30% para teste; 154 amostras de eucalipto com informações de manejo; 77 amostras para validar a detecção de mudanças [p. 5, p. 9].

## 4. Método

- Segmentação aleatória da série de NDVI em M subsequências com início e fim sorteados (distribuição uniforme); cálculo do CUSUM em cada subsequência, escolha do maior CUSUM como candidato a breakpoint e uso do sSIC (α = 1,01) para número e posição dos pontos [p. 6–7].
- Remoção de falsos pontos por teste de Chow entre modelos harmônicos (j = 2) ajustados antes e depois de cada breakpoint, com nível de significância de 0,05 [p. 7–8].
- Classificação contínua de cada segmento temporal por Random Forest, usando termos harmônicos, NDVI médio, tendência, duração e magnitude do segmento, elevação, declividade e aspecto (mtry padrão, ntree = 500) [p. 8].
- Regras de atribuição dos pontos de corte e de estabilidade para derivar época de corte, geração, ciclo de rotação e idade em meses em 2021 [p. 8].

## 5. Resultados principais

- Detecção de mudanças: random localization obteve PA/UA/OA de 89,8%/89,0%/84,9% para cortes e 89,3%/87,0%/84,7% para estabilidade; a segmentação global obteve 35,2%/59,4%/36,8% e 30,7%/60,5%/43,2% [p. 13].
- Número médio de breakpoints na área de eucalipto: 3,5 (random localization) contra 2,0 (global); 26,6% dos pixels com mais de 4 breakpoints no primeiro método contra 0,1% no segundo; a segmentação global não detectou nenhum breakpoint antes de 1994 ou depois de 2018 [p. 11].
- Classificação contínua da cobertura: OA de 89,2%, com PA de 88,2% e UA de 89,6% para eucalipto [p. 11].
- Gerações sucessivas em 2021: OA de 80,5%; primeira e segunda geração somam 226,3 km² e 91,5 km², ou 69,0% e 27,9% da área de eucalipto [p. 12–13].
- Idade: R² de 0,91 e RMSE de 13,3 meses; excluindo cinco amostras com erro de geração, R² de 0,98 e RMSE de 6,06 meses [p. 13].
- Rotação de 5–8 anos em 66,9% da área; povoamentos com mais de 10 anos somam apenas 2,2%; idade média de 6,6 anos (primeira geração) e 3,3 anos (segunda geração) [p. 13].
- Distribuição de idade em 2021: 1 ano = 14,5% (maior classe) e 7 anos = 12,9% [p. 15].

## 6. Limitações que os próprios autores reconhecem

- Generalidade não testada em ecossistemas com mudanças pouco frequentes; em florestas estáveis o método, mais sensível, pode gerar falsos pontos de mudança [p. 18].
- O modelo harmônico pode overfittar o processo de mudança e não capturar a recuperação rápida no início da sucessão; um modelo harmônico fixo não representa usos e coberturas distintos ao longo do tempo [p. 18].
- Dados com espaçamento irregular e pontos de mudança afastados do meio da subsequência não recebem pesos, o que ainda precisa ser incorporado [p. 18].
- Incertezas na idade: em alguns pixels existe apenas o ponto de estabilidade, sem o de corte, porque o eucalipto cresce muito rápido no primeiro ano e há lacunas por nuvens [p. 18].
- O método de comparação (segmentação global) depende do parâmetro fixo h (0,15), que subestima o número de breakpoints, e um h fixo é considerado inadequado pelos autores [p. 15–16].

## 7. O que serve ao projeto e o que não serve

- Serve: a estrutura de detecção de mudanças em série temporal Landsat entrega, por pixel, data de plantio/corte, geração, ciclo de rotação e idade — variáveis explicativas centrais para biomassa e estoque de carbono de silvicultura de eucalipto [p. 8, p. 19].
- Serve: o desenho de validação (amostras de campo, interpretação em Google Earth e TimeSync, PA/UA/OA, R² e RMSE) é replicável para o mapeamento em Goiás [p. 5, p. 8–9].
- Não serve: o artigo não estima biomassa nem carbono — não há modelo alométrico, dados de inventário de biomassa ou estoque de carbono [p. 19].
- Não serve: área, clima e espécie são de Fujian (China), sem Cerrado ou Goiás; o sensor é apenas Landsat/NDVI, e a integração multissensorial (Sentinel-1/2, fusão MODIS-Landsat) é apenas indicada como pesquisa futura [p. 18].

## 8. Frases citáveis (literais)

- "The overall accuracy of identification was 80.5%, and successive generations in 2021 were mainly first- and second-generation, accounting for 69.0% and 27.9% of the total eucalyptus area, respectively." [p. 2]
- "However, some uncertainties in the detection of stand ages still exist because there was no cutting time, only stable time, in some pixels (stands)." [p. 18]
