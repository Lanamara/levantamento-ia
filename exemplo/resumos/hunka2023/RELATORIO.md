# RELATORIO — Hunka et al. (2023)

## 1. Referência
HUNKA, Neha; SANTORO, Maurizio; ARMSTON, John; DUBAYAH, Ralph; McROBERTS, Ronald E.; NÆSSET, Erik; QUEGAN, Shaun; URBAZAEV, Mikhail; PASCUAL, Adrián; MAY, Paul B.; MINOR, David; LEITOLD, Veronika; BASAK, Paromita; LIANG, Mengyu; MELO, Joana; HEROLD, Martin; MÁLAGA, Natalia; WILSON, Sylvia; DURÁN MONTESINOS, Patricia; ARANA, Alexs; DE LA CRUZ PAIVA, Ricardo Ernesto; FERRAND, Jeremy; KEOKA, Somphavy; GUERRA-HERNÁNDEZ, Juan; DUNCANSON, Laura (2023). *On the NASA GEDI and ESA CCI biomass maps: aligning for uptake in the UNFCCC global stocktake*. **Environmental Research Letters**, v. 18, n. 12, 124042. DOI: 10.1088/1748-9326/ad0b60. Publicado em 23/11/2023 [p. 3].

## 2. Pergunta do estudo
Os dois mapas globais de densidade de biomassa aérea (AGBD) mais recentes — GEDI (NASA) e CCI 2020 v4 (ESA) — concordam entre si e com inventários florestais nacionais, e o que precisa ser alinhado para que sirvam ao relato nacional à UNFCCC? [p. 3, p. 5]

## 3. Área e dados
- **Local:** global, restrito à faixa de observação do GEDI (±~51,6° de latitude); as comparações com inventários cobrem México, Peru, Laos (Lao PDR) e 30 regiões/províncias da Espanha [p. 5, p. 7, p. 8].
- **Período:** produtos GEDI de 2019–2021; CCI referente a 2020 [p. 7]. Ciclos de inventário: México 3º ciclo (2015–2019), Peru em curso desde 2011, Espanha 4º ciclo (2008–2019), Laos 3º ciclo (2019) [p. 8].
- **Sensores/fontes:** GEDI L4B (LiDAR de forma de onda, células de 1 km × 1 km) e CCI 2020 v4 (LiDAR + SAR: ALOS-2, Sentinel-1, ICESat e ICESat-2; pixel de ~100 m no equador) [p. 7]. Referência de campo: inventários florestais nacionais (NFIs), mais SRTM para declividade [p. 8, p. 10].
- **Amostras:** México 9.955 parcelas; Peru 358; Espanha (30 regiões) 39.534; Laos 1.394 unidades secundárias de amostragem (SSUs) [p. 8]. Total comparado: 80 estratos florestais [p. 9]. Ecossistemas: 688 ecorregiões em 13 biomas [p. 6].

## 4. Método
1. Intercomparação dos mapas por ecorregião (TEOW) e por continente/bioma, com GLMs para testar diferenças sistemáticas [p. 6, p. 7].
2. Teste de sobreposição: fração de células de 1 km em que a média do CCI cai dentro do IC 95% do GEDI (média ± 1,96 × erro padrão) [p. 6].
3. Comparação com NFIs seguindo o CEOS Biomass Validation Protocol: média, EP e IC 95% por estrato florestal nacional [p. 8].
4. Inferência estatística por modelos de estimação de pequenas áreas Fay–Herriot (FH-SAE), que separam desvio sistemático de erro amostral; declividade (percentil 90 do SRTM a 1 km) testada como covariável [p. 8, p. 9, p. 10].

