# Relatório — Lang et al. (2023), modelo global de altura de dossel

Páginas citadas seguem a marcação `[página N]` do TEXTO.txt (p. N do PDF; página impressa = 1777 + N).

## 1. Referência

LANG, Nico; JETZ, Walter; SCHINDLER, Konrad; WEGNER, Jan Dirk. **A high-resolution canopy height model of the Earth**. *Nature Ecology & Evolution*, v. 7, p. 1778–1789, nov. 2023. DOI: 10.1038/s41559-023-02206-6. Recebido em 9/6/2023, aceito em 24/8/2023, publicado online em 28/9/2023 [p. 1]; versão corrigida em 2024 [p. 12]. Financiamento parcial da Barry Callebaut Sourcing AG [p. 12].

## 2. Pergunta do estudo

É possível, com um único modelo global de aprendizado profundo que funde LiDAR esparso do GEDI com imagens ópticas densas do Sentinel-2, gerar um mapa consistente de altura do topo do dossel em 10 m para toda a Terra — inclusive fora da cobertura do GEDI e com incerteza por pixel?

## 3. Área e dados

- **Local:** toda a massa continental da Terra, excluindo a Antártida, em 18.011 tiles de 100 km × 100 km [p. 10]; o treinamento usa só a faixa do GEDI, entre 51,6° N e 51,6° S [p. 2, p. 8]. O mapa final é global, com ~1,3 × 10¹² pixels [p. 4].
- **Período:** mapa do ano 2020 [p. 1]; imagens Sentinel-2 de maio a setembro de 2020 — no treino, uma cena por tile (a de menor cobertura de nuvem); no mapa, as 10 cenas com menos nuvem por tile [p. 8, p. 10]; referências GEDI de abril a agosto de 2019 e 2020 [p. 8]. A missão GEDI coletou de abril de 2019 a março de 2023 [p. 2].
- **Sensores/fontes:** Sentinel-2 L2A, 12 bandas (10, 20 e 60 m, reamostradas para 10 m) [p. 8]; GEDI L1B, altura RH98 (98% da energia retornada), pegada de 25 m [p. 8]. Validação independente: LiDAR aerotransportado LVIS e ALS (modelos de 1 m) [p. 8].
- **Amostras:** 600 × 10⁶ amostras de treino (recortes de 15 × 15 pixels = 150 × 150 m em torno de cada pegada GEDI) [p. 2, p. 8]; validação com n = 88.332.537 pixels [p. 3]; 20% dos tiles (100 × 100 km) retidos para validação e 80% para treino [p. 2]; comparação com o mapa UMD sobre 87 milhões de pegadas [p. 3]; validação aérea em 24 regiões de tiles (12 LVIS + 12 ALS), em 11 países [p. 4].

## 4. Método

1. **Rede neural convolucional totalmente convolucional**, treinada de ponta a ponta com supervisão esparsa: a perda só é minimizada nos pixels com referência GEDI, mas a saída cobre todos os pixels; entrada de 15 canais (12 bandas Sentinel-2 + coordenadas geográficas em codificação cíclica), saída de 2 canais (média e variância), 8 blocos residuais com 256 filtros [p. 8, p. 9].
2. **Conjunto (ensemble) de 5 CNNs** treinadas de zero, cada uma por 5.000.000 iterações, batch 64, otimizador Adam (taxa inicial 0,0001, reduzida 10× após 2 e 3,5 milhões de iterações); perda = log-verossimilhança gaussiana negativa [p. 9].
3. **Três medidas para não subestimar dosséis altos:** prior geográfico (lat/lon como canais), rebalanceamento da perda pelo inverso da frequência por intervalo de 1 m (√(1/N), ajuste fino de 750.000 iterações só na camada de regressão da média) e agregação de 10 datas por pixel com média ponderada pelo inverso da variância [p. 2, p. 9].
4. **Avaliação:** validação por tiles retidos do GEDI, comparação com o mapa global UMD (GEDI RH95 + Landsat, 30 m, reprojetado para 10 m), validação com LVIS/ALS independentes e calibração da incerteza (UCE/AUCE) [p. 3, p. 4, p. 10].

Processamento: ~160 TB de imagens Sentinel-2, ~27.000 horas de GPU (~3 anos de GPU), mapa global em 10 dias de tempo real [p. 4].

## 5. Resultados principais

