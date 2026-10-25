# Relatório — Goergen, Narvaes & Adami (2021)

## 1. Referência

GOERGEN, L. C. G.; NARVAES, I. S.; ADAMI, M. **Estimation of wood volume of *Eucalyptus dunnii* and *urograndis* of different ages using TM/Landsat 5i**. *Ciência Florestal*, Santa Maria, v. 31, n. 2, p. 683-704, abr./jun. 2021. DOI: 10.5902/1980509834751. [p. 1; p. 22]

## 2. Pergunta do estudo

Estimar o volume comercial com casca (Vcc) de povoamentos de *Eucalyptus dunnii* e *E. urograndis* em diferentes idades (25, 34, 50 e 59 meses) e condições de sítio a partir de reflectância de bandas TM/Landsat-5 e de índices de vegetação. [p. 3]

## 3. Área e dados

- **Local:** município de Alegrete, região da Campanha do Rio Grande do Sul (55°30'W, 29°48'S), bioma Pampa, clima Cfa, Argissolo Vermelho Eutrófico Arênico, 110-150 m de altitude. [p. 3]
- **Período:** inventários em 2009 (plantios de 34 meses de *dunnii* e 25 meses de *urograndis*) e em 2011 (59 e 50 meses, respectivamente); imagens de 25/09/2009 e 17/10/2011. [p. 4]
- **Sensor/fonte:** Landsat-5 TM, órbita-ponto 224/81, resolução espacial de 30 m, imagens gratuitas do INPE; bandas TM1, TM2, TM3, TM4, TM5 (SWIR1) e TM7 (SWIR2) mais os índices SR, NDVI, SAVI (L = 0,5), GNDVI e MVI — 11 atributos espectrais ao todo. [p. 4-5]
- **Amostras:** amostragem sistemática, 1 unidade por 9 ha, **42 unidades amostrais** em 386,6 ha plantados — 23 de *E. dunnii* e 19 de *E. urograndis*; parcelas permanentes de ~314 m² (raio de 10 m), espaçamento 3,5 x 2,0 m (*dunnii*) e 3,5 x 2,5 m (*urograndis*), sem desbaste ou poda. [p. 4]

## 4. Método

1. Inventário florestal convencional: CAP de todos os indivíduos e altura total de 15 árvores iniciais mais as 5 mais grossas, com clinômetro Haglöf; coordenadas dos pontos por GPS Garmin Etrex Legend. [p. 4]
2. Processamento das imagens: georreferenciamento (base "geocover" NASA/GLCF) e correção atmosférica — número digital → radiância de topo de atmosfera → reflectância de superfície pelo algoritmo FLAASH no ENVI 4.5 (modelo "Mid-latitude summer", aerossol rural, visibilidade de 100 km). [p. 4-5]
3. Reflectância média dos pixels de cada unidade amostral usada como variável explicativa em regressão linear múltipla, após análise descritiva, verificação de multicolinearidade e correlação de Pearson com o Vcc. [p. 5]
4. Seleção de modelos por R², erro-padrão da estimativa (Syx), estatística F e 95% de confiança; validação por *bootstrap* com 1.000 reamostragens com reposição, porque o n era insuficiente para reservar 20% para validação independente. [p. 6-7]

## 5. Resultados principais

**Modelos ajustados (Tabela 3) [p. 10]:**

| Modelo | Variável dependente | Ano | Equação | F | R² | Syx (m³ ha⁻¹) |
|---|---|---|---|---|---|---|
| 1 | Vcc (*urograndis* + *dunnii*, 50 e 59 meses) | 2011 | 593,80 − 376,55 (SAVI 0,5) − 2009,96 (SWIR1–TM5) + ε | 30,80* | 0,61 | 27,58 |
| 2 | Vcc (*urograndis*, 25 meses) | 2009 | −18,65 + 96,59 (SAVI 0,5) + ε | 16,51* | 0,49 | 3,42 |
| 3 | Vcc (*dunnii*, 34 meses) | 2009 | 234,01 − 161,48 (SAVI 0,5) − 466,49 (SWIR1–TM5) + ε | 2,06 | 0,17 | 8,69 |

\* significativo a 5% de probabilidade. [p. 10]

