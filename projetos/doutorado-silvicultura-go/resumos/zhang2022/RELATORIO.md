# RELATÓRIO — Yi Zhang (2022)

## 1. Referência

Zhang, Y.; Lu, D.; Jiang, X.; Li, Y.; Li, D. *Forest Structure Simulation of Eucalyptus Plantation Using Remote-Sensing-Based Forest Age Data and 3-PG Model*. **Remote Sensing**, v. 15, n. 1, art. 183, 2023 (publicado online em 29/12/2022). DOI: 10.3390/rs15010183.

O `TEXTO.txt` corresponde ao artigo do DOI indicado, com 19 páginas e conteúdo integral (Introdução, Métodos, Resultados, Discussão, Conclusões, Apêndice e Referências) [p. 1, 19]. Observação: a data de publicação é 29/12/2022, mas a referência oficial da revista é 2023.

## 2. Pergunta do estudo

Verificar se dados de idade florestal obtidos de sensoriamento remoto (série temporal Landsat) conseguem sustentar o modelo 3-PG na simulação acurada de DBH, altura (H) e estoque de carbono aéreo (ACS) de plantios de eucalipto nas escalas de parcela (SP) e de subcompartimento florestal (FSC), e quão sensíveis são essas simulações à idade usada como entrada [p. 3].

## 3. Área e dados

- Local: Yuanling State Forestry Farm, condado de Yunxiao, Zhangzhou, província de Fujian, China; clima monçônico marítimo subtropical, temperatura média anual de 21,2 °C e precipitação anual de 1730,6 mm [p. 3].
- Espécies: *Eucalyptus grandis* × *urophylla* e *Eucalyptus urophylla* S.T. Blake; eucalipto introduzido na área por volta de 2005 [p. 3].
- Inventário FSC: dados de 2017 do órgão florestal, 140 subcompartimentos, 379,2 ha, com idade concentrada em 0–4 e 9–12 anos [p. 4, 5].
- Parcelas de campo (SP): 17 parcelas de 20 m × 20 m, medidas em janeiro, julho e dezembro de 2021; idades de 1 a 13 anos; DBH médio de 3,62–16,26 cm e H média de 4,02–19,69 m; total de 44 observações de DBH e 41 de H [p. 4].
- UAV lidar: julho de 2021, densidade média de 60 pontos/m², CHM em 1 m; modelo de predição de ACS com 17 observações e validação leave-one-out (R² 0,87; RMSE 8,73 Mg/ha; RRMSE 18,72%) [p. 5].
- Idade florestal por sensoriamento remoto: série temporal Landsat, 30 m × 30 m, gerada por segmentação por localização aleatória e classificação contínua por random forest, RMSE de 13 meses em 2021 e erro de cerca de 12 meses na área de estudo [p. 6].
- Meteorologia: estação local 2008–2021, estendida a 1997–2007 com dados da NASA; radiação solar 1997–2021 do POWER/LaRC [p. 5].

## 4. Método

- Modelo 3-PG (processos fisiológico-ecológicos, escala mensal, quatro submodelos: luz, produção e alocação de biomassa, balanço hídrico e mortalidade), executado no pacote `r3PG` em R [p. 6].
- Calibração e validação na escala SP com dados de campo; parâmetros alométricos do fuste ajustados localmente: aWS = 0,0259 e nWS = 2,8762 (R² = 0,9998); biomassa inicial de fuste, raiz e folha de 1, 2 e 0,5 Mg/ha [p. 7].
- Três cenários na escala FSC: (a) idade do inventário FSC de 2017; (b) idade do Landsat de janeiro de 2021; (c) idades ajustadas em ±3, ±6 e ±12 meses para análise de sensibilidade; validação com H e ACS derivados do lidar [p. 8].
- Avaliação por R², RMSE e RRMSE; comparação também com e sem informação de desbaste (thinning) [p. 8, 9].

## 5. Resultados principais

