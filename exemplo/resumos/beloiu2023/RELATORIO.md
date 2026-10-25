# Relatório — Beloiu et al. (2023)

## 1. Referência

BELOIU, M.; HEINZMANN, L.; REHUSH, N.; GESSLER, A.; GRIESS, V. C. **Individual Tree-Crown Detection and Species Identification in Heterogeneous Forests Using Aerial RGB Imagery and Deep Learning**. *Remote Sensing*, v. 15, n. 5, art. 1463, 2023. DOI: 10.3390/rs15051463. [p. 1]

## 2. Pergunta do estudo

Avaliar se um detector de objetos profundo (Faster R-CNN) aplicado apenas a ortofotos aéreas RGB de acesso aberto consegue detectar copas individuais e identificar/geolocalizar quatro espécies arbóreas em florestas temperadas heterogêneas, comparando modelos mono e multiespécie e o efeito das condições de sítio. [p. 2–3]

## 3. Área e dados

- **Local:** norte da Suíça, regiões do Planalto Central e do Jura, abrangendo nove cantões (Vaud, Fribourg, Bern, Solothurn, Luzern, Aargau, Jura, Basel-Landschaft, St. Gallen), entre 400 e 1.200 m de altitude, clima temperado. [p. 3]
- **Período:** ortofotos do período vegetativo obtidas entre 2017 e 2021 [p. 4]; dados de campo (verdade terrestre) coletados entre 1995 e 2020 [p. 4].
- **Sensores/fontes:** apenas imagem óptica RGB — ortofotos SWISSIMAGE (Swisstopo) a 10 cm, câmera ADS100 (Leica Geosystems), ortorretificadas com o MDE swissALTI3D (50 cm) [p. 3]; verdade terrestre de três fontes: Arborizer, programa LWF e Inventário Florestal Nacional suíço (NFI) [p. 4]. Nenhum LiDAR, multiespectral ou SAR foi usado.
- **Amostras:** 17.610 árvores geolocalizadas no conjunto bruto [p. 4]; após filtragem (dbh ≥ 20 cm coníferas / ≥ 25 cm folhosas, posição social dominante/co-dominante e inspeção visual), 11.437 árvores: 9.552 treino, 1.062 validação e 823 teste [p. 4, Tabela 1; p. 5]. Oito sítios de teste independentes de 1 ha [p. 5].
- **Observação de consistência:** o texto afirma "11,437 and 10,614 geolocated trees for training and validation" [p. 4], número que não fecha com a Tabela 1 (9.552 + 1.062 = 10.614 de treino+validação); adoto a Tabela 1.

## 4. Método

1. **Rotulagem:** extensão da copa gerada por buffer fixo de 4 m (coníferas) e 5 m (folhosas) ao redor de cada ponto de campo, com correção manual de pontos deslocados; recortes de 256 × 256 pixels (25,6 × 25,6 m), divisão 90% treino / 10% validação feita de forma espacial para evitar árvores vizinhas nos dois conjuntos. [p. 4]
2. **Modelo:** Faster R-CNN com backbone ResNet-101, pesos descongelados, 50 épocas, batch 16, SGD com learning rate 0,0001, Focal Loss para desbalanceamento, limiar mínimo de confiança 0,5, early stopping e supressão de não máximos (sobreposição > 70%). [p. 5–6]
3. **Experimentos:** modelos monoespécie e quatro modelos multiespécie (abeto-fir, abeto-fir-pinheiro, abeto-fir-faia, abeto-fir-pinheiro-faia), com e sem aumento de dados (rotação de 90°), testados em oito sítios com diferentes densidades, declividades (3–10° e ~35°) e iluminação. [p. 5, p. 10]
4. **Avaliação:** precisão, recall, F1, IoU (limiar 0,5), AP e matrizes de confusão, comparando mono vs. multiespécie e o efeito de estrutura do povoamento e iluminação. [p. 6, p. 7]

## 5. Resultados principais

**Modelos monoespécie (sem aumento de dados)**
- F1 médio de 0,76. [p. 7]
- *Picea abies*: F1 0,86; precisão 0,93; recall 0,80; AP 0,78; 189 TP, 15 FP, 48 FN. [p. 7, Tabela 2]
- *Abies alba*: F1 0,84; precisão 0,81; recall 0,86; AP 0,78; 110 TP, 25 FP, 18 FN. [p. 7, Tabela 2]
- *Fagus sylvatica*: F1 0,75; precisão 0,77; recall 0,74; AP 0,64; 126 TP, 38 FP, 46 FN. [p. 7, Tabela 2]
- *Pinus sylvestris*: F1 0,59; precisão 0,50; recall 0,73; AP 0,57; 19 TP, 19 FP, 7 FN. [p. 7, Tabela 2]

**Modelos multiespécie**
- Melhor média entre os quatro modelos: 0,81 de F1 no modelo das três coníferas (abeto-fir-pinheiro). [p. 8]
- *Pinus sylvestris* sobe para F1 0,92 (precisão 1,00; recall 0,85; AP 0,85) no modelo de três coníferas; e F1 0,92 (precisão 0,96; recall 0,88) no modelo de quatro espécies. [p. 8–9, Tabela 3]
- *Picea abies*: F1 0,85 no modelo abeto-fir e 0,79 no de três coníferas. [p. 8, Tabela 3]
- *Abies alba*: F1 0,54 (abeto-fir), 0,72 (três coníferas), 0,60 (com faia) e 0,55 (quatro espécies) — o mais sensível à combinação. [p. 8–9, Tabela 3]
- *Fagus sylvatica*: F1 0,56 no modelo com faia e 0,46 no modelo de quatro espécies; recall cai para 0,30 neste último. [p. 9, Tabela 3]
- Média geral multiespécie 0,73 contra 0,74 dos modelos monoespécie. [p. 11]

