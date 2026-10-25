# RELATÓRIO — Dubayah et al. (2022), GEDI

## 1. Referência

DUBAYAH, R.; ARMSTON, J.; HEALEY, S. P.; BRUENING, J. M.; PATTERSON, P. L.; KELLNER, J. R.; DUNCANSON, L.; SAARELA, S.; STÅHL, G.; YANG, Z.; TANG, H.; BLAIR, J. B.; FATOYINBO, L.; GOETZ, S.; HANCOCK, S.; HANSEN, M.; HOFTON, M.; HURTT, G.; LUTHCKE, S. **GEDI Launches a New Era of Biomass Inference from Space**. *Environmental Research Letters* (preprint em avaliação por pares) [p. 1]. Ano: 2022 (o texto registra "As of 2022" [p. 38]; ano de publicação não é declarado explicitamente). DOI: 10.1088/1748-9326/ac8694.

## 2. Pergunta do estudo

Quais são as estimativas de densidade e estoque de biomassa acima do solo — com incerteza estatisticamente formal — que dois anos e meio de observações do lidar GEDI permitem produzir para as terras tropicais e temperadas, em escalas de 1 km, de país e subnacional? [p. 2, p. 5]

## 3. Área e dados

- **Local:** superfície terrestre entre 51,6° N e 51,6° S (limite orbital da ISS); países inteiros ou majoritariamente nessa faixa, com exceções para China, Argentina e Chile, e exclusão do Alasca [p. 11, p. 16]; subnacional apenas para os EUA contíguos, em ~12.000 hexágonos de 640 km² (64.000 ha) [p. 5, p. 20].
- **Período:** 18 de abril de 2019 a 4 de agosto de 2021 (2,5 anos de observações) [p. 5, p. 6].
- **Sensores/fontes:** lidar GEDI a bordo da ISS — 3 lasers gerando 8 transectos, pegadas de 25 m de diâmetro, 60 m ao longo da órbita e 600 m entre transectos [p. 4, p. 38]; classificação PFT do MODIS MCD12Q1 v6 para estratificação [p. 39]; dados de campo e lidar aerotransportado para calibração [p. 5]; inventário FIA do USFS e FAO/FRA 2020 para validação [p. 10, p. 11].
- **Amostras:** mais de 5 bilhões de predições de biomassa por pegada [p. 5]; observações suficientes (≥2 trilhas) em 74,2% das células de 1 km [p. 14]; 338.451 parcelas FIA, ~28 por hexágono [p. 10]; ~20.000 pegadas GEDI por hexágono, podendo passar de 100.000 [p. 10]; 169 países com estimativa GEDI e FAO [p. 16]; base de calibração com 8.587 formas de onda simuladas em 21 países após controle de qualidade, de um total de 31.414 [p. 39]; 35 estratos de predição (PFT × região) [p. 39].

## 4. Método

1. Predição de AGBD por pegada com modelos lineares paramétricos, ajustados por combinação PFT × região do mundo, calibrados com o maior conjunto global de dados de campo e lidar aerotransportado já compilado [p. 5, p. 8].
2. As pegadas de alta qualidade são tratadas como amostra por conglomerados aleatoriamente alocada ao longo das trilhas dos lasers; filtros: flag de qualidade do L2A, sensibilidade do feixe >0,98 em EBT tropical e >0,95 nas demais, exclusão de geolocalização degradada e de nuvens/neblina [p. 6, p. 7].
3. Estimador híbrido model-based (Patterson et al.) para média e variância em células de 1 km, combinando incerteza de amostragem e de modelo (matriz de covariância dos parâmetros); agregação a partir de tiles de 6 km com pesos e termos de covariância por trilhas compartilhadas e modelos comuns (Eqs. 12–22) [p. 8, p. 9, p. 40–42].
4. Validação por comparação de médias: teste t de diferença de médias contra hexágonos FIA [p. 10] e comparação de AGB e AGBD por país com a FAO/FRA 2020, esta última convertida para toda a área terrestre [p. 11].

## 5. Resultados principais

