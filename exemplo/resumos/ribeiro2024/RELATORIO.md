# RELATÓRIO — Fabiana Piontekowski Ribeiro (2024)

## 1. Referência

Ribeiro, F.P.; de Sousa, T.R.; Silva, F.R.d.C.; da Fonseca, A.C.P.; dos Santos, M.G.B.; dos Santos, J.R.; de Jesus, D.R.; Lozada, C.M.C.; Valadão, M.B.X.; Miguel, E.P.; de Oliveira, A.D.; de Carvalho, A.M.; Gatto, A. (2024). *Individual Carbon Modeling in Eucalyptus Stands in the Cerrado Region*. **Forests**, 15, 1332. DOI: 10.3390/f15081332.

O `TEXTO.txt` está íntegro: 13 páginas, com referências e disclaimer finais. Ele traz, porém, trechos duplicados do arquivo de revisão ("FOR PEER REVIEW"), com o mesmo conteúdo do artigo publicado.

## 2. Pergunta do estudo

Como plantios de eucalipto de diferentes idades e clones se comportam quanto ao estoque de C por compartimento e qual modelo matemático de nível individual estima esse C com maior acurácia na região do Cerrado.

## 3. Área e dados

- Local: quatro áreas experimentais no Distrito Federal, Brasil — duas na Fazenda Água Limpa (UnB), 15°58′ S, 47°54′ W, e duas no Núcleo Rural Quebrada dos Neres, Paranóá, 15°53′ S, 47°39′ W e 15°53′ S, 47°38′ W [p. 3].
- Clima Aw (Köppen), duas estações bem definidas; temperaturas médias anuais de 20,3, 22,3 e 20,9 °C e chuvas de 1500, 1052 e 1272 mm em 2014, 2015 e 2016, respectivamente [p. 3].
- Material: *Eucalyptus urophylla* × *Eucalyptus grandis*. A1 = clone EAC1528, 48 meses, 12 ha, plantado em dezembro de 2011, espaçamento 3,5 × 1,7 m; A2 = clone Urograndis, 60 meses, 1,2 ha, novembro de 2009, 3 × 2 m; A3 = clone I224, 72 meses, 3,29 ha, janeiro de 2010, 3 × 2 m; A4 = clone GG100, 72 meses, 19 ha, dezembro de 2009, 3,5 × 1,7 m [p. 3–4].
- Amostragem: 49 parcelas aleatórias de 10 × 10 m e 20 × 30 m; cubagem rigorosa de 49 árvores (usadas também no k-fold) [p. 4–5]. Data do inventário: não informado.
- Sensores ou fontes: não informado — o estudo não usa sensoriamento remoto; os dados vêm de inventário florestal, cubagem e análise elementar em laboratório [p. 4–5].

## 4. Método

- Inventário e cubagem: DBH de todos os indivíduos, altura total medida com clinômetro e hipsômetro eletrônico (Haglöf HEC-2); árvores classificadas em suprimidas, intermediárias e dominantes, abatidas a 10 cm do solo e cubadas pelo método de Smalian [p. 4].
- Biomassa e C por compartimento: folhas, galhos, madeira e casca pesados verdes em balança de 300 kg (0,05 kg); amostras secas em estufa a 103 ± 2 °C (folhas a 65 ± 2 °C) e C determinado em analisador elementar CHNS Macro Vario Cube [p. 4].
- Carbono de raízes: dez monólitos circulares por árvore, diâmetro médio de 23 cm, profundidade de 0–60 cm, marcados a 50 cm do toco e a 50 cm entre si; volume por cilindro (V = πr²h) [p. 4–5].
- Análise estatística: Shapiro–Wilk, ANOVA e Tukey (p < 0,05) no SISVAR 5.6; três modelos (Schumacher–Hall, Schumacher–Hall adaptado com idade e Spurr) selecionados por r, RMSE% e AIC, com validação cruzada k-fold (5 subconjuntos de 10, 10, 10, 10 e 9 árvores) no R 4.3.2 [p. 5].

