# RELATÓRIO — Larissa Pereira Ribeiro Teodoro (2023)

## 1. Referência

- Autores: Larissa Pereira Ribeiro Teodoro; Rosilene Estevão; Dthenifer Cordeiro Santana; Izabela Cristina de Oliveira; Maria Teresa Gomes Lopes; Gileno Brito de Azevedo; Fábio Henrique Rojo Baio; Carlos Antonio da Silva Junior; Paulo Eduardo Teodoro.
- Título: *Eucalyptus Species Discrimination Using Hyperspectral Sensor Data and Machine Learning* (Technical Note).
- Revista: *Forests* (MDPI), v. 15, art. 39.
- DOI: 10.3390/f15010039 — confere com o solicitado; o `TEXTO.txt` está completo (10 páginas, incluindo referências) e é o artigo do DOI.
- Datas: recebido em 23/11/2023, aceito em 21/12/2023, publicado em 23/12/2023 [p. 1]; a citação editorial é *Forests* **2024**, 15, 39 [p. 1] — por isso o ano aparece como 2023 (online) e 2024 (volume).

## 2. Pergunta do estudo

Se cinco espécies de eucalipto podem ser discriminadas a partir da assinatura espectral de folhas medida por sensor hiperespectral e classificada por algoritmos de aprendizado de máquina, e qual o menor número de amostras por espécie suficiente para essa classificação [p. 2].

## 3. Área e dados

- Local: área experimental da Universidade Federal de Mato Grosso do Sul, Chapadão do Sul (18°41′33″ S, 52°40′45″ W, 810 m), Mato Grosso do Sul, Brasil — **não é Goiás** [p. 3]. Clima Aw, chuva de 750 a 1800 mm ano⁻¹, temperatura média de 20 a 25 °C [p. 3].
- Plantio de eucalipto com 10 anos de implantação; delineamento em blocos casualizados, 4 repetições, 28 plantas por parcela, espaçamento 3 m × 1,5 m [p. 3].
- Espécies (5): *Eucalyptus camaldulensis*, *Corymbia citriodora*, *E. saligna*, *E. grandis* e *E. urophyla* [p. 3].
- Período de coleta: agosto de 2022 e janeiro de 2023 [p. 3].
- Fonte: sensor hiperespectral de baixo custo Ocean Insight® STS-VIS, faixa de 335,14 a 820,80 nm [p. 3]. Foram usadas as bandas de 400 a 700 nm (visível) e de 701 a 820 nm (NIR), em bandas de 0,45 nm, totalizando 1024 bandas espectrais [p. 3]. Leituras feitas em laboratório, até 12 h após a coleta [p. 3] — portanto é espectroscopia foliar, não imageamento orbital ou aéreo.
- Amostras: 50 folhas por espécie por unidade experimental, totalizando 200 amostras por coleta [p. 3]; 200 folhas por espécie no total [p. 1]. Conjuntos avaliados: n = 50, n = 100 e n = 200 amostras por espécie [p. 3].

## 4. Método

- Classificação supervisionada com as 1024 bandas espectrais como variáveis de entrada e as cinco espécies como saída [p. 3].
- Modelos: ANN (multilayer perceptron, backpropagation, duas camadas ocultas de 10 neurônios, taxa de aprendizado 0,3, momentum 0,2, 500 épocas), árvores de decisão J48 e REPTree, random forest (RF, 100 árvores) e regressão logística (LR) como controle; demais parâmetros no padrão do Weka [p. 3–4].
- Validação cruzada estratificada e aleatória, k-fold = 10 com 10 repetições (100 execuções por modelo), no Weka 3.9.4 [p. 4].
- Métricas: porcentagem de classificações corretas (CC, %) e F-measure [p. 4]; ANOVA em delineamento inteiramente casualizado com 10 repetições (folds) e agrupamento de médias por Scott–Knott a 5% [p. 4].

## 5. Resultados principais

- Curvas espectrais distintas entre as espécies, com diferenças mais marcadas a partir de 700 nm [p. 1]; na região do visível, *E. camaldulensis* e *E. urophylla* pouco se diferenciaram [p. 7].
- Discriminação considerada acurada, com valores acima de 75% de CC e 0,75 de F-measure [p. 5].
- Melhor resultado de CC: ANN com 97,08% em n = 50 (F-measure 0,95) [p. 6]. Com n = 100, RF = 93,08% e ANN = 91,50%; com n = 200, LR = 94,06%, ANN = 93,60% e RF = 93,09% [p. 6].
- Piores resultados: REPTree, 78,64% de CC e F-measure 0,81 em n = 50; J48, 83,56% em n = 100 [p. 6].
- Sem diferença estatística de CC entre os três tamanhos de conjunto de dados [p. 1]; n = 50 folhas por espécie foi considerado suficiente [p. 7].
- Observação: a terceira coluna da Tabela 1 está rotulada "150", mas o texto e a legenda indicam n = 200 [p. 6].

## 6. Limitações que os próprios autores reconhecem

- O número limitado de amostras obtidas é apontado como desafio para treinar modelos de classificação de espécies arbóreas com alta acurácia [p. 7].
- Os autores recomendam novos estudos em outras regiões do mundo e com outras espécies, em plantios e em vegetação nativa, para ampliar o alcance da distinção em nível de espécie [p. 8].
- Não há discussão explícita de outras limitações (por exemplo, leitura foliar em laboratório em vez de dossel imageado) [p. 7–8].

## 7. O que serve ao projeto e o que não serve

- Serve: o desenho de validação (k-fold = 10 com 10 repetições, CC e F-measure, Scott–Knott a 5%) é replicável em classificações e comparações de modelos do projeto [p. 4].
- Serve: o resultado de que n = 50 folhas por espécie basta indica economia de campo e laboratório em levantamentos de silvicultura [p. 7].
- Serve: a indicação de que a separabilidade espectral se concentra de 700 nm em diante é referência para escolher faixas de bandas em estudos de dossel [p. 1; p. 7].
- Não serve: o artigo não estima biomassa, estoque de carbono, volume ou produtividade — a variável-resposta é a espécie — e não há dados de Goiás nem uso de sensoriamento multissensorial ou orbital [p. 3; p. 5–6].

## 8. Frases citáveis (literais)

- "Our findings revealed the existence of distinct spectral curves between the species, with the differences being more marked from the 700 nm range onwards." [p. 1]
- "However, our findings show that the smallest sample size evaluated (n = 50) is sufficient to classify species with high accuracy." [p. 7]
