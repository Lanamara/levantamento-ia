# RELATÓRIO — Xiandie Jiang (2023)

## 1. Referência

Jiang, X.; Li, D.; Li, G.; Lu, D. (2023). *Eucalyptus carbon stock estimation in subtropical regions with the modeling strategy of sample plots – airborne LiDAR – Landsat time series data*. Forest Ecosystems, 10, 100149. DOI: 10.1016/j.fecs.2023.100149.
O `TEXTO.txt` está integral (17 páginas, incluindo referências) e corresponde ao DOI acima [p. 1–17].

## 2. Pergunta do estudo

Se um modelo de estoque de carbono de eucalipto baseado apenas na idade do povoamento (em meses ou em anos), calibrado pela cadeia parcelas – LiDAR aerotransportado – série temporal Landsat, mantém acurácia quando transferido no tempo e no espaço em regiões subtropicais da China [p. 1, p. 3].

## 3. Área e dados

- **Local:** Yunxiao County, sudeste de Fujian (1.166 km²; 21,3 °C; 1.730 mm/ano) e Gaofeng Forest Farm, norte de Nanning, Guangxi (21,6 °C; 1.300 mm/ano) [p. 4].
- **Período:** LiDAR aéreo de Yunxiao em julho/2021 e de Gaofeng em janeiro/2018; parcelas medidas em janeiro, julho e dezembro/2021 (Yunxiao) e em janeiro/2018 e janeiro/2020 (Gaofeng) [p. 4–5].
- **Sensores/fontes:** LiDAR aerotransportado com >40 pontos·m⁻² (Yunxiao) e 8 pontos·m⁻² (Gaofeng) [p. 5]; série temporal Landsat NDVI de 30 m — Yunxiao de agosto/1986 a janeiro/2021, Gaofeng de maio/1986 a janeiro/2021 [p. 5–6]; mapas de eucalipto com acurácia do produtor de 88,2% e do usuário de 89,6% (Yunxiao) e 90,1% (2018) e 88,0% (2020) em Gaofeng [p. 5].
- **Amostras:** 46 parcelas de campo em Yunxiao e 58 em Gaofeng, de 20 × 20 m, medidas com DBH e equações alométricas [p. 4–5]; após o upscaling por LiDAR, 216 amostras de 30 × 30 m (110 em Yunxiao, 106 em Gaofeng) [p. 7]. As contagens por data divergem entre Table 1, Table 3 e o texto [p. 4–5].

## 4. Método

- **Carbono por parcela:** equações alométricas por espécie (Eucalyptus: W = 0,138 D^2,436; Chinese fir: W = 0,096 D^2,410) e coeficiente de carbono de 0,4764 e 0,5127, respectivamente; conversão para t·ha⁻¹ [p. 5].
- **Sítios típicos:** métricas de altura extraídas do CHM de 1 m em janela de 20 × 20 m; correlação de Pearson + stepwise regression (p = 0,05/0,10) e validação leave-one-out [p. 5].
- **Modelo regional:** amostras de 30 × 30 m estratificadas por idade, 60% treino e 40% teste [p. 6]; idade em meses obtida de NDVI Landsat por random localization segmentation + teste de Chow [p. 6]; regressão linear simples com idade log-transformada, comparando meses × anos e cenários com e sem estratificação por região [p. 6].
- **Transferência e erro:** modelos de julho/2021 aplicados a janeiro e dezembro/2021 e de janeiro/2018 a janeiro/2020 (escala temporal); Gaofeng → Yunxiao (escala espacial), com DTPS para comparar estimativas [p. 6]; propagação de erro avaliada por Monte Carlo com 1.000 simulações [p. 15].

## 5. Resultados principais

