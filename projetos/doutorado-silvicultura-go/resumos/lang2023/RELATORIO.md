# RELATÓRIO — Nico Lang (2023)

## 1. Referência

Nico Lang, Walter Jetz, Konrad Schindler e Jan Dirk Wegner (2023). "A high-resolution canopy height model of the Earth". *Nature Ecology & Evolution*, vol. 7, p. 1778–1789. DOI: 10.1038/s41559-023-02206-6. Publicado online em 28 de setembro de 2023 [p. 1].

## 2. Pergunta do estudo

É possível estimar a altura do topo do dossel em escala global, a 10 m de resolução, fundindo LiDAR esparso do GEDI com imagens ópticas Sentinel-2 por meio de aprendizado profundo, com incerteza associada e sem calibração local [p. 1–2]?

## 3. Área e dados

- **Local:** toda a massa continental da Terra, exceto a Antártida; o treinamento fica restrito à faixa do GEDI, entre 51,6° N e S [p. 8, p. 10].
- **Período:** mapa do ano 2020; referências GEDI de abril a agosto de 2019 e 2020; imagens Sentinel-2 de maio a setembro de 2020 [p. 8, p. 2].
- **Sensores/fontes:** Sentinel-2 L2A (12 bandas, 10/20/60 m, reamostradas para 10 m) [p. 8]; GEDI L1B v1, forma de onda completa, pegada de 25 m, métrica RH98 [p. 8]; validação independente com LiDAR aerotransportado LVIS e ALS de pequena pegada [p. 4].
- **Amostras:** 600 × 10^6 amostras de treino (patches de 15 × 15 pixels em cada pegada GEDI) [p. 2, p. 8]; validação em 20% dos tiles de 100 × 100 km, com n = 88.332.537 pontos [p. 2, p. 3]; comparação com o mapa UMD em 87.406.779 pegadas [p. 16]; 24 tiles aéreos independentes (12 LVIS, 12 ALS) em 11 países das Américas do Norte e Central e da Europa [p. 4].
- **Processamento global:** 18.011 tiles Sentinel-2 [p. 10]; ≈ 1,3 × 10^12 pixels e ≈ 160 TB de imagens [p. 4].

## 4. Método

- **Rede:** ensemble de cinco CNNs totalmente convolucionais (blocos residuais com convoluções separáveis, 8 blocos, 256 filtros), sem downsampling; 15 canais de entrada (12 bandas Sentinel-2 + coordenadas geográficas em codificação cíclica) e duas saídas (média e variância da altura) [p. 8].
- **Supervisão esparsa:** regressão pixel a pixel treinada apenas nos pixels com referência GEDI; perda de verossimilhança gaussiana negativa (NLL), que fornece a incerteza aleatória [p. 9].
- **Correção do viés de copas altas:** reponderação da perda pelo inverso da frequência de amostras em intervalos de 1 m (raiz quadrada, suavizada), com ajuste fino apenas da camada final de regressão da média [p. 2, p. 9].
- **Inferência:** dez datas por local, cada imagem processada por um membro sorteado do ensemble, e fusão por média ponderada pelo inverso da variância; avaliação por RMSE, MAE e ME, além das versões balanceadas por intervalos de 5 m (aRMSE, aMAE, aME) [p. 4, p. 9–10].

## 5. Resultados principais

