# RELATÓRIO — Gabriele Delogu (2024)

## 1. Referência

Delogu, G.; Perretta, M.; Caputi, E.; Patriarca, A.; Funsten, C.C.; Recanatesi, F.; Ripa, M.N.; Boccia, L. **Leveraging the Potential of PRISMA Hyperspectral Data for Forest Tree Species Classification: A Case Study in Southern Italy**. *Remote Sensing*, 2024, 16(24), 4788. DOI: 10.3390/rs16244788. Publicado em 22/12/2024 [p. 1]. O `TEXTO.txt` contém as 23 páginas do artigo e corresponde ao DOI informado; não está truncado.

## 2. Pergunta do estudo

Saber se uma única imagem hiperespectral PRISMA (GSD de 30 m) permite classificar categorias florestais definidas pela espécie arbórea predominante em ambiente de alta biodiversidade, e qual acurácia se obtém com diferentes volumes de informação espectral (205 bandas, 30 ou 16 componentes principais) [p. 1, 3].

## 3. Área e dados

- **Local:** Parque Regional Natural das Serre, Calábria, sul da Itália; região de interesse (ROI) de ~441 km²; parque com 17.700 ha; elevação de 800 a 1.400 m; clima Csa/Csb; ~1.600 mm de chuva por ano na estação de Mongiana [p. 3].
- **Sensor:** PRISMA, produto L2D (reflectância de superfície, atmosfericamente corrigido e ortorretificado), cena de 25/07/2023; 234 bandas originais, reduzidas a 205; GSD de 30 m, 30 km de faixa e 240 bandas de ≤12 nm no sensor [p. 2, 7].
- **Campo:** levantamento em março de 2024, com GNSS Geomax Zenith35 e os aplicativos EyeLand e QField [p. 6].
- **Amostras:** 784 parcelas de 30 × 30 m, que geraram o DS_1 com 766 pixels rotulados; o DS_2 acrescentou 1.865 pixels (informação de campo + fotointerpretação no QGIS); 7 classes [p. 7–8].

## 4. Método

1. **Pré-processamento:** conversão HDF5 → GeoTIFF, recorte da ROI e remoção de bandas sem informação (104–112, 147–163 e 232–234), restando 205 bandas; normalização *min–max* e máscara NDVI > 0,4 → Cube_R1_M [p. 7–9].
2. **Redução de dimensionalidade:** PCA com 30 componentes (99,9% da variância) → Cube_R2_M; e com 16 componentes (99,8%) → Cube_R3_M; o cubo de 205 bandas foi o terceiro conjunto [p. 9].
3. **Classificação:** CNN de cinco camadas (Hu et al., 2015), baseada só na assinatura espectral (sem informação espacial), no plugin AVHYAS do QGIS; 200 épocas, *learning rate* 0,001 e parada antecipada; 15 experimentos (3 cubos × 5 seleções aleatórias) [p. 10–11].
4. **Validação:** 70% treino e 30% validação; teste apenas com pixels de campo do DS_1 (40% para classes com mais de 100 pixels e 80% para classes menores); métricas OA, Kappa, UA, PA e F1 [p. 10–11].

## 5. Resultados principais

- **Validação:** OA média de 0,927 (Cube_R1_M), 0,924 (Cube_R2_M) e 0,923 (Cube_R3_M); a maior acurácia isolada foi 0,973, com Cube_R3_M [p. 12–13].
- **Teste:** melhor média com Cube_R2_M — OA 0,890, Kappa 0,864 e F1 0,808; Cube_R3_M: 0,885 / 0,858 / 0,800; Cube_R1_M: 0,876 / 0,847 / 0,783 [p. 13].
- **F1 por classe no teste (Cube_R2_M):** *grassland and shrubs* 0,95; *beech* 0,90; *holm oak* 0,82; *fir* 0,81; *pine* 0,78; *hygrophilous* 0,72; *chestnut* 0,68 [p. 14].
- **Validação por classe:** *chestnut* 0,96 com Cube_R1_M; *beech* e *grassland and shrubs* acima de 0,90; pior valor para *hygrophilous* (0,82) [p. 13].
- **Piores testes:** *hygrophilous* 0,65 (Cube_R1_M) e *chestnut* 0,67 (Cube_R3_M) [p. 13].
- **Síntese do Discussion:** OA média de 0,92 na validação e 0,88 no teste; Kappa 0,91 e 0,86; F1 0,92 e 0,80 [p. 17].
- **Custo computacional:** treino e validação da CNN nunca passaram de 10 minutos (laptop com Ryzen 7 PRO 7840HS, 32 GB de RAM) [p. 11].
- **Abstract:** F1 acima de 0,75 para *fir* (0,81), *pine* (0,77), *beech* (0,90) e *holm oak* (0,82); *beech* com a maior acurácia (0,92) e *chestnut* (0,68) e *hygrophilous* (0,69) com as menores [p. 1]. Observação: esses valores do abstract misturam médias de cubos diferentes — *pine* 0,77 é a média do Cube_R1_M (0,78 no Cube_R2_M) e *beech* 0,90 só aparece nos cubos de PCA (Cube_R2_M e Cube_R3_M) [p. 1, 14].

## 6. Limitações que os próprios autores reconhecem

- Uso de uma única imagem, sem série temporal nem fusão de fontes; os resultados provavelmente melhorariam com análise multitemporal ou com LiDAR [p. 18].
- As acurácias muito altas podem indicar *overfitting*, considerando o tamanho de DS_1 e DS_2; uma base rotulada maior reduziria a variação entre testes [p. 18].
- Coberturas mistas são pior classificadas: sem processamento adicional, como *spectral unmixing*, a classificação com 30 m é menos eficaz nessas áreas [p. 18].
- Disponibilidade escassa de dados hiperespectrais: poucos satélites ativos, clima que impede aquisições regulares, revisita de ~16 dias e dificuldade de acesso aos dados [p. 18].
- O pós-processamento dos dados de campo coletados por smartphone é demorado e exige verificação pixel a pixel [p. 18].
- A classe "Grassland and shrubs" não teve parcelas de campo: os 200 pixels vieram só de fotointerpretação [p. 8].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o encadeamento de pré-processamento (remoção de bandas ruins, *min–max*, máscara NDVI) e o teste de dimensionalidade (205 bandas vs. 30 e 16 CPs, retendo 99,8–99,9% da variância) é replicável com PRISMA/EnMAP em talhões de Goiás [p. 9].
- **Serve:** o protocolo de acurácia — teste apenas com pixels de campo (DS_1), cinco repetições aleatórias e F1 por classe — e a evidência de que 30 m bastam em cobertura pura, situação mais próxima de silvicultura do que de floresta natural [p. 10–11, 18].
- **Não serve:** o artigo não estima biomassa nem estoque de carbono — não há AGB, volume, equações alométricas ou variáveis contínuas, apenas classes discretas [p. 1, 3].
- **Não serve:** as classes e espécies mediterrâneas (*Fagus*, *Abies alba*, *Pinus nigra*, *Castanea sativa*, *Quercus ilex*) não se transferem para eucalipto/pinus de Goiás; cena única e ausência de LiDAR ou de série temporal limitam o uso para estrutura de dossel [p. 7, 18].

## 8. Frases citáveis (literais)

- "The final result, measured on a test dataset, showed an F1 greater than 0.75 for four classes: fir (0.81), pine (0.77), beech (0.90), and holm oak (0.82)." [p. 1]
- "It is likely that the results could be further improved with multitemporal analysis or by combining different sources (e.g., LiDAR)." [p. 18]