## 5. Resultados principais
- Diferenças entre CCI e GEDI, na média por ecorregião, ficam em geral entre **−50 e +25 Mg ha⁻¹** (percentis 10–90), com padrão geográfico [p. 9].
- Apenas **~13% das ecorregiões** apresentam diferença absoluta > **50 Mg ha⁻¹** [p. 13].
- CCI superestima sistematicamente em quase todos os biomas da América do Sul; subestima no leste/sudeste da Ásia (GLM, p < 0,05) [p. 9].
- Sobreposição CCI × IC 95% GEDI: até **50% das células** em algumas ecorregiões tropicais da América do Sul e Sudeste Asiático; só **~20%** nas terras baixas congolesas [p. 9].
- Contra os NFIs, **47 dos 80 estratos** (mais da metade) tiveram um ou ambos os produtos dentro do IC 95% do inventário; nenhuma sub ou superestimativa significativa no conjunto (p > 0,05, modelos nulos) [p. 9].
- Modelo nulo GEDI−NFI: intercepto **0,36** (EP 5,81; p = 0,95); CCI−NFI: intercepto **9,33** (EP 5,2; p = 0,08) [p. 12].
- Declividade explica os desvios: com o percentil 90 de declividade, **R² = 0,95** (GEDI, β = 3,15; p = 4,34 × 10⁻⁸) e **R² = 0,73** (CCI, β = 2,34; p = 1,06 × 10⁻⁴) [p. 12].
- Espanha: diferença média por estrato de **~12 Mg ha⁻¹** para o GEDI e **~22 Mg ha⁻¹** para o CCI [p. 12].
- Contexto político: de **75** submissões à UNFCCC, apenas **5%** dos países usam mapas de AGBD, e versões de uma década atrás [p. 4].

## 6. Limitações reconhecidas pelos autores
- Os enquadramentos de incerteza dos dois produtos não são comparáveis; o CCI é tratado como estimativa pontual, sem IC, porque a variância dos dados de treinamento não é contabilizada [p. 6, p. 7, p. 11].
- Como relatórios de NFI (sem os dados de parcela) alimentaram os modelos do CCI, o exercício **não é validação independente** dos mapas [p. 8, p. 11].
- O GEDI superestima AGBD em estratos montanhosos, por erros de forma de onda em relevo complexo (subestimativa da elevação do solo / superestimativa da altura do dossel) [p. 10].
- Estratificação global grosseira: florestas de montanha do Peru e florestas decíduas do Laos foram tratadas com modelos de folhosas perenes (EBT), inadequados [p. 11].
- Falta de dados de treinamento representativos e de referência independente em muitas regiões; por isso recomendam calibração local antes do uso operacional [p. 12].
- Não é possível concluir se os produtos podem ser fundidos num único mapa ("biomass harmonized"), justamente pela dissimilaridade das incertezas [p. 11].

## 7. O que serve ao projeto e o que não serve
- **Serve:** o desenho de comparação produto × inventário por estrato, com FH-SAE separando viés sistemático de erro amostral — replicável para talhões/estratos de silvicultura em Goiás [p. 8, p. 9].
- **Serve:** a evidência de que falta treinamento em **florestas plantadas** nos modelos GEDI L4A, o que explica parte dos desvios na Espanha (eucalipto e pinus sob manejo) [p. 12] — alerta direto para silvicultura goiana.
- **Serve:** a discussão de erro por declividade e de métricas de altura (RH98, RH50) como diagnóstico de viés em terreno complexo [p. 10, p. 11].
- **Não serve:** não há carbono (só AGBD, sem fração de carbono, raízes ou estoque total), nem calibração local para Cerrado/Goiás, nem sensores multissensoriais de altíssima resolução; o enquadramento é diplomático (GST/UNFCCC), não silvicultural [p. 3, p. 13].

## 8. Frases citáveis
> "The lack of consistency amongst AGBD maps is a cause of confusion, and hinders objective comparisons and uptake of maps" [p. 4]

> "In over half the forest strata (47 of 80), either one or both products are accurate, i.e. they overlap the 95% CIs of NFI-estimated AGBD" [p. 9]
