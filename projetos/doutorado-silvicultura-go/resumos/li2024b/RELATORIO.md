# RELATÓRIO — Yiman Li (2024)

## 1. Referência

Li, Y.; Liu, X.; Liu, M.; Wu, L.; Zhu, L.; Huang, Z.; Xue, X.; Tian, L. (2024). *Historical Dynamic Mapping of Eucalyptus Plantations in Guangxi during 1990–2019 Based on Sliding-Time-Window Change Detection Using Dense Landsat Time-Series Data*. **Remote Sensing**, 16, 744. DOI: 10.3390/rs16050744 [p. 1]. O `TEXTO.txt` corresponde ao artigo do DOI indicado (21 páginas, íntegro).

## 2. Pergunta do estudo

Reconstruir a dinâmica histórica das plantações de eucalipto em Guangxi entre 1990 e 2019 — época de plantio, gerações e ciclos de rotação — a partir de séries temporais densas Landsat, usando um método de *sliding-time-window change detection* (STWCD) [p. 1].

## 3. Área e dados

- Local: província de Guangxi, China (20°54′–26°24′N, 104°28′–112°04′E), 14 cidades; área declarada de 236,7 km2 e 19 cenas Landsat WRS-2 sobrepostas [p. 4]. A área é apresentada assim no texto.
- Período: imagens de 1990 a 2021; produto final mapeado de 1990 a 2019 [p. 4, p. 10, p. 18].
- Sensores: Landsat 5 TM (1990–2011), Landsat 7 ETM+ (1999–2021) e Landsat 8 OLI (2013–2021), Collection 1 Level-2 SR, 30 m, revisita de 16 dias, processados no Google Earth Engine (GEE); bandas red e NIR e máscara CFMask [p. 5].
- Amostras: 749 pontos sorteados e interpretados visualmente, dos quais 250 pixels puros de eucalipto [p. 5]; validação com 494 ROIs de eucalipto (13.001 pixels) e 255 ROIs de não-eucalipto (15.612 pixels) [p. 12]; 103 pontos amostrais com 193 eventos de plantio [p. 12].

## 4. Método

1. NDVI mensal por pixel, com composição de máximo mensal, em vez de série anual, para preservar mudanças rápidas [p. 7].
2. Janela temporal deslizante de 3 anos (36 meses) com passo de 1 ano, gerando 30 subsequências sobrepostas entre janeiro de 1990 e dezembro de 2021 [p. 7–8].
3. LandTrendr aplicado a cada subsequência mensal de NDVI (parâmetros: `maxSegments` 8, `spikeThreshold` 0,9, `recoveryThreshold` 1,0, `pvalThreshold` 0,15, `minObservationsNeeded` 12) para achar pontos de corte e de crescimento [p. 10].
4. *Pattern matching* sobre a trajetória de referência: Mag ≥ 0,25, 3 ≤ Dur ≤ 17 meses, 20 ≤ Rate ≤ 200 e NDVI médio ≥ 0,7 no 1º e no 2º ano após o plantio; primeiro evento = 1ª geração, eventos seguintes = 2ª geração, intervalo entre plantios = ciclo de rotação [p. 11].

## 5. Resultados principais

- Acurácia global da identificação de eucalipto: 90,08% no resumo [p. 1] e OA = 90,87% na avaliação (PA 90,75%, UA 89,32%, matriz com 28.613 pixels) [p. 12]. Os dois valores diferem no próprio artigo.
- Anos de plantio estimados vs. observados: R2 = 0,98, RMSE = 0,68, diferença máxima de 2 anos; 6 erros de omissão e 2 de comissão [p. 12].
- Gerações até 2019: 1ª e 2ª somam 95% da área; áreas de 2.669.566 ha (75,79%), 698.564 ha (19,83%), 138.490 ha (3,93%) e 15.589 ha (0,44%) para 1ª, 2ª, 3ª e >4ª gerações [p. 14].
- Rotação predominante de 4 a 8 anos; média de 8 anos na 1ª rotação, 6,4 anos na 2ª e 5,5 anos na 3ª [p. 15–16].
- Área plantada crescente, com picos em 2011 e 2014; convergência com as áreas reportadas por Deng et al. entre 2013 e 2018; parte do aumento veio de conversão de lavoura [p. 15].
- Eventos mais recentes detectados em dois pontos de Gaofeng Forest: 2009 (P1) e 2018 (P2) [p. 13].

## 6. Limitações que os próprios autores reconhecem

- Dependência do NDVI de dois anos após a mudança impede captar os dois anos mais recentes de plantio, limitando a detecção a 2019 [p. 18].
- Nuvens e chuva frequentes reduzem observações ópticas de qualidade; o erro de PA é 6,47% maior que o de UA, indicando leve superestimação, com possibilidade de leve subestimação de área [p. 18].
- Métodos mais sensíveis poderiam identificar melhor distúrbios (vento, fogo, seca, pragas, corte), mas introduzir mais falsos pontos de mudança em florestas estáveis [p. 18].
- Erros de localização do ponto de mudança por ruído no ajuste linear podem gerar desvios de até 2 anos [p. 12].

## 7. O que serve ao projeto e o que não serve

- Serve: o esquema "janela deslizante + LandTrendr + pattern matching" em GEE para obter ano de plantio e idade do povoamento em séries Landsat densas — insumo direto para estratificar biomassa e estoque de carbono por idade [p. 18].
- Serve: os limiares e a lógica de separar gerações e ciclos de rotação (4–8 anos) são transferíveis a plantações de ciclo curto, com ajuste da janela ao ciclo da espécie [p. 17].
- Não serve: o artigo não estima biomassa nem carbono; trata apenas de identificação de eucalipto e de sua dinâmica temporal [p. 1, p. 18].
- Não serve: é monossensor (Landsat 30 m, sem SAR, Sentinel-2 ou LiDAR), específico para eucalipto em Guangxi, com validação por interpretação visual, e o produto termina em 2019 [p. 5, p. 18].

## 8. Frases citáveis (literais)

- "This study provides an effective approach for identifying eucalyptus plantation dynamics that can be applied to other short-rotation plantations." [p. 1]
- "The biomass of plantations is a crucial carbon pool within forest ecosystems, and the obtained age information of eucalyptus also provides vital support for estimating carbon stocks." [p. 18]
