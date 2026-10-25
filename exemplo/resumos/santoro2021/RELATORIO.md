# Relatório — Santoro et al. (2021)

## 1. Referência

SANTORO, M.; CARTUS, O.; CARVALHAIS, N.; ROZENDAAL, D. M. A.; AVITABILE, V.; ARAZA, A.; DE BRUIN, S.; HEROLD, M.; QUEGAN, S.; RODRÍGUEZ-VEIGA, P.; BALZTER, H. *et al.* **The global forest above-ground biomass pool for 2010 estimated from high-resolution satellite observations.** *Earth System Science Data*, v. 13, p. 3927–3950, 2021. DOI: 10.5194/essd-13-3927-2021. [p. 1]

## 2. Pergunta do estudo

Gerar um mapa global de biomassa acima do solo (AGB) de florestas para ~2010, em resolução de 1 ha, a partir de observações de radar, lidar e óptico, e avaliar sua validade e magnitude frente a inventários de campo e às estatísticas do FRA/FAO. [p. 3]

## 3. Área e dados

- **Local:** global (todos os continentes, com análise separada por continente, país e ecozona da FAO); nenhum sítio no Brasil além de um exemplo ilustrativo no Pará (Figs. 3–4). [p. 9]
- **Período:** observações em torno de 2010 — mosaicos ALOS PALSAR de 2007–2010 (usado o de 2010), Envisat ASAR de 2010–2011, reflectâncias Landsat 7 de 2010, ICESat GLAS de 2003–2009; máscara florestal CCI-LC de 2010. [p. 3–4, 8]
- **Sensores/fontes:** ALOS PALSAR banda L (HH e HV, 20 m; 14 728 tiles) [p. 3–4]; Envisat ASAR banda C (30–1000 m, ~80 % em modo GMM, 1 km final) [p. 4]; ICESat GLAS GLA14 (26,5 milhões de footprints, ~65 m) [p. 4]; Landsat 7 bandas 3, 4, 5 e 7 (~30 m) [p. 4]; CCI-LC e ecozonas FAO para estratificação. [p. 8]
- **Amostras:** 110 897 parcelas de inventário florestal de campo para validação [p. 7]; 6 456 células de 0,1° com ao menos 5 parcelas (~1 % da cobertura florestal global) [p. 9]; ~1 600 unidades de manejo florestal na Rússia [p. 8]; 233 relatórios nacionais do FRA, dos quais 171 com AGB. [p. 5, 13]

## 4. Método

1. Estimativa do volume de madeira em pé (GSV) por inversão do *Water Cloud Model* com o algoritmo BIOMASAR, aplicado separadamente ao ASAR/C (1 km, multitemporal) e ao PALSAR/L (25 m). [p. 5–6]
2. Reescala da estimativa C para 25 m por regressão linear múltipla (σ⁰HH, σ⁰HV e bandas 3, 4, 5 e 7 do Landsat), calibrada por tile de 1° × 1°, com correção de viés na retransformação logarítmica. [p. 6]
3. Combinação ponderada das estimativas C+ e L (pesos por sensibilidade da banda, nº de observações, erros de treino e efeito topográfico), seguida de média espacial em janela 4 × 4 para reduzir speckle → pixel de ~1 ha. [p. 6]
4. Conversão GSV → AGB por densidade da madeira (WD, predita por aprendizado de máquina) e fator de expansão de biomassa (BEF, potência generalizada de Thurner et al., 2014); incerteza por propagação de erros e validação contra parcelas agregadas a 0,1°. [p. 6–8]

## 5. Resultados principais

