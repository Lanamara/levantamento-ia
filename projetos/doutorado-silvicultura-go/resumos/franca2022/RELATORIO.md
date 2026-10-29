# RELATÓRIO — Luciano Cavalcante de Jesus França (2022)

## 1. Referência

- França, L.C.d.J.; Lopes, L.F.; Morais, M.S.d.; Lisboa, G.d.S.; Rocha, S.J.S.S.d.; Morais Junior, V.T.M.d.; Santana, R.C.; Mucida, D.P.
- Título: *Environmental Fragility Zoning Using GIS and AHP Modeling: Perspectives for the Conservation of Natural Ecosystems in Brazil*.
- Revista: *Conservation* (MDPI), v. 2, p. 349–366, 2022. Recebido em 28 abr. 2022; aceito em 2 jun. 2022; publicado em 7 jun. 2022 [p. 1].
- DOI: 10.3390/conservation2020024 — confere com o `TEXTO.txt`, que está completo (18 páginas, incluindo referências).
- Artigo de acesso aberto (CC BY 4.0) [p. 1].

## 2. Pergunta do estudo

Quais áreas da Bacia Hidrográfica do Rio Jequitinhonha (MG) apresentam fragilidade ambiental potencial (PEF) e emergente (EEF) crítica, de modo a orientar zoneamento ambiental e prioridades de conservação e restauração [p. 1].

## 3. Área e dados

- Local: Bacia Hidrográfica do Rio Jequitinhonha (JRHB), estado de Minas Gerais, sudeste do Brasil; 66.319 km² [p. 2]. Área efetivamente mapeada: 64.151,35 km² [p. 10].
- Relevo: de 100 m (jusante) a mais de 1800 m (montante) [p. 2]. Clima Cwb, Cwa e As [p. 2]. População estimada de 789.862 habitantes; o rio abastece 70 dos 82 municípios da bacia [p. 2].
- Sensores e fontes (todos gratuitos): DEM/SRTM do Earth Explorer (USGS); classes de solo da FEAM; domínios geológicos do CPRM; precipitação das isoietas de média anual de 1977–2006 (CPRM); hierarquia fluvial derivada do DEM/SRTM pelo método de Strahler; uso e cobertura da terra de 2018 do MapBiomas (adicionado apenas para a EEF) [p. 3].
- Processamento: ArcGIS 10.5, datum WGS 1984, projeção UTM zona 23S [p. 3–4].
- Período: as camadas-base não têm data única; a série de chuva vai de 1977 a 2006 [p. 3] e o uso da terra é de 2018 [p. 3].
- Amostras: não informado — o estudo é de modelagem espacial em escala de bacia, sem amostragem de campo. O único conjunto de julgamentos é o de 3 decisores entrevistados para as comparações pareadas do AHP [p. 7].

## 4. Método

1. **PEF por álgebra de mapas**: cinco planos de informação (declividade, solos, geologia, hierarquia fluvial, chuva) reclassificados em 5 graus de fragilidade (1 = baixa a 5 = extremamente alta) [p. 3, p. 5–6].
2. **EEF**: sobreposição da PEF com o plano de uso e cobertura da terra, critério mais pesado do modelo [p. 3, p. 10].
3. **AHP**: comparações pareadas em escala de 1 a 9, com três decisores; cálculo de autovetor, índice de consistência (CI) e razão de consistência (CR) [p. 6–7].
4. **WLC em GIS**: cada critério padronizado é multiplicado pelo seu peso e somado pixel a pixel (`S = Σ wi·xi`), com reclassificação final em 5 classes pelo método de Jenks [p. 7].

## 5. Resultados principais

