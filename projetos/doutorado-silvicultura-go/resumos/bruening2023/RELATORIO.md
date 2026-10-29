# RELATÓRIO — Jamis M. Bruening (2023)

## 1. Referência

Bruening, J.; May, P.; Armston, J.; Dubayah, R. (2023). *Precise and unbiased biomass estimation from GEDI data and the US Forest Inventory*. **Frontiers in Forests and Global Change**, 6:1149153. DOI: 10.3389/ffgc.2023.1149153 [p. 1].

O `TEXTO.txt` corresponde ao artigo completo do DOI (18 páginas, incluindo referências); não está truncado.

## 2. Pergunta do estudo

Quais são as causas das diferenças sistemáticas entre as estimativas de AGBD (aboveground biomass density) do GEDI e as estimativas design-based do inventário florestal norte-americano (FIA) por hexágonos, e como corrigi-las dentro do arcabouço de hybrid inference [p. 2].

## 3. Área e dados

- Local: Estados Unidos continental (CONUS), em tesselação de hexágonos iguais de ~640 km², n = 12.550 hexágonos [p. 2].
- Período dos dados GEDI: 18/04/2019 a 11/05/2022 [p. 3]. Período das parcelas FIA utilizado: não informado.
- Sensores/fontes: GEDI L2A (métricas de forma de onda por footprint), GEDI L4A (AGBD por footprint) e produto GEDI L4B em grade de 1 km [p. 3]; parcelas de campo do FIA (~27 parcelas por hexágono) [p. 3]; estimativas FIA pós-estratificadas de Menlove e Healey (2020) como referência [p. 2].
- Amostras: 12.550 hexágonos, dos quais 11.631 hexágonos "intactos" (área ≥ 600 km²) com média de 43.516 observações GEDI cada [p. 10]; 9.851 hexágonos com duas ou mais parcelas florestais FIA para cálculo de erro-padrão [p. 11–12]; 10 estratos florestais de calibração [p. 6–7].

## 4. Método

1. Repetição da validação GEDI–FIA por hexágono (dB = FIA − GEDI) e uso da estatística *t* de McRoberts et al. (2019) como heurística de diferença sistemática, não como teste formal [p. 4].
2. Filtragem adicional: (a) nuvens/nevoeiro, removendo observações com altura máxima acima de 1,75 × a altura máxima observada nas tabelas de árvores do FIA [p. 4]; (b) topografia, removendo observações em declive cuja altura de dossel exceda o percentil 99 das alturas de terreno plano na mesma classe de cobertura [p. 4].
3. Modelos SISA (scale-invariant small area): modelos Fay-Herriot com erro autorregressivo simultâneo (SAR), calibrados em 10 estratos usando médias hexagonais de métricas GEDI como preditoras e as estimativas FIA como resposta; 66 modelos candidatos (DBT) e 91 (MIX/NT), com seleção por similaridade das distribuições em nível de parcela [p. 5–7].
4. Validação por recalibração em quatro resoluções hexagonais (~12.400, ~1.770, ~250 e ~640 km²), comparando intervalos de confiança de 95% de β [p. 7–8]; geração das estimativas "filtered" e "fusion" com hybrid inference em hexágonos e em grade de 1 km [p. 3].

## 5. Resultados principais

- Estimativas originais: GEDI 52,40 Mg ha⁻¹ vs. FIA 35,43 Mg ha⁻¹; diferença média (FIA − GEDI) de −10,48 Mg ha⁻¹ e RMSD de 27,99 Mg ha⁻¹; mediana de *t* = −1,13 (Q1 −2,81; Q3 0,24) [p. 10–11].
- Após filtragem: diferença média −8,46 Mg ha⁻¹, RMSD 27,04 Mg ha⁻¹, mediana de *t* = −0,87 (−2,47; 0,48) [p. 11].
- Após fusão (SISA): AGBD média 40,53 Mg ha⁻¹, diferença média 1,39 Mg ha⁻¹, RMSD 18,10 Mg ha⁻¹, mediana de *t* = 0,11 (−0,88; 0,98) [p. 10–11].
- Redução de viés total de 86,7%, sendo 19,3% pela filtragem e 67,5% pelos modelos SISA [p. 11].
- Filtro de nuvens removeu 618.615 observações, 0,11% das que passavam nos filtros originais do GEDI [p. 10].
- A filtragem removeu, em média, 59 observações por hexágono e reduziu a estimativa em 1,91 Mg ha⁻¹; nenhuma remoção em 3.752 hexágonos; 14,1% dos hexágonos tiveram >100 observações removidas (queda média de 8,8 Mg ha⁻¹ em 1.768 hexágonos); 0,58% tiveram >1.000 removidas (queda média de 21,94 Mg ha⁻¹ em 73 hexágonos) [p. 10].
- Efeito dos modelos SISA: queda média de 9,85 Mg ha⁻¹ entre "filtered" e "fusion"; maior queda em DBT_S (−53,68 Mg ha⁻¹) e maior aumento em NT_M (+26,45 Mg ha⁻¹) [p. 10].
- Erro-padrão médio por hexágono: 1,94 (original), 1,85 (filtered), 2,57 (fusion) e 10,88 Mg ha⁻¹ (FIA); em percentual da média: 6,0%, 7,1%, 12,9% e 38,1% [p. 11–12].
- Em 1 km: AGBD média de 45,6 Mg ha⁻¹ (original) e 37,2 Mg ha⁻¹ (fusion); erro-padrão médio de 4,5 e 4,8 Mg ha⁻¹ em células <100 Mg ha⁻¹, e 11,4% e 10,9% da média em células >100 Mg ha⁻¹ [p. 12].
- Consistência de β entre escalas: DBT_S, DBT_N, NT_N e NT_W estáveis (44,4% de cobertura florestal); DBT_C, MIX_N e NT_C instáveis (25,5% florestados); MIX_S, NT_S e NT_W intermediários (42,8%) [p. 10].
- Modelos L4A da América do Norte: DBT com n = 873, NT com n = 1,391 e GSW com n = 89 parcelas de calibração [p. 5].

