# RELATÓRIO — Rajesh Vanguri (2024)

## 1. Referência

- Autores: Rajesh Vanguri, Giovanni Laneve, Agata Hościło.
- Ano: 2024.
- Título: *Mapping forest tree species and its biodiversity using EnMAP hyperspectral data along with Sentinel-2 temporal data: An approach of tree species classification and diversity indices*.
- Revista: Ecological Indicators, v. 167, artigo 112671 [p. 1].
- DOI: 10.1016/j.ecolind.2024.112671 [p. 1].
- Verificação: o `TEXTO.txt` corresponde ao artigo do DOI informado e está íntegro (páginas 1 a 14, incluindo referências); não há truncamento.

## 2. Pergunta do estudo

Classificar espécies arbóreas e derivar índices de biodiversidade em Kampinos National Park (Polônia), combinando dados hiperespectrais EnMAP com séries temporais multiespectrais Sentinel-2 e algoritmos de aprendizado de máquina [p. 1].

## 3. Área e dados

- Local: Kampinos National Park e entorno, região da Mazóvia, próximo a Varsóvia, Polônia central [p. 1–2]; o parque cobre cerca de 385 km² [p. 2], com cerca de 70 % de área florestal e, desta, cerca de 67 % de pinheiro [p. 2].
- Período: Sentinel-2 em 22/04/2023, 03/06/2023, 15/08/2023, 06/09/2023 e 29/01/2024 (dois tiles por data) [p. 3]; EnMAP em 28/09/2023 [p. 4]; visita de campo em 13/04/2024 [p. 11].
- Sensores: 10 imagens Sentinel-2 L2A (tiles T34UDC e T34UDD), reduzidas a 5 imagens após mosaico e recorte pela extensão do EnMAP [p. 3–4]; 3 imagens EnMAP L2A, 224 bandas, 420–2450 nm, 30 m de resolução e faixa de 30 km [p. 3–4].
- Referência de campo: base do Inventário Florestal Nacional polonês (Polish Forest Data Bank, FDB), restrita a povoamentos puros com dominância ≥ 90 % de uma espécie, incluindo 10 % aleatório dos povoamentos 100 % pinheiro [p. 4]; nove espécies e duas subespécies de carvalho [p. 4].
- Amostras (polígonos/pixels): pinheiro 30/7.204; carvalho 160/5.883; amieiro 183/3.884; bétula 96/1.610; lariço 12/533; abeto 8/97; álamo 5/69; faia 5/50; acácia-negra 6/25 [p. 5].
- Biomassa, estoque de carbono ou dados de campo para carbono: não informado (o artigo só cita "carbon sequestration" em revisão de literatura) [p. 2].

## 4. Método

- Pré-processamento Sentinel-2: seleção de 7 bandas (B2, B3, B4, B5, B8, B11, B12), reamostragem para 30 m, conversão de DN para reflectância BOA e cálculo de 9 índices (AFRI_1600, CCCI, CIgreen, CIrededge, EVI, NDVI_MIR, NDVI, SAVI, NDMI), empilhados em cubo de 16 camadas [p. 4].
- Pré-processamento EnMAP: co-registro com Sentinel-2 por *Basic Pixel Alignment* no QGIS e remoção de 5 bandas com valores zero [p. 4]; empilhamento dos dois sensores em 299 atributos por pixel (219 EnMAP + 80 Sentinel-2) [p. 5].
- Redução de dimensionalidade: Gaussian Random Projection, ICA e PCA, com ICA de melhor desempenho e seleção dos 50 componentes principais [p. 5, 7].
- Classificação: cinco algoritmos (RF, SVM, GBC, CatBoost, XGBoost) treinados separadamente para needle-leaf (3 classes) e broad-leaf (6 classes), com tuning de hiperparâmetros, divisão 70:30 (treino/teste) e avaliação por F1 [p. 5, 7]; mapa final montado pela combinação das saídas (SVM nas classes 1, 2, 4a, 4b, 5, 7, 8 e 9; RF nas classes 4 e 6; bétula só quando CatBoost e SVM concordam) [p. 8]; índices de diversidade calculados em janela de 9 pixels (90 m) [p. 9].

## 5. Resultados principais

