# RELATÓRIO — Xiao-Qi Lin (2023)

## 1. Referência

Lin, X.; Ren, C.; Li, Y.; Yue, W.; Liang, J.; Yin, A. (2023). "Eucalyptus Plantation Area Extraction Based on SLPSO-RFE Feature Selection and Multi-Temporal Sentinel-1/2 Data". *Forests*, 14(9), 1864. DOI: 10.3390/f14091864.

O `TEXTO.txt` está completo (26 páginas, incluindo referências) e corresponde ao artigo do DOI; ele traz, porém, blocos duplicados da versão de revisão por pares, com o mesmo conteúdo repetido em sequência.

## 2. Pergunta do estudo

Verificar se a fusão de dados multitemporais Sentinel-1/2 com seleção de atributos por SLPSO-RFE eleva a acurácia da extração de áreas de plantio de eucalipto em comparação com dados de uma única estação e com o esquema ReliefF-RFE.

## 3. Área e dados

- Local: condado de Luzhai, cidade de Liuzhou, região autônoma de Guangxi (China), 2.974,8 km², entre ~24°14′–24°50′ N e ~109°28′–110°12′ E [p. 3–4].
- Período: verão (junho a agosto de 2020) e inverno (dezembro de 2020 a fevereiro de 2021) [p. 5].
- Sensores: Sentinel-1 GRD nas polarizações VV e VH (10 m) e Sentinel-2; quatro composições medianas sazonais fundidas por *stacking* em uma imagem de 28 bandas [p. 5]. Verificação com UAV Phantom 4 RTK, 0,05 m [p. 14].
- Amostras: 400 de treinamento (180 de eucalipto, 130 de vegetação não-eucalipto, 90 de não-vegetação) e 300 de teste [p. 6].

## 4. Método

- Construção do conjunto de atributos: bandas multiespectrais, 5 índices de vegetação, 6 índices de *red-edge* e texturas GLCM derivadas do SAR; cálculo de pesos por ReliefF e descarte dos 10% de menor peso [p. 6, p. 12].
- Seleção final por SLPSO-RFE: o SLPSO busca o classificador e os hiperparâmetros do RFE, com 200 partículas e 20 iterações; melhor modelo RF com 365 árvores, `n_features_to_select` = 12, `step` = 5, `cv` = 6 [p. 10].
- Segmentação orientada a objetos por SNIC (size 5, compactness 0, connectivity 8, neighborhood 256, seed nulo) sobre as 56 bandas do subconjunto ótimo [p. 12].
- Classificação por RF, CART e SVM em nove cenários (dados de uma estação ou multitemporais × ReliefF-RFE ou SLPSO-RFE × três classificadores), avaliados por matriz de confusão (OA, Kappa, F1, PA, UA) e por imagens de UAV [p. 13–14, p. 18].

## 5. Resultados principais

- Subconjunto ótimo com 56 atributos; *red-edge* e texturas aparecem entre os de maior peso [p. 12, p. 21].
- Dados de uma estação com ReliefF-RFE: OA de 80,23% (SVM), 82,42% (CART) e 83,43% (RF); Kappa de 0,71, 0,75 e 0,75 [p. 18].
- Multitemporal com ReliefF-RFE: OA de 85,48%, 88% e 89,43%; Kappa de 0,79, 0,81 e 0,84 [p. 18].
- Multitemporal com SLPSO-RFE: OA de 95,48% (SVM), 96% (CART) e 97,97% (RF); Kappa de 0,94, 0,94 e 0,96; F1 de 93,33, 94,01 e 96,43 [p. 18].
- Ganho do SLPSO-RFE sobre o ReliefF-RFE em dados multitemporais: 10%, 8% e 8,54% de OA para SVM, CART e RF; sobre o cenário de uma estação com ReliefF-RFE: 15,25%, 13,58% e 14,54% [p. 22].
- Ganho apenas por usar duas estações em vez de uma: 5,25%, 5,58% e 6% de OA [p. 22].
- Validação por UAV: cenários 7–9 acima de 90% de concordância de área; o cenário 9 atinge 97% na área 1 e 95,78% na área 2 [p. 20].
- Retroespalhamento do eucalipto: VV e VH em −5 dB e −12 dB no verão, passando a −13 dB e 24 dB no inverno (valores como estão no texto) [p. 22]; análise sobre 195 amostras de 2020–2021 [p. 21].

## 6. Limitações que os próprios autores reconhecem

- Separar eucalipto de outras formações é difícil nas imagens multiespectrais de 10 m do Sentinel-2, o que torna a escolha de amostras árdua [p. 20].
- As variações sazonais do eucalipto "não são pronunciadas", de modo que o ganho trazido apenas pela dimensão temporal foi pequeno [p. 21].
- O SAR usado restringe-se a coeficientes de retroespalhamento e texturas, sem atributos de polarização, porque o GEE não oferece suporte a dados SLC necessários ao cálculo da matriz de polarização [p. 21].
- O próprio trabalho se limita à extração de área; os autores propõem como continuação o uso de SAR totalmente polarimétrico e de imagens ópticas de maior resolução espacial [p. 22].

## 7. O que serve ao projeto e o que não serve

- Serve: o desenho multitemporal Sentinel-1/2 (verão e inverno) com composições medianas sazonais é diretamente replicável para mapear talhões de eucalipto em Goiás, etapa prévia de qualquer estimativa de biomassa e carbono [p. 5].
- Serve: o subconjunto de atributos com índices de *red-edge* e texturas GLCM, e o pipeline ReliefF → SLPSO-RFE, são candidatos a teste como preditores em modelos de AGB, não só de classe [p. 12, p. 21].
- Serve: a validação por UAV e por matriz de confusão (OA, Kappa, PA, UA, F1) fornece um protocolo de acurácia barato para checar mapas de área [p. 18–20].
- Não serve: o artigo não estima biomassa nem estoque de carbono, não usa dados de campo de biomassa e não apresenta modelo alométrico; a área de estudo é o sul da China, sem teste no Cerrado goiano [p. 3–4].

## 8. Frases citáveis (literais)

- "The findings reveal that employing SLPSO–RFE for feature selection significantly elevates the classification precision of eucalyptus plantations across all three classifiers." [p. 1]
- "This suggests that while there are seasonal variations in eucalyptus, they are not pronounced." [p. 21]
