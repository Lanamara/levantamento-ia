# RELATÓRIO — Venkata Shashank Konduri (2023)

## 1. Referência

Konduri, Venkata Shashank; Morton, Douglas C.; Andela, Niels (2023). "Tracking Changes in Vegetation Structure Following Fire in the Cerrado Biome Using ICESat-2". *Journal of Geophysical Research: Biogeosciences*, 128, e2022JG007046. DOI: 10.1029/2022JG007046 [p. 1]. Texto integral e íntegro (15 páginas) — corresponde ao DOI indicado.

## 2. Pergunta do estudo

Qual é o efeito da frequência de queima e do tempo desde a última queima sobre a altura do dossel e a cobertura fracional de vegetação lenhosa nos principais tipos de vegetação do Cerrado, e quão rápido se dá a recuperação pós-fogo [p. 3].

## 3. Área e dados

- **Local:** bioma Cerrado (Brasil), com gradiente leste-oeste de precipitação [p. 4]; análise restrita a áreas sem mudança de cobertura da terra entre 2001 e 2020, ~76% da área do bioma nos quatro tipos considerados [p. 4].
- **Período:** burned area de janeiro de 2001 a junho de 2021 [p. 4–5]; cobertura da terra 2001–2020 [p. 3]; precipitação 2001–2019 [p. 4]; ICESat-2 de 28/09/2018 a 14/06/2021 [p. 4].
- **Sensores/fontes:** ICESat-2 ATL03 e ATL08 (v. 5, feixes fortes) [p. 4]; MODIS MCD64A1 Collection 6, 500 m (Terra e Aqua) [p. 4–5]; MapBiomas Collection 5, 30 m [p. 3]; IMERG v. 06, 0,1° (~10 km) [p. 4].
- **Amostras:** 1.838 arquivos ICESat-2; 6,18 milhões de segmentos de 20 m, com ~358 milhões de fótons [p. 4]; quatro classes de cobertura: pastagem ~31%, savana 29%, floresta 14%, campo 8% do bioma [p. 3]; a maioria das células de 1 km contém ao menos 3.200 segmentos de 20 m [p. 5].

## 4. Método

1. Derivação, por segmento de 20 m, da altura média do dossel (média de `ph_h` dos fótons de dossel) e da cobertura fracional (razão entre fótons de dossel/topo e total de fótons) [p. 4]; segmentos com presença de água, área urbana, nuvem ou aerossol foram excluídos [p. 4].
2. Cálculo, para cada segmento, da frequência de queima (número de queimas do pixel de 500 m entre janeiro de 2001 e a data do ICESat-2, agrupada em 0, 1, 2, 3 e ≥4) e do tempo desde a queima, ambos ajustados à data de aquisição do lidar [p. 5].
3. Estratificação por tipo de cobertura, zona de precipitação (baixa 0–20, moderada 20–80, alta 80–100 percentis) e classe de tempo desde o fogo, em abordagem *space-for-time* (substituição espaço-por-tempo) [p. 4–5].
4. Ajuste de retas às medianas das distribuições por classe de frequência de queima e por classe de tempo desde a queima; a inclinação é tomada como taxa de perda ou de recuperação, com mapas de 1 km e de 2° [p. 7–10].

## 5. Resultados principais