**Erros de identificação e confusão entre espécies**
- 4% das *Picea abies* identificadas como *A. alba* e 2% no sentido inverso; 7% de *A. alba* como *Pinus sylvestris*; 7% de *F. sylvatica* como *A. alba*; 31% de *Pinus sylvestris* como *A. alba*. [p. 7]
- No modelo de quatro espécies, só 4% das *F. sylvatica* foram confundidas com *Pinus sylvestris*, ou seja, a misidentificação (FP) cai à medida que entram mais espécies no treino. [p. 9]

**Aumento de dados e condições de sítio**
- F1 médio "todas as espécies" com e sem aumento: 0,70/0,81 (abeto-fir), 0,81/0,69 (três coníferas), 0,68/0,71 (com faia), 0,67/0,73 (quatro espécies) — efeito inconsistente. [p. 10, Tabela 4]
- *Abies alba* foi a espécie mais beneficiada: 0,54 → 0,74 (abeto-fir) e 0,55 → 0,80 (quatro espécies). [p. 10, Tabela 4]
- *Pinus sylvestris* no modelo de quatro espécies despencou de 0,92 para 0,39 com aumento de dados. [p. 10, Tabela 4]
- Iluminação: F1 0,85 em sítios com iluminação ótima contra 0,80 em encosta norte sombreada a ~35°. [p. 10]
- Densidade: diferença de F1 de 0,14 entre povoamento maduro homogêneo e heterogêneo; em uma mancha de ~30 × 30 m, apenas 3 de 25 árvores foram detectadas. [p. 10]
- Sítios de teste exemplares: F1 0,74 (sítio 2) e F1 0,78 (sítio 3). [p. 10]
- Custo computacional: 30 min de treino por espécie contra mais de 6 h nos modelos multiespécie; de 3 a mais de 14 h com aumento de dados. [p. 6]

## 6. Limitações reconhecidas pelos autores

- A data de aquisição das ortofotos não acompanha os metadados, o que impediu avaliar o efeito da fenologia na discriminação das espécies. [p. 3; p. 13]
- Podem existir rótulos faltantes, sobretudo para copas menores, e a defasagem temporal entre verdade terrestre e imagem pode afetar o desempenho. [p. 12–13]
- O número de falsos negativos aumenta conforme mais espécies entram no modelo; as árvores não detectadas são a principal causa da queda de acurácia. [p. 12]
- Erro submétrico dos pontos de campo e efeito de inclinação das copas (deslocamento aparente em relação ao ponto no solo) exigem correção manual. [p. 4]
- Desbalanceamento de classes, com *Pinus sylvestris* sub-representada; o baixo desempenho dessa espécie nos modelos monoespécie é atribuído ao pequeno número de amostras de treino. [p. 4; p. 11]
- A inspeção visual da base de referência é demorada e sujeita a interpretação equivocada. [p. 12]
- O aumento de dados exige tempo computacional longo e seus ganhos foram espécie- e sítio-específicos. [p. 13]
- A explicabilidade dos modelos CNN ainda precisa ser investigada em estudos futuros. [p. 12]
- Grupos de árvores jovens foram pouco detectados, o que reduz a acurácia em povoamentos densos e heterogêneos. [p. 10]

## 7. O que serve e o que não serve ao projeto

**Serve**
1. O desenho de detecção de copas por objeto (Faster R-CNN + recortes de 256 px, split espacial 90/10) e o conjunto de métricas (F1, IoU 0,5, AP, matriz de confusão) são diretamente replicáveis para contar e geolocalizar árvores em talhões de silvicultura em Goiás, como etapa prévia a inventário e à extrapolação de biomassa.
2. A demonstração de que RGB de alta resolução e acesso aberto sustenta identificação de espécies a custo baixo é o argumento para priorizar ortofotos e VANT RGB no arranjo multissensorial do projeto, reservando LiDAR/multiespectral para atributos estruturais e biofísicos.

**Não serve**
3. Não estima biomassa, estoque de carbono, altura, volume ou AGB: o dbh aparece apenas como critério de filtragem da base, e não há nenhuma modelagem biofísica — o artigo entrega localização e identidade de espécie, não quantificação de carbono.
4. O contexto é floresta temperada nativa europeia, com quatro espécies europeias e sítios de 1 ha; não cobre silvicultura plantada (eucalipto/pinus), Cerrado goiano, escala de talhão/paisagem nem validação com parcelas de biomassa.

## 8. Frases citáveis

> "In conclusion, the presented method can accurately map the location of four individual tree species in heterogeneous forests and may serve as a basis for future inventories and targeted management actions to support more resilient forests." [p. 1]

> "Thus, our findings indicate that low-cost or open-source aerial RGB data can provide a reliable basis for object detection models to identify individual tree species at larger spatial scales." [p. 12]
