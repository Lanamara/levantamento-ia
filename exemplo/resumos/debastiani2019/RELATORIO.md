# Relatório — Debastiani et al. (2019)

*As páginas citadas seguem as marcas `[página N]` do TEXTO.txt (p. 1 = p. 109 do artigo).*

## 1. Referência

DEBASTIANI, A. B.; SANQUETTA, C. R.; CORTE, A. P. D.; REX, F. E.; PINTO, N. S. **Evaluating SAR-optical sensor fusion for aboveground biomass estimation in a Brazilian tropical forest.** *Annals of Forest Research*, v. 62, n. 1, p. 109-122, 2019. DOI: 10.15287/afr.2018.1267. [p. 1]

## 2. Pergunta do estudo

Avaliar se a fusão de dados SAR de banda C (Sentinel-1), métricas de textura e dados ópticos (Sentinel-2) com algoritmos de aprendizado de máquina estima a biomassa acima do solo (AGB) em uma floresta tropical de alta biomassa, e qual a importância relativa das variáveis de radar e ópticas nessa estimativa. [p. 1, p. 3]

## 3. Área e dados

- **Local:** Floresta Nacional do Jamari (Flona Jamari), Rondônia, Amazônia brasileira (9º9' S, 62º58' W), cerca de 220.000 ha de Floresta Ombrófila Densa. [p. 3]
- **Período:** imagem Sentinel-1 adquirida em 15/02/2016 e Sentinel-2 com data de ingestão 25/08/2015 [p. 4, Tabela 1]; voo LiDAR em 21/09/2015 [p. 5]. A Tabela 2 registra "2011/11/17" como data de aquisição do LiDAR, em contradição com o texto. [p. 5]
- **Sensores/fontes:** Sentinel-1A (banda C, produto GRD, modo IW, polarizações VV e VH, órbita descendente) e Sentinel-2A (MSI, 13 bandas, 10-60 m), via Copernicus/ESA [p. 3-4]; LiDAR aerotransportado Optech Orion, usado para gerar a AGB de referência (projeto *Sustainable Landscapes Brazil*, EMBRAPA/USFS/USAID) [p. 5].
- **Amostras:** 286 quadrados de 100 × 100 m (escala de análise fixada em 100 m), em área de 500 ha coberta pelo LiDAR [p. 4-5]. AGB variou de 139 a 516 Mg/ha [p. 7].

## 4. Método

1. **Processamento SAR (SNAP 5.0):** calibração radiométrica para Sigma 0, filtro Lee refinado para *speckle* e correção de terreno Range-Doppler (UTM WGS84); texturas GLCM em janela 5×5 (contraste, dissimilaridade, homogeneidade, ASM, energia, MAX, entropia, média, variância, correlação) e componentes principais (PCA). [p. 4]
2. **Processamento óptico:** Sentinel-2 nível 1C com correção atmosférica no QGIS 2.18.16 (plugin de classificação semiautomática); índices SAVI (fator de solo 0,25), RVI, LAI e NDVI; estatísticas (mín., máx., média, desvio-padrão e variância) agregadas por célula de 100 m. [p. 4]
3. **Variável-resposta por LiDAR (FUSION 3.60):** DTM, normalização da nuvem, estatísticas a 100 m e AGB pela equação AGB = (3,119 + 0,564·P25 + 0,062·Var)² + 1,74, de D'Oliveira et al. (2012). [p. 5-6]
4. **Modelagem:** três tratamentos — T1 = Sigma 0 VV e VH; T2 = T1 + texturas; T3 = T2 + 8 bandas Sentinel-2 (B02-B08, B8a) + 4 índices; seleção de variáveis pelo CFS (*CfsSubsetEval*) no WEKA; algoritmos de ML (o resumo anuncia 12, mas a Tabela 3 lista 11) com validação cruzada k = 10 e RMSE absoluto e relativo; erro total por propagação de erros de Saatchi et al. (2011b). [p. 6-7]

## 5. Resultados principais

