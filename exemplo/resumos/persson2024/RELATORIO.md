# RELATÓRIO — Henrik Jan Persson (2024)

## 1. Referência

Persson, H. J.; Huuva, I. (2024). *Polarimetric Measures in Biomass Change Prediction Using ALOS-2 PALSAR-2 Data*. **Remote Sensing**, 16(6), 953. Technical Note. DOI: 10.3390/rs16060953. O `TEXTO.txt` está completo (13 páginas, com referências e conclusões) e corresponde ao DOI informado.

## 2. Pergunta do estudo

Saber se imagens SAR totalmente polarimétricas em banda L (ALOS-2 PALSAR-2) estimam a mudança de biomassa acima do solo com mais precisão do que uma ou duas polarizações, comparando polarizações cruzadas, co+cruzadas, a decomposição de Freeman–Durden e o RVI, e verificando se a polarimetria contorna a saturação e como a estrutura da floresta afeta a sensibilidade [p. 3].

## 3. Área e dados

- Local: Remningstorp, sul da Suécia (58°30′N 13°40′E), ~1200 ha de floresta hemi-boreal manejada, predominantemente conífera (Norway spruce, Scots pine, birch) [p. 3].
- Período: inventário de campo após a estação de crescimento de 2014 e novamente após 2021; cenas SAR de 11/06/2015 e 03/06/2021 [p. 3–4].
- Sensores: duas cenas ALOS-2 PALSAR-2 em modo stripmap HBQ, totalmente polarimétricas, banda L, resolução de 6 m, ângulo off-nadir 28,4°, mesma órbita ascendente [p. 4]; modelo digital do terreno de 2018 (2 × 2 m, laser aerotransportado) [p. 4].
- Amostras: 46 parcelas de campo com 40 m de raio, distribuídas subjetivamente [p. 3].

## 4. Método

- Estimativa **direta** de ΔAGB (2015→2021) por regressão linear, com preditores pareados nas duas datas e sem calcular a diferença de cada preditor; preditor mantido se significativo (t-test, 5%) em ao menos uma data [p. 4–5].
- Quatro modelos: (1) média das polarizações cruzadas (HV+VH)/2; (2) modelo 1 + VV e HH; (3) componentes da decomposição de Freeman–Durden (vol, dbl, surf); (4) RVI = 8γ⁰_HV / (γ⁰_HH + γ⁰_VV + 2γ⁰_HV) [p. 5].
- Processamento em SNAP 9.0.0: calibração radiométrica, filtro de speckle Lee-Sigma (17 × 17, alvo 3 × 3, sigma 0,9), multilooking 2 × 4, correção geométrica com DTM e reamostragem para pixels de 10 m [p. 6].
- Validação por leave-one-out cross-validation (LOOCV), com RMSE e bias das predições [p. 6].

## 5. Resultados principais

- RMSE caiu de 84,9 t/ha (modelo 1) para 79,4 (modelo 2), 69,7 (modelo 3, Freeman–Durden) e 50,4 t/ha (modelo 4, RVI); R² de 0,45 a 0,82; N = 46 [p. 7].
- Bias: −0,795; −0,245; 0,662; 0,391 t/ha nos modelos 1–4, todos abaixo de 1 t/ha em valor absoluto [p. 7].
- O modelo 4 (RVI) teve redução de erro de 41 pontos percentuais em relação ao modelo 1 e o maior R² (0,82) [p. 7].
- Modelos 3 e 4 reduziram a variância sobretudo nas parcelas de corte raso, indicando melhor captura da mudança do mecanismo de espalhamento dominante [p. 7].
- Nenhum ponto claro de saturação foi observado no máximo de ΔAGB previsto pelo modelo 4; reduções de 300 t/ha já haviam sido previstas com dados aerotransportados de banda L totalmente polarimétricos [p. 7].
- Para o estado de AGB, o ponto de saturação subiu com mais polarizações, chegando a ~200 t/ha, acima dos 100 t/ha comumente citados para banda L [p. 7].
- Estrutura florestal: sensibilidade ao AGB caiu acima de hL de 20 m [p. 8], de BA de 30 m²/ha [p. 8] e de 500 stems/ha [p. 8–9]; nenhuma relação clara com espécie arbórea foi observada [p. 7].
- Apenas a componente de superfície (surf) da decomposição de Freeman–Durden foi significativa, não a de volume [p. 9].

## 6. Limitações que os próprios autores reconhecem

- Os níveis gerais de ruído podem confundir a análise; parcelas maiores seriam custosas, e uma alternativa seria agregar várias parcelas em povoamentos homogêneos maiores [p. 10].
- A coerência interferométrica não foi avaliada, apesar do potencial em banda L [p. 10].
- Clima e umidade não foram investigados: as duas cenas foram escolhidas sem precipitação e com fenologia semelhante, então os resultados podem não se generalizar a condições de umidade, congelamento ou datas muito diferentes [p. 10].
- Usar um único modelo para crescimento e para grandes perdas florestais pode ser desvantajoso; modelos separados podem ser preferíveis [p. 6].
- Erros sistemáticos (por exemplo, efeito de espécie) podem ficar ocultos nas estimativas de mudança, pois o mesmo erro pode aparecer nas duas datas [p. 7].
- São necessárias mais parcelas ou parcelas maiores para explicar as diferenças entre os modelos 3 e 4 [p. 7].

## 7. O que serve ao projeto e o que não serve

- Serve: o desenho de estimar ΔAGB diretamente por regressão com preditores pareados nas duas datas e validar por LOOCV é replicável em talhões de silvicultura em Goiás [p. 4–6].
- Serve: a comparação entre polarizações cruzadas, co+cruzadas, Freeman–Durden e RVI oferece um protocolo de quatro modelos para testar se a polarimetria agrega precisão, e o RVI é uma razão, portanto menos sensível a topografia e a erros de calibração [p. 5].
- Serve: o uso de variáveis de estrutura (hL, BA, densidade de fustes) para mapear onde a sensibilidade ao AGB se perde é um método direto para investigar saturação em povoamentos plantados [p. 6–8].
- Não serve diretamente: o artigo trata de floresta hemi-boreal conífera no sul da Suécia, com 46 parcelas e apenas duas datas; não há carbono, estoque de carbono nem conversão de biomassa em carbono (não informado), nem qualquer dado de Goiás ou de plantações tropicais [p. 3–4].

## 8. Frases citáveis (literais)

- "We conclude that by using fully polarimetric SAR images, forest biomass changes can be estimated more accurately compared to using single- or dual-polarization images." [p. 1]
- "The saturation point was shifted upwards by adding more polarizations, with the highest saturation point around 200 tons/ha, which is higher than the commonly cited 100 tons/ha for the L-band." [p. 7]
