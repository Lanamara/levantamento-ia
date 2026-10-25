# RELATÓRIO — Carneiro et al. (2020)

## 1. Referência

CARNEIRO, Gustavo Fluminense; FERREIRA, Matheus Pinheiro; VOLOTÃO, Carlos Frederico de Sá. **Multi-source remote sensing data improves the classification accuracy of natural forests and eucalyptus plantations** (Dados de sensoriamento remoto de múltiplas fontes eleva a exatidão de classificação de florestas naturais e plantadas). *Revista Brasileira de Cartografia*, v. 72, n. 1, p. 110–125, 2020. DOI: 10.14393/rbcv72n1-50477. Instituto Militar de Engenharia (IME), Rio de Janeiro [p. 1].

## 2. Pergunta do estudo

Combinar dados de sensoriamento remoto de múltiplas fontes (óptico Landsat-8 + radar Sentinel-1 + SRTM) aumenta a exatidão de classificação e a separabilidade espectral entre floresta natural e plantio de eucalipto? [p. 2]

## 3. Área e dados

- **Local:** estado do Espírito Santo, 46.074,44 km²; clima tropical úmido, precipitação anual de 1.045 a 1.375 mm e temperatura média de 17,9 ºC a 25 ºC [p. 3].
- **Período:** ano de 2017 (1º de janeiro a 31 de dezembro) [p. 4].
- **Sensores/fontes:** Landsat-8/OLI — 137 cenas, 6 bandas (B, G, R, NIR, SWIR1, SWIR2), 30 m, reflectância TOA, coleção Tier 1 [p. 4]; Sentinel-1/C-SAR — 175 imagens, modo IW, polarizações VV e VH, GRD, 10 m [p. 4]; SRTM V3 (SRTM Plus), 1 arco-segundo (~30 m), usado para declividade [p. 4]; NDVI e 4 bandas de textura GLCM (energia, contraste, correlação, entropia) calculadas sobre a banda NIR do Landsat-8 [p. 6–7].
- **Apoio:** SOS Mata Atlântica (classe floresta natural), MapBiomas Coleção v3.1 (plantada, pastagem, agricultura) e imagens de alta resolução do Google Earth Pro; todo o processamento no Google Earth Engine [p. 4–5, 7].
- **Amostras:** 400 polígonos, 100 por classe, totalizando **410.251 pixels** — floresta natural 245.353, floresta plantada 79.285, pastagem 45.659, agricultura 39.954 [p. 8]. Conjunto final com 14 atributos [p. 8].

## 4. Método

1. **Pré-processamento no GEE:** filtros geométrico, temporal e de qualidade de pixel (só "CLEAR TERRAIN"); composição pela mediana de 2017 para Landsat-8 e Sentinel-1; recorte pelo limite do ES; NDVI (Eq. 1), texturas GLCM sobre a NIR e declividade via `ee.Terrain.slope` [p. 5–6].
2. **Coleta de amostras:** vetorização manual de 400 polígonos sobre imagens de alta resolução de 2017 no Google Earth, usando SOS Mata Atlântica e MapBiomas como referência, com posterior verificação na imagem Landsat-8 de 2017 [p. 7–8].
3. **Classificação:** Random Forest com 500 árvores, mtry = raiz do número de variáveis, normalização [0–1], 60% treino / 40% teste e limite de 5.000 amostras de treino por classe; 10 modelos de dados (combinações de bandas), repetidos 100 vezes com troca das amostras e respeito à identidade dos polígonos (treino e teste de polígonos distintos) [p. 8–9].
4. **Avaliação:** F1-score, exatidão global e desacordo total; importância de variáveis por OOB no pacote `randomForest` do R; distância de Jeffries–Matusita (JM, Eqs. 2–3) calculada no ENVI 5.5 para todas as combinações par a par de classes [p. 9–10].

## 5. Resultados principais

