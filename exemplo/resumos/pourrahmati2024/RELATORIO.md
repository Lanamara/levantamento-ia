# RELATÓRIO — Manizheh Rajab Pourrahmati (2024)

## 1. Referência

Manizheh Rajab Pourrahmati, Nicolas Baghdadi, Henrique Ferraco Scolforo, Clayton Alcarde Alvares, Jose Luiz Stape, Ibrahim Fayad, Guerric le Maire (2024). *Integration of very high-resolution stereo satellite images and airborne or satellite Lidar for Eucalyptus canopy height estimation*. Science of Remote Sensing, 10, 100170. DOI 10.1016/j.srs.2024.100170 [p. 1]. O `TEXTO.txt` está íntegro (do resumo às referências) e corresponde a esse DOI.

## 2. Pergunta do estudo

Se a integração de imagens stereo Pleiades com Lidar aerotransportado (ALS) ou orbital (GEDI) permite estimar a altura do dossel de plantações de eucalipto com acurácia suficiente, e se o GEDI pode substituir o DTM derivado de ALS quando não há voo Lidar [p. 2–3].

## 3. Área e dados

- **Locais:** dois sítios no Brasil — São Paulo (SP), semi-montanhoso, altitude 600–1050 m, declividade média 18° (máxima 28°); e Mato Grosso do Sul (MS), plano, altitude 250–400 m, declividade média 2° [p. 3].
- **Período:** imagens Pleiades de setembro de 2020 (SP) e maio de 2021 (MS) [p. 3–4]; ALS de 2017 [p. 3]; GEDI L2A de 2019 a 2023 [p. 4]; inventário de campo de 2012 a 2023 em SP e de 2018 a 2023 em MS [p. 4].
- **Sensores/fontes:** Pleiades 1B, banda pancromática, GSD de 0,72–0,82 m, razão B/H de 0,57 (SP) e 0,78 (MS) [p. 4]; ALS com sensor Harrier 68i, densidade de 5,0 pt/m², footprint de 31 cm, altura de voo de 629,23 m, DTM de 0,5 m e acurácia altimétrica de 5 cm [p. 3–4]; GEDI L2A, métrica `elev_lowestmode_a1`, footprint de ~25 m [p. 4–5].
- **Amostras:** 60 parcelas de 400 m² em SP e 55 em MS, em grade quase sistemática a cada 10 ha [p. 4]. Faixas de H<sub>mean</sub>: 6,6–30,4 m (SP) e 9,3–19,9 m (MS); H<sub>max</sub>: 8,2–36,9 m (SP) e 11–21,9 m (MS); idade de 1,9–10,7 anos (SP) e 1,8–4,5 anos (MS) [p. 4]. Densidade média de 1220 árvores/ha (SP) e 1190 (MS) [p. 4]. Número de tiros GEDI usados: não informado.

## 4. Método

- **DSM a partir de stereo:** DSM<sub>P</sub> gerado pelo serviço DSM-OPT (ForM@Ter/MicMac), sem GCPs, alinhado ao Copernicus GLO-30, 1 m e reamostrado para 0,5 m; corrigido em −2,0 m (SP) e +5,5 m (MS) por viés medido sobre estradas [p. 5].
- **CHM com ALS:** CHM<sub>ALS</sub> = DSM<sub>P</sub> − DTM<sub>ALS</sub>; por parcela, CHM<sub>ALSmax</sub> é a média dos 10% de pixels mais altos e CHM<sub>ALSmean</sub> a média de todos os pixels [p. 5].
- **CHM com GEDI:** CHM<sub>Gedi</sub> = DSM<sub>P</sub> − DTM<sub>Gedi</sub>, com DTM<sub>Gedi</sub> = `elev_lowestmode_a1` + Δ, sendo Δ a diferença de elevação GLO-30 entre o tiro GEDI e a parcela, além da conversão geoidal para WGS84 [p. 5].
- **Validação:** comparação com H<sub>mean</sub> (média de 10 árvores centrais) e H<sub>max</sub> (quatro árvores mais altas), com interpolação linear das medições de campo para a data Pleiades (intervalo máximo de seis meses); métricas RMSE, rRMSE, r de Pearson e bias, mais análise do efeito da declividade (0–28°) [p. 5].

