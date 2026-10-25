# RELATÓRIO — Almeida et al. (2021)

## 1. Referência

ALMEIDA, Alessandro Araujo Amaral de; THIERSCH, Monica Fabiana Bento Moreira; BERNARDI, Lucas Kröhling; PÁDUA, Franciane Andrade de; MORENO ARTEAGA, Argemiro José; THIERSCH, Claudio Roberto. **Artificial neural networks and remote sensing for volumetric prediction in a Eucalyptus sp. plantation.** *Research, Society and Development*, v. 10, n. 12, e250101220466, 2021. DOI: 10.33448/rsd-v10i12.20466. [p. 1]

## 2. Pergunta do estudo

Avaliar o desempenho de redes neurais artificiais (RNA) associadas a imagens Sentinel-2 na estimativa do volume com casca de um povoamento de *Eucalyptus* sp. [p. 3]

## 3. Área e dados

- **Local:** interior do estado de São Paulo, município de Botucatu; clima temperado quente (mesotérmico, Köppen) [p. 3].
- **Período:** inventário florestal e imagens, ambos de 2016 [p. 4].
- **Sensores/fontes:** imagens Sentinel-2, 4 bandas a 10 m (B02 490 nm, B03 560 nm, B04 665 nm, B08 842 nm), mais NDVI e razões entre bandas; inventário pré-corte de campo; material genético como variável categórica (1 a 9) [p. 4].
- **Amostras:** 569 parcelas retangulares permanentes, área média de 280,38 m², em povoamento com nove variedades clonais, espaçamento 3×2 m, idades de 5,3 a 6,3 anos [p. 3]. Divisão aleatória 70% treinamento / 30% validação [p. 4].
- **Variável-resposta:** volume com casca por hectare, obtido pela fórmula de Smalian [p. 4].

## 4. Método

1. Extração dos níveis de cinza das 4 bandas em buffer de 100 m ao redor das coordenadas de cada parcela; cálculo do NDVI = (ivp − vm)/(ivp + vm) e das razões entre bandas [p. 4].
2. Normalização das variáveis numéricas para o intervalo 0–1 e treinamento supervisionado [p. 4].
3. Arquitetura Multi-Layer Perceptron com 21 neurônios de entrada, 2 camadas ocultas e 1 neurônio de saída, algoritmo Backpropagation; 25 configurações testadas variando o número de neurônios nas camadas ocultas [p. 4–5].
4. Avaliação por erro padrão residual (Sxy, em m³/ha e em %) e análise gráfica de resíduos (dispersão e quantil-quantil); todo o processamento em R [p. 5].

## 5. Resultados principais

- Melhor rede: MLP 8-3-1 (8 e 3 neurônios nas camadas ocultas, 21 variáveis de entrada); Sxy de **10,63%** no treinamento e **12,00%** na validação [p. 6–7].
- Sxy em valores absolutos na Tabela 2: **33,35 m³/ha** (treinamento) e **38,33 m³/ha** (generalização) [p. 7]. *Atenção: o texto corrido da p. 6 associa 38,33 m³/ha a 10,63% e 33,35 m³/ha a 12,00%, invertendo os valores da tabela — inconsistência interna do artigo.*
- Volume observado: mínimo 143,89, média 315,45, máximo 456,29 m³/ha, desvio ± 46,79 m³/ha [p. 6].
- Idade: 5,30 a 6,30 anos, média 5,69 ± 0,32 [p. 6].
- Bandas (mín.–máx., média): B02 758–815 (779) ± 9,71; B03 581–675 (621) ± 16,61; B04 363–510 (406) ± 21,52; B08 2220–3421 (2734) ± 266,79 [p. 6].
- NDVI: 0,68 a 0,80, média 0,74 ± 0,02 — vegetação intensa, sem falhas de plantio evidentes [p. 6].
- Volume estimado no mapa final (Figura 4): **228,40 a 366,50 m³/ha** [p. 7].
- Comparações: Lima et al. (2017) 8,48% e 12,90% (treino/validação); Miguel et al. (2015) 4,93% e 6,01% [p. 7]; Zhou et al. (2020) Syx de 31,45% (45,44 m³/ha) [p. 7]; Santi et al. (2015) 40 m³/ha e 30 m³/ha [p. 7].
- Resíduos: tendência a superestimar abaixo de ~330 m³/ha e a subestimar acima desse valor; resíduos próximos da normalidade no gráfico q-q [p. 8].

## 6. Limitações reconhecidas pelos autores

- Viés sistemático dos resíduos em função do nível de volume (superestimativa abaixo de ~330 m³/ha e subestimativa acima), detectado apenas pela análise gráfica [p. 8].
- Usaram **uma única** arquitetura de RNA (MLP), justificada pela prevalência dessa arquitetura na literatura (78% dos trabalhos), sem testar alternativas como RBF [p. 4].
- O próprio artigo afirma que são necessários mais estudos com RNA para estimar parâmetros florestais, a fim de obter metodologias confiáveis e resultados mais consistentes [p. 9].
- A variação de volume (144 a 456 m³/ha) pode decorrer de danos (vento, fogo) em partes do povoamento, ou seja, há heterogeneidade não controlada nos dados [p. 4].

## 7. O que serve ao projeto e o que não serve

**Serve**

- Desenho metodológico replicável para silvicultura: parcelas de campo + bandas, razões entre bandas e NDVI de satélite óptico como entrada de RNA para estimar volume [p. 4].
- Protocolo de validação (split 70/30, Sxy em % e m³/ha, análise gráfica de resíduos + q-q) útil como padrão de comparação para os modelos do projeto [p. 5].
- Evidência de que a arquitetura MLP com duas camadas ocultas resolve o problema com erro de validação ~12%, com processamento 100% em software livre (R) e imagens gratuitas [p. 7, p. 9].
- Alerta metodológico sobre viés residual dependente do nível de volume — relevante ao extrapolar modelos para talhões com estoques distintos [p. 8].

**Não serve**

- Não é Goiás: área em Botucatu (SP), outro clima e outro histórico de manejo [p. 3].
- Não estima biomassa nem estoque de carbono — a variável é volume com casca (m³/ha); carbono não é abordado no artigo [p. 4].
- Não é multissensorial: usa apenas Sentinel-2 (óptico, 4 bandas a 10 m), sem LiDAR, SAR ou dados de drone [p. 4].
- Escopo restrito a *Eucalyptus* sp. clonal com 5,3–6,3 anos, sem extrapolação testada para outras idades, espécies ou regiões [p. 3].

## 8. Frases citáveis (literais)

> "The fact that the error of the validation is close to that of the training indicates the non-occurrence of overfitting, i.e., the variables used for the training were sufficient for the neural network to be generalized and applied to other data." [p. 7]

> "it is verified that the neural networks tend to overestimate when the volume is less than approximately 330 m³/ha and to underestimate when the volume exceeds approximately 330 m³/ha, as can be observed in the trend line." [p. 8]
