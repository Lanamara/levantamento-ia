# RELATÓRIO — Micael de Souza Fraga (2018)

## 1. Referência

Micael de Souza Fraga; Eduardo Morgan Uliana; Demetrius David da Silva; Flávio Bastos Campos; Maria Lúcia Calijuri; Diego Magalhães de Souza Santos (2018). *Climatic zoning for eucalyptus cultivation through strategic decision analysis*. Revista Ambiente & Água — An Interdisciplinary Journal of Applied Science, v. 13, n. 1, e2119, Taubaté. DOI: 10.4136/ambi-agua.2119. Recebido em 30/03/2017, aceito em 18/12/2017 [p. 1].

## 2. Pergunta do estudo

Quais áreas do estado do Espírito Santo são climaticamente aptas ao desenvolvimento de *Eucalyptus grandis* e *Eucalyptus urophylla*, e como conciliar a aptidão conflitante entre as duas variedades? [p. 2]

## 3. Área e dados

- Local: estado do Espírito Santo, Brasil, 46.078 km², entre os meridianos 39°38' e 41°50' W e os paralelos 17°52' e 21°19' S [p. 3].
- Período: série histórica de 30 anos (1979–2008) [p. 3].
- Fontes meteorológicas: 79 estações pluviométricas da rede da ANA, do INMET e do CPTEC [p. 3]; temperatura do ar estimada pelo software CALCLI a partir de coordenadas e distância da costa [p. 3].
- Balanço hídrico climatológico mensal por Thornthwaite e Mather, com capacidade de armazenamento de água no solo (DAC) de 300 mm [p. 3].
- Declividade: modelo digital de elevação do radar SRTM, resolução espacial de 90 m (escala 1:250.000) [p. 3].
- Amostras: 79 pontos pluviométricos [p. 3]; nenhuma amostra de campo de biomassa ou carbono é descrita.
- Restrições espaciais: áreas alagadas, unidades de conservação (APP, reservas biológicas, parques estaduais), hidrografia e perímetro urbano [p. 4].

## 4. Método

- Padronização *fuzzy* dos quatro fatores de decisão (precipitação média, temperatura média, déficit hídrico e declividade), com funções sigmoidal simétrica e sigmoidal/linear decrescente [p. 5].
- Interpolação por krigagem ordinária, com escolha do modelo de semivariograma pela maior correlação em validação cruzada (coeficiente de Pearson, teste t a 5%) [p. 3].
- Ponderação pelo método AHP (matriz de comparação par a par) no módulo WEIGHT e agregação/compensação por Weighted Linear Combination (WLC) no módulo MCE, ambos do Idrisi Selva [p. 4–5].
- Resolução de conflito entre variedades pelo módulo Multi-Objective Land Allocation (MOLA), com pesos iguais e 5.000 km² para cada variedade [p. 6].

## 5. Resultados principais

- Pesos finais dos fatores: 0,522 para déficit hídrico anual; 0,1998 para temperatura média anual; 0,1998 para precipitação média anual; 0,0781 para declividade, somando 1 [p. 4].
- Aptidão padronizada em escala contínua de 0 (menos adequado) a 255 (mais adequado) [p. 5–6]; o mapa final variou de 0 a 255 [p. 6].
- Temperatura média anual do estado de aproximadamente 22,6 °C, variando de 17 °C a 24 °C, com amplitude térmica de 7 °C [p. 6].
- Precipitação média anual de aproximadamente 1.256,67 mm ano⁻¹, variando de 916 a 1.766 mm ano⁻¹ [p. 6].
- Déficit hídrico anual variando de 0 a 349 mm ano⁻¹ [p. 6].
- Grande parte do estado apresenta alta aptidão para as duas variedades; a região noroeste e parte da região norte apresentaram menor aptidão para ambas, associada aos maiores déficits hídricos [p. 8].
- *Eucalyptus urophylla* mostrou menor aptidão em algumas localidades da região serrana, por precipitação acima do limite superior ótimo dessa variedade [p. 8].
- Considerando os 10.000 km² mais adaptáveis, as áreas mais adequadas estão na região serrana, parte da região sul e próximo ao litoral nordeste [p. 9]; a maior parte das áreas de conflito foi alocada para *E. urophylla*, e as áreas de maior precipitação total para *E. grandis* [p. 9].
- Exigências adotadas: *E. grandis* — temperatura 6–32 °C, precipitação 1.000–1.800 mm, déficit hídrico 0–400 mm, declividade 0–100%; *E. urophylla* — 12–29 °C, 1.000–1.500 mm, 0–400 mm, 0–100% [p. 5].
- Contexto citado: plantios de eucalipto no Brasil somavam 5,56 milhões de ha em 2014, com projeção de cerca de 8 milhões de ha para 2020 [p. 2].

## 6. Limitações que os próprios autores reconhecem

- Necessidade de estudos adicionais com outros fatores (edáficos e legislação específica) e de análise de impacto ambiental e socioeconômico da expansão florestal [p. 9].
- A função sigmoidal decrescente usada para o déficit hídrico faz desse parâmetro um fator limitante, pois a aptidão cai à medida que o déficit se afasta de zero, mesmo com máximo dentro da faixa recomendada [p. 8].
- Restrição pluviométrica: ambas as espécies têm 1.000 mm como limite inferior de precipitação anual, e *E. urophylla* tem limite superior de 1.500 mm ano⁻¹, inferior ao observado em algumas regiões do estado [p. 6].
- A declividade recebeu o menor peso por não ser parâmetro climático, sendo considerada apenas pelo efeito na produtividade das máquinas de colheita [p. 5].

## 7. O que serve ao projeto e o que não serve

- Serve: a cadeia metodológica fuzzy → AHP → WLC → MOLA no Idrisi Selva é diretamente transferível para zoneamento de aptidão da silvicultura em Goiás, inclusive com pesos explícitos e critérios de restrição espacial [p. 4–6].
- Serve: a justificativa e a quantificação do déficit hídrico como fator dominante (peso 0,522) e do balanço hídrico com DAC de 300 mm oferecem base defensável para escolher preditores climáticos [p. 3–4].
- Serve parcialmente: a lógica de alocação de área-alvo (10.000 km², 5.000 km² por variedade) pode orientar priorização espacial de expansão, mas sem relação com biomassa ou carbono [p. 6].
- Não serve: o artigo não trata de biomassa, estoque de carbono, sensoriamento remoto multissensorial nem de Goiás — o recorte é aptidão climática de duas variedades no Espírito Santo, com única fonte de sensoriamento remoto (SRTM) usada apenas para declividade [p. 1–3].

## 8. Frases citáveis (literais)

- "The annual average temperature of the state of Espírito Santo is approximately 22.6°C, and varies from 17°C to 24°C, with a thermal amplitude of 7°C." [p. 6]
- "The MOLA tool solved the conflict of suitability between the two eucalyptus species." [p. 10]