- Modelo 1: melhor ajuste, com correlação de **78%** entre observado e estimado e Syx equivalente a **11,32%** da média amostral. [p. 11]
- Modelo 1: SWIR1 (TM5) com p = 0,0437 e SAVI 0,5 com p = 1,79 x 10⁻⁵; nas 1.000 simulações do *bootstrap*, o SAVI nunca assumiu valor zero, enquanto o TM5 assumiu zero em poucas observações. [p. 10; p. 11]
- Modelo 2: correlação de **70%** entre observado e estimado, variância média do erro de **11,69 m³ ha⁻¹** e apenas **18** das 1.000 permutações (~2%) com p > 0,05; SAVI 0,5 foi a única variável significativa (p = 0,0008). [p. 10; p. 14-15]
- Modelo 3: **não significativo** — correlação observado/estimado de apenas **41%**, R² concentrado entre 0,1 e 0,3 e **644** das 1.000 simulações com p > 0,05; os p-valores das variáveis foram 0,1745 (SWIR1) e 0,1677 (SAVI 0,5). [p. 9; p. 15-16]
- Correlações de Pearson com o Vcc (Tabela 2) [p. 9]:
  - *dunnii* 34 meses: só TM4 significativa (−0,32).
  - *urograndis* 25 meses: TM4 0,72; SAVI 0,5 0,70; MVI 0,64; SWIR2-TM7 0,45; TM2 0,41; SWIR1-TM5 −0,39.
  - Conjunto 50/59 meses: SAVI 0,5 −0,75; TM4 −0,74; SR −0,70; NDVI −0,68; MVI −0,66; SWIR1-TM5 −0,61; TM2 −0,54.
- Todas as correlações significativas encontradas no trabalho foram **negativas**. [p. 8]
- Superfícies de distribuição do Vcc geradas para 30 m indicaram volumes maiores para *E. dunnii* e menores para *E. urograndis*. [p. 13]

## 6. Limitações reconhecidas pelos autores

- A intensidade amostral foi insuficiente para reservar 20% das observações independentes para validação, o que obrigou o uso de *bootstrap*. [p. 6]
- O modelo de 34 meses de *E. dunnii* não foi significativo a 0,05 e se mostrou ineficiente para gerar Vcc, com baixa aderência à reta de regressão (R² = 0,17). [p. 9; p. 15-16]
- A resolução espacial de 30 m do Landsat-5/TM provoca mistura espectral entre vegetação e solo muito maior que imagens de alta resolução; para maior detalhamento seria necessário usar imagens de alta resolução espacial. [p. 15; p. 18]
- Os resultados, embora significativos, foram inferiores aos de Macedo et al. (2017), que obtiveram R² de 0,70 com imagens de 0,50 m. [p. 15]
- Condições de sítio distintas entre os três modelos gerados limitam a comparação. [p. 11]

## 7. O que serve ao projeto e o que não serve

**Serve:**
- Desenho metodológico replicável: bandas TM + índices de vegetação (SR, NDVI, SAVI, GNDVI, MVI) como preditores em regressão linear múltipla, com checagem de multicolinearidade e seleção por R²/Syx/F. [p. 5-6]
- Validação por *bootstrap* (1.000 reamostragens) como alternativa quando o n de parcelas é pequeno — situação provável em levantamentos de silvicultura. [p. 6-7]
- Evidência de que o SAVI 0,5 domina em povoamentos jovens com dossel não fechado, e o SWIR1 (TM5) ganha peso com o aumento do conteúdo de lignina/estrutura do dossel — argumento transferível para talhões de diferentes idades em Goiás. [p. 1; p. 18]
- Comprovação de que imagens ópticas gratuitas de média resolução servem para mapear volume em grandes áreas a custo baixo. [p. 18]

**Não serve:**
- Área de estudo é Alegrete/RS (Pampa, clima Cfa), não Goiás — nenhuma calibração é transferível para o Cerrado goiano. [p. 3]
- A variável resposta é volume comercial com casca (m³ ha⁻¹), não biomassa nem estoque de carbono; o artigo não quantifica carbono. [p. 1; p. 10]
- Sensor único e descontinuado (Landsat-5 TM, cenas de 2009 e 2011), sem qualquer abordagem multissensorial (sem LiDAR, Sentinel, radar ou fusão de sensores). [p. 4-5]
- Base amostral pequena (42 parcelas) e modelo jovem não significativo, o que limita a robustez estatística como referência direta. [p. 4; p. 16]

## 8. Frases citáveis

> "The vegetation index adjusted to the soil (SAVI 0.5) was relevant in the construction of the three models dueto the different degrees of contribution of the soil component, as a result the non-closure of the crowns in young stands at different ages." [p. 1]

> "In despite of the spatial resolution used (30m), it was efficient in the generation of volumetric modeling of a large area, in this way, serving as a tool suitable for mapping areas quickly and economically compared to conventional forest inventory;" [p. 18]

---

**Observação de leitura:** há inconsistências internas no texto — a p. 7 cita idades de "24 and 25 months" para as duas espécies (o restante do artigo trabalha com 25, 34, 50 e 59 meses), e a p. 17 menciona uma "34-month-old *Eucalyptus urograndis*" quando a parcela de 34 meses é de *E. dunnii*. O número de idades do desenho experimental é 4 (25, 34, 50 e 59 meses).
