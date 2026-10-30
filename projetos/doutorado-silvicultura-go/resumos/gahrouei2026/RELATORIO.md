# RELATÓRIO — Omid Reisi Gahrouei (2026)

## 1. Referência

Gahrouei, Omid Reisi; Côté, Jean-François; Giguère, Philippe; Guindon, Luc; Bournival, Philippe; Béland, Martin (2026). "Large-scale tree species classification in Canadian boreal forest using PRISMA hyperspectral and LiDAR data". *Forestry: An International Journal of Forest Research*, 99(4), cpag064. DOI: 10.1093/forestry/cpag064 [p. 1].

O `TEXTO.txt` está completo (páginas 1 a 19, com resumo, métodos, resultados, discussão, conclusão, agradecimentos, material suplementar e referências) e corresponde ao DOI acima. Recebido em 29/11/2025, revisado em 03/07/2026, aceito em 12/07/2026, publicado em 26/08/2026 [p. 1].

## 2. Pergunta do estudo

A fusão de imagens hiperespectrais orbitais (PRISMA) com dados ALS (LiDAR aerotransportado), por *deep learning* multimodal, consegue classificar em escala regional — e com acurácia comparável à fotointerpretação — as espécies arbóreas dominantes da floresta boreal do leste do Canadá [p. 2–3]?

## 3. Área e dados

- **Local:** sul da província de Quebec, Canadá, entre 46°N e 50°N, predominantemente na ecozona boreal, domínios bioclimáticos de balsam fir/white birch e balsam fir/yellow birch [p. 3]. Mapa final produzido em área independente de 900 km² [p. 9].
- **Período:** PRISMA e Landsat 8 adquiridos de 1º de julho a 31 de agosto de 2021, 2022 e 2023 [p. 3–4]; ALS de 2014 a 2020 [p. 5]; parcelas temporárias oriundas do programa de inventário de 2018 [p. 5]. Defasagem entre LiDAR e HSI de 0 a 8 anos, mediana de 5 anos [p. 16].
- **Sensores/fontes:**
  - PRISMA HSI nível 2D: 26 imagens, nuvem ≤20%, 239 bandas, 30 m, revisita de 29 dias [p. 3, 5]; 193 bandas estreitas efetivamente usadas (400–2500 nm) [p. 10].
  - Landsat 8 OLI (comparação): >186 imagens, nuvem <50%, 11 bandas, 30 m [p. 4–5].
  - ALS: seis modelos de sensor, 1064 nm, densidade média de 1,5–4 pts/m², precisão horizontal 0–0,50 m e vertical 0–0,25 cm [p. 5].
  - Referência: mapa ecoflorestal de 2023 de Quebec (fotointerpretação) e parcelas de campo do MRNF [p. 5].
- **Amostras:** 11.848 povoamentos selecionados — black spruce (3756), balsam fir (2762), white birch (2078), trembling poplar (1935), yellow birch (706), jack pine (611) [p. 6]; 133.118 pseudo-parcelas extraídas (até 20 por povoamento, raio de 11,28 m) [p. 6]; divisão em 94.164 para treino, 38.984 para validação e 285 parcelas de campo independentes para teste (164 PSP + 121 TSP), sendo 18 imagens (16.200 km²) para treino e 7 imagens (6.300 km²) para ajuste de hiperparâmetros [p. 6–7].

## 4. Método

1. **Pré-processamento:** correção geométrica em duas etapas com AROSICS (CHM de 1 m → pancromática de 5 m → HSI de 30 m), máscaras de nuvem/sombra pelo método de Zhai et al. (2018), exclusão das bandas 1350–1460 nm, 1804–1994 nm e 2463–2500 nm (absorção atmosférica) e filtro *smoothing spline* (fator 0,001) [p. 3–4].
2. **Construção do treino:** povoamentos do mapa ecoflorestal com altura >7 m, espécie dominante com área basal relativa >50%, área ≥2,5 ha, compacidade Polsby-Popper ≥0,25, sem distúrbio desde 2000; pseudo-parcelas a 60 m da borda e a ≥600 m das parcelas de teste [p. 5–6].
3. **Arquitetura multimodal:** fusão intermediária (*intermediate fusion*) entre um ramo DGCNN sobre a nuvem de pontos ALS (k = 20 vizinhos, quatro camadas EdgeConv de 64/64/128/256, *embedding* de 2048 dimensões) e um ramo CNN 1D sobre o cubo hiperespectral (20 kernels, tamanho 21, *max-pooling* 4, camadas densas de 100 e 50 nós); 50 feições de cada ramo concatenadas e enviadas a um MLP com *softmax* [p. 6].
4. **Delineamento experimental:** ablação de modalidades (HSI, Landsat, ALS, Landsat+ALS, PRISMA+ALS), ablação de regiões espectrais (VIS 400–700 nm, NIR 700–1300 nm, SWIR 1300–2500 nm), estratificação por pureza da parcela (0,5–1 a 0,9–1) e por tipo florestal (B-C, B-B, C-C), visualização t-SNE com índices IS e IC, e validação em parcelas de campo independentes e contra o mapa ecoflorestal [p. 7–9]. Treino com Adam (lr 0,001, *batch* 64, até 100 épocas), *cross-entropy* e aumento de dados (rotação, ruído e remoção de pontos no ALS; escurecimento/clareamento no HSI) [p. 7].