## 6. Limitações que os próprios autores reconhecem

- Circularidade: as estimativas FIA foram usadas para calibrar os modelos SISA que geram as estimativas "fusion", logo a concordância fusion–FIA é esperada [p. 16].
- A hipótese de invariância de escala foi violada em algum grau em parte das áreas: SISA viesado para baixo acima de ~50 Mg ha⁻¹ em DBT_C e NT_C, e viés provavelmente maior em MIX_N, MIX_S e NT_S [p. 16].
- A escolha de 10 estratos foi "somewhat arbitrary", e a estratificação poderia ser mais orientada por dados [p. 16].
- As parcelas de calibração do GEDI são espacialmente agrupadas e representam melhor alguns estratos, podendo quebrar a hipótese de linearidade local [p. 16].
- A população de interesse difere: o FIA só estima biomassa em terras florestais, enquanto o GEDI não distingue floresta de não floresta [p. 16].
- O filtro de nuvens só remove observações com alturas acima das árvores mais altas; recomendam algoritmos melhores para nuvens baixas e nevoeiro [p. 13].
- Filtrar observações pode violar a hipótese de hybrid inference de amostra aleatória por cluster, e não implementaram tratamento de não-resposta [p. 13].
- Nos dados de calibração, os modelos L4A explicaram maior fração da variância e tiveram RMSE menor que os SISA (esperado, pois foram ajustados nesses dados); os SISA foram menos viesados apenas nas faixas <60 e >500 Mg ha⁻¹, sendo viesados para cima entre 150 e 250 Mg ha⁻¹ [p. 9–10].
- Não existe dado de referência padronizado para validar mapas globais de biomassa em 1 km [p. 2].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o arcabouço SISA/Fay-Herriot, que permite calibrar modelos de AGBD em nível de unidade (footprint) a partir de médias agregadas — solução para a ausência de parcelas de campo coincidentes com footprints, situação típica em povoamentos de silvicultura em Goiás [p. 5–7, 16].
- **Serve:** a demonstração de que a relação estrutura–biomassa varia espacialmente e que estratificação regional reduz viés, argumento para modelos regionais em vez de modelos globais do L4A [p. 5, 13–15].
- **Serve:** o protocolo de filtragem de observações afetadas por topografia e nuvens e a lógica de hybrid inference com incerteza formal (erro-padrão por unidade), replicável para quantificar incerteza do estoque [p. 4, 11–12].
- **Não serve:** a parametrização é toda norte-americana (FIA, NLCD, ecorregiões EPA, estratos L4A, 12.550 hexágonos do CONUS) e o objeto são florestas nativas dos EUA, sem floresta plantada nem variáveis de silvicultura; os preditores são apenas métricas de forma de onda do GEDI, sem sensor óptico ou dado multissensorial; e o artigo estima AGBD, não estoque de carbono (fração de carbono não informada) [p. 2–3, 6–7].

## 8. Frases citáveis (literais)

- "In total, our improvements to GEDI’s AGBD estimation process resulted in a bias reduction of 86.7%; 19.3% due to improved filtering, and the remaining 67.5% due to the SISA models." [p. 11]
- "The ability to calibrate unit level models at an aggregated scale is important because it helps overcome challenges in obtaining representative training data for remote sensing based models of AGBD." [p. 16]
