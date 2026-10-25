# Relatório de leitura — Quegan et al. (2019)

*As páginas entre colchetes seguem as marcas `[página N]` do arquivo TEXTO.txt (não a paginação da revista, 44–60).*

## 1. Referência

Quegan, S.; Le Toan, T.; Chave, J.; Dall, J.; Exbrayat, J.-F.; Ho Tong Minh, D.; Lomas, M.; Mariotti D'Alessandro, M.; Paillou, P.; Papathanassiou, K.; Rocca, F.; Saatchi, S.; Scipal, K.; Shugart, H.; Smallman, T. L.; Soja, M. J.; Tebaldini, S.; Ulander, L.; Villard, L.; Williams, M. (2019). **The European Space Agency BIOMASS mission: measuring forest above-ground biomass from space.** *Remote Sensing of Environment*, 227, 44–60. DOI: 10.1016/j.rse.2019.03.032 [p. 1]

## 2. Pergunta do estudo

Como medir do espaço, globalmente e com precisão suficiente, a biomassa acima do solo (AGB) e a altura das florestas — e suas mudanças — para reduzir as grandes incertezas nos cálculos de estoques e fluxos de carbono da biosfera terrestre? [p. 5]

## 3. Área e dados

- **Local:** sem sítio único; a missão tem alvo global, cobrindo florestas entre 75° N e 56° S [p. 13]. Os dados usados para desenvolver os algoritmos vêm de campanhas aéreas na Guiana Francesa (Paracou, Nouragues), Indonésia (Sungai-Wai, Mawas, Bornéu), Suécia (Remningstorp, Krycklan), Gabão (Lopé, Mondah, Mabounie, Rabi, Pongara), Gana (Ankasa) e Costa Rica (La Selva), além de um sítio desértico na Tunísia (Ksar Ghilane) [p. 20–22, 40–41]. Nenhum sítio no Brasil ou em Goiás.
- **Período:** campanhas entre novembro de 2004 (Indrex-2) e fevereiro de 2017 (Pongara); torres de medição contínua de 2011 a 2016 (Tropiscat, Afriscat) e a partir de dezembro de 2016 (Borealscat); imagens PALSAR-2 de 8/8/2014 e 8/8/2015 [p. 20–22, 34]. Missão prevista para lançamento em 2022, com 5 anos de operação [p. 5, 18].
- **Sensores/fontes:** SAR aerotransportado em banda P (E-SAR e F-SAR, DLR; SETHI, ONERA), AIRSAR da NASA, escaterômetros de torre em banda P, PALSAR-2 (banda L), lidar aerotransportado e parcelas de campo [p. 19–22].
- **Número de amostras:** não informado. O texto cita "six major ESA airborne campaigns" [p. 19–20], regiões de interesse de 200 m × 200 m (Fig. 3) [p. 27] e parcelas de 1 ha (Fig. 4) [p. 28], mas não dá o total de parcelas ou de pontos.

## 4. Método

1. **Sensor:** SAR de abertura sintética totalmente polarimétrico em banda P (435 MHz, 6 MHz de banda), com antena refletor de 12 m, resolução azimutal de ~7,9 m e ~50 m após 6 looks [p. 16–17].
2. **Três técnicas combinadas:** polarimetria (PolSAR), interferometria polarimétrica (Pol-InSAR) e tomografia SAR (TomoSAR), usadas para estimar AGB e altura [p. 17].
3. **Fase tomográfica e fase interferométrica:** 7 passagens com 3 dias de separação e linha de base de 15% da crítica (0,823 km), 18 dias por subfaixa e 60 dias para a faixa completa, repetida 6 + 1/3 vezes (425 dias); depois, ciclos de 3 passagens e 228 dias, com cobertura global a cada 7 meses [p. 18].
4. **Recuperação da AGB e da altura:** cancelamento do solo (superfície + duplo rebatimento) para isolar o espalhamento volumétrico e inversão não linear de um modelo de espalhamento (eqs. 3–5) [p. 24–26]; altura por inversão do modelo RVoG com três aquisições polarimétricas [p. 30]; distúrbio por teste de razão de verossimilhança sobre a matriz de covariância polarimétrica de 6 looks [p. 32].

## 5. Resultados principais