## 5. Resultados principais

- O modelo multimodal PRISMA+ALS obteve OA de 76,5%, Kappa de 67,2% e F1 médio de 76,6% nas 285 parcelas de campo [p. 9].
- Comparação de modalidades: PRISMA isolado (CNN) OA 67,0% e F1 63,3%; ALS isolado (DGCNN) OA 65,3% e F1 56,6%; Landsat+ALS OA 68,8%; Landsat isolado OA 56,8% [p. 9].
- O ganho da fusão sobre os modelos unimodais é de 9,5 pontos percentuais de OA [p. 9, 17]; o resumo, porém, reporta +11,2% sobre ALS isolado [p. 1] — os dois valores coexistem no texto.
- HSI superou Landsat na mesma resolução espacial em 7,7% de OA [p. 9, 17].
- Por espécie: yellow birch F1 90,0% (PA 81,8%); black spruce PA 84,6% e F1 80,5%; white birch F1 66,7% (PA 75,0%) [p. 9].
- Pureza da parcela: OA de 76,5% (0,5–1), 77,3% (0,6–1), 84,5% (0,7–1), 85,8% (0,8–1) e 88,0% (0,9–1) [p. 9]. Com pureza >80% o artigo cita OA de 86% para espécies e 95% para tipo florestal [p. 12].
- Tipo florestal: em parcelas mistas conífera-folhosa (B-C), OA de 66,7% com ALS, 81,0% com HSI e 85,7% com a fusão; em parcelas de mesmo tipo (B-B/C-C), apenas 67,7% (HSI) e 71,4% (fusão) [p. 9].
- Regiões espectrais: NIR agregou +2,4% e SWIR +3,2% de OA, somando +5,6% sobre o VIS [p. 10, 16]; jack pine e yellow birch ganharam 32,4% e 16,3% de F1 com NIR+SWIR [p. 10].
- Separação de feições (t-SNE): IS de 0,439 e IC de 0,853 para o modelo multimodal, contra IS de 0,278 e IC de 0,816 para Landsat+ALS [p. 10–11].
- Aumento de dados contribuiu com +5% de OA [p. 12].
- Mapa de espécie dominante (900 km², 30 m): OA de 78,9% e Kappa de 58,2% frente ao mapa ecoflorestal; F1 de 82,4% (balsam fir), 80,4% (yellow birch), 78,5% (white birch), 78,0% (black spruce), 53,1% (jack pine) e 41,0% (trembling poplar) [p. 9, 14].
- Custo computacional do modelo multimodal: 35,42 min por época de treino e 10,84 ms por classificação [p. 9].

## 6. Limitações que os próprios autores reconhecem

- Defasagem temporal entre ALS e HSI de 0 a 8 anos (mediana de 5 anos), que pode afetar o desempenho e deveria ser minimizada [p. 16].
- Não foi possível usar informação temporal (multitemporal) do PRISMA devido à cobertura limitada do sensor [p. 15].
- Confusão residual entre trembling poplar e white birch, e entre balsam fir e black spruce; a separabilidade (IS) segue insuficiente mesmo após a fusão [p. 15].
- Erros de geolocalização do PRISMA e o erro máximo de posicionamento de 5 m do protocolo de campo são fontes de incerteza, sobretudo em povoamentos mistos [p. 16].
- Treino e validação vieram exclusivamente de povoamentos maduros (altura >7 m); florestas jovens não foram avaliadas [p. 16].
- Uso de ALS de baixa densidade (1,5–4 pts/m²); densidades maiores deveriam ser testadas [p. 5, 16].
- Probabilidades *softmax* são imperfeitas por problemas de calibração de redes neurais; e é necessário integrar mais espécies e avaliar outras ecozonas [p. 12].

## 7. O que serve ao projeto e o que não serve

- **Serve — desenho experimental:** a sequência de ablações (modalidade, região espectral, pureza, tipo florestal) mais validação em parcelas independentes e comparação com mapa operacional é diretamente replicável para silvicultura em Goiás, inclusive o uso de polígonos de inventário para gerar pseudo-parcelas em massa (133.118) [p. 6, 7–9].
- **Serve — evidência de ganho multissensorial:** a fusão estrutura (LiDAR) + espectro rendeu +9,5 pontos de OA, e NIR/SWIR renderam +5,6% sobre o VIS [p. 9, 16] — argumento quantitativo para justificar sensoriamento multissensorial no projeto.
- **Serve — produto operacional:** o mapa de probabilidade com limiar de 0,5, usado para sinalizar áreas que exigem verificação por fotointerpretação [p. 12], é um formato de entrega útil para inventário florestal.
- **Não serve — escopo:** o artigo não estima biomassa nem estoque de carbono em nenhum momento; trata apenas de classificação de espécie dominante, com 76,5% de OA [p. 9], e as seis espécies boreais e o contexto de Quebec (ALS 2014–2020, PRISMA 30 m) não têm validação para plantios de Goiás nem para fitofisionomias de Cerrado [p. 3, 5].

## 8. Frases citáveis (literais)

1. "Results indicated that combining HSI with ALS improved the overall accuracy (OA) by 11.2% compared with ALS alone, reaching an OA of 76.5% across both mixed and pure plots." [p. 1]
2. "The temporal gaps between the LiDAR and HSI data used in this study ranged from 0 to 8 years, with a median of 5 years." [p. 16]
