# RELATÓRIO — Danilo Roberti Alves de Almeida (2021)

## 1. Referência

Almeida, D.R.A.; Broadbent, E.N.; Ferreira, M.P.; Meli, P.; Almeyda Zambrano, A.M.; Gorgens, E.B.; Resende, A.F.; Almeida, C.T.; Amaral, C.H.; Dalla Corte, A.P.; Silva, C.A.; Romanelli, J.P.; Prata, G.A.; Papa, D.A.; Stark, S.C.; Valbuena, R.; Nelson, B.W.; Guillemot, J.; Féret, J.-B.; Chazdon, R.; Brancalion, P.H.S. (2021). *Monitoring restored tropical forest diversity and structure through UAV-borne hyperspectral and lidar fusion*. Remote Sensing of Environment, v. 264, 112582. DOI: 10.1016/j.rse.2021.112582.

## 2. Pergunta do estudo

A fusão de dados lidar e hiperespectrais embarcados em UAV permite avaliar a estrutura, a diversidade arbórea e a biomassa acima do solo de plantios de restauração florestal tropical?

## 3. Área e dados

- Local: plantio experimental de restauração em Anhembi, SP, sudeste do Brasil, em área antes ocupada por pastagem, na Mata Atlântica [p. 3].
- Período: plantio estabelecido em maio de 2006; inventário de campo em novembro de 2019, com 13,5 anos de idade; voos de 27 a 30 de agosto de 2019 [p. 3–4].
- Delineamento: 12 parcelas de 45 × 48 m, inteiramente casualizadas, com 20, 60 e 120 espécies nativas e quatro repetições por tratamento [p. 3]; sobreviveram 58 e 114 espécies nos tratamentos de 60 e 120 espécies [p. 3]. Por baixa cobertura hiperespectral em uma parcela, o tratamento de 120 espécies teve três repetições nas análises com HSI, ou seja, 11 parcelas [p. 3].
- Sensores: sistema GatorEye sobre hexacóptero DJI Matrice 600 Pro, com lidar Velodyne VLP-32c Ultra Puck (32 lasers, 905 nm, 600.000 disparos/s), sensor hiperespectral Headwall Nano VNIR (270 bandas, 400–1000 nm) e espectrômetro ascendente Ocean Optics Flame para conversão a reflectância [p. 4].
- Aquisição: voo a 100 m de altitude, quatro linhas de voo, 12–14 m/s, céu limpo; densidade final da nuvem lidar de 360 ± 137 pontos/m², 80,4% de primeiros retornos; resolução espacial final do HSI de 0,20 m [p. 4].
- Amostras: 12 parcelas (11 para HSI); 18 variáveis HSI e 3 atributos estruturais do lidar por parcela [p. 3–4].

## 4. Método

- Lidar: geração de CHM, DTM e DSM; altura do dossel (CH, média e desvio-padrão por parcela), LAI e LAI de sub-bosque (LAI.under, soma do perfil de LAD entre 1 e 5 m), com nuvem normalizada filtrada para primeiros retornos e homogeneizada a 30 pontos/m² antes do cálculo do LAD pelo método MacArthur-Horn [p. 4].
- HSI: 15 índices de vegetação (estruturais, clorofila, antocianina/carotenoide e fisiologia), dois primeiros componentes da transformação minimum noise fraction (MNF.1 e MNF.2) e ângulo espectral entre pares de pixels, calculado só em pixels de dossel iluminado com NDVI > 0,8 e altura > 4 m, usando o percentil 90% por parcela [p. 4–5].
- Estatística: correlação de Spearman entre variáveis HSI e lidar em nível de pixel (0,20 m); ANOVA e Tukey entre níveis de riqueza em nível de parcela, com média e desvio-padrão intraparecla como medida de heterogeneidade [p. 5].
- AGB: biomassa lenhosa por indivíduo pela equação alométrica de Ferez et al. (2015), com área seccional, altura total e densidade da madeira; regressões lineares simples e múltiplas com remoção de outliers por resíduos studentizados e validação leave-one-out (LOOCV) [p. 3, 5].

## 5. Resultados principais