- Acurácia global entre 85 % e 93 % para o mapeamento de espécies [p. 1]; F1 global de 0,91 para o mapa combinado [p. 12].
- Needle-leaf: F1 entre 0,98 e 0,99 em todos os conjuntos de atributos [p. 7] e acurácias acima de 90 % sem tuning [p. 7].
- Broad-leaf: F1 entre 0,86 e 0,93, com queda leve em RF, CatBoost e XGBoost conforme cresce o número de atributos [p. 7]; 50 atributos considerados ótimos [p. 7].
- Contribuição das fontes nos 50 componentes: 51 % EnMAP e 49 % Sentinel-2 no modelo perenifólio; 52 % EnMAP e 48 % Sentinel-2 no caducifólio [p. 7].
- Bandas EnMAP mais relevantes para ambos os modelos: 418–454 nm (8 bandas), 686–756 nm (8 bandas) e 879–1128 nm (20 bandas) [p. 8].
- Efeito do tuning no F1 (SVM, broad-leaf): classe 1 de 0 para 0,67; classe 2 de 0,22 para 0,55; classe 7 de 0,32 para 0,54 [p. 8].
- Dados combinados superaram Sentinel-2 ou EnMAP isolados nas classes 1, 2, 3, 6 e 7; Sentinel-2 foi melhor nas classes 4a e 4b [p. 8].
- Índices EnMAP: 186 de 256 índices disponíveis puderam ser calculados [p. 8].
- Validação em cinco povoamentos heterogêneos, com áreas de 61.446; 16.601; 59.563; 162.321 e 110.646 m² [p. 9]; exemplo do povoamento 17-12-1-07-379-f: FDB com 90 % da classe 6 e 10 % "other", SVM com 22,5 % da classe 4 e 77,5 % da classe 6, RF e CatBoost com 4,2 % e 95,7 % [p. 9–10].
- Validação de campo em grade de 60×60 m no parque, com quatro espécies (pinheiro, carvalho, amieiro, bétula), em dois sítios: todas as espécies corretamente classificadas nas quadras visitadas [p. 11].
- Índices de diversidade derivados do mapa (resolução de 90 m) [p. 9]: Shannon-Wiener de 0 a 1,735 [p. 12]; Simpson de 0 a 0,814 [p. 12]; riqueza de espécies de 1 a 6 [p. 12]; índice de biodiversidade próprio de 0,111 a 0,666 [p. 12].
- Biomassa ou estoque de carbono quantificado: não informado.

## 6. Limitações que os próprios autores reconhecem

- A cobertura do EnMAP restringe o escopo do mapeamento de espécies; sugerem novas aquisições e outros sensores hiperespectrais (PRISMA) para ampliar a área e o número de espécies [p. 12].
- Não foi possível validar em campo todas as quadras de 60×60 m, por causa da extensão do parque e de restrições de acesso; a validação foi completada por consulta *online* ao portal do Inventário Florestal Nacional [p. 11].
- Nos polígonos de referência do FDB, a distribuição espacial precisa das espécies dentro do povoamento é desconhecida [p. 4].
- Por restrição de espaço, apenas o F1 foi apresentado, embora precisão e recall tenham sido calculados [p. 7].
- Anomalia de faixa ("strip-like area") mal classificada por todos os algoritmos exceto SVM, associada a diferenças de reflectância dentro da mesma espécie [p. 11–12].
- Não há limitação declarada sobre carbono ou biomassa (variáveis não abordadas) — não informado.

## 7. O que serve ao projeto e o que não serve

- Serve: o desenho de fusão EnMAP (hiperespectral) + Sentinel-2 multitemporal com redução por ICA e 50 componentes, replicável para estratificar espécies e, por consequência, dosséis de silvicultura em Goiás [p. 5, 7].
- Serve: o protocolo de validação contra polígonos de inventário florestal (povoamentos puros ≥ 90 %, divisão 70:30) e a análise de contribuição por sensor (51/49 e 52/48 %), útil para justificar a combinação multissensorial [p. 4, 7].
- Serve: os índices de diversidade em janela de 9 pixels (90 m) como descritores auxiliares de heterogeneidade de povoamentos, não como proxy de biomassa [p. 9, 12].
- Não serve: o artigo não estima biomassa, AGB nem estoque de carbono (nenhuma variável, alometria ou validação de carbono) e trata de floresta temperada polonesa com apenas 3 imagens EnMAP e sem LiDAR, contexto distinto da silvicultura goiana [p. 2, 4].

## 8. Frases citáveis (literais)

- "Achieving an overall accuracy of 85% to 93%, our study demonstrates the efficacy of this integrated approach in tree species mapping." [p. 1]
- "Future research should focus on increasing coverage of EnMAP data which restricts the scope of species mapping, indicating the need for additional data acquisition, possibly exploiting the availability of other hyperspectral sensors (PRISMA), to expand the study area and increase the number of species considered." [p. 12]
