# RELATÓRIO — Aobo Liu (2021)

## 1. Referência

Liu, A.; Cheng, X.; Chen, Z. (2021). Performance evaluation of GEDI and ICESat-2 laser altimeter data for terrain and canopy height retrievals. *Remote Sensing of Environment*, 264, 112571. DOI: 10.1016/j.rse.2021.112571. [p. 1]

O `TEXTO.txt` está íntegro e corresponde a esse DOI; não está truncado. No arquivo original, alguns sinais de menos aparecem como bytes nulos, sem alterar os valores numéricos.

## 2. Pergunta do estudo

O estudo avalia a acurácia dos produtos GEDI L2A e ICESat-2 ATL08 na recuperação da altura do terreno e do dossel, usando lidar aerotransportado do mesmo ano como referência em 40 sítios dos EUA, e identifica os fatores que controlam esses erros [p. 1].

## 3. Área e dados

- **Local:** 40 sítios NEON na América do Norte — 5 no Alasca, 1 no Havaí e os demais nos EUA continentais; cerca de 7000 km²; longitude 157°W–71°W, latitude 19°N–71°N e elevação 6–3513 m [p. 3].
- **Período:** 2019, majoritariamente de março a setembro (um sítio no Havaí em janeiro); ICESat-2 e GEDI restritos à estação de crescimento [p. 4].
- **Sensores/fontes:** NEON ALS (Optech Gemini; DTM e CHM de 1 m), ICESat-2 ATL08 v4 e GEDI L2A v2 [p. 4].
- **Amostras:** 42.636 segmentos ATL08 (9.970 de alta latitude) e 90.472 footprints GEDI para terreno; 20.967 estimativas de dossel ICESat-2 e 61.598 GEDI [p. 5–8].

## 4. Método

1. Validação na resolução nativa: buffers circulares de 25 m para GEDI e retangulares de 100 m × 12 m para ICESat-2; DTM/CHM NEON como referência; conversão de WGS84 para GEOID12A no VDatum [p. 6].
2. Correção de geolocalização do GEDI: simulação de waveform com o NEON, comparação com o waveform L1B real em raio de 20 m e passos de 1 m, adotando a posição de maior correlação de Pearson [p. 6].
3. Métricas: bias, MAE, R², RMSE e %RMSE [p. 7].
4. Random Forest Regression (%IncMSE) para ordenar slope, altura de dossel, cobertura, classe de uso, SNR, n_seg_ph e sensitivity; análise estratificada por feixe e por dia/noite [p. 9–11].

## 5. Resultados principais

- **Terreno, latitudes médias/baixas:** RMSE 2,24 m (ICESat-2) e 4,03 m (GEDI); MAE 0,91 m e 1,80 m [p. 7].
- **Terreno, alta latitude (só ICESat-2):** RMSE 0,98 m; MAE 0,39 m [p. 7].
- **Referências externas:** SRTM e GMTED tiveram RMSE de 10 m e 22 m, piores que os dois altímetros [p. 7].
- **GEDI sem correção de geolocalização:** RMSE 4,15 m e MAE 2,13 m; mesmo corrigido, superestima o terreno em 0,97 m [p. 7][p. 9].
- **Dossel, todos os dados:** GEDI R² 0,82 e %RMSE 30,9%; ICESat-2 R² 0,61 e %RMSE 40,2%; ambos subestimam a altura do dossel [p. 8].
- **Viés do ICESat-2:** superestima a altura em dwarf shrublands e subestima em floresta; o resíduo migra para baixo conforme a altura do dossel aumenta [p. 11].
- **Fatores dominantes:** slope é o principal fator para terreno; a própria altura do dossel é o principal fator para dossel [p. 11].
- **Dossel, só power/strong beam noturno:** RMSE 3,93 m (ICESat-2) e 3,56 m (GEDI); %RMSE 24,8% e 23,3%; R² 0,89 e 0,90 [p. 9].
- **Ganho do filtro:** RMSE cai de 7,21 para 3,93 m (ICESat-2) e de 5,02 para 3,56 m (GEDI) [p. 14].
- **Terreno por slope:** RMSE 0,62/2,88 m (ICESat-2/GEDI) com slope <5° e 7,45/6,70 m com slope >30° [p. 11].
- **Terreno por vegetação:** até 0,72/1,35 m sem vegetação; 3,20/5,84 m em floresta; 0,38 m na tundra do Alasca (ICESat-2) [p. 11].
- **Dossel por altura:** RMSE 2,58/2,01 m para <5 m e 8,67/6,44 m para >40 m [p. 11].
- **Altura relativa:** RMSE estável em 4–5 m (ICESat-2) e 3–4 m (GEDI) [p. 9].
- **Resíduos terreno–dossel:** R −0,26 (ICESat-2) e −0,50 (GEDI) em todos os dados; −0,54 e −0,72 com cobertura >90% [p. 11–12].
- **Amostras válidas de dossel:** 64% dos 32.666 segmentos ICESat-2 e 68% dos 90.472 footprints GEDI [p. 8].
- **Síntese:** ICESat-2 é melhor para terreno; GEDI é melhor para dossel [p. 11][p. 14].