- O LAI derivado do lidar correlacionou-se com quase todas as variáveis HSI; os índices estruturais tiveram as maiores correlações (r > 0,50; p < 0,05) [p. 5].
- Os índices estruturais cresceram com o LAI entre 0 e 2 m²/m² e saturaram acima desse valor; o mesmo padrão de saturação ou queda ocorreu para CH entre 15 e 20 m [p. 1, 5].
- O CH correlacionou-se com sete variáveis HSI, sendo o EVI a de maior correlação (r = 0,22; p = 0,006) [p. 5].
- O LAI.under não teve correlação significativa com nenhuma variável HSI [p. 5].
- AGB média por tratamento: 69,5 ± 10,4 Mg/ha (20 espécies), 94,3 ± 9,8 Mg/ha (60 espécies) e 88,7 ± 15,6 Mg/ha (120 espécies); a diferença foi significativa apenas entre 20 e 60 espécies a 5%, e os dois tratamentos mais ricos superaram o de 20 espécies a 10% de significância [p. 5].
- O CH foi maior nos tratamentos de 60 e 120 espécies; a heterogeneidade do CH não diferiu entre tratamentos (p = 0,59), mas a heterogeneidade do LAI foi maior nos dois tratamentos mais ricos (p < 0,001) [p. 5].
- O LAI foi maior no tratamento mais rico, com aumento significativo ao longo dos níveis de riqueza a 10% de significância; o LAI.under não diferiu entre tratamentos [p. 5].
- Entre os índices estruturais, VARI, SR, NDVI e EVI aumentaram com a riqueza; SIPI diminuiu, CI.rededge e CI.green aumentaram; CARI e mARI não diferiram [p. 5–6].
- ACI foi menor no tratamento de menor riqueza e CRI foi maior no mais rico [p. 6]; RVSI diminuiu e REP aumentou com a riqueza, enquanto WBI e PRI não mostraram relação clara [p. 6].
- MNF.1 aumentou em média e heterogeneidade com a riqueza; MNF.2 não diferiu entre tratamentos [p. 6].
- O ângulo espectral diferiu entre níveis de riqueza apenas a 10% de significância (p = 0,09) no teste de Tukey, e a 5% quando a riqueza foi tratada como preditor contínuo em regressão linear (Tabela S2) [p. 8–9].
- AGB correlacionou-se significativamente (p < 0,001) com CH (r = 0,81) e com RVSI (r = 0,78), EVI (r = 0,76) e CARI (r = 0,77) [p. 8].
- Após remover um outlier, o melhor preditor de AGB foi CH (r² = 0,82; RMSE = 7,62; RMSE relativo = 9,0%), seguido por RVSI (r² = 0,75; RMSE = 8,98; RMSE relativo = 10,1%) [p. 8].
- Modelos de regressão múltipla não trouxeram ganho significativo sobre os modelos simples [p. 8].

## 6. Limitações que os próprios autores reconhecem

- As relações encontradas, incluindo a saturação dos índices de vegetação, podem depender da estação e da resolução espacial, questão que precisa ser respondida para conectar observações de UAV a sensores aerotransportados e orbitais de grão mais grosso [p. 9].
- O LAI derivado do lidar é um proxy do LAI real e inclui contribuições de área de outros componentes do dossel, como galhos [p. 9].
- O HSI é limitado à superfície do dossel, o que explica a ausência de correlação com o LAI de sub-bosque [p. 9].
- A AGB avaliada é apenas a de fustes, sem galhos e folhas [p. 9].
- A baixa maturidade e a homogeneidade estrutural do plantio de 13 anos podem explicar a ausência de diferença na heterogeneidade de altura e no LAI de sub-bosque; a saturação dos índices reduz a heterogeneidade espacial e limita a discriminação de diversidade em dossel mais denso [p. 9].
- Os sistemas UAV-lidar-HSI ainda são relativamente caros e potencialmente inacessíveis a governos, ONGs, pequenos proprietários e empresas, e exigem alto conhecimento técnico para operação e processamento; em países tropicais há ainda barreiras de tarifas de importação e falta de assistência técnica local [p. 10].
- O lidar orbital GEDI não é espacialmente contínuo e tem precisão e acurácia muito menores que lidar aerotransportado e de UAV [p. 10].

## 7. O que serve ao projeto e o que não serve

- Serve: o modelo de AGB com altura do dossel (r² = 0,82; RMSE relativo = 9,0%) é referência direta para estimativa de biomassa com lidar em plantios [p. 8].
- Serve: a fusão lidar + HSI não melhorou a predição de AGB frente ao CH isolado, o que apoia modelos parcimoniosos e priorização do lidar para biomassa [p. 8].
- Serve: a saturação dos índices de vegetação acima de LAI ≈ 2 m²/m² é alerta metodológico para silvicultura de alta produtividade, onde o LAI tende a ser maior [p. 1, 5, 9].
- Não serve: o estudo não trata de silvicultura comercial, estoque de carbono, eucalipto ou Goiás; são 12 parcelas de restauração na Mata Atlântica com 13 anos, sem modelagem de carbono [p. 3, 8].

## 8. Frases citáveis (literais)

- "To our knowledge, this is the first study to use both lidar and HSI onboard a UAV to monitor tropical forest restoration (but see Vaglio Laurin et al., 2014 for a pioneer attempt in a mature tropical forest)." [p. 8]
- "UAV-lidar-HSI systems are still relatively expensive and potentially unaffordable by some decision-making organizations such as governments, NGOs, small landowners, and companies." [p. 10]