- **Regime de fogo:** ~64% do bioma nunca queimou no registro MODIS; 13%, 7%, 5% e 11% queimaram 1, 2, 3 e ≥4 vezes, respectivamente [p. 5]. Cerca de 19% queimou nos últimos 5 anos; 9%, 6% e 2% queimaram há 5–10, 10–15 e 15–22 anos [p. 5]. Dois terços da área queimada concentram-se no MATOPIBA, ao norte [p. 5].
- **Perda por fogo em altura:** a queda da altura média do dossel foi de 40 cm por fogo em florestas e 30 cm por fogo em savanas, consistente entre zonas de precipitação [p. 6].
- **Perda por fogo em cobertura:** em florestas o efeito sobre a cobertura fracional foi pequeno, com <1% de perda por fogo na zona de precipitação moderada [p. 6]; em savanas a queda foi forte e consistente, de 5,1%–6,3% por fogo em todas as zonas de precipitação [p. 8]; em campos, 3%–4% por fogo [p. 8].
- **Recuperação da altura:** em florestas, +8,1 e +9,2 cm ano⁻¹ nas áreas de alta e média precipitação, contra 3 cm ano⁻¹ onde a chuva é <1.500 mm [p. 8]; a altura segue recuperando por mais de 20 anos após o fogo [p. 8] e permanece abaixo do valor de áreas não queimadas mesmo nos fogos mais antigos (14–20 anos) [p. 1].
- **Recuperação da cobertura:** em florestas de média e alta precipitação a cobertura retorna ao nível de áreas não queimadas em cerca de 4 a 6 anos [p. 8] (dentro de 5 anos, no resumo) [p. 1]; em savanas, +1,1% e +1,8% ano⁻¹ nas zonas de alta e média precipitação, contra 0,7% ano⁻¹ na de baixa chuva [p. 8], com estabilização após 10–12 anos [p. 10].
- **Gradiente espacial:** correlação entre recuperação e precipitação com Pearson's r = 0,35 para altura e r = 0,44 para cobertura lenhosa em savanas [p. 8]; diferenças de três a quatro vezes nas taxas dentro de um mesmo tipo de cobertura [p. 8].
- **Estrutura observada:** >70% de cobertura de dossel em áreas florestais e <20% em campos, pastagens e lavouras [p. 5]; ICESat-2 detectou cobertura lenhosa (>50 cm) em ~81% dos segmentos de 20 m em campos e ~70% em pastagens [p. 5].
- **Pastagens:** resposta atenuada ou invertida — altura e cobertura lenhosa aumentam com a frequência de queima nas zonas moderada e alta de precipitação, atribuído ao uso do fogo no manejo [p. 6, p. 8].

## 6. Limitações que os próprios autores reconhecem

- A substituição *space-for-time* assume severidade de fogo semelhante entre coortes de tempo desde o fogo; efeito de seca não foi detectado, mas a premissa persiste [p. 11].
- Fatores de confusão não controlados: topografia, solos e uso da terra adjacente, que afetam nutrientes e efeitos de borda [p. 11].
- A amostragem do ICESat-2 é mais esparsa que a de GEDI ou de lidar aerotransportado; a heterogeneidade em pequenas escalas é mitigada, mas não eliminada, pelo tamanho amostral [p. 11].
- A resolução de 500 m do produto de área queimada não capta variabilidade de extensão e severidade dentro do perímetro, sobretudo em matas de galeria e microsítios úmidos [p. 10]; erros de omissão e comissão moderam as estimativas de perda e recuperação [p. 11].
- O limiar de 50 cm do algoritmo ATL08 mascara a camada herbácea e a fração lenhosa abaixo de 50 cm; a altura estimada reflete vegetação lenhosa, não a vegetação total [p. 5, p. 12].
- A sazonalidade da queima não foi considerada [p. 10]; o efeito da resolução espacial dos produtos de sensoriamento não foi avaliado explicitamente [p. 11].
- A acurácia do MapBiomas para o Cerrado é de ~80%, com erros de classificação entre tipos de vegetação nativa [p. 3].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o desenho metodológico — métricas de estrutura lenhosa por segmento de 20 m (altura média do dossel e cobertura fracional) derivadas de fótons do ICESat-2 (ATL03/ATL08), aplicáveis a povoamentos em Goiás [p. 4].
- **Serve:** a demonstração de que altura e cobertura fracional respondem de forma distinta e em escalas de tempo distintas (cobertura recupera em anos; altura, em décadas), o que justifica medir estrutura vertical e não apenas índices ópticos ao estimar biomassa e carbono [p. 8, p. 10].
- **Serve (com ressalva):** a lógica de estratificar por gradiente ambiental (precipitação) e por histórico de distúrbio antes de comparar coortes, útil para separar efeito de manejo de efeito climático [p. 4–5].
- **Não serve:** o artigo não estima biomassa nem estoque de carbono — entrega apenas proxies estruturais, sem modelo alométrico nem valores de carbono [p. 3, p. 11]; e trata de vegetação nativa do Cerrado sob regime de fogo, não de silvicultura plantada, sem dados de plantios comerciais (pastagem e lavoura entram apenas como classes de manejo) [p. 3, p. 6].

## 8. Frases citáveis (literais)

- "The decline in mean canopy height averaged 40 cm per fire in forests and 30 cm per fire in savannas." [p. 6]
- "By contrast, passive optical data are primarily sensitive to fractional cover (Staver et al., 2011), and this limitation could potentially lead to overestimation of ecosystem recovery (Potapov et al., 2021)." [p. 10]