- **Sítios típicos (LiDAR):** R²v = 0,84, RMSE 9,53 t·ha⁻¹ e RMSEr 16,93% em Yunxiao; R²v = 0,90, RMSE 7,01 t·ha⁻¹ e RMSEr 14,56% em Gaofeng [p. 6–7]. HME (altura média) e H55 foram os preditores mais importantes [p. 6].
- **Amostras regionais:** 216, com carbono entre 1,4 e 99,0 t·ha⁻¹, média 52,6 e desvio-padrão 18,9 t·ha⁻¹ [p. 7].
- **Modelos por idade, com estratificação:** modelo em meses com RMSE 6,51 t·ha⁻¹ (Yunxiao) e 6,33 t·ha⁻¹ (Gaofeng) [p. 7]; RMSEr de 12,65% e 12,00%, contra 13,76% e 13,78% dos modelos em anos [p. 8]. Sem estratificação: RMSE 7,52 t·ha⁻¹ (meses) e 7,92 t·ha⁻¹ (anos) [p. 8].
- **Plantios jovens (<24 meses):** o modelo em meses reduziu o RMSEr em 16,45% (Yunxiao) e 8,01% (Gaofeng) com estratificação; 6,17% e 3,44% sem estratificação [p. 8]. Acima de 48 meses, meses e anos se equivalem [p. 8].
- **Transferência temporal:** RMSE de 7,63 t·ha⁻¹ (janeiro/2021) e 8,50 t·ha⁻¹ (dezembro/2021) ao aplicar o modelo de julho/2021 em Yunxiao [p. 12].
- **Transferência espacial (Gaofeng → Yunxiao):** RMSE aumentou 2,54 t·ha⁻¹ e RMSEr 4,94% no modelo em meses; 0,65 t·ha⁻¹ e 3,22% no modelo em anos [p. 9]. Para estoque < 20 t·ha⁻¹, RMSE 17,74 t·ha⁻¹ (RMSEr 121,01%) do modelo transferido contra 9,17 t·ha⁻¹ (62,55%) do local [p. 12].
- **Produto de idade:** R² 0,91 e RMSE de 13,3 meses [p. 6]; 6,06 meses após remover cinco amostras mal classificadas [p. 12].
- **Mudança de estoque:** plantios de 1–3 anos em Yunxiao ganharam até 20 t·ha⁻¹ em um ano; aos 144 meses o ganho caiu para 2 t·ha⁻¹ por ano [p. 10]. Em Gaofeng, perdas > 45 t·ha⁻¹ por desmatamento [p. 10].
- **Monte Carlo (1.000 simulações):** RMSEr médio de 13,97% (Yunxiao) e 15,1% (Gaofeng) validando com parcelas de campo [p. 15]; erro das parcelas para o LiDAR de cerca de 15%–17% [p. 15].

## 6. Limitações que os próprios autores reconhecem

- A idade vem de produto com RMSE de 13,3 meses; para eucalipto com menos de 24 meses, erro de 12 meses na idade inflou o erro do carbono em quase 20%, enquanto acima de 100 meses o desvio não passou de 4 t·ha⁻¹ [p. 12].
- Nuvens frequentes no subtropical/tropical reduzem as imagens Landsat de qualidade e rebaixam a acurácia da idade; sugerem combinar Landsat, Sentinel-2 e Sentinel-1 [p. 12].
- A transferência espacial foi pior que a temporal; é preciso cautela onde plantios jovens dominam, e os autores recomendam incorporar dados de solo e clima ao modelo [p. 12].
- O carbono regional usou estimativas LiDAR como referência em vez de parcelas de campo, e parcelas em sítios típicos continuam necessárias; a propagação de erros ainda precisa ser mais bem quantificada [p. 12, p. 15].
- Modelo com idade como único preditor não atende locais diferentes [p. 8].

## 7. O que serve ao projeto e o que não serve

- **Serve:** a estratégia em dois estágios (parcelas → LiDAR → série temporal Landsat) para multiplicar amostras em escala regional, com evidência de que o erro da primeira etapa não se acumula integralmente (RMSEr 13,97% e 15,1%) [p. 15].
- **Serve:** idade em meses como preditor para eucalipto jovem (<24 meses) e a exigência de estratificação regional; o alerta de que a transferência espacial falha justamente em estoques < 20 t·ha⁻¹ [p. 8, p. 12].
- **Serve:** referências de acurácia (RMSEr 12,0%–16,9%) e desenho de validação (leave-one-out nas parcelas, divisão 60/40 nas amostras LiDAR, DTPS entre cenários) [p. 5–8].
- **Não serve:** equações alométricas e coeficientes de carbono são de espécies chinesas (0,4764 e 0,5127) [p. 5]; o estudo usa apenas LiDAR e Landsat NDVI, sem Sentinel-1/2, GEDI, solo ou clima [p. 5, p. 12]; clima e manejo (rotação de 6–10 anos) são de outro contexto [p. 2].

## 8. Frases citáveis (literais)

- "Therefore, LiDAR-predicted carbon stock at the local scale is valuable for enlarging the number of samples for model development and validation at the regional scale." [p. 15]
- "However, both the month-based and year-based models expressed relatively poor transferability at a spatial scale." [p. 1]
