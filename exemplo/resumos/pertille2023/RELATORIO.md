# RELATORIO — Pertille et al. (2023)

## 1. Referência
PERTILLE, Carla Talita; NICOLETTI, Marcos Felipe; DOBNER JR., Mario. **Estimating the commercial volume of a *Pinus taeda* L. plantation using active and passive sensors**. *CERNE*, v. 29, e-013108, 2023. DOI: 10.1590/01047760202329013108.

## 2. Pergunta do estudo
Comparar as estimativas de volume comercial de um povoamento de *Pinus taeda* L. obtidas por inventário florestal tradicional e por imagens de radar (Sentinel-1) e ópticas (Sentinel-2) [p. 2].

## 3. Área e dados
- **Local:** propriedade rural em Rio Negro, Paraná, Brasil (26°11'06"S, 49°33'11"W), Segundo Planalto Paranaense, clima Cfa, precipitação média anual de 1.200 mm; povoamento de 27,5 ha, com árvores de 11 e 12 anos, espaçamento 3 x 2,5 m e 1.333 árvores/ha [p. 2].
- **Período:** inventário de campo em abril de 2021 [p. 2]; imagem Sentinel-1 datada de 10/04/2021 [p. 2] e imagem Sentinel-2 de 04/25/2021 [p. 4].
- **Sensores/fontes:** Sentinel-1 (banda C, modo IW, nível 1C, produto SLC, dupla polarização VV e VH, resolução espacial de 5 a 20 m, resolução temporal de 12 dias; obtida no Alaska Satellite Facility) [p. 2]; Sentinel-2 (13 bandas, 10/20/60 m, reamostrada para 10 m; obtida no portal USGS) [p. 2, 4]; inventário florestal como referência [p. 2].
- **Amostras:** 48 parcelas retangulares de 550 m² [p. 2]; alturas medidas em 20% das árvores de cada parcela [p. 2]; cubagem de 72 árvores de diferentes classes diamétricas [p. 2]. Variáveis extraídas por parcela: 8 variáveis do Sentinel-1 (Tabela 2) [p. 3] e 14 índices de vegetação mais 3 parâmetros biofísicos do Sentinel-2 [p. 4].

## 4. Método
1. **Inventário e volume de referência:** DAP de todas as árvores (fita dendrométrica), altura de 20% delas (hipsômetro Vertex), equação hipsométrica de Curtis para as demais; volume por árvore pela função de afunilamento de 5º grau (modelo Schöpfer) ajustada com dados de cubagem de 72 árvores; volume por parcela como variável dependente (m³ 0,05 ha⁻¹) [p. 2, 4].
2. **Sentinel-1:** processamento no SNAP (recorte da área de interesse, correção orbital, remoção de ruído térmico, calibração sigma, Deburst, filtro Lee para speckle, GR Square Pixel e correção de terreno Range Doppler com interpolação bilinear) para obter os coeficientes de retroespalhamento VH e VV; no SIG, derivação de 8 índices, incluindo mRFDI, RVI, RVIad e as adaptações Ad_1 a Ad_5 [p. 3].
3. **Sentinel-2:** correção atmosférica com Sen2Cor no SNAP e reamostragem das bandas para 10 m; cálculo de 14 índices de vegetação e de 3 parâmetros biofísicos (IAF, FAPAR, FVC) pelo modelo PROSAIL; médias extraídas por parcela com raio de 13,25 m a partir das coordenadas centrais obtidas em campo [p. 4].
4. **Análise:** correlação de Pearson entre variáveis e volume; modelos de regressão por *stepwise* (forward e backward) no R 4.1.2 em três cenários (só Sentinel-2; só Sentinel-1; combinação), selecionados por R² ajustado, Syx%, análise gráfica de resíduos, AIC, BIC e RMSE; comparação dos quatro tratamentos por ANOVA e teste de Tukey, após Shapiro-Wilk [p. 4-5].

## 5. Resultados principais
- Dendrometria do povoamento: DAP médio de 26,3 cm, diâmetro quadrático médio de 26,7 cm, altura total média de 17,4 m, área basal de 39,8 m².ha⁻¹ e volume comercial total de 228,5 m³.ha⁻¹ [p. 5] (Tabela 1: mínimo 172,8 e máximo 273,3 m³.ha⁻¹; desvio-padrão 21,5; CV de 9% para volume) [p. 3].
- Correlações de Pearson entre volume e variáveis imageadas variaram de -0,3622 a 0,3425 [p. 5] (o texto corrido cita -0,3621 a 0,3424) [p. 5].
- Sentinel-1: maior correlação com o mRFDI (0,3317); as demais adaptações foram praticamente nulas (RVIad 0,0130; Ad_1 -0,0131; Ad_2 -0,0132; Ad_3 0,0008; Ad_4 0,0511; Ad_5 0,1031) [p. 5].
- Sentinel-2: melhor índice o DVI (0,3425); em valor absoluto, ARI1 (-0,3622), ARI2 (-0,3275), FVC (0,3355), FAPAR (0,3074) e IRECI (0,3174) [p. 5].
- Foram ajustados 11 modelos. Os modelos só com Sentinel-2 foram superiores, com R² ajustado de 0,51 a 0,40 e Syx% de 3,66% a 8,97%; a combinação Sentinel-1 + Sentinel-2 ficou com R² ajustado abaixo de 0,30 e Syx% acima de 10%; os modelos só com Sentinel-1 tiveram o pior ajuste [p. 5]; o modelo 9 (Sentinel-1 puro) teve R² ajustado de 0,17 e Syx de 11,0% [p. 6].
- Melhor modelo (modelo 1: ARI1, ARI2, CRI2 e FVC): R² ajustado de 0,51, Syx de 3,6%, AIC de 134,8 e BIC de 185,3 [p. 6]. O modelo 2 (ARI1, ARI2, CRI2 e IAF) ficou com R² ajustado de 0,48 e Syx de 3,7% [p. 6].
- Volume médio por parcela (m³ 0,05 ha⁻¹), resumo: inventário 12,56±1,17; Sentinel-2 12,56±1,03; Sentinel-1 12,56±0,94 [p. 1]. A Tabela 6, porém, traz 12,56 (228,5 m³.ha⁻¹) para o inventário, 12,61 (228,5) para Sentinel-2, 12,82 (228,7) para Sentinel-1 e 12,71 (228,7) para a combinação [p. 7] — há divergência entre o resumo e a tabela.
- ANOVA e Tukey: dados com distribuição normal e **sem diferenças significativas** entre os volumes estimados pelos quatro tratamentos [p. 5, 7]; R² de 0,1742 é citado na discussão como equivalente ao de Mauya et al. (2019) para Sentinel-1 [p. 7].

## 6. Limitações reconhecidas pelos autores
- A modelagem usou apenas *stepwise*; os autores sugerem testar aprendizado de máquina para melhorar as estimativas volumétricas [p. 7].
- O uso de Sentinel-1 "não foi satisfatório", atribuído à limitada sensibilidade do sensor aos componentes da vegetação e à dependência do retroespalhamento em relação à estrutura do dossel, geometria de imageamento, resolução em range e azimute, distorção de relevo, ruído speckle e efeito Doppler [p. 7].
- A complexidade de entender e processar informações de sensores ativos permanece um desafio [p. 7].
- Sugerem novos testes com outros sensores ativos, em outras bandas espectrais e modos de polarização, e para outras espécies florestais [p. 1].

## 7. O que serve ao projeto e o que não serve
- **Serve:** desenho metodológico replicável — inventário de campo como referência, extração de médias por parcela em SIG, correlação de Pearson, *stepwise* em três cenários e validação estatística (ANOVA/Tukey) da diferença entre inventário e sensoriamento; é o esqueleto direto para volume, biomassa e carbono em silvicultura goiana [p. 4-5, 7].
- **Serve:** catálogo pronto de preditores para teste — índices adaptados ao Sentinel-1 (mRFDI, RVI, RVIad, Ad_1 a Ad_5) [p. 3] e índices Sentinel-2 com bandas red-edge (ARI1, ARI2, IRECI, NDVI red-edge, S2REP), além de IAF, FAPAR e FVC via PROSAIL [p. 4].
- **Serve:** resultado de expectativa para o desenho multissensorial — na banda C, o radar agregou pouco ao volume de dossel fechado e a combinação foi pior que o óptico isolado; para o cerrado/silvicultura tropical sob análise, isso indica priorizar Sentinel-2 e buscar comprimentos de onda maiores (L-band) ou dados de estrutura (LiDAR/drone) [p. 5, 7].
- **Não serve:** o estudo é de uma única data, um único povoamento de *Pinus taeda* no Paraná, com 48 parcelas e 11-12 anos, e estima apenas volume comercial — não há biomassa, estoque de carbono, equações alométricas, incerteza associada nem qualquer dado de Goiás ou de eucalipto, de modo que valores, modelos e coeficientes não são transferíveis [p. 2, 4, 5].

## 8. Duas frases citáveis
> "We found no significant differences between the volumetric estimates derived from remote sensing data and forest inventory techniques." [p. 1]

> "The use of Sentinel-1 data in this study was not satisfactory, since the modeling resulting from these data did not present significant parameters." [p. 7]
