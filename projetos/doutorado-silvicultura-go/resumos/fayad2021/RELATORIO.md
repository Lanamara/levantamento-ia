# RELATÓRIO — Ibrahim Fayad (2021)

## 1. Referência

Fayad, Ibrahim; Baghdadi, Nicolas; Alcarde Alvares, Clayton; Stape, Jose Luiz; Bailly, Jean Stéphane; Scolforo, Henrique Ferraço; Cegatta, Italo Ramos; Zribi, Mehrez; Le Maire, Guerric (2021). *Terrain Slope Effect on Forest Height and Wood Volume Estimation from GEDI Data*. Remote Sensing, 13(11), 2136. DOI: 10.3390/rs13112136 [p. 1]. O `TEXTO.txt` está completo (22 páginas, incluindo referências) e corresponde ao DOI indicado.

## 2. Pergunta do estudo

Qual é o efeito da declividade do terreno nas estimativas de altura dominante e de volume de madeira de plantios de Eucalyptus obtidas com dados GEDI, e qual abordagem de correção de declividade produz os melhores resultados [p. 4]?

## 3. Área e dados

- Local: cinco regiões do Brasil — Maranhão, Bahia, Espírito Santo, Mato Grosso do Sul e São Paulo, ao longo de um gradiente latitudinal [p. 4].
- Período: inventários de campo entre 1 de abril e 1 de junho de 2019; tiros GEDI de até dois meses antes ou depois do inventário [p. 5, p. 7].
- Sensores/fontes: GEDI L1B (waveforms brutos) e L2A (métricas de altura), footprint de 25 m, laser de 1064 nm a 242 Hz, resolução vertical de 15 cm (1 ns) [p. 6, p. 7]; SRTM DEM de 30 m para declividade (S) e rugosidade (ROUG) [p. 7].
- Amostras: 168 povoamentos de Eucalyptus; 2.128 tiros GEDI selecionados e 1.477 (~69.4%) retidos após filtragem [p. 7]; parcelas de ~400 m², uma por 10 ha, com 30 a 100 árvores (média de 58) [p. 5].
- Declividade dos povoamentos: 86,4% abaixo de 10%, 11,2% entre 10 e 20% e 2,4% entre 20 e 45% [p. 5].

## 4. Método

- Cinco modelos para altura dominante (Hdom): MH1 (Wext e S, regressão linear), MH2 (RH100 e S), RFHRH (RHn, S e ROUG em Random Forest) e dois modelos de Wang et al. — sRFHRHT+HG (ground return simulado) e fRFHRHT+HG (ground return ajustado) [p. 8, p. 12].
- Quatro modelos para volume (V): MV1 (lei de potência com RH100 e S), RFVRH (RHn, S, ROUG), sRFVRHT+HG e fRFVRHT+HG [p. 12].
- Métricas de Wang et al.: waveform de solo nu simulada por gaussiana cuja largura cresce com a declividade (σs = σb + β·γ·tanθ, β = 0.5, γ = 25 m), alinhada ao waveform pelo botloc, gerando sRHn e sHGn; variante fGHn obtida por decomposição gaussiana automática do ground return original [p. 8–11].
- Random Forest com 500 árvores, validação cruzada de 5 folds mantendo footprints de um mesmo povoamento em uma única partição; métricas R², RMSE, bias e RMSPE [p. 11].

## 5. Resultados principais