- AGBD média de **108,9 Mg/ha** nas células de 1 km cujo PFT predominante é floresta; **126,7 Mg/ha** em floresta perenifólia de folha larga (EBT) e **9,5 Mg/ha** em campo/savana/mata (GSW); maior valor por PFT×região em EBT do Norte da Ásia, **167,6 Mg/ha** [p. 13].
- Média global de todas as terras: **35,89 Mg/ha** [p. 49], com mediana de 6 Mg/ha e média de 36 Mg/ha na distribuição por célula [p. 14]; floresta: média 109, mediana 80; EBT: média 127, mediana 97; GSW: média 9, mediana 2 [p. 14].
- Cobertura e precisão: **74,2%** das células de 1 km têm duas ou mais trilhas [p. 14]; **70,4%** de todas as células atendem ao requisito de erro padrão da missão [p. 15]; entre as células com observações suficientes, **77,3%** das de alta biomassa e **97,2%** das de baixa biomassa atendem, **94,8%** no conjunto [p. 15]; erro padrão médio de **15,2%** (alta biomassa, mediana 11,2%) e **3,4 Mg/ha** (baixa biomassa, mediana 1,0 Mg/ha) [p. 15]; exceção GSW com erro médio de **30,8%** [p. 16].
- Países: AGB total GEDI vs FAO com **r² = 0,86**, **RMSD = 3,2 Pg** e diferença média (FAO – GEDI) de **−0,63 Pg** [p. 16]; China e Indonésia com **27,7 Pg** e **23,3 Pg** a mais no GEDI [p. 16]; erro relativo de AGBD por país com média **7,7%** e mediana **3,9%** [p. 16]; nos **169** países com ambas as estimativas, GEDI soma **480,2 Pg** contra **373,1 Pg** da FAO, diferença de **107,1 Pg**, cerca de **29%** mais [p. 16]; AGBD por país com **R² = 0,57**, **RMSD = 47,7 Mg/ha** e GEDI maior em **126 de 169** países [p. 18]; erro padrão médio de AGBD de **3,4 Mg/ha**, com **7,3 Mg/ha** na Indonésia e **19,3 Mg/ha** em Papua-Nova Guiné [p. 19].
- EUA (hexágonos FIA): **r² = 0,81**, **RMSD = 28,3 Mg/ha**, inclinação **0,99** [p. 20]; GEDI com **52,6 Mg/ha** e **3,2 Tg** por hexágono contra **41,9 Mg/ha** e **2,6 Tg** do FIA [p. 20]; diferença média (FIA – GEDI) de **−0,64 Tg**, ou **24,3%** mais estoque no GEDI [p. 20]; **21%** dos hexágonos sem intervalo de confiança do FIA por AGBD zero [p. 22].
- Precisão: **95%** das células com as duas passagens exigidas atendem ao requisito da missão [p. 25]; erro padrão de **1,1%** para os EUA [p. 29]; área de estudo com cerca de **105 milhões** de células de 1 km sobre terra [p. 25]; GEDI estima **51 Pg** a mais, somados China e Indonésia [p. 27].

## 6. Limitações reconhecidas pelos autores

- A transferibilidade dos modelos de calibração é assumida; onde os dados de treino não representam a população, há viés não contabilizado pelo estimador [p. 8]; o conjunto de calibração é especialmente escasso na Ásia, provável fonte de viés [p. 27].
- O estimador híbrido de variância não considera o erro residual do modelo, assumido desprezível para áreas grandes (simulações indicam 1 km como suficiente) [p. 8].
- Assume-se que a amostra GEDI se comporta como conglomerados aleatórios; os estimadores não consideram probabilidades desiguais de inclusão, o que obriga a agregar a partir de 6 km [p. 8, p. 9]; a ressonância orbital de 2020 agravou a irregularidade da amostragem [p. 9, p. 29].
- Células com menos de duas trilhas não têm estimativa nem erro padrão; a meta de 80% das células não foi atingida por causa da mudança de altitude da ISS [p. 7, p. 25].
- Incerteza dos modelos alométricos de árvore não é incluída, o que pode tornar os erros padrão otimistas, sobretudo nos trópicos [p. 29].
- Artefatos de nuvens baixas e de declividade (acima de ~15°–20°) podem gerar métricas de altura espúrias e biomassa superestimada; a detecção de outliers é imperfeita [p. 28].
- As diferenças sistemáticas frente à FAO incluem a biomassa fora de floresta medida pelo GEDI e não pela FAO, além de filtragem incompleta de formas de onda anômalas, artefatos topográficos e má especificação de modelo [p. 16, p. 17, p. 26].

## 7. O que serve ao projeto e o que não serve

**Serve**
- O arcabouço de inferência híbrida (amostragem + modelo, com covariância dos parâmetros) é diretamente transponível para estimar biomassa e carbono com incerteza em Goiás, inclusive com amostras de lidar não contínuas [p. 8, p. 24].
- O GHMB (Generalized Hierarchical Model-Based inference), de dois níveis de modelo, é a base metodológica explícita para fusão multissensorial com dados wall-to-wall (TanDEM-X, NISAR, BIOMASS), com modelos calibrados localmente [p. 30].
- A estratificação PFT × região e os produtos L4A/L4B fornecem referência e classes de comparação para Cerrado e pastagens (GSW, média de 9,5 Mg/ha) [p. 13, p. 39].
- O desenho de validação — teste de diferença de médias e uso de intervalos de confiança para flagrar viés — é replicável com inventários florestais e parcelas de campo [p. 10, p. 28].

**Não serve**
- Escala e recorte: o estudo entrega células de 1 km, países e hexágonos dos EUA; não há Goiás, nem floresta plantada/silvicultura, e as classes de PFT não distinguem plantios [p. 5, p. 13, p. 39].
- Os mapas são feitos só com dados GEDI, sem fusão ou extrapolação espacial com outros sensores, e não são wall-to-wall [p. 24].
- Há lacunas de amostragem: 74,2% das células com ≥2 trilhas e nenhuma estimativa onde há só uma trilha, o que impede uso como camada contínua [p. 7, p. 14].
- As incertezas declaradas não incluem erro alométrico nem violações das premissas de inferência, e podem ser otimistas — cautela ao adotá-las como benchmark no projeto [p. 22, p. 29].

## 8. Duas frases citáveis (literais)

1. "Biomass density had a mean of 108.9 Mg/ha for 1 km cells whose predominant plant functional type (PFT) class was forest." [p. 13]
2. "Thus, the theory upon which GEDI’s estimation of uncertainty is built can be extended to sensor fusion." [p. 30]
