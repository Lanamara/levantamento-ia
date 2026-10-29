# RELATÓRIO — Ibrahim Fayad (2021)

## 1. Referência

Ibrahim Fayad, Nicolas N. Baghdadi, Clayton Alcarde Alvares, Jose Luiz Stape, Jean Stéphane Bailly, Henrique Ferraço Scolforo, Mehrez Zribi e Guerric Le Maire (2021). "Assessment of GEDI's LiDAR Data for the Estimation of Canopy Heights and Wood Volume of Eucalyptus Plantations in Brazil". *IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing*, vol. 14, pp. 7095–7110. DOI 10.1109/JSTARS.2021.3092836.

O `TEXTO.txt` está completo (16 páginas, Introdução ao fim das biografias) e corresponde ao DOI informado. Não há truncamento.

## 2. Pergunta do estudo

Qual é a acurácia dos dados LiDAR do GEDI na estimativa da altura dominante (Hdom) e do volume de madeira (V) de povoamentos de Eucalyptus no Brasil, e como essa acurácia depende das métricas usadas, do tipo de modelo (linear ou não linear), do algoritmo de processamento da forma de onda e de características de aquisição?

## 3. Área e dados

- Local: quatro regiões do Brasil — Bahia & Espírito Santo, Mato Grosso do Sul, São Paulo e Maranhão —, em gradiente latitudinal amplo e com diferentes climas e solos [p. 2]. **Nenhum sítio em Goiás.**
- Povoamentos: clones e híbridos de *E. grandis* e *E. urophylla*, 1000–1667 árvores/ha, corte a cada 6–7 anos, produtividade média de 40 m³/ha/ano (80% dos talhões entre 30–50 m³/ha/ano) [p. 2]; volume na colheita de 180–300 m³/ha e Hdom de 20–35 m [p. 2–3].
- Sensor: GEDI (LiDAR espacial na ISS), laser de 1064 nm, pegada de 25 m de diâmetro, 242 Hz, 1246 bins, resolução vertical de 1 ns (15 cm), alcance máximo de 186,9 m [p. 3]. Produtos L1B e L2A do LP DAAC (nenhuma métrica do L2B foi usada) [p. 5].
- Amostras: 6166 pegadas adquiridas entre abril e setembro de 2019, das quais 92,15% aproveitáveis [p. 6]; 566 talhões de Eucalyptus [p. 6]; 5517 tiros GEDI efetivamente analisados [p. 14].
- Inventário: parcelas permanentes de ~400 m² com 30–100 árvores (média de 58), densidade de uma parcela por 10 ha, inventário a menos de dois meses da passagem do GEDI [p. 6–7].
- Auxiliar: DEM SRTM de 30 m, do qual se derivaram slope (S), Terrain Index (TI) e roughness [p. 7].

## 4. Método

- Extração de métricas da forma de onda (RHn de 10% a 100%, toploc, botloc, Wext, Leadext, Trailext, RHpn com 1 < p ≤ 3) em seis algoritmos de processamento (a1 a a6), com a posição do solo definida pelo campo SM (último modo detectado) ou pelo modo mais forte entre os dois últimos (HL2M) [p. 5–6].
- Para Hdom: seis modelos lineares da literatura (eq. 3–8), regressão linear stepwise (SRH) e random forest (RFH, 100 árvores) [p. 8].
- Para V: duas funções de potência em Hdom (eq. 9 e 10), stepwise (SRV) e random forest (RFV) [p. 8].
- Validação cruzada 5-fold com separação por talhão (pegadas do mesmo talhão só em treino ou só em validação), avaliada por R², bias, RMSE, RMSPE e AIC [p. 8].

## 5. Resultados principais

