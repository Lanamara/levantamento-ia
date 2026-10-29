# RELATÓRIO — Derblai Casaroli (2018)

## 1. Referência

- Autores: Derblai Casaroli; Flávio de Oliveira Rosa; José Alves Júnior; Adão Wagner Pêgo Evangelista; Barbara Vieira de Brito; Diogo Silva Pena.
- Ano: 2018.
- Título: "Aptidão edafoclimática para o mogno-africano no Brasil" ("Edaphoclimatic aptitude to African mahogany in Brazil").
- Revista: Ciência Florestal (Santa Maria), v. 28, n. 1, p. 357-368, jan.-mar. 2018. ISSN 1980-5098.
- DOI: 10.5902/1980509831606 — confere com o texto integral fornecido em `TEXTO.txt` [p. 1].

## 2. Pergunta do estudo

Quais zonas do território brasileiro apresentam aptidão edafoclimática (temperatura, pluviosidade e solo) para o cultivo do mogno-africano (*Khaya ivorensis* A. Chev.) [p. 1; p. 3].

## 3. Área e dados

- Área de estudo: todo o território brasileiro; região de referência = 11 países da Costa Ocidental Africana (Libéria, Costa do Marfim, Gana, Togo, São Tomé e Príncipe, Nigéria, Camarões, Gabão, República do Congo, República Democrática do Congo e Angola) [p. 3].
- Período: não informado (normais climatológicas e bases consultadas com acesso em 2013) [p. 3].
- Fontes: normais climatológicas de temperatura e pluviosidade anual do IBAMA (2013); mapas de solos da EMBRAPA (2006) e do IBGE (2013); clima e solo da região de origem por Grey (1979), FreeMeteo (2013) e USDA (1999); altitudes do MDE SRTM, GEOTIFF, 90 m, 16 bits, WGS-84 [p. 3].
- Número de amostras: não informado para solos; o modelo climático foi gerado a partir das posições geográficas das estações meteorológicas, sem número declarado [p. 3]. Produtos derivados: 6 classes de precipitação (150 a 3.625 mm), 9 classes de temperatura média anual (13 °C a 29 °C) e 37 classes de solos [p. 4].

## 4. Método

- Critérios de exigência definidos a partir da região de origem: temperatura basal inferior 18 °C, superior 35 °C; faixa ótima 23,5 °C a 29,5 °C; temperatura ótima 27,5 °C; precipitação apta de 830 a 3.000 mm ano⁻¹; solos aptos = Argissolo, Latossolo, Neossolo Quartzarênico, Neossolo Litólico, "Insular" e "Equatorial" [p. 3; p. 7].
- Geração de mapas-base de precipitação, temperatura e solos no ArcGIS, com interpolação por Krigagem Ordinária (*Interpolate to Raster*, Spatial Analyst) e desmembramento do plano de informação de solos em dez PIs [p. 3].
- Validação do modelo por regressão linear simples entre temperatura estimada e observada, com correlação *r* de Pearson, R² e índice de concordância *d* de Willmott; validação cruzada dos semivariogramas [p. 3; p. 6].
- Sobreposição das três variáveis em classes de aptidão: apta; restrições leves; restrições moderadas; restrita; inapta [p. 7–8].

## 5. Resultados principais

- Ajuste da estimativa de temperatura: r = 0,81, R² = 0,78 e d de Willmott = 0,86 [p. 4].
- Validação cruzada: temperatura com média 0,0737 e erro quadrático médio 1,9350; precipitação com média -5,8331 e erro quadrático médio 272,30 [p. 6].
- Semivariogramas: temperatura com pepita 0, alcance 1,966 e patamar 3,454; precipitação com pepita 101.986,7, alcance 0,593 e patamar 2.153,97 [p. 6].
- Aptidão apenas climática: 45,72% do território apto, 17,12% com baixas restrições, 31,68% com médias restrições, 5,44% com altas restrições e 0,04% inapto [p. 9].
- Aptidão apenas edáfica: 70,07% apto e 29,93% inapto [p. 9].
- Aptidão edafoclimática final: 55,62% apto, 11,66% apto com restrições leves, 25,00% apto com restrições moderadas e 7,71% restrito [p. 1; p. 9].
- Região inapta identificada: 0,01% do país, próxima ao litoral de São Paulo [p. 9].
- Estados predominantemente aptos ou com restrições leves: Amapá, Goiás, Tocantins, Ceará, Rondônia, Roraima, Pará, Piauí e grande parte do Mato Grosso, além do sul e sudoeste do Maranhão, norte, nordeste e sul do Mato Grosso do Sul, norte e leste da Amazônia e quase toda a faixa litorânea do Rio Grande do Norte ao norte do Rio de Janeiro [p. 9].
- Restrição principal no Sul do Brasil: térmica, com temperaturas inferiores a 18 °C em parte do ano [p. 9].
- Inconsistência interna observada: o resumo define como aptas temperaturas de 23 °C a 29 °C [p. 1], enquanto o método e a Figura 3 definem como apta a faixa de 18 °C a 35 °C e ótima de 23,5 °C a 29,5 °C [p. 7].

## 6. Limitações que os próprios autores reconhecem

- Carência de informações sobre solos viáveis, o que dificulta o zoneamento edáfico e levou ao uso de critérios comparativos entre solos da origem e do Brasil [p. 10].
- Cultivos de mogno-africano registrados na literatura apenas na região Centro-Oeste, não havendo determinação do crescimento na região considerada restrita [p. 10].
- As restrições indicadas apontam dificuldades possíveis de adaptação, não desempenho comprovado em campo [p. 10].
- Necessidade de estudos de campo nas diferentes regiões edafoclimáticas para validar as informações geradas [p. 10].

## 7. O que serve ao projeto e o que não serve

- Serve: critérios edafoclimáticos explícitos (18–35 °C; 830–3.000 mm ano⁻¹; classes de solo) que permitem estratificar áreas de silvicultura de *Khaya ivorensis* em Goiás antes da amostragem de biomassa [p. 3; p. 7].
- Serve: Goiás é citado entre os estados predominantemente aptos ao plantio, com respaldo em estudos anteriores no estado [p. 9; p. 10] — útil como justificativa de recorte espacial do projeto.
- Serve: uso de SRTM (90 m) para altitude e de Krigagem Ordinária com validação por *r*, R² e *d* pode ser replicado como camada auxiliar de predição [p. 3; p. 4].
- Não serve: o artigo não trata de sensoriamento remoto multissensorial, biomassa, estoque de carbono ou inventário florestal; não há número de amostras de campo, dados de crescimento, volume ou carbono, e nenhuma relação entre atributos espectrais e biomassa é estabelecida [p. 3–10].

## 8. Frases citáveis (literais)

- "Para a precipitação pluvial, consideraram-se aptas as regiões com intensidades na faixa entre 830 e 3.000 mm ano-1, tais valores se referem à menor e à maior precipitação encontrada na região de origem, sendo inaptas as áreas com precipitação inferior a 830 e superior a 3.000 mm ano-1." [p. 7]
- "Entretanto, vale ressaltar que, estudos de campo, nas diferentes regiões edafoclimáticas do Brasil, deverão ser realizados para validar estas informações." [p. 10]
