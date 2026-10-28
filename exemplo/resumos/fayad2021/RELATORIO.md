# RELATÓRIO — Ibrahim Fayad (2021)

## 1. Referência

Ibrahim Fayad, Dino Ienco, Nicolas Baghdadi, Raffaele Gaetano, Clayton Alcarde Alvares, Jose Luiz Stape, Henrique Ferraço Scolforo, Guerric Le Maire (2021). "A CNN-based approach for the estimation of canopy heights and wood volume from GEDI waveforms". *Remote Sensing of Environment*, v. 265, 112652. DOI: 10.1016/j.rse.2021.112652 [p. 1].

O `TEXTO.txt` está completo (páginas 1 a 16, incluindo referências) e corresponde ao DOI informado [p. 1, p. 16].

## 2. Pergunta do estudo

É possível estimar altura dominante (Hdom) e volume de madeira (V) de plantios de Eucalyptus diretamente das formas de onda do GEDI, sem calcular métricas, com precisão comparável à de um modelo Random Forest baseado em métricas, e generalizar esse modelo para regiões distantes [p. 3]?

## 3. Área e dados

- **Local:** cinco regiões produtoras de Eucalyptus no Brasil — Maranhão (MA), Bahia (BA), Espírito Santo (ES), Mato Grosso do Sul (MS) e São Paulo (SP) —, ao longo de um gradiente latitudinal de 2°15′S a 24°43′S [p. 3]. Goiás não está entre as regiões estudadas [p. 3].
- **Período:** footprints GEDI adquiridos entre 20 de abril e 4 de setembro de 2019; inventários de campo da Suzano com diferença máxima de 2 meses em relação à passagem do satélite [p. 4].
- **Sensores e fontes:** GEDI a bordo da ISS, produtos L1B (waveforms geolocalizadas) e L2A (métricas); três lasers, oito tracks, pegada de 25 m de diâmetro, frequência de 242 Hz, até 1246 bins, resolução vertical de 1 ns (15 cm) [p. 4]. Inventário florestal em 566 talhões, com 2 a 8 parcelas permanentes de ~400 m² por talhão (30 a 100 árvores, média de 58) [p. 4].
- **Amostras:** 6166 footprints sobre os 566 talhões, dos quais 5682 utilizáveis após filtragem [p. 5]. Na validação cruzada de 5 folds, em média 4452 footprints para treino e 1065 para teste [p. 8].

## 4. Método

1. **Abordagem metric-free com duas famílias de CNN.** A 1D-CNN trata a waveform como sinal sequencial (10 blocos, 8 com convolução, kernel 3); a 2D-CNN reorganiza a waveform em matriz de ~35×35 (raiz quadrada do número de bins) para aumentar o contraste interno do sinal [p. 6–7].
2. **Regressão multi-output.** Um único modelo estima Hdom e V ao mesmo tempo, com perda igual à soma das MAE das duas variáveis e dois neurônios de saída [p. 7].
3. **Quatro variantes testadas:** CNN1D_s e CNN1D_f (waveform subset, 1225 amostras, e full, 1444 amostras, em representação 1D) e CNN2D_s e CNN2D_f (as mesmas entradas em representação 2D) [p. 8].
4. **Treino e comparação.** Adam com learning rate 1×10⁻⁴, batch 64, dropout 0.2; validação cruzada de 5 folds mantendo todos os footprints de um mesmo talhão numa só partição; métricas R², RMSE e RMSPE; baseline Random Forest com 500 árvores e métricas RHn (10% a 100%, passo de 10%) do algoritmo a1; experimentos de transferência espacial treinando em MS e em MS+SP, com rand.t test (199 permutações, α = 0.05) [p. 8–9].

## 5. Resultados principais