- Modelos lineares (eq. 3–8), algoritmo a1: RMSE de 1,70 a 2,31 m e R² de 0,80 a 0,89; o melhor foi a eq. 8 (RMSE = 1,70 m, R² = 0,89) [p. 9]. Terreno (TI, S) não trouxe ganho significativo [p. 9].
- SRH (stepwise): RMSE = 1,44 m e R² = 0,93, com RH90, RH10, RH80 e RH100 como variáveis relevantes [p. 9]. Só com RH90: RMSE = 1,63 m e R² = 0,90; com RH90 + RH1,8¹⁰: RMSE = 1,5 m e R² = 0,91 [p. 9].
- Média das estimativas por pegada (SRH): RMSE = 1,33 m e R² = 0,93; média por talhão: RMSE = 1,32 m e R² = 0,93 [p. 12]. RMSPE de 7,1% para Hdom [p. 12].
- Algoritmos: nos modelos lineares, RMSE de 2,40 m (R² = 0,78, a3) a 5,06 m (R² = 0,02, a5) [p. 10]; usando só Wext com a5, RMSE = 4,38 m e R² = 0,26 [p. 11]. Com SRH e RFH, a5 caiu para 1,6 m (R² = 0,90) e 1,80 m (R² = 0,88) [p. 11]. O a5 teve RMSE ~16% maior que o a1 [p. 14].
- Escolha do retorno de solo: ganho de 12 a 20 cm de RMSE em Hdom com HL2M [p. 11]; sem efeito significativo em V [p. 12].
- Volume: os quatro modelos ficaram entre RMSE = 24,39 e 27,45 m³/ha e R² de 0,87 a 0,90 [p. 11]; SRV foi o melhor, com RMSE = 24,39 m³/ha e R² = 0,90 (23,93 m³/ha e R² = 0,91 na média por talhão) [p. 12]; RMSPE de 20,4% [p. 12].
- Erro relativo em V: ~18% para V < 250 m³/ha e ~40% para V > 250 m³/ha, com bias subindo de 2,2 para 26,5 m³/ha [p. 12].
- RH90 explicou mais de 87% da variabilidade de Hdom e mais de 84% da de V [p. 12]; no SRV entraram RH90, RH10, RH30, RH80 e RH20 [p. 14].
- Idade do povoamento como preditor adicional: RMSE de Hdom caiu de 1,33 para 1,18 m (~13%) e o de V de 24,39 para 22,77 m³/ha (~7%) [p. 13].
- Feixes: melhores resultados nos feixes 8, 3 e 4 e pior no feixe 5, com diferença de 46 cm em Hdom e 9 m³/ha em V [p. 14]. O campo `selected_algorithm` indicou o a1 em mais de 99% das pegadas [p. 13].

## 6. Limitações que os próprios autores reconhecem

- Subestimação de V para volumes acima de 250 m³/ha, apesar dos esforços [p. 12], [p. 14].
- Intervalo de até dois meses entre inventário e aquisição, que pode gerar até 50 cm de crescimento em Hdom e 10 m³/ha em V [p. 7].
- Heterogeneidade interna dos talhões: a variabilidade entre parcelas chega a mais de 6 m em alguns casos, o que questiona o uso de médias por talhão [p. 14].
- Um único modelo generalizado para toda a base; modelos treinados localmente reduziram o RMSE de Hdom em até 16 cm e o erro de V em até 12,8 m³/ha [p. 14].
- Propriedades biofísicas do dossel (dimensão de copa, LAI, distribuição de ângulos foliares, mortalidade) não quantificáveis só com GEDI [p. 13].
- Resultados válidos para plantações de Eucalyptus, em terreno plano a suavemente ondulado (declividade média de 4,7 ± 3%) [p. 10], [p. 13].
- O `quality_flag` (0 ou 1) não alterou a acurácia após a filtragem aplicada [p. 14].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o desenho metodológico para validação de LiDAR espacial em silvicultura — métricas RHn, SRH com RH90 como preditor dominante, validação cruzada 5-fold separada por talhão e checagem de sensibilidade a algoritmos (a1–a6) e ao retorno de solo — é diretamente transferível para Eucalyptus em Goiás.
- **Serve:** a ordem de grandeza do erro esperado em plantações brasileiras planas (Hdom ~1,3 m; V ~24 m³/ha, ~20%), útil como referência de comparação para um estudo em Goiás.
- **Serve (parcialmente):** a idade do povoamento como preditor auxiliar (ganho de 13% em Hdom e 7% em V) e a ideia de calibrar modelos futuros de radar (P-band BIOMASS) com GEDI.
- **Não serve:** o artigo não trata de Goiás, não estima biomassa nem estoque de carbono (só volume mercantil de madeira), não faz fusão multissensorial (usa apenas GEDI e SRTM) e não cobre terreno acidentado — logo, não substitui a etapa de biomassa/carbono nem a componente multissensorial do projeto.

## 8. Frases citáveis (literais)

- "The most important GEDI variable for the estimation of Hdom and V is RH90, which explained respectively more than 87% and 84% of the variability of Hdom and V." [p. 12]
- "Finally, given the high accuracy of GEDI data on the estimation of tree heights and volume, GEDI can provide an excellent source of information to calibrate and validate upcoming and future radar missions, such as the upcoming P-band BIOMASS mission." [p. 14]
