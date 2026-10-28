# RELATÓRIO — Fabien Hubert Wagner (2025)

## 1. Referência

Wagner, F.H.; Breunig, F.M.; Balbinot, R.; Silva, E.A.; Soares, M.C.; Kramm, M.A.; Hirye, M.C.M.; Carter, G.; Dalagnol, R.; Hagen, S.C.; Saatchi, S. (2025). *Monitoring the Early Growth of Pinus and Eucalyptus Plantations Using a Planet NICFI-Based Canopy Height Model: A Case Study in Riqueza, Brazil*. **Remote Sensing**, 17, 2718. DOI: 10.3390/rs17152718.

O `TEXTO.txt` corresponde ao artigo do DOI indicado: 21 páginas, do resumo às referências, sem truncamento.

## 2. Pergunta do estudo

Um modelo de aprendizado profundo de altura de dossel treinado com imagens Planet NICFI na Amazônia e Mata Atlântica consegue (i) isolar artefatos sazonais ligados a declividade e orientação em floresta natural estável e (ii) acompanhar as trajetórias de crescimento de plantios de Pinus e Eucalyptus ao longo de oito anos?

## 3. Área e dados

- Local: Riqueza, Santa Catarina, Brasil; recorte da quadricula Planet NICFI 0720-0864, ~20 × 20 km, domínio de Mata Atlântica, elevação de 200 a 610 m, clima Cfa, precipitação anual de 1919 mm e temperatura média de 18 °C [p. 3].
- Período: série NICFI de 1 de dezembro de 2015 a 1 de maio de 2025, com 67 datas — observações semestrais até 1 de junho de 2020 e mensais de 1 de setembro de 2020 a 1 de maio de 2025 [p. 5].
- Sensores/fontes: Planet NICFI RGB-NIR a ~4,78 m (bandas R, G, B e NIR, convertidas para 8 bits, sem correção atmosférica) [p. 5]; CHM de UAV obtido com Phantom 4 e Matrice 100 (câmeras RGB), processado no Metashape, em 8 campanhas entre 1 de junho de 2017 e 1 de maio de 2025, resoluções de 0,028 a 0,084 m [p. 4–5]; SRTM de 1 arco-segundo (~30 m) para declividade e orientação [p. 6].
- Amostras: 9 espécies de Pinus plantadas em junho de 2017 e 10 de Eucalyptus plantadas em novembro de 2016 [p. 4]; os talhões de Pinus foram simplificados em oito unidades maiores e os de Eucalyptus mantidos como parcelas puras [p. 4]; ao todo 40 parcelas analisadas — Pinus 1–8, Eucalyptus 9–24, pastagem 25–32 e floresta natural 33–40 [p. 13]. Para a análise sazonal, 714.432 pixels de floresta estável, sendo 14.884 por combinação de declividade × orientação (48 combinações), no período de 1 de maio de 2021 a 1 de abril de 2025 [p. 7].

## 4. Método

- Modelo U-Net adaptado para regressão, aplicado às imagens RGB-NIR NICFI a ~4,78 m para prever altura média do dossel; erro médio de 3,68 m na amostra de validação do trabalho original [p. 5].
- Comparação em nível de parcela entre altura prevista e CHM de UAV (média e desvio padrão), com MAE, RMSE, bias, teste t pareado e janela de ±3 meses nas datas de campo [p. 7].
- Análise sazonal por modelo linear de Fourier (termos seno e cosseno do dia do ano) com interação com classes de declividade (6 classes) e orientação (8 classes), ajustado por mínimos quadrados ordinários sobre medianas por data e combinação [p. 6].
- Média móvel de 12 meses para reduzir ruído sazonal; critério de ±1 desvio padrão para visualização e 1,96 × desvio padrão para o intervalo de 95% [p. 7]; teste de buffer negativo de 5 m nas parcelas [p. 12].

## 5. Resultados principais

