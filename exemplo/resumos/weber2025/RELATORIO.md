# RELATÓRIO — Weber et al. (2025)

> Fonte: `TEXTO.txt` (texto integral; páginas indicadas como [p. N] são as do arquivo, marcadas `[página N]`).

## 1. Referência

WEBER, Manuel; BENEKE, Carly; WHEELER, Clyde. **Unified Deep Learning Model for Global Prediction of Aboveground Biomass, Canopy Height and Cover from High-Resolution, Multi-Sensor Satellite Imagery**. Descartes Labs Inc., Santa Fe, NM, EUA, 3 jan. 2025 [p. 1].

- **Revista:** não informada no texto. O arquivo é a versão de preprint arXiv:2408.11234v2 (31/12/2024) [p. 1]. O DOI do pedido (10.3390/rs17091594) indica, pelo padrão do identificador, *Remote Sensing* (MDPI) 17(9):1594 — dedução a partir do DOI, não do texto.
- 27 páginas; preprint com revisão por pares não indicada no arquivo.

## 2. Pergunta do estudo

Um único modelo de aprendizado profundo, treinado com dados GEDI amostrados globalmente e imagens multissensor de 10 m, consegue prever simultaneamente biomassa acima do solo (AGBD), altura do dossel (CH) e cobertura do dossel (CC), com incertezas, de forma globalmente escalável e mais acurada que modelos de variável única do estado da arte? [p. 1–3]

## 3. Área e dados

**Local.** Global. Amostragem uniforme sobre terra firme na faixa de latitude [−51,6°, 51,6°] e longitude [−180°, 180°] [p. 5]. Mapas globais cobrem 57° S a 67° N, limite dado pela disponibilidade de Sentinel-1 [p. 16]. Estudos independentes: 8 parcelas na África Central e 5 no Sul da Ásia [p. 13]; sítios NEON nos estados AL, CA, FL, GA, OR, UT, VA e WA (EUA) [p. 15]; área de desmatamento no Brasil a 59°26'46" W, 7°1'4" S, 507 kha [p. 18].

**Período.** Compósitos de 2021 (2021/2022 no hemisfério sul); DEM com ano fixo 2000; GEDI aceito até ±1 mês da janela do compósito [p. 6]. Implantação global para 2023 (preenchida com 2021 onde houve falha do Sentinel-1) e implantação anual de 2016 a 2023 em áreas locais [p. 1, p. 16–17]. Na prática, o modelo só é implantável a partir de 2017 por falta de dados de entrada [p. 14].

**Sensores / fontes.** Sentinel-2 (6 bandas: RGB, NIR, SWIR1, SWIR2), Sentinel-1 (VV e VH), SRTM (altitude, aspecto, declividade) e coordenadas geográficas codificadas em [−1, 1] → tensor de 13 canais, todos reamostrados para 10 m [p. 5, p. 7]. Verdade de campo: GEDI L2a (métricas RH, CH = RH98), L2b (CC) e L4a (AGBD), com `l4_quality_flag` = 1 [p. 4–6].

**Amostras.** 276.766 amostras criadas, das quais 14.745 (5%) separadas como teste [p. 6]; cada amostra é um tile de 512×512 pixels (dividido em 4 sub-tiles de 256×256 no treino, totalizando ~1 M de amostras) [p. 2, p. 5]; exigência de >20 footprints GEDI por tile [p. 5–6]; ~67 M (3,8 M) medições de campo no treino (teste) [p. 2, p. 6]; 13,8 M de cenas processadas [p. 6]; média de 50 cenas por amostra [p. 6].

> **Inconsistência interna:** na p. 11 o conjunto de teste é descrito como tendo "13,8 M individual GEDI footprints", valor que na p. 6 corresponde ao total de cenas, não a footprints (lá, teste = 3,8 M pontos). Usar 3,8 M.

## 4. Método