- **Modelo 1 (só Landsat-8):** exatidão global 88,29%, desacordo total 11,71%; F1 de 93,43% (floresta natural), 85,48% (plantada), 82,48% (pastagem) e 69,18% (agricultura) [p. 10].
- **Modelo 5 (Landsat-8 + VV + VH):** exatidão global 91,29%, desacordo total 8,71%; F1 de 95,65%, 88,38%, 86,19% e 77,19% para NF, PF, P e A [p. 10].
- **Ganho do radar:** +3,0% de exatidão global e queda do desacordo total de 11,71% para 8,71% [p. 10, 13]; F1 melhorou 2,22% (NF), 2,9% (PF), 3,71% (P) e 8,01% (A) [p. 10].
- **Modelo 9 (Landsat-8 + VV + VH + energia):** exatidão global 91,31% e desacordo total 8,69%, o melhor resultado, praticamente empatado com o modelo 5 [p. 11].
- **Textura e NDVI não ajudaram:** modelo 2 (com NDVI) caiu para 88,19% de exatidão global e 11,81% de desacordo [p. 10]; modelos com contraste (89,45%/10,55%), correlação (89,75%/10,25%) e entropia (89,64%/10,36%) ficaram abaixo do modelo 5 [p. 11].
- **Matriz de confusão:** o erro de pixels de floresta natural classificados como plantada caiu 2,3%; a taxa de agricultura classificada como pastagem caiu 5% com a inclusão do Sentinel-1 [p. 11].
- **Separabilidade (JM):** ganho de 11,98% entre floresta natural e plantada e de 45,12% entre agricultura e pastagem [p. 12].
- **Importância de variáveis:** NIR, VV e VH foram os atributos mais importantes [p. 11–12].
- **Atenção — inconsistência interna:** a conclusão afirma aumento da exatidão global "de 89,29% para 91,29%" [p. 13], mas a Tabela 6 registra 88,29% para o modelo 1 [p. 10]; o valor 89,29% não aparece na tabela.

## 6. Limitações reconhecidas pelos autores

- **Ausência de dados de campo:** "no field data was not available" — os polígonos foram definidos sobre imagens de alta resolução do Google Earth Pro e validados apenas por referências de mapeamento (SOS Mata Atlântica, MapBiomas) [p. 5, 7].
- **Textura GLCM sem ganho, atribuída à resolução espacial:** acredita-se que os 30 m do Landsat-8 tenham sido o obstáculo principal; imagens de maior resolução espacial provavelmente dariam melhores resultados com bandas de textura [p. 12].
- **Dificuldade de separar vegetações espectroscopicamente semelhantes:** reconhecida explicitamente, com expectativa de melhora apenas com imagens de melhor resolução espacial e espectral [p. 12].
- **Escopo temporal:** análise restrita a um único ano (2017) — o texto não trata isso como limitação, mas é o recorte efetivo dos dados [p. 4].

## 7. O que serve ao projeto e o que não serve

- **Serve — desenho metodológico replicável:** fusão óptico + SAR (Landsat-8 e Sentinel-1) com Random Forest, 10 modelos de bandas, 100 repetições com separação de polígonos entre treino e teste e avaliação por exatidão global, desacordo total, F1 e JM — arcabouço diretamente transferível para a silvicultura em Goiás [p. 8–10].
- **Serve — evidência quantitativa do ganho do radar na confusão floresta natural × plantada:** F1 da classe plantada +2,9% e JM +11,98% [p. 10, 12], exatamente o par crítico do projeto.
- **Serve — economia de esforço:** NDVI e texturas GLCM em resolução de 30 m não agregaram (ou pioraram) o resultado [p. 10–12], o que desaconselha repetir essas variáveis no mesmo nível de resolução.
- **Não serve — não trata de biomassa nem de carbono:** o artigo é classificação de uso/cobertura (4 classes) e não estima biomassa, estoque de carbono ou qualquer variável biofísica; também não é em Goiás (ES, Mata Atlântica) e não usa dados de campo [p. 1, 5, 8].

## 8. Frases citáveis (literais)

> "Combining Landsat-8 and Sentinel-1 was effective for improving the classification accuracy of natural forests and tree plantations, increasing the Overall Accuracy from 89.29% to 91.29% and decreasing the Total Disagreement from 11.71% to 8.71%." [p. 13]

> "The computation of GLCM bands did not improve the classification results (Table 6). It is believed that the spatial resolution of Landsat-8 (30 m) may have been a key obstacle." [p. 12]
