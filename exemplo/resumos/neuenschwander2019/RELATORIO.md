# RELATÓRIO — Amy Neuenschwander (2019)

## 1. Referência
Neuenschwander, Amy L.; Magruder, Lori A. (2019). *Canopy and Terrain Height Retrievals with ICESat-2: A First Look*. Remote Sensing, 11(14), 1721. Recebido em 04/06/2019, aceito em 19/07/2019, publicado em 20/07/2019 [p. 1]. DOI: 10.3390/rs11141721. O `TEXTO.txt` está íntegro (13 páginas, do resumo às referências) e corresponde a esse DOI.

## 2. Pergunta do estudo
Qual é a acurácia das alturas de terreno e de dossel recuperadas pelo produto ATL08 do ICESat-2, medida contra lidar aerotransportado, e o que os primeiros transectos revelam sobre o uso do sensor em diferentes ecossistemas vegetais [p. 1, p. 4].

## 3. Área e dados
- Qualitativo: floresta boreal a nordeste de Edmonton, Alberta, em transecto de 25 km, 21/02/2019, período noturno, feixe forte GT1L [p. 5]; floresta tropical com desmatamento no Brasil, cerca de 50 km, GT2L, 19/03/2019 [p. 6]; savana/woodland de Mopane e Acacia no Botsuana, a leste do Delta do Okavango, cerca de 14 km, GT3L, 03/02/2019 [p. 6]; manguezal no México [p. 7].
- Quantitativo: um transecto sobre a Finlândia, granulo ATL08_20181124001516_08610105, com aquisição ICESat-2 em 24/11/2018 [p. 9].
- Verdade de referência: lidar aerotransportado do National Land Survey of Finland, adquirido em 2014, densidade de aproximadamente 1 pt/m² e precisão vertical de 0,12 m [p. 8]. Dos 200 km de dados ATL08, aproximadamente 110 km tinham lidar aerotransportado correspondente [p. 8].
- Amostras: 1.105 segmentos ATL08 de 100 m para a validação de terreno [p. 8] e 854 estimativas de altura de dossel [p. 9]. Produto na versão preliminar v001 (release 001) [p. 7].

## 4. Método
- ATLAS: laser de 532 nm com contagem de fótons, 10 kHz, 70 cm entre disparos no solo, seis feixes em três pares separados por aproximadamente 3,3 km, razão forte/fraco de 4:1 e pegada nominal de 17 m [p. 2, p. 4].
- ATL08: o algoritmo classifica os fótons do ATL03 em ruído, ground, canopy e top of canopy e calcula estatísticas em passos de 100 m ao longo da órbita, incluindo h_te_median, h_te_BestFit e h_canopy_abs (percentil 98 da altura de dossel) [p. 3–4, p. 8–9].
- Geolocalização: fótons com signal_confidence 3 ou 4 são deslocados recursivamente em cross-track e along-track até minimizar o erro vertical contra a superfície de terreno do lidar aerotransportado [p. 7].
- Validação: o lidar aerotransportado é extraído em uma caixa de 100 × 14 m em torno do centro de cada segmento ATL08 e comparado por mediana de terreno e percentil 98 de dossel [p. 8–9].

## 5. Resultados principais
- Geolocalização: 0 m em cross-track e −5 m em along-track, isto é, desvio de 5 m, dentro do requisito de missão de 6,5 m [p. 7, p. 1]; os fótons ATL03 tiveram offset vertical de 0 m com RMSE de 3,25 m [p. 8].
- Terreno: erro absoluto médio inferior a 0,5 m (mediana 0,37 m; best fit 0,39 m) [p. 8]; RMSE de 0,85 m para h_te_median e 0,82 m para h_te_BestFit [p. 9]; R² = 0,99 entre ATL08 e lidar aerotransportado [p. 9].
- Dossel: erro absoluto médio de aproximadamente 3,2 m e RMSE de 3,69 m no transecto analisado [p. 9]. O resumo reporta RMSE de 0,85 m e 3,2 m para terreno e dossel [p. 1], valor de dossel que não coincide com o RMSE de 3,69 m da seção de resultados [p. 9].
- Comparação histórica: o ICESat/GLAS apresentava acurácias de 3–8,5 m em áreas de baixo relevo topográfico [p. 10].
- Qualitativo: os três exemplos indicam que alturas de dossel em escala de watershed são viáveis [p. 6]; o "ringing" especular abaixo da superfície permite separar floresta alagada, como o manguezal, da floresta não alagada [p. 7].

## 6. Limitações que os próprios autores reconhecem
- Os resultados quantitativos vêm de uma única granulo e de um transecto, e os autores pedem avaliação em locais adicionais [p. 11].
- A versão v001 não tem calibração de ranging aplicada, portanto a acurácia vertical ainda não está calibrada [p. 11]; correções no ATL08 devem chegar na release v002 [p. 11]; a lista de problemas conhecidos inclui nuvens, atenuação do sinal e parâmetros mal selecionados no ground finding [p. 11].
- O lidar aerotransportado é de 2014 e o ATL08 de 24/11/2018; a diferença temporal impede distinguir erro de medição de mudança real da vegetação [p. 9–10].
- A densidade de pontos é menor que a do lidar aerotransportado e o cálculo por árvore não é realista, só em escala de stand/landscape [p. 4, p. 6–7]; fica em aberto quanta cobertura de dossel é necessária em ecossistemas baixos [p. 7].

## 7. O que serve ao projeto e o que não serve
- Serve: o desenho de validação (caixa de 100 × 14 m, mediana de terreno e percentil 98 de dossel, MAE e RMSE) é replicável para cruzar ATL08 com lidar aerotransportado em talhões de silvicultura goianos [p. 8–9].
- Serve: o ATL08 entrega altura de dossel e métricas de estrutura em passos de 100 m, escala de stand compatível com talhões, e o exemplo de savana/woodland no Botsuana é o análogo estrutural mais próximo do Cerrado [p. 4, p. 6].
- Não serve: os valores de acurácia (0,85 m para terreno; 3,69 m para dossel) vêm de um transecto boreal na Finlândia, em v001, e não são transferíveis para Goiás nem para eucalipto [p. 9, p. 11].
- Não serve: o artigo mede altura, não biomassa nem estoque de carbono; não há modelo alométrico, parcela de campo, dados de plantio, abordagem multissensorial, e Goiás não é citado [p. 1, p. 11].

## 8. Frases citáveis (literais)
- "The vertical RMSE for the terrain and canopy height retrievals for one transect are 0.85 m and 3.2 m respectively." [p. 1]
- "It is important to emphasize that ICESat-2 does not have the same point density compared to typical airborne lidar missions and calculations at the per-tree level are not realistic." [p. 4]