1. **Compósitos e fusão multissensorial:** máscara de nuvem/sombra própria + mediana de todas as cenas Sentinel-2 na janela sazonal (jun–ago no hemisfério norte, dez–fev no sul, 6 meses nos trópicos); mesma composição aplicada a VV/VH sem máscara de nuvem; camadas reamostradas por interpolação bilinear para 10 m e empilhadas em 13 canais [p. 5–6].
2. **Arquitetura:** CNN com encoder ResNet-50, decoder em pirâmide de features (FPN, dimensão fixa 128) e 6 cabeças de predição (3 variáveis + 3 incertezas), cada cabeça com 3 convoluções 1×1; 28,71 milhões de parâmetros [p. 7].
3. **Treino fracamente supervisionado (teacher–student):** como os rótulos GEDI são esparsos (1 footprint de 25 m atribuído a 1 pixel de 10 m), gera-se um mapa-alvo contínuo com rótulos "soft" por similaridade espectral de cosseno nas 6 bandas do Sentinel-2 (razão hard/soft ≈ 1/1000); duas redes idênticas trocam de papel a cada iteração, com decaimento exponencial do peso dos soft labels (1 → 1e−3 → 1e−2) [p. 7–9]. Perda = log-verossimilhança negativa gaussiana com termo λσ² e balanceamento por pixel de hard/soft [p. 9].
4. **Treino em 3 etapas + avaliação:** (i) 40 épocas no dataset completo, batch 72, 4 GPUs A10G, Adam, lr 1e−7→1e−4; (ii) cabeças 1–3 congelando encoder/decoder, em subconjuntos balanceados por PDF inversa; (iii) cabeças de incerteza [p. 9–10]. Avaliação no teste global (distribuição original e reamostrada uniforme) e em dados independentes (Rodda et al. para AGBD; NEON para CH), mais fine-tuning em 7 métricas RH para equações alométricas locais [p. 11–15, p. 19].

## 5. Resultados principais

**Resumo do abstract:** MAE de 26,1 Mg/ha (3,7 m; 9,9%) e RMSE de 50,6 Mg/ha (5,4 m; 15,8%) para AGBD (CH, CC) [p. 1]. Esses valores são os da **distribuição original** do teste, não da uniformizada (ver tabela).

**Teste global GEDI (14.745 amostras)** [p. 11]:

| Variável | Distribuição | corr | ME | MAE | MAPE | RMSE |
|---|---|---|---|---|---|---|
| AGBD (Mg/ha) | original | 0,83 | 10,75 | 26,07 | 166,60% | 50,59 |
| AGBD (Mg/ha) | uniforme | 0,70 | −10,83 | 62,95 | 48,03% | 86,74 |
| CH (cm) | original | 0,85 | 83,51 | 370,95 | 35,19% | 543,81 |
| CH (cm) | uniforme | 0,80 | −20,09 | 455,46 | 27,56% | 624,94 |
| CC (%) | original | 0,88 | −1,92 | 9,86 | 104,10% | 15,75 |
| CC (%) | uniforme | 0,75 | −3,40 | 13,92 | 45,26% | 18,68 |

Após reamostragem uniforme restam 200 mil a 450 mil pontos, conforme a variável [p. 11]. O MAPE de 166,60% para AGBD na distribuição original é incompatível com MAE/RMSE e com o abstract — provável erro de tabela; não usar sem checar.

**Viés por faixa de valor** [p. 11–12]: superestimativa de AGBD entre 0 e 200 Mg/ha e subestimativa acima de 200 Mg/ha; CH adere bem até 25 m e depois subestima; CC subestima perto de 100% de cobertura. Comparado a Bereczky et al. (2024), desempenho de AGBD é comparável entre 0–200 Mg/ha e melhor acima de 200 Mg/ha; para CH, supera Pauls et al. (2024) em toda a faixa, exceto árvores <10 m [p. 12].

**Validação independente — AGBD (Rodda et al., 13 parcelas, África Central e Sul da Ásia)** [p. 13–14]: ME = −6,46 Mg/ha, MAE = 60,21 Mg/ha, RMSE = 84,95 Mg/ha, R² = 0,39. Total estimado 8,62 Mt contra 8,95 Mt de referência, diferença de 3,63% [p. 14]. Três sítios (Achanakmar, Betul, Yellapur) foram excluídos por subestimativa ligada à composição de 6 meses [p. 14].

**Validação independente — CH (NEON, LiDAR aerotransportado de 1 m, 2021)** [p. 15]: RMSE = 7,46 m, ME = 0,17 m, MAE = 5,57 m, R² = 0,51; erro absoluto quase sempre <5 m até 50 m de altura.

**Detecção de mudança (Brasil, 2017–2023)** [p. 18]: perda de cobertura arbórea de 103,3 kha contra 101,2 kha do Global Forest Watch (diferença de 2,1%; concordância média dentro de 10%); perda de biomassa de 14,9 Mt, equivalente a 25,66 Mt de CO₂.

**Fine-tuning local (7 métricas RH + equações alométricas de Rodda et al.)** [p. 19]: MAE cai 15,3% para 50,96 Mg/ha, RMSE cai 16,2% para 71,18 Mg/ha e R² sobe de 0,39 para 0,58.

**RMSE por tipo funcional de planta** [p. 22]: AGBD (Mg/ha) 66,98 DBT; 84,33 EBT; 66,53 ENT; 24,30 GSW. CH (cm) 585,31; 700,01; 608,94; 318,72. CC (%) 21,82; 21,53; 21,19; 9,05.

## 6. Limitações reconhecidas pelos autores