- Pesos AHP: uso e cobertura da terra 40% (0,40); declividade 27% (0,27); chuva 16% (0,16); hierarquia fluvial 10% (0,10); classes de solo 5% (0,05); domínios geológicos 2% (0,02) [p. 9].
- Consistência do modelo: CI = 0,09; CR = 0,07; λmax = 6,45 com n = 6 [p. 9].
- PEF: média 30,00% (19.244,07 km²); levemente baixa 28,90% (18.540,93 km²); baixa 19,38% (12.430,57 km²); alta 16,40% (10.519,63 km²); extremamente alta 5,33% (3.416,15 km²) [p. 9–10].
- EEF: média 53,78% (34.503,55 km²); levemente baixa 33,36% (21.399,14 km²); alta 9,83% (6.305,45 km²); baixa 2,57% (1.646,90 km²); extremamente alta 0,46% (296,27 km²) [p. 10].
- As classes média e levemente baixa somam cerca de 60% da PEF e cerca de 70% da EEF [p. 1].
- A classe média sobe de 30% na PEF para 53,78% na EEF, enquanto a baixa cai de 19,38% para 2,57% [p. 9–10, p. 12].
- As fragilidades alta e extremamente alta concentram-se no alto Jequitinhonha, região de hotspot de biodiversidade (Reserva da Biosfera da Serra do Espinhaço) [p. 1, p. 11–12].
- Declividade: a classe 12–30% (terreno acidentado) predomina com 25,4% (16.606,84 km²); 9,2% da bacia tem declives acima de 30% [p. 4].
- Solos: argissolos (red ultisols) 22,98% (~15.238,04 km²); argissolos vermelho-amarelos 19,98% (~13.253,57 km²); neossolos litólicos 14% (~9.035,3 km²) [p. 4].
- Chuva: de 800 mm (médio/baixo Jequitinhonha) a 1300 mm (alto Jequitinhonha) [p. 4–5].
- Uso da terra: pastagem 39,18% (25.576,02 km²); formações savânicas 21,07% (13.758,73 km²); formações florestais 17,25% (11.262,93 km²); mosaicos de agricultura e pastagem 6,90% (4.506,01 km²); culturas semiperenes 5,79% (3.780,69 km²); plantios florestais 4,20% (2.745,19 km²); campestres 4,20% (2.745,19 km²) [p. 6].
- Hierarquia fluvial até 7ª ordem; cursos de 1ª e 2ª ordens somam 11.058,10 km e 5.491,64 km [p. 4].

## 6. Limitações que os próprios autores reconhecem

- "One of the fundamental challenges of modeling EF is the attribution of weights based on specific technical and scientific knowledge"; faltam estudos de validação dos índices de fragilidade, sobretudo testes em larga escala sobre a probabilidade real de erosão e sedimentação [p. 13].
- Persiste viés arbitrário na decisão dos pesos; recomendam machine learning e programação matemática para estimá-los [p. 13].
- O modelo "does not directly incorporate the 'social fraction'", indicador de sustentabilidade social; sugerem incluí-lo em estudos futuros [p. 13].
- Desafio de escalabilidade, por se tratar de área de grandes dimensões territoriais [p. 13].
- As recomendações de uso e conservação são de perspectiva regional e exigem análise do contexto local [p. 14].
- Os critérios solo (5%) e geologia (2%) receberam baixo peso, em parte pela escala grosseira do mapeamento de Minas Gerais (1:500.000) [p. 11].

## 7. O que serve ao projeto e o que não serve

- **Serve**: o arcabouço AHP + WLC + GIS como camada de zoneamento multicritério replicável e de baixo custo, que pode ser acoplada a mapas de biomassa/estoque de carbono como um dos planos de informação.
- **Serve**: a lógica PEF (atributos naturais estáveis) → EEF (PEF + uso e cobertura), útil como análogo conceitual para separar o potencial biofísico do carbono do carbono efetivamente observado sob uso antrópico.
- **Serve**: o uso de bases públicas gratuitas (SRTM, MapBiomas, CPRM, FEAM) e a documentação do fluxo em ArcGIS, com pesos e razões de consistência explicitados, o que permite auditoria e adaptação para Goiás.
- **Não serve**: não há biomassa, estoque de carbono, inventário florestal, LiDAR ou sensoriamento multissensorial; plantios florestais aparecem só como classe de uso da terra (4,20%, 2.745,19 km²) [p. 6], sem qualquer medição estrutural; a área é Minas Gerais, não Goiás, e o índice de fragilidade não foi validado em campo [p. 13].

## 8. Frases citáveis (literais)

- "The methodological approach involved the integration of the analytic hierarchy process (AHP) and weighted linear combination (WLC) into a geographic information system (GIS)." [p. 1]
- "The methodology applied in this study can be replicated in other global ecoregions." [p. 1]