- Produtos: AGB e altura em grade de 200 m × 200 m (4 ha) e distúrbio severo em ~50 m × 50 m [p. 5, 14].
- Exigência de acurácia: RMSE menor que AGB/5 quando AGB > 50 t/ha e de 10 t/ha ou melhor quando AGB < 50 t/ha; altura com RMSE < 30% para árvores acima de 10 m [p. 14].
- Cobertura global leva 425 dias na fase tomográfica e 228 dias por ciclo na fase interferométrica [p. 15].
- Órbita: 671,9 km de altitude, inclinação de 98°, três subfaixas de 54,32, 54,41 e 46,06 km, ângulos de incidência de 23° a 33,9° [p. 17–18].
- Validação do esquema de inversão em AfriSAR (La Lopé, Gabão): r = 0,97, RMSE de 41 t/ha, ou 16% da biomassa média [p. 27].
- Tomografia a 30 m de altura no TropiSAR: sensibilidade de ~50 t/ha por dB e coeficiente de correlação de ~0,84 em escala de 1 ha [p. 28].
- Entre 20 m e 40 m de altura concentram-se ~35% a 40% da AGB total em florestas tropicais densas [p. 28].
- Regressões em floresta boreal: RMSE relativo de 27% (35 t/ha) em Krycklan e 22% (40 t/ha) em Remningstorp; a mudança de AGB foi estimada com RMSE de 20 t/ha, cerca de metade do erro das estimativas individuais [p. 24].
- Em floresta tropical da Guiana Francesa, a AGB foi estimada por regressão polarimétrica com RMSE relativo < 20% [p. 24].
- Distúrbio: o σ⁰ HV cai 5 dB quando a AGB vai de 500 t/ha a quase zero, mas muda só ~1 dB entre 100 e 200 t/ha; detecção a 99% de significância implica ~1% de falsos alarmes [p. 33].
- Ganho no ciclo de carbono: assimilar um mapa pan-tropical de biomassa reduziu em 49,5 ± 29,2% o intervalo de confiança de 95% do tempo de residência do carbono vegetal no sistema CARDAMOM [p. 37].
- Contexto das incertezas: a absorção terrestre (Uland) é 3,0 GtC/ano com incerteza de 0,8 GtC/ano (26%), e o fluxo de mudança de uso da terra é 1,3 GtC/ano com incerteza de 0,7 GtC/ano (54%) [p. 7–8].
- Saturação da banda L em torno de 100 t/ha; a banda P é apresentada como necessária para florestas densas [p. 10].

## 6. Limitações reconhecidas pelos autores

- Restrições do sistema de rastreio de objetos espaciais (SOTR) excluem América do Norte e Europa e limitam a cobertura a 75° N–56° S [p. 13].
- A biomassa subterrânea não pode ser medida pela missão nem por qualquer sensor remoto; só é inferida por alometria [p. 15].
- Em florestas boreais e temperadas o valor da tomografia "is less clear" e "the preferred algorithm for BIOMASS in these cases is still not fixed" [p. 29].
- O algoritmo de inversão precisa ser insensível a mudanças ambientais; no inverno boreal o backscatter cai e a estação "will most likely not be useful for biomass estimation" [p. 19].
- Há poucas parcelas permanentes de qualidade nos trópicos, a escala das parcelas (1 ha ou menos) não coincide com o pixel de 4 ha e as coordenadas são imprecisas [p. 34–35]; para zonas temperada e boreal "concrete plans to gather in situ data in these regions are not currently in place" [p. 35].
- A banda de 6 MHz limita as linhas de base e a resolução espacial, e a baixa frequência reduz a sensibilidade à altura em florestas esparsas [p. 31].
- A tomografia só existe na primeira fase da missão [p. 28]; as variações temporais e espaciais dos coeficientes de calibração `a` e `b` são desconhecidas [p. 27].
- No produto de distúrbio, não se sabe o quanto efeitos ambientais (umidade do solo) elevam a taxa de falsos alarmes, e é necessário um mapa florestal inicial acurado [p. 32–33].
- Cintilação ionosférica em altas latitudes pode corromper mapas de velocidade de gelo; a avaliação só será possível com o satélite em órbita [p. 42].

## 7. O que serve ao projeto e o que não serve

**Serve**

- Referência central para justificar banda P, Pol-InSAR e TomoSAR na estimativa de AGB em florestas densas, com metas quantitativas de erro (AGB/5; 10 t/ha; 30% na altura) que podem ser usadas como benchmark [p. 14].
- Desempenho reportado serve de expectativa realista para fusão multissensorial: 41 t/ha (16%) e r = 0,97 com dados aéreos filtrados a 6 MHz [p. 27], e ~50 t/ha por dB na camada de 30 m [p. 28].
- A lógica de cancelamento do solo + inversão física e a validação com parcelas de campo mais lidar agregado a 4 ha são diretamente transferíveis para talhões de silvicultura em Goiás [p. 26–27, 35–36].
- A ênfase em distúrbio/degradação e no uso da biomassa em modelos de carbono (tempo de residência, CARDAMOM) dialoga com a parte de estoque de carbono do projeto [p. 32, 36–37].

**Não serve**

- Não há nenhum dado de Goiás, do Cerrado ou de floresta plantada (eucalipto/pinus); os sítios são florestas naturais tropicais, boreais, temperadas e savana africana [p. 20–22].
- É um artigo de descrição de missão, sem delineamento amostral próprio: não informa número de amostras nem apresenta validação estatística de campo que o projeto possa reaproveitar [p. 20–22, 27].
- Os dados orbitais em banda P só existirão após o lançamento em 2022; para o projeto, a banda P disponível é apenas aerotransportada e fora do Brasil [p. 5, 19].
- Não traz equações alométricas nem relações altura–biomassa para espécies plantadas; a allometria citada é pan-tropical (Chave et al. 2014) [p. 35].

## 8. Duas frases citáveis

> "The estimates are highly correlated with the reference data (r = 0.97), exhibit only a small amount of bias across the whole biomass range, and give a RMSE of 41 t/ha (16% of the average biomass)." [p. 27]

> "L-band radar offers access to biomass values up to around 100 t/ha before losing sensitivity (e.g. Mitchard et al., 2009)." [p. 10]