- Pinus: previsões dentro de menos de um desvio padrão das alturas de UAV na maior parte do tempo [p. 11]; MAE abaixo de 0,4 m antes de 2018, 1,51 m em 2019 e 2,00 m em 2025, este último com bias de −1,55 m não significativo (p = 0,0785) [p. 12, p. 14].
- Eucalyptus: crescimento detectado, mas subestimação forte na fase de crescimento rápido — em junho de 2021, bias de −8,32 m, MAE de 8,32 m e RMSE de 8,96 m (p < 0,001) [p. 12, p. 14]; em maio de 2025 o bias caiu para −1,38 m, não significativo (p = 0,061) [p. 14].
- Taxas de crescimento: percentil 95 do crescimento anual por parcela de 2,73 m/ano para Pinus e 7,16 m/ano para Eucalyptus [p. 10].
- Artefato sazonal em floresta estável: superestimação de ~3 m em encostas voltadas ao sul entre os dias do ano 150 e 250 e subestimação superior a −3 m nas encostas norte mais íngremes [p. 7]; R² do modelo sazonal de 0,8227 (a legenda da Figura 2 indica 0,8225) [p. 7–8], explicando 82% da variância [p. 16]; os artefatos chegam a ~25% do valor médio [p. 17].
- Distorções geométricas: deslocamentos de registro de até quatro pixels NICFI, ~20 m, no Pinus, e de ~dois pixels, ~10 m, no Eucalyptus [p. 8–9].
- Buffer negativo de 5 m reduziu o desvio padrão em 96,8% das parcelas de Pinus e 91,0% das de Eucalyptus, com reduções médias de 0,35 m e 0,30 m [p. 12].
- Controles: pastagens com altura prevista quase sempre zero, com falsos positivos ligados a culturas sazonais que não duram mais de 3 meses [p. 12–13]; floresta natural com médias acima de 15 m, tendência estável ou levemente decrescente e coeficiente de variação de 26,3% [p. 14].

## 6. Limitações que os próprios autores reconhecem

- Não está determinado se a altura de Eucalyptus na fase de crescimento rápido pode ser estimada com precisão, nem se a subestimação vem da falta de amostras de treino ou da textura homogênea do dossel [p. 17].
- O modelo foi testado em apenas uma região tropical e em uma única mistura de espécies; o desempenho em outros contextos ecológicos ou climáticos ainda precisa ser avaliado [p. 17].
- Os mecanismos exatos dos artefatos sazonais permanecem parcialmente inexplicados (efeitos fenológicos ou topográficos) e não existe ainda método eficaz para removê-los [p. 17]; a correção por BRDF é difícil na resolução de 4,78 m e o NICFI passou a exigir assinatura [p. 17].
- A dependência de imagens RGB-NIR de alta qualidade e de dados de referência confiáveis pode limitar o uso em regiões onde esses dados não existem [p. 17]; erros de geolocalização e distorção impedem o acompanhamento de árvores individuais [p. 18].
- Dados de UAV de Eucalyptus de 2022 foram perdidos [p. 5], e não há dados de campo para dizer se a aparente redução de altura nas florestas naturais 35–38 é real ou artefato [p. 14].

## 7. O que serve ao projeto e o que não serve

- Serve: referência metodológica direta para estimar altura de dossel de silvicultura com imagens ópticas de ~5 m e U-Net, com validação por CHM de UAV e métricas em nível de parcela (MAE, RMSE, bias, teste t) [p. 7, p. 12] — desenho replicável para Goiás.
- Serve: o diagnóstico quantificado de artefato sazonal por declividade × orientação (R² de 0,8227) e a correção prática por média móvel de 12 meses e agregação por parcela [p. 7–8], útil em relevo ondulado.
- Serve: recomendações operacionais — projetar talhões grandes, aplicar buffer negativo de 5 a 10 m nas bordas e evitar a série semestral em favor da mensal a partir de outubro de 2020 [p. 12, p. 16–17].
- Não serve: o artigo não estima biomassa nem estoque de carbono, não usa fusão multissensorial (apenas óptico NICFI e UAV) e seu modelo foi treinado em florestas tropicais úmidas, com subestimação grave em Eucalyptus de crescimento rápido [p. 12, p. 17]; o clima subtropical Cfa e as espécies do sul do Brasil diferem do Cerrado goiano [p. 3].

## 8. Frases citáveis (literais)

- "We find that the model closely tracks Pinus growth at the parcel scale, with predictions generally within one standard deviation of UAV-derived heights." [p. 1]
- "In contrast, for Eucalyptus plantations, the model underestimates average parcel height during rapid growth phases, particularly when canopies are dense, isotropic, with reduced spatial variability in reflectance, and ground pixels are no longer visible." [p. 15]