- Hdom, declividade 0–10%: MH1 com o pior desempenho, RMSE de 2.06 m; os demais modelos com RMSE entre 1.34 m e 1.42 m e R² entre 0.93 e 0.94 [p. 12, p. 14].
- Hdom, declividade >20%: RMSE de 1.65 m (RFHRH, R² 0.86) a 3.26 m (MH1, R² 0.45); bias de ~1.2 m em MH1 e MH2 e de 0.65 m em RFHRH [p. 13]. Aumento de 14% no RMSE entre 10–20% e >20% [p. 1, p. 19].
- fRFHRHT+HG na classe >20%: RMSE de 1.26 m, R² 0.92, RMSPE de 6% e bias de 0.11 m, sem aumento de erro com a declividade [p. 13, p. 14].
- Diferença mediana (estimado − in situ) de Hdom: MH2 passa de −0.08 m (10–15%) para 1.2 m (>20%); RFHRH de −0.06 m para 0.59 m; modelos de Wang entre −0.25 e 0.17 m [p. 14].
- V, MV1 e RFVRH: RMSE de ~27.5 m³·ha⁻¹ (R² ~0.9) em 0–10% para ~48.7 m³·ha⁻¹ (R² ~0.75) em >20%; bias de 0.21 e −1.60 m³·ha⁻¹ para 13.95 e 11.42 m³·ha⁻¹ [p. 15]. Aumento de 74% no RMSE de RFVRH entre 0–10% e >10% [p. 1, p. 19].
- sRFVRHT+HG: RMSE de 27.57 m³·ha⁻¹ (0–10%), 53.82 m³·ha⁻¹ (10–20%) e 49.12 m³·ha⁻¹ (>20%) [p. 15].
- fRFVRHT+HG: mais preciso, com RMSE de 26.78 m³·ha⁻¹ (R² 0.92) em 0–10% a 36.29 m³·ha⁻¹ (R² 0.86) em >20% [p. 15]; bias estável, de 1.32 a 2.65 m³·ha⁻¹ [p. 15].
- Intercepto da distribuição de erros por declividade: 0.069 para HT100 contra ≈0.003 para sRHT100 e fRHT100 [p. 18, p. 20].
- Conclusão geral: degradação máxima de 1 m na altura para declividades de 20–45% e de no máximo 20 m³·ha⁻¹ no volume [p. 1, p. 20].

## 6. Limitações que os próprios autores reconhecem

- O SRTM DEM de 30 m não é adequado para footprints GEDI de 25 m; seria necessário um DEM mais fino, de 10 m [p. 17–18].
- Poucas aquisições com declividade acima de 20%, sendo necessário avaliar o método de Wang et al. em declividades altas [p. 19].
- A área tem Eucalyptus homogêneo; a distribuição desigual de copas em florestas naturais pode aumentar a incerteza, e os métodos devem ser testados nesses ambientes [p. 19].
- A simulação do ground return usa gaussiana simétrica, mas os retornos de FW LiDAR são assimétricos; uma função lognormal poderia ser mais adequada [p. 18].
- As métricas f dependem de um ground return distinto no waveform, que pode não ser detectável em terreno muito inclinado [p. 20].
- As diferenças de RMSE entre classes de declividade podem vir da proporção maior de dados com V alto nas classes de 10–20% e 20–45% [p. 17].

## 7. O que serve ao projeto e o que não serve

- Serve: o desenho de correção de declividade sobre métricas de waveform (fRHn e fHGn via decomposição gaussiana) é diretamente transferível para estimativas de biomassa com GEDI em Goiás, com ganho de acurácia e remoção do viés ligado à declividade [p. 13, p. 15].
- Serve: a comparação de modelos lineares contra Random Forest e o protocolo de validação (5 folds por povoamento) como referência metodológica para ajuste e validação no projeto [p. 11].
- Serve como alerta: o DEM de 30 m é insuficiente para footprints de 25 m, o que indica a necessidade de DEM de maior resolução no projeto [p. 17].
- Não serve: o artigo estima volume de madeira (V), não biomassa nem estoque de carbono, e trata de plantios de Eucalyptus, não de vegetação nativa de Goiás; além disso, 86,4% dos dados estão em declividades abaixo de 10% e o estudo é monossensor (GEDI), sem fusão multissensorial [p. 5, p. 15].

## 8. Frases citáveis (literais)

- "In this study, there were very few acquisitions with slopes higher than 20%, and while the slope effects were greatly reduced for slope ranges 0–20%, it is necessary to analyze the pertinence of the Wang et al. [26] methodology for high slopes." [p. 19]
- "These results indicate that the 30-m resolution SRTM DEM is not suitable for the 25-m wide GEDI footprints." [p. 19]