- **Saturação e subestimativa em valores altos de AGBD e CH**, atribuídas à falta de dados de treino nessas faixas e à saturação do sinal de entrada; no caso da AGBD soma-se a incerteza crescente da verdade de campo [p. 11, p. 12, p. 20].
- **A verdade de campo do GEDI L4a é incerta e a incerteza cresce com a AGBD**; o treino trata os alvos como exatos, o que impede representar mapeamentos descontínuos e provavelmente contribui para a saturação [p. 5, p. 22].
- **Calibração das incertezas imperfeita:** as bandas de 1σ são superestimadas em valores baixos (cobertura >68%) e subestimadas em valores altos (<68%); "we reserve addressing this discrepancy for future work" [p. 12, p. 21].
- **Compósito tropical de 6 meses inclui cenas de árvores sem folha**, causando deslocamento do sinal e subestimativa de AGBD em sítios de floresta decídua; exigiria janela menor, deixada para trabalho futuro [p. 14].
- **Cobertura temporal limitada a 2017 em diante** por disponibilidade de dados de entrada [p. 14]; **cobertura espacial limitada a 57° S–67° N**, pela disponibilidade de Sentinel-1 [p. 16], com treino amostrado apenas até ±51,6° [p. 5].
- **Superestimativa de CH abaixo de 5 m**, atribuída ao número muito pequeno de pontos GEDI <3 m [p. 15].
- **Nenhuma recalibração foi aplicada** nos testes com dados independentes, embora os autores a apontem como necessária e a deixem para trabalhos futuros [p. 14, p. 15].

## 7. O que serve ao projeto e o que não serve

**Serve**

1. **Arquitetura e pipeline replicáveis em Goiás:** fusão S1 (VV/VH) + S2 (6 bandas) + SRTM + coordenadas em 13 canais a 10 m, com uma única rede prevendo AGBD, CH e CC e suas incertezas em um passe — desenho diretamente transponível para talhões de silvicultura, inclusive porque o Sentinel-2 cobre Goiás desde 2016 e o artigo mostra implantação histórica anual [p. 1, p. 5, p. 16–17].
2. **Estratégia de transferência para alometrias locais:** o fine-tuning das cabeças RH com equações alométricas regionais reduziu MAE em 15,3% e RMSE em 16,2%, e R² de 0,39 para 0,58, congelando encoder/decoder [p. 19] — é exatamente o tipo de ajuste que o projeto precisa para Eucalyptus/Pinus em Goiás.
3. **Protocolo de validação e contabilidade de carbono:** métricas em distribuição original e uniformizada, erros por faixa de valor e por PFT [p. 11–12, p. 22], além da conversão de perda de biomassa em CO₂ (14,9 Mt → 25,66 Mt) e da comparação com o Global Forest Watch [p. 18] — modelo de como reportar estoque e mudança.
4. **Uso das incertezas como filtro:** o modelo entrega σ por pixel e o artigo documenta onde a cobertura de 1σ falha [p. 12, p. 21], o que permite mascarar estimativas não confiáveis em vez de usá-las cegamente.

**Não serve**

1. **Não há silvicultura:** o treino e a avaliação são florestas naturais e biomas globais, com PFTs DBT/EBT/ENT/GSW [p. 12–13, p. 22]; plantios de eucalipto (dossel baixo, rotação curta, talhadia, espaçamento regular) estão fora do domínio de calibração das alometrias do GEDI L4a [p. 4].
2. **Nenhum dado de Goiás ou do Cerrado:** o único exemplo brasileiro é desmatamento na Amazônia (7° S) [p. 18]; não há parcela, inventário ou LiDAR de referência no Brasil.
3. **Resolução e footprint não servem para escala de talhão/parcela:** pixel de 10 m e alvo derivado de footprint GEDI de 25 m atribuído a um único pixel [p. 6] impedem estimativas por linha de plantio ou por parcela pequena; a comparação com NEON mostra erro absoluto de até ~5 m em altura [p. 15].
4. **Pipeline não reprodutível de forma aberta:** máscara de nuvem proprietária, sistema de tiling e plataforma Descartes Labs, além de GPU A10G e ~1 M de amostras [p. 5–7, p. 10]; não há código nem pesos disponibilizados no texto.

## 8. Duas frases citáveis (literais)

> "The model achieves a mean absolute error for AGBD (CH, CC) of 26.1 Mg/ha (3.7 m, 9.9 %) and a root mean squared error of 50.6 Mg/ha (5.4 m, 15.8 %) on a globally sampled test dataset, demonstrating a significant improvement over previously published results." [p. 1]

> "However, the fine-tuned model decreases the MAE by 15.3 % to 50.96 Mg/ha and the RMSE by 16.2 % to 71.18 Mg/ha." [p. 19]