## 5. Resultados principais

- Teor médio de C: A3 (clone I224) = 55,40 dag kg−1, superior a A1 (44,84), A2 (43,10) e A4 (42,80) dag kg−1; CV geral de 4,76% [p. 6].
- Em A3 houve diferença entre compartimentos: madeira 57,93 dag kg−1 > galhos 56,94 > folhas 56,25 > casca e raízes 56,10 dag kg−1 [p. 6].
- A madeira respondeu por ≥ 69,06% do C em todas as áreas; A3 estocou 64% mais C que A4 na mesma idade [p. 6].
- Estoque médio de C por árvore: A3 = 82,58 kg (parte aérea 76,13; raízes 6,45), A4 = 51,34 kg (47,09; 4,24), A1 = 41,75 kg (37,61; 4,14) e A2 = 30,01 kg (27,22; 2,78) [p. 7].
- Estoque total por hectare variou de 35,64 a 233,35 Mg ha−1 C, com o clone I224 em 233,35 Mg ha−1 [p. 9–10].
- Modelo 1 (Schumacher–Hall adaptado, com DBH, h e idade): r = 0,99, RMSE% = 9,65 e AIC = 258; modelo 2: r = 0,98, RMSE% = 12,86, AIC = 279; modelo 3 (Spurr): r = 0,98, RMSE% = 12,83, AIC = 278 [p. 7].
- Coeficientes do modelo 1: β0 = 0,00113; β1 = 2,14718; β2 = 1,15236; β3 = 0,83763 [p. 7].
- Validação k-fold do modelo 1: r entre 0,980 e 0,996, RMSE% entre 9,42 e 12,26 e média de r = 0,989 e RMSE% = 10,96 [p. 9].
- Densidade básica da madeira: I224 0,677 g cm−3, GG100 0,595, EAC1528 0,531 e Urograndis 0,433 g cm−3 [p. 9].
- Ganho econômico estimado com créditos de carbono (BRL 22,00 ha−1): A3 BRL 921,11, contra A4 BRL 330,39 na mesma idade [p. 9–10].

## 6. Limitações que os próprios autores reconhecem

- A cubagem rigorosa é "costly and time-consuming", o que limita a operação, embora seja necessária para a acurácia [p. 10].
- As raízes costumam ser omitidas nas estimativas de estoque de C pelas dificuldades e custos de medição [p. 2].
- Os resíduos percentuais não mostram tendência clara de estimativa, com valores observados e estimados divergentes [p. 10].
- Amostra restrita: 49 árvores e quatro áreas em uma única região (Distrito Federal), com idades de 48 a 72 meses [p. 4–5].

## 7. O que serve ao projeto e o que não serve

- Serve: teores de C por compartimento (42,80 a 57,93 dag kg−1) e estoques por árvore e por hectare em eucalipto no Cerrado, utilizáveis como referência de campo e como fator de conversão biomassa → C [p. 6–7].
- Serve: o modelo de Schumacher–Hall adaptado (DBH, altura e idade; r = 0,99, RMSE% = 9,65) e o protocolo de seleção e validação (r, RMSE%, AIC, k-fold) como linha de base para comparar estimativas por sensoriamento remoto [p. 7–9].
- Não serve: não há sensoriamento remoto, sensor, imagem ou variável espectral no estudo — o dado é destrutivo e dendrométrico, então nada do método é transferível para a abordagem multissensorial [p. 4–5].
- Não serve: a área é o Distrito Federal, não Goiás, e a amostra é pequena e restrita a quatro clones de 48–72 meses, o que limita a extrapolação para outras idades, materiais e sítios [p. 3–4].

## 8. Frases citáveis (literais)

- "The non-linear Schumacher–Hall model, adapted to include age, resulted in the best fit, with r, RMSE%, and AIC values of 0.99, 9.65%, and 258, respectively." [p. 10]
- "In the stands in this study, the total C stock ranged from 35.64 to 233.35 Mg ha−1 C." [p. 9]