- Escala SP com idade de inventário: R² de 0,80 a 0,93 para DBH, H e ACS [p. 9]; considerar o desbaste elevou o R² de ACS, DBH e H em 0,09, 0,06 e 0,07 e reduziu o RRMSE em 8,54%, 6,75% e 4,2% [p. 9].
- Escala SP com idade Landsat: R² acima de 0,85 para os três atributos e RRMSE abaixo de 20% [p. 9]; o resumo reporta R² de 0,87 a 0,94 e RRMSE abaixo de 20% na escala SP [p. 1].
- Escala FSC com idade do inventário: R² muito baixo e RMSE alto; para FSC plantados após 2015, RMSE de 2,91 m (H) e 14,22 Mg/ha (ACS); para FSC plantados antes de 2015, RMSE de 14,06 m (H) e 80,78 Mg/ha (ACS) [p. 10].
- Escala FSC com idade Landsat: R² de 0,7 para ACS, RMSE de 9,12 Mg/ha e RRMSE de 28,24% [p. 1].
- Sensibilidade em SP: RMSE de DBH aumenta 33,45% com +12 meses; RMSE de H e de ACS aumentam 42,92% e 82,91% com −12 meses; menor RMSE de DBH em −6 meses e de H e ACS em +6 meses [p. 11].
- Sensibilidade em FSC: RMSE de H e ACS aumentam 12,2% e 41,23% com +12 meses; R² de H varia de 0,68 (sem ajuste) a 0,74 e o de ACS de 0,70 a 0,77; RMSE de ACS de 9,12 a 12,88 Mg/ha [p. 12].
- Coeficiente de carbono usado na conversão de biomassa em ACS: 0,4764 [p. 4]; equações de biomassa por órgão com R² de 0,871 a 0,978 [p. 5].

## 6. Limitações que os próprios autores reconhecem

- A resposta da NPP ao desbaste não foi bem explorada, com efeitos positivos, negativos e neutros coexistindo na literatura; deveria ser tratada em simulações futuras [p. 14].
- A idade derivada de série temporal Landsat não detecta manejo como desbaste, por causa da resolução espacial e temporal grosseira, o que reduz a acurácia da simulação; sugerem análise de mistura espectral ou dados de maior resolução espaço-temporal (Sentinel, Gaofen) [p. 14].
- É difícil obter a data exata de plantio (mês), sobretudo com coexistência de rebrota e plantio, e o modelo exige o mês de plantio, o que prejudica a simulação do crescimento inicial do eucalipto [p. 12].
- A heterogeneidade espacial dentro do FSC (manejo e distúrbios diferenciados, diferenças de altura de até 20–25 m) pode causar superestimação ou subestimação; recomendam redesenhar os limites dos FSC [p. 13].
- A simulação foi feita para os 140 FSC como unidade, não por pixel, por falta de dados de solo, meteorologia e densidade de árvores em alta resolução espacial [p. 8].

## 7. O que serve ao projeto e o que não serve

- Serve: a arquitetura metodológica de usar idade florestal derivada de série temporal Landsat como driver de um modelo de processos (3-PG) para estimar DBH, H e carbono em eucalipto, com validação independente por UAV lidar — desenho diretamente transferível para a silvicultura de Goiás [p. 6, 8].
- Serve: a quantificação do erro propagado da idade florestal no estoque de carbono (até 82,91% em SP com −12 meses e 41,23% em FSC com +12 meses), que justifica orçamento de incerteza em qualquer estimativa de carbono por sensoriamento remoto [p. 1, 11, 12].
- Serve: a evidência de que idade de inventário desatualizada (2017 aplicada a 2021) inviabiliza a simulação em escala de talhão (RMSE de ACS de 80,78 Mg/ha antes de 2015), reforçando a necessidade de atualização anual da idade [p. 10].
- Não serve diretamente: o artigo é de uma única fazenda em Fujian, com 17 parcelas e 140 FSC, sem validação destrutiva de biomassa e com dados de campo não públicos; não há transferência de parâmetros para Cerrado nem uso de sensores multiespectrais de alta resolução (Sentinel-2, Planet) além do Landsat de 30 m [p. 4, 6, 15].

## 8. Frases citáveis (literais)

- "The forest age data from Landsat are very effective for driving the 3-PG model." [p. 10]
- "The maximum difference in ACS is 82.91% at the SP scale if the forest age decreases 12 months and 41.23% at the FSC scale if the forest age increases 12 months." [p. 1]