- AGB de referência: 139 a 516 Mg/ha, média 296 Mg/ha, coeficiente de variação 20%, curtose 1,075 e assimetria 0,672 [p. 7]; média de 297 Mg/ha para as 286 parcelas [p. 8]. *Os dois valores de média aparecem no texto.*
- O CFS selecionou 5 variáveis no T1, 9 no T2 e 10 no T3 [p. 7-8]. As correlações lineares foram fracas; a maior foi Var(SAVI), r = 0,442, seguida de Mín(banda 12), r = -0,414 [p. 7].
- T1 (só backscatter): RMSE de 58,030 Mg/ha (Robust Regression) a 83,651 Mg/ha (Random Tree); média de 62,358 Mg/ha ou 21,011% [p. 8].
- T2 (+ textura): melhor SMOreg com 59,639 Mg/ha e pior Random Tree com 85,369 Mg/ha; média de 54,569 Mg/ha ou 18,386% [p. 8]. *A média informada é inferior à maioria dos valores da Tabela 5; reproduzo como está no texto.*
- T3 (+ óptico): RMSE de 47 a 70 Mg/ha, com melhora média de 3% sobre os demais tratamentos [p. 8]. Menor RMSE com Robust Regression, 47,660 Mg/ha (16,058%), que representou apenas 73% da amplitude [p. 8-9]; Random Tree com 70,996 Mg/ha (23,921%) cobrindo 100% da variabilidade [p. 9].
- Amplitude da AGB representada pelo Random Tree: 91,33% no T1, 99,81% no T2 e 100% no T3 [p. 9].
- Erro total: alometria 40,2 Mg/ha ou 17,47%; amostragem 22,8%; predição 23,921%; erro total de aproximadamente 41,1% [p. 9]. A conclusão cita RMSE de 23,9% [p. 12].

## 6. Limitações reconhecidas pelos autores

- Falta de dados de inventário de campo para o ano de interesse, o que levou a usar AGB derivada de LiDAR como variável dependente; por isso os erros de medição não foram considerados no erro total [p. 6, p. 9].
- Ausência de estação meteorológica na área de estudo: parte dos erros ligada à umidade do solo e da vegetação, que afeta o backscatter, não pôde ser quantificada [p. 11].
- Consideração apenas da vegetação arbórea acima de um diâmetro mínimo de inclusão, deixando parte do estrato arbóreo de fora [p. 11].
- Erro total elevado (41,1%), com implicações práticas [p. 11].
- Saturação do backscatter da banda C em locais de alta AGB, sem alternativa gratuita em banda P [p. 2, p. 11].
- Os algoritmos em geral não capturam a amplitude da AGB e produzem valores intermediários pouco sensíveis aos preditores [p. 8].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o desenho de fusão multissensorial (SAR C + texturas GLCM + bandas e índices ópticos) com seleção de atributos por CFS e validação cruzada k = 10 é diretamente replicável em povoamentos de Goiás, e o controle de "amplitude representada" (91,33%, 99,81%, 100%) [p. 9] é uma métrica que o projeto deveria adotar junto ao RMSE.
- **Serve:** o achado de que a banda C satura em alta biomassa e a indicação da banda P/L [p. 11] justificam incluir L-band, LiDAR ou GEDI no projeto em vez de depender apenas do Sentinel-1.
- **Não serve:** o cenário é floresta tropical amazônica com média de ~296-297 Mg/ha [p. 7-8], não silvicultura; os RMSE de 47 a 85 Mg/ha não são transferíveis para talhões de eucalipto ou pínus em Goiás.
- **Não serve:** a referência é LiDAR e não inventário de campo [p. 6], o alvo é AGB (sem conversão para estoque de carbono), a grade é de 100 m (grosseira para talhões) e há uma única data, sem série temporal.

## 8. Duas frases citáveis

> "However, most of the algorithms fail to capture the range of AGB, producing intermediate values, that are to a large extent insensitive to the values of predictor variables." [p. 8]

> "It is known that saturation of the backscatter occurs in bands with lower wavelengths in places with high AGB values, being indicated the use of the P band, since this one presents greater penetration and sensitivity with AGB" [p. 11]