## 5. Resultados principais

- **CHM<sub>ALSmax</sub> vs. H<sub>mean</sub>, sítio SP:** bias de 1,4 m, RMSE de 3,1 m, rRMSE de 18,5% e r = 0,98 [p. 6].
- **CHM<sub>ALSmax</sub> vs. H<sub>mean</sub>, sítio MS:** bias de 1,9 m, RMSE de 2,3 m, rRMSE de 17,3% e r = 0,92 [p. 6].
- **Subestimativa em plantios jovens:** para alturas abaixo de 20 m, bias de 1,9 m (MS) e 2,8 m (SP) [p. 6].
- **Declividade:** unbiased RMSE de 1,6 m para declives < 10° e de 2,6 m para > 10°; não houve correlação significativa entre CHM<sub>ALS</sub> e declividade [p. 6, p. 8].
- **DTM<sub>Gedi</sub> vs. DTM<sub>ALS</sub>:** r = 0,99 nos dois sítios; bias de 3,3 m e RMSE de 8 m (rRMSE 1,0%) em SP; bias de 0,6 m e RMSE de 2,7 m (rRMSE 0,8%) em MS [p. 9].
- **CHM<sub>Gedimax</sub> vs. H<sub>mean</sub>:** SP com bias de 1,3 m, RMSE de 3,6 m, rRMSE de 20,5% e r = 0,92; MS com bias de 2,2 m, RMSE de 3,4 m, rRMSE de 24,9% e r = 0,76 [p. 6].
- **Perda de acurácia do GEDI frente ao ALS:** cerca de 2% em SP e 7,6% em MS [p. 9].

## 6. Limitações que os próprios autores reconhecem

- A baixa resolução espacial do GEDI (footprint de 25 m) pode limitar o uso em terreno complexo ou dossel denso [p. 9–10].
- A razão B/H de 0,57 em SP excede a faixa ótima e pode contribuir para erros no DSM<sub>P</sub> em relevo complexo [p. 9].
- A declividade máxima analisada foi de 28°, e declives maiores podem revelar padrões não capturados [p. 8].
- Subestimativa sistemática em plantios jovens com dossel aberto, atribuída a falhas de plantio, menor densidade e fechamento progressivo do dossel [p. 6–7].
- Parte dos erros pode vir das medições de campo (sobretudo topo de árvores altas) e da qualidade do DSM<sub>P</sub> [p. 9]; é necessário quantificar cada fonte de erro e desenvolver estratégias de mitigação [p. 9].
- A interpolação temporal de até seis meses introduz erro tipicamente inferior a 50 cm [p. 5]; o DTM<sub>ALS</sub> só existia onde havia parcelas de campo [p. 4, p. 10].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o par metodológico DSM de stereo VHR menos DTM Lidar para gerar CHM, com validação por H<sub>mean</sub>/H<sub>max</sub> de parcelas de inventário — desenho diretamente transferível para eucalipto em Goiás [p. 5].
- **Serve:** a evidência de que o GEDI (`elev_lowestmode_a1`, com correção por GLO-30) substitui o DTM de ALS com r = 0,99 e perda de 2% a 7,6% na acurácia, o que viabiliza o método onde não há voo Lidar [p. 9].
- **Serve:** os vieses quantificados (subestimativa abaixo de 20 m, correção de −2,0/+5,5 m no DSM, efeito da declividade) como pontos de controle e estratificação do ajuste local [p. 5–6].
- **Não serve:** o artigo entrega altura de dossel, não biomassa nem estoque de carbono; não cobre Goiás nem Cerrado; usa ALS de 2017 [p. 3], uma data Pleiades por sítio [p. 4] e declara que os dados não podem ser compartilhados [p. 11].

## 8. Frases citáveis (literais)

- "Two points are highlighted: 1) for all slope ranges, Pleiades underestimates canopy height; 2) the variation of the residuals is higher for slopes greater than 10°." [p. 6]
- "The advantage of using GEDI data lies in its freely accessible global coverage, offering an alternative to ALS data for DTM extraction, particularly in regions where ALS data availability is limited or cost-prohibitive." [p. 2]