- AGB total global de **522 Pg** para área florestal de **4 833,4 milhões de ha**, média de **108 Mg ha⁻¹** (Tabela 2) [p. 12]; na Tabela 1, por ecozona, **521,0 Pg** para **4 825,4 milhões de ha**, também 108 Mg ha⁻¹ [p. 11]; o texto de resultados cita **521 Pg** e **4 825 milhões de ha** [p. 9].
- Estoques de carbono acima do solo de **246 Pg C**, com fração de carbono de 0,47 [p. 9].
- Maior valor previsto: **757 Mg ha⁻¹** (GSV de 1 087 m³ ha⁻¹) no noroeste do Pacífico dos EUA; **99 %** das florestas abaixo de **360 Mg ha⁻¹** e **90 %** abaixo de **182 Mg ha⁻¹** [p. 8].
- Desvio-padrão da AGB em média **50 %**, com intervalo interquartil de **44 % a 61 %**; abaixo de 100 % em ~**95 %** dos pixels mapeados [p. 9].
- Validação: nas 6 456 células de 0,1°, inventário variou de **0 a 1 670 Mg ha⁻¹** (mediana 43; média 60; percentil 99 de 351) e o mapa de **0 a 358 Mg ha⁻¹** (mediana 57; média 67; percentil 99 de 278); concordância de tendência até ~**250 Mg ha⁻¹**, com subestimação acima disso [p. 9].
- Por ecozona: tropical **331,3 Pg**, **2 251,7 milhões de ha**, **147 Mg ha⁻¹** (64 % da AGB total e 47 % da área); temperada **71,6 Pg** e **102 Mg ha⁻¹**; boreal **81,2 Pg** e **60 Mg ha⁻¹**; subtropical **36,2 Pg** e **75 Mg ha⁻¹**; polar **0,6 Pg** e **18 Mg ha⁻¹** [p. 9, Tabela 1 p. 11].
- Floresta tropical úmida (TAr) com mediana de AGB de **238 Mg ha⁻¹** [p. 10]; desvio-padrão relativo mediano entre **44 % e 57 %** na maioria das ecozonas, chegando a **69 %** (TBSh), **92 %** (TBWh) e **84 %** (polar) [p. 11].
- Comparação com o FRA 2010: **522 Pg vs. 468 Pg (+11 %)**, área do CCI-LC **23 % maior**, mas AGB média do FRA **9 % maior** (119 vs. 108 Mg ha⁻¹) [p. 13]; total do FRA de 468,5 Pg em 3 926,1 milhões de ha [p. 12].
- Por continente: América do Sul **155,9 Pg** e **183 Mg ha⁻¹**; África **84,8 Pg** e **108 Mg ha⁻¹** (−24 % vs. FRA); Ásia **89,4 Pg** e **115 Mg ha⁻¹** (+17 %); Europa e Rússia **91,2 Pg** e **72 Mg ha⁻¹**; América do Norte e Central **77,9 Pg** e **80 Mg ha⁻¹**; Oceania **23,3 Pg** e **129 Mg ha⁻¹** [p. 12, Tabela 2].
- Concordância com o FRA por país aumenta com a capacidade do inventário nacional: correlação de **0,46 a 0,91**, RMSD relativo de **30 % a 74 %** e diferença média de **−42 % a −12 %** [p. 16]; diferença mediana de **−60 %** na África (51 países), **−8 %** na Europa (42) e **+2 %** na América do Sul (9) [p. 16].
- Reavaliação de mapas anteriores: vieses de até **120 %** do valor de inventário em florestas tropicais secas, subtrópicos e zona temperada [p. 2].
- Ampliando para classes não florestais, o pool terrestre de AGB lenhosa chega a **600 Pg**, equivalentes a ~**282 Pg C** [p. 20].

## 6. Limitações reconhecidas pelos autores

- A validação não indica a validade das estimativas por pixel, mas apenas a acurácia dos padrões espaciais generalizados [p. 8].
- Base de validação é oportunística, com distribuição desigual, tamanhos de parcela variados e equações alométricas distintas; a maioria das parcelas é menor que 1 ha [p. 7].
- Em florestas tropicais densas a estimativa dependeu de **uma única observação** de radar em banda L, e a banda C não resolve AGB acima de ~150 Mg ha⁻¹ (variação de retroespalhamento < 0,3 dB), gerando viés e valores no limite inferior das estimativas globais [p. 20].
- O treinamento forçado à relação média entre retroespalhamento e biomassa causa superestimação em AGB baixa e subestimação em AGB alta [p. 19].
- Modelagem imperfeita do retroespalhamento do PALSAR em terreno inclinado gera viés adicional [p. 20].
- Em regiões pouco amostradas, como savanas, as estimativas podem ser limitadas pelas observações usadas para WD e BEF; não foi possível quantificar o impacto de vieses locais de BCEF [p. 20].
- O conjunto pode não ser acurado o suficiente para um país usar como base única de reporte de biomassa e carbono [p. 20].
- Ausência de estimativas de AGB nas ilhas do Pacífico ocidental, com efeito considerado negligenciável no total [p. 20].

## 7. O que serve ao projeto e o que não serve

- **Serve:** a arquitetura metodológica completa — estimar GSV por inversão física (Water Cloud/BIOMASAR) e converter para AGB com WD e BEF — é diretamente transferível para povoamentos de silvicultura em Goiás. [p. 5–6]
- **Serve:** o protocolo de validação (agregação de mapa e parcelas a células de 0,1°, RMSD relativo e viés, estratificação por ecozona/região) e a propagação formal de incerteza servem de modelo para o desenho amostral do projeto. [p. 6–8]
- **Serve:** como referência de teto de desempenho e de limitação física — saturação da banda C e dependência de uma só observação L, com incerteza relativa média de 50 % em 1 ha — o que sustenta o argumento por sensoriamento multissensorial (lidar, P-band, multitemporal) na silvicultura. [p. 9, 20]
- **Não serve:** não há dado, análise ou discussão sobre Goiás, Cerrado antropizado ou florestas plantadas; a máscara CCI-LC restringe o produto a cobertura florestal, e a época é 2010, anterior à série GEDI/Sentinel-1/2 usada hoje; os vieses regionais documentados desaconselham usar o produto como verdade de referência local. [p. 8, 20]

## 8. Frases citáveis (literais)

> "With a total global AGB of 522 Pg, our estimate of the terrestrial biomass pool in forests is lower than most estimates published in the literature (426–571 Pg)." [p. 2]

> "This effectively led to use of a single radar observation to estimate biomass in dense tropical forests, causing our values to be at the low end of the range of estimates of the terrestrial AGB pool (Table 3 and Table S1 in the Supplement)." [p. 20]
