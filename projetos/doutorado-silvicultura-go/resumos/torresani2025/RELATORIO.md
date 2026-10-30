# RELATÓRIO — Michele Torresani (2025)

## 1. Referência

Torresani, M.; Rossi, C.; Mina, M.; Menegaldo, I.; Cappuccio, M.; Perrone, M.; Hakkenberg, C. R.; Rocchini, D.; Puletti, N.; Stendardi, L.; Montagnani, L.; Tognetti, R. (2025). Spectral heterogeneity from the spaceborne imaging spectrometer EnMAP reveals biodiversity patterns in forest ecosystems. *International Journal of Applied Earth Observation and Geoinformation*, v. 144, art. 104902 [p. 1]. DOI: 10.1016/j.jag.2025.104902 [p. 1].

## 2. Pergunta do estudo

Testar se a heterogeneidade espectral (SH) derivada do sensor hiperespectral EnMAP se correlaciona com a diversidade de espécies arbóreas em florestas montanas dos Alpes italianos e qual combinação de métrica, região espectral e abordagem espacial apresenta melhor desempenho.

## 3. Área e dados

- Local: porção do Tirol do Sul, Província Autônoma de Bolzano/Bozen, norte da Itália [p. 3].
- Período: inventário de campo entre 2021 e 2024 [p. 3]; imagem EnMAP de 9 de setembro de 2023 [p. 4]; LiDAR ALS de 2006 [p. 7].
- Sensores/fontes: EnMAP (242 bandas, 420–2450 nm, 30 m, duas cenas Level 2A) [p. 2, 4]; ALS LiDAR para cobertura de copa (CC) [p. 7]; GPS RTK com acurácia <20 cm [p. 3].
- Amostras: 52 parcelas de 13 m de raio (26 m de diâmetro), com árvores de DBH >10 cm; 42 parcelas analisadas após exclusão de 10 por bandas corrompidas ou ausentes [p. 3].

## 4. Método

- Diversidade de campo: riqueza de espécies e Shannon's H calculados por parcela [p. 3–4].
- SH calculada com Rao's Q e CV em três níveis: bandas individuais (219 retidas), faixas VIS, NIR e SWIR, e índices de vegetação (VIs) [p. 4–5].
- Três abordagens espaciais: peso igual aos quatro pixels EnMAP que intersectam a parcela; peso proporcional à área de sobreposição; e peso com restrição a parcelas com CC >70% derivada do ALS LiDAR [p. 5–7].
- Regressões lineares entre SH e diversidade, com R2 e inclinação; Moran's I indicou ausência de autocorrelação espacial significativa [p. 3–4].

## 5. Resultados principais

- Nas 42 parcelas, a riqueza variou de 1 a 4 espécies, o Shannon's H de 0,14 a 1,36 e a CC de 41,4% a 96,5% [p. 7].
- Bandas individuais: R2 máximo de 0,38 com a abordagem weighted CC >70%; correlações maiores no NIR, intermediárias no VIS e baixas ou negativas no SWIR [p. 8].
- Faixas espectrais: R2 máximo de 0,34 (CV no NIR, weighted CC >70%) [p. 8]; o resumo registra R2 até 0,35 [p. 1].
- VIs: ajustes em geral baixos, com R2 >0,2 apenas para TGI e SIPI2; NDVI esteve entre os mais baixos [p. 8, 10].
- Riqueza de espécies gerou correlações mais fortes que Shannon's H; Rao's Q e CV produziram resultados semelhantes [p. 8, 11].
- Após a remoção de bandas ruins, 219 bandas foram mantidas [p. 4].

## 6. Limitações que os próprios autores reconhecem

- Descompasso temporal entre o campo (2021–2024) e a imagem EnMAP (setembro de 2023) [p. 11].
- ALS LiDAR de 2006, único conjunto disponível para a região [p. 11–12].
- Riqueza arbórea baixa (1 a 4 espécies), o que limita a generalização para florestas mais diversas [p. 12].
- Uso de apenas 42 das 52 parcelas disponíveis [p. 12].
- Uma única imagem, de início de outono, sem avaliação da variação sazonal [p. 13].
- Incertezas de geolocalização das parcelas e de correção geométrica da imagem [p. 11].
- Escolha de bandas para os VIs e uso da média absoluta no cálculo do CV [p. 10].

## 7. O que serve ao projeto e o que não serve

- Serve: o arcabouço da Spectral Variation Hypothesis (SVH) e as métricas Rao's Q e CV, com validação por regressão e R2, são replicáveis para heterogeneidade espectral em povoamentos de Goiás.
- Serve: a ponderação pela sobreposição pixel-parcela e o filtro por CC >70% com LiDAR tratam o desalinhamento entre parcelas pequenas e pixels de 30 m e reduzem o efeito de solo exposto [p. 5–7].
- Serve: o achado de que o NIR concentra o sinal e de que riqueza de espécies responde melhor que Shannon's H orienta a seleção de bandas e da variável-resposta.
- Não serve: o artigo não mede biomassa nem estoque de carbono; seu alvo é diversidade de espécies em floresta alpina temperada/subalpina, não silvicultura em Goiás, e a análise usa uma única data EnMAP.

## 8. Frases citáveis (literais)

- "The Spectral Variation Hypothesis (SVH) proposes that spectral heterogeneity (SH), derived from optical data, can serve as a proxy for estimating biodiversity." [p. 1]
- "Our results clearly highlight the importance of spatial approach selection when testing the SVH." [p. 10]