- Precisão no GEDI retido: RMSE 6,0 m, MAE 4,0 m e viés (ME) 1,3 m; balanceado por intervalos de 5 m: aRMSE 7,3 m, aMAE 5,5 m, aME −1,8 m [p. 2, p. 3].
- Ablação (aRMSE / aMAE / aME): só Sentinel-2 8,3 / 7,1 / −5,4 m; + geografia 7,6 / 6,3 / −4,3 m; + balanceamento 7,3 / 5,8 / −3,1 m; ensemble final 7,3 / 5,5 / −1,8 m [p. 3].
- Contra o mapa UMD, o viés de subestimação cai de −7,1 m para −1,7 m (87 milhões de pegadas) [p. 3]; na média das regiões dentro da cobertura GEDI: nosso RMSE 7,9 m e viés 1,7 m (16,2%) vs. UMD 9,1 m e −4,5 m (−25,2%) [p. 4].
- Fora da cobertura GEDI (12 regiões com LiDAR aéreo): RMSE médio 5,3 m e viés 0,5 m (19,4%); na região mais ao norte (Finlândia, 70° N), RMSE 3,0 m e viés 0,5 m (17,1%) [p. 4]. Em 9 das 12 regiões com dado UMD o nosso mapa teve erro menor [p. 4].
- Incerteza: removendo os 20% mais incertos, o RMSE cai 13% (6,0 → 5,2 m) e o viés 23% (1,3 → 1,0 m) [p. 4].
- Distribuição global: 53,6 × 10⁶ km² (41% da terra) com vegetação >5 m; 39,6 × 10⁶ km² (30%) >10 m; 6,7 × 10⁶ km² (5%) >30 m [p. 5]. Apenas 34% dos dosséis >30 m estão em áreas protegidas [p. 1, p. 5].
- Viés por bioma: superestimação média de ≈2,5 m em manguezais, tundra e coníferas tropicais; deserto com erro marginal e sem viés [p. 2].
- Aplicação de carbono (Sabah, Bornéu): boa concordância com densidade de carbono aéreo de campanha LiDAR, com alturas até 65 m, e relação sensível até ≈60 m [p. 7].
- Pegada de carbono do mapa: 6.750 kWh; 338 kg CO₂-eq (Estocolmo) ou 3.848 kg CO₂-eq (Ohio); mapa atual estimado em ≈729 kg CO₂-eq [p. 10].

## 6. Limitações reconhecidas pelos autores

- A resolução espacial efetiva é menor que os 10 m nominais: cada pixel indica a maior altura de dossel dentro de uma pegada GEDI de ≈25 m de diâmetro [p. 6].
- A supervisão esparsa faz o modelo nunca ver explicitamente variações de alta frequência da altura entre pixels vizinhos, e a incerteza de geolocalização do GEDI versão 1 (15–20 m) adiciona ruído [p. 6].
- Tendência a superestimar áreas de dossel muito baixo (<5 m) [p. 2, p. 6].
- Artefatos de mosaico em altas latitudes do hemisfério norte, em boa parte offsets constantes entre tiles, e artefatos menores em regiões de nuvem persistente [p. 6].
- Incerteza alta em Papua-Nova Guiné, Alasca e Tibete; indica limites de usar imagens ópticas como único preditor [p. 5, p. 6].
- O modelo foi treinado para ser invariante a mudanças fenológicas de maio a setembro, mas não é robusto fora desse período em regiões de forte sazonalidade [p. 8].
- A tundra é sub-representada porque o GEDI não passa de 51,6° N, e suas referências são ruidosas [p. 2].
- Mapear biomassa em 10 m não é recomendado em regiões tropicais densas (copas maiores que um pixel); sugere-se resolução mais grosseira (ex.: 0,25 ha) [p. 7].
- A sensibilidade para detectar mudanças (ex.: crescimento anual) é limitada pela acurácia do modelo e ainda precisa ser avaliada [p. 7].

## 7. O que serve ao projeto e o que não serve

**Serve**
1. É o desenho metodológico replicável para o objetivo do projeto: fundir LiDAR amostral (GEDI) com imagens ópticas densas via CNN, com supervisão esparsa e incerteza por pixel — o mesmo esquema é transferível para talhões de silvicultura em Goiás [p. 2, p. 6].
2. Serve de camada de referência e linha de base: mapa global de 2020 em 10 m, aberto, com tiles e app interativo, para Goiás e para comparar com estimativas locais de altura de dossel [p. 1, p. 10].
3. Serve como argumento e protocolo de validação: separação treino/validação por tiles, uso de LiDAR aéreo independente, métricas balanceadas por intervalo de altura e filtro por incerteza para reduzir RMSE e viés [p. 3, p. 4].
4. Serve a parte de carbono: mostra que altura de dossel é preditora de estoque de carbono e até onde a relação é sensível (≈60 m), com ressalva sobre resolução de mapeamento [p. 7].

**Não serve**
1. Não entrega biomassa nem estoque de carbono: o produto é altura do topo do dossel; carbono aparece só como análise exploratória em Bornéu, sem modelo de AGB [p. 7].
2. Não é multissensorial no sentido do projeto: usa apenas Sentinel-2 (óptico) + GEDI; não inclui SAR nem LiDAR aerotransportado como preditores [p. 8].
3. Não foi calibrado nem validado para silvicultura de Goiás: as 24 regiões de validação aérea estão na América do Norte, América Central e Europa, nenhuma no Brasil; áreas urbanas e cultivos são excluídos das análises por bioma [p. 4, p. 6].
4. Não é multitemporal para a região: o mapa é de 2020 (imagens de maio a setembro), e a aptidão para detectar mudança ano a ano ainda não foi avaliada [p. 1, p. 7, p. 8].

## 8. Frases citáveis

> "According to our map, only 5% of the global landmass is covered by trees taller than 30 m." [p. 1]

> "The average root mean square error (aRMSE) of the height estimates, balanced across all 5-m height intervals, is 7.3 m, and the average mean error (aME, that is, bias) is −1.8 m." [p. 2]

(Trecho entre aspas acima sem o marcador de referência bibliográfica que aparece no original.)