- Erro balanceado: aRMSE de 7,3 m e aME de −1,8 m; sem balanceamento, RMSE de 6,0 m, MAE de 4,0 m e viés de 1,3 m [p. 2].
- Ablação: aRMSE cai de 8,3 m (só Sentinel-2) para 7,3 m (ensemble final) e o aME passa de −5,4 m para −1,8 m [p. 2].
- Frente ao mapa global UMD (GEDI + Landsat), o viés médio por intervalo de altura cai de −7,1 m para −1,7 m nos 87 milhões de pegadas de validação [p. 3].
- Validação com LiDAR aerotransportado dentro da cobertura GEDI: RMSE de 7,9 m e viés de 1,7 m (16,2%) contra 9,1 m e −4,5 m (−25,2%) do UMD [p. 4].
- Fora da cobertura GEDI: RMSE médio de 5,3 m e viés de 0,5 m (19,4%); na região mais ao norte (Finlândia, 70° N), RMSE de 3,0 m e viés de 0,5 m [p. 4].
- Cobertura global: 53,6 × 10^6 km² (41% da massa continental) com vegetação > 5 m; 39,6 × 10^6 km² (30%) > 10 m; 6,7 × 10^6 km² (5%) > 30 m [p. 5].
- Apenas 34% de todas as copas > 30 m estão em áreas protegidas [p. 5].
- Filtragem dos 20% mais incertos reduz o RMSE em 13% (6,0 m para 5,2 m) e o viés em 23% (1,3 m para 1,0 m) [p. 4].
- Custo computacional: ≈ 27.000 horas de GPU (≈ 3 anos de GPU), 10 dias de tempo real; ≈ 6.750 kWh e ≈ 729 kg CO2-equivalente para o mapa atual [p. 4, p. 10].
- Em Sabah (Bornéu), a altura estimada acompanha a densidade de carbono acima do solo, com relação sensível até ≈ 60 m [p. 6].

## 6. Limitações que os próprios autores reconhecem

- A resolução espacial efetiva é inferior aos 10 m nominais: cada pixel indica a maior altura de copa dentro de uma pegada GEDI de ≈ 25 m de diâmetro [p. 6].
- A supervisão esparsa impede que o modelo veja variações de alta frequência entre pixels vizinhos, e a incerteza de geolocalização do GEDI versão 1 (15–20 m) adiciona ruído [p. 6].
- Artefatos de mosaico em altas latitudes do hemisfério norte, em boa parte deslocamentos constantes entre tiles [p. 6].
- Tendência a superestimar áreas de vegetação muito baixa (< 5 m); acima de 35 m o viés negativo cresce com a altura, embora menor que o do UMD [p. 4, p. 6].
- A calibração da incerteza piora para valores baixos (< 4 m de desvio padrão) e varia por bioma, podendo exigir recalibração [p. 4].
- O modelo é treinado para o período de maio a setembro e não é robusto fora dele em regiões de alta sazonalidade [p. 8].
- A tundra é sub-representada, pois o GEDI não vai além de 51,6° N, e suas referências locais são ruidosas [p. 2].
- Mapear biomassa diretamente a 10 m pode não ser significativo nos trópicos, onde copas individuais excedem o pixel; recomenda-se resolução mais grosseira (por exemplo, 0,25 ha) [p. 6–7].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o desenho metodológico (Sentinel-2 como único preditor na inferência, ensemble probabilístico, supervisão esparsa com GEDI) é diretamente replicável para Goiás, que está dentro da cobertura GEDI e dispõe de acervo Sentinel-2 gratuito [p. 2, p. 8].
- **Serve:** a camada de incerteza por pixel permite filtrar estimativas ruins e reduzir RMSE e viés, útil no controle de qualidade de mapas de silvicultura [p. 4].
- **Serve com ressalva:** a altura de dossel é tratada como indicador de biomassa e estoque de carbono, mas o estudo não gera mapa de biomassa; a conversão exige equações alométricas e dados de campo [p. 6].
- **Não serve:** não há validação nem calibração para plantios de eucalipto ou para o Cerrado goiano — as 24 áreas de validação aérea estão nas Américas do Norte/Central e na Europa, e as estimativas sofrem superestimação em vegetação baixa (< 5 m) e resolução efetiva de ≈ 25 m, inadequada para talhões de curta rotação [p. 4, p. 6].

## 8. Frases citáveis (literais)

- "Our approach improves the retrieval of tall canopies with typically high carbon stocks." [p. 1]
- "Notably, the relationship between carbon and canopy height is sensitive up to ≈ 60 m." [p. 6]