## 6. Limitações que os próprios autores reconhecem

- **Geolocalização do GEDI:** 10 m na v2, contra <5 m (tipicamente 2–3 m) do ICESat-2; a comparação por centroide penaliza o GEDI sem correção [p. 6].
- **Sem cross-over:** a amostragem esparsa e as diferenças de resolução e inclinação orbital impediram comparar passagens sobrepostas; não havia produto ICESat-2 em grade [p. 3].
- **Cobertura do dossel:** o CHM NEON usa limiar de 2 m, ignora sub-bosque e subestima a cobertura; a razão de células pode superestimar; os erros se compensam em parte [p. 6].
- **Limite físico do ATL08:** 0–4 fótons por pulso sobre vegetação, baixa chance de detectar o topo e tendência a subestimar a altura; ruído solar afeta o produto [p. 5].
- **Amostra sem filtro de relevo:** os autores incluíram todas as amostras, inclusive slope alto, o que eleva o erro nominal em troca de maior representatividade [p. 8].
- **Referência também incerta:** o NEON tem dificuldade de detectar o solo sob dossel muito denso, o que reduz a acurácia do terreno e pode enviesá-lo para cima [p. 12–13].
- **Origem do viés do ICESat-2:** o deslocamento dos resíduos com a altura do dossel não tem explicação estabelecida [p. 11].
- **RFR:** o modelo tem pouco poder explicativo; os autores usam apenas a ordem de importância, não as proporções [p. 11].

## 7. O que serve ao projeto e o que não serve

- **Serve — GEDI como fonte principal de altura de dossel:** é a escolha preferida quando produtos de altura de dossel de GEDI e ICESat-2 são usados para estimar biomassa florestal [p. 11]; a faixa de cobertura do GEDI (51,6°N–51,6°S) inclui Goiás [p. 2], e a missão tem amostragem mais densa em latitudes médias e baixas [p. 14].
- **Serve — filtro operacional e estratificação de erro:** usar power beam e dados noturnos reduz o RMSE do GEDI de 5,02 para 3,56 m [p. 14]; slope, altura do dossel e cobertura são os fatores a estratificar [p. 11].
- **Não serve — biomassa e carbono:** não há estimativa de biomassa nem de estoque de carbono no artigo (resultados não informados); ele entrega altura do terreno e do dossel [p. 1].
- **Não serve — transferência direta para Goiás/silvicultura:** a validação são 40 sítios NEON nos EUA em 2019 [p. 3], sem Cerrado, Goiás ou plantios de eucalipto; e o desenho não testa fusão multissensorial com óptico ou SAR [p. 3].

## 8. Frases citáveis (literais)

- “ICESat-2 outperforms GEDI across the board for terrain height retrieval, although they both have better accuracy than existing SRTM and GMTED DEM products.” [p. 11]
- “Therefore, the GEDI dataset should be the preferred choice when canopy height products of ICESat-2 and GEDI are used to estimate forest biomass.” [p. 11]