- **Hdom, saída única:** RF com RMSE de 1.45 m (R² = 0.92); CNN1D_s 1.73 m (R² = 0.89); CNN1D_f 1.94 m (R² = 0.86); CNN2D_s 1.54 m (R² = 0.90); CNN2D_f 1.61 m (R² = 0.90) [p. 9].
- **V, saída única:** RF com RMSE de 27.61 m³·ha⁻¹ (R² = 0.88); CNN1D_s 30.08 (R² = 0.85); CNN1D_f 33.33 (R² = 0.82); CNN2D_s 28.42 (R² = 0.87); CNN2D_f 27.76 m³·ha⁻¹ (R² = 0.88) [p. 9].
- **Multi-output:** RF com 1.47 m (R² = 0.92) para Hdom e 27.60 m³·ha⁻¹ (R² = 0.88) para V; as CNN ficaram entre 1.53 m (CNN2D_s) e 2.02 m (CNN1D_f) para Hdom e entre 26.83 m³·ha⁻¹ (CNN2D_s) e 34.83 m³·ha⁻¹ (CNN1D_f) para V [p. 9].
- **Por região, Hdom:** RMSPE de 6.8% a 7.9% com CNN e de 6.8% a 8.2% com RF; o pior caso foi a BA, com 1.79 m (RMSPE 11.4%, R² = 0.70) na CNN e 1.71 m (RMSPE 11.7%, R² = 0.67) no RF; em MA a CNN foi melhor (1.48 m contra 1.67 m) e em MS o RF foi melhor (1.35 m contra 1.45 m) [p. 9].
- **Por região, V:** RMSPE de 15.3% a 21.8% com CNN e de 16.1% a 22.3% com RF em ES, SP e MS; BA com 26.4% (R² = 0.71) na CNN e 26.0% (R² = 0.73) no RF; MA foi a pior região, com 30.32 m³·ha⁻¹ (RMSPE 24.4%, R² = 0.65) na CNN contra 35.92 m³·ha⁻¹ (RMSPE 37.6%, R² = 0.50) no RF [p. 9–10].
- **Síntese da discussão:** RMSPE entre 7.96% e 9.95% para Hdom e entre 21.45% e 32.02% para V com as CNN, contra 7.45% e 22.46% com o RF [p. 11].
- **Transferência espacial, Hdom:** treinando só em MS, o RMSE da CNN subiu de 5 cm (ES) a 44 cm (MA) e o do RF de 5 cm (BA) a 28 cm (ES); no cenário MS→SP a CNN fez 2.07 m e o RF 1.56 m (R² = 0.86 e 0.92) [p. 10, p. 12].
- **Transferência espacial, V:** MS→SP com RMSE de 44.31 m³·ha⁻¹ (CNN) e 36.33 m³·ha⁻¹ (RF); em MA o RMSE passou de 31.07 m³·ha⁻¹ (treino só MS) para 39.59 m³·ha⁻¹ (treino MS+SP), com R² de 0.40 [p. 12–13].
- **Custo computacional:** pré-processamento da CNN2D abaixo de 2 s (~3340 waveforms/s), treino de ~12 min e inferência abaixo de 1 min; o RF exigiu horas de pré-processamento e ~3 min de treino [p. 12, p. 14].
- **Tamanho dos modelos:** a 2D-CNN tem cerca de 1 milhão de parâmetros e a 1D-CNN cerca de 7 milhões [p. 12].

## 6. Limitações que os próprios autores reconhecem

- O V só é estimado com boa acurácia em regiões com relação alométrica Hdom–V semelhante à do treino; os autores atribuem isso a uma limitação inerente ao LiDAR de forma de onda, que não mede volume de tronco [p. 13].
- As formas de onda não carregam informação suficiente sobre o volume do tronco, porque medem apenas a estrutura vertical dentro da pegada [p. 13].
- As CNN exigem procedimento de treino e otimização de hiperparâmetros mais sofisticados e treinam mais devagar que o RF (12 min contra 3 min) [p. 12].
- Acrescentar uma região ao treino não garante ganho: o RMSE de V em MA subiu de 31.07 para 39.59 m³·ha⁻¹ ao somar SP ao treino [p. 11, p. 13].
- A acurácia da CNN para Hdom variou conforme a estrutura florestal entre treino e teste, com melhores resultados quando as alturas das árvores eram semelhantes [p. 1, p. 13].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o desenho metodológico de CNN metric-free sobre waveforms L1B do GEDI, que dispensa a escolha de algoritmo de métricas e serve de alternativa para estimar altura de dossel em talhões de silvicultura [p. 6–7, p. 11].
- **Serve:** a evidência de que a estimativa de V (e, por extensão, de biomassa e carbono) depende da relação alométrica local, o que justifica calibração e validação específicas para Goiás em vez de transferir modelos de outras regiões [p. 13].
- **Não serve:** o artigo não estima biomassa nem estoque de carbono, apenas altura dominante e volume comercial de madeira [p. 5, p. 13].
- **Não serve:** não há dado multissensorial nem área de Cerrado ou de Goiás — o estudo usa somente GEDI L1B/L2A em plantios clonais homogêneos de Eucalyptus nas cinco regiões descritas [p. 3–4].

## 8. Frases citáveis (literais)

- "To avoid metric computation, we leverage deep learning techniques and, more in detail, convolutional neural networks with the aim to analyze the GEDI Level 1B geolocated waveforms." [p. 1]
- "For both approaches, the successful transfer of the model, as stated previously, relies on the constancy of the allometric relationship of Hdom and V between GEDI data from the training and the testing sites." [p. 13]
