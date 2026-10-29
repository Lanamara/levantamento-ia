# RELATÓRIO — Cleonice Batista Regis Soares (2021)

## 1. Referência

Soares, Cleonice Batista Regis; Martins, Alécio Perini (2021). "Análise empírica da fragilidade ambiental na microrregião Rio Vermelho (GO)". **Geosul**, Florianópolis, v. 36, n. 80, p. 68–94, set./dez. 2021. DOI: 10.5007/2177-5230.2021.e74266.

O `TEXTO.txt` está completo (introdução, método, resultados, considerações finais, referências e notas de autor) e corresponde ao artigo do DOI indicado.

## 2. Pergunta do estudo

Identificar níveis hierarquizados de Fragilidade Potencial e de Fragilidade Emergente na Microrregião Geográfica Rio Vermelho (GO), para subsidiar a tomada de decisão e o planejamento do uso sustentável dos recursos naturais.

## 3. Área e dados

- Microrregião Geográfica Rio Vermelho, noroeste goiano, entre 14°00'–16°15'S e 49°45'–51°45'W, com 9 municípios (Araguapaz, Aruanã, Britânia, Faina, Goiás, Itapirapuã, Jussara, Matrinchã e Santa Fé de Goiás), 20.214,8 km² e 86.408 habitantes estimados em 2018 [p. 4].
- Período: uso e cobertura da terra de 2018; série pluviométrica de 32 anos (1985–2017); mapeamento temático de 2018 [p. 5–6].
- Sensores e fontes: Landsat-8 OLI (223/071, 223/070, 222/071), resolução espacial de 15/30 m, USGS (2018); SRTM de 30 m (dissecação, hipsometria, declividade); solos em 1:1.000.000 (Projeto RADAMBRASIL/Agência Ambiental de Goiás, 2005); geologia e geomorfologia em 1:500.000 (SIC); base cartográfica em 1:100.000 (IBGE, 2016); 19 postos pluviométricos da rede ANA [p. 5].
- Amostras: 121 pontos cadastrados com GPS de navegação em 2 campanhas de campo para validar o mapa de 2018 [p. 6]; 19 postos pluviométricos [p. 5]. Número de amostras de treinamento da classificação: não informado.

## 4. Método

- Modelo de Ross (1994), com hierarquização em 5 classes e pesos de 1 (muito baixa) a 5 (muito alta) para cada variável [p. 7].
- Fragilidade Potencial: sobreposição de dissecação do relevo (matriz de índices, dados SRTM), erosividade da chuva (EI30 = 67,355 (r²/P)^0,85; Wischmeier e Smith, 1978, adaptada por Lombardi e Moldenhauer, 1977) e classes de solo [p. 7–8]; pluviosidade interpolada por IDW a partir dos 19 postos [p. 8].
- Fragilidade Emergente: Fragilidade Potencial combinada ao grau de proteção do uso e cobertura da terra (Landsat-8 OLI, classificação supervisionada semiautomática por segmentação e pós-classificação visual; SPRING 5.5.5 e ArcGIS 10.6.1) [p. 6, 9].
- Validação: matriz de erro e coeficiente kappa de Cohen (Congalton, 1991), com nível de confiança de 94% [p. 6–7].

## 5. Resultados principais

- Fragilidade Potencial (2018), 4 classes: muito baixa 37,57%, baixa 29,13%, média 32,81% e alta 0,49% [p. 18]; áreas de 7.594,056; 5.888,996; 6.633,376 e 98,378 km², total de 20.214,81 km² [p. 19].
- As classes muito baixa e baixa somam 66,7% da área [p. 19].
- Fragilidade Emergente (2018), 3 classes: baixa 69,04% (13.955,449 km²), média 30,94% (6.254,637 km²) e alta 0,02% (4,724 km²) [p. 20–21]; não há classes muito baixa nem muito alta [p. 20].
- A classe emergente resulta praticamente da junção das classes muito baixa e baixa da fragilidade potencial [p. 20].
- Erosividade média de 507,4571 t ha⁻¹ ano⁻¹, classe média [p. 14]; pluviosidade entre 1.300 e 1.700 mm, concentrada de outubro a março [p. 14].
- Fragilidade pluviométrica: baixa 52,26% e média 37,74% [p. 13].
- Dissecação do relevo: muito baixa 19.082,28 km² (94,40%), baixa 741,57 km² (3,67%), média 301,81 km² (1,49%), alta 80,14 km² (0,40%) e muito alta 9,01 km² (0,04%) [p. 15].
- Solos: muito baixa 9.908,01 km² (49,01%, Latossolos), média 1.671,37 km² (8,27%, Argissolos), alta 5.971,43 km² (29,54%, Cambissolos) e muito alta 2.664 km² (13,18%, Neossolos) [p. 16].
- Grau de proteção do uso e cobertura: muito baixa 0,75 km² (0,004%), baixa 476,4 km² (2,36%), média 11.788,12 km² (58,31%, pastagem e silvicultura) e alta 7.949,54 km² (39,33%) [p. 17].
- Cinco unidades de paisagem, entre elas Planície Fluvial (1.179,97 km²/5,84%) [p. 9] e relevo de morros, colinas e estruturas dobradas com forte dissecação (4.411,16 km²/5,84%) [p. 13].
- Desmatamento: 675,44 km² entre 2000 e 2010 e 276,31 km² entre 2010 e 2018 [p. 21].
- APP com 2.041,23 km² (10,10%), dos quais 154,19 km² a recompor; Reserva Legal averbada com 641,18 km² (3,17%) e proposta com 2.464,73 km² (12,19%) [p. 21–22].
- Agricultura irrigada por pivô central: 112,5 km² em 2000 para 253,02 km² em 2018; sequeiro: 17,53 km² para 225,65 km² [p. 22]; pivôs centrais de 12 para 249 entre 1988 e 2018 [p. 22].

## 6. Limitações que os próprios autores reconhecem

- A atribuição de pesos às variáveis "é dotada de subjetividade", podendo levar a divergências por serem abstrações da realidade baseadas em conceitos [p. 24].
- O modelo fornece apenas "níveis básicos de diferenças entre os ambientes analisados" [p. 24].
- Apontam a necessidade de estudos em escalas maiores para estruturar planos de desenvolvimento sustentável [p. 24].
- Ressalvam que as áreas de fragilidade muito baixa não dispensam sistemas de manejo, por causa de suas limitações de uso [p. 15].

## 7. O que serve ao projeto e o que não serve

- Serve: o fluxo de trabalho é replicável no Cerrado goiano (Landsat-8 OLI + SRTM 30 m, segmentação e classificação supervisionada no SPRING, sobreposição ponderada no ArcGIS) e foi validado com 121 pontos de campo e kappa de 94% [p. 6–7], o que serve como referência de acurácia para mapear uso e cobertura em áreas de silvicultura.
- Serve: os números de transição de uso (pivô central de 112,5 para 253,02 km²; sequeiro de 17,53 para 225,65 km² entre 2000 e 2018; desmatamento de 675,44 km² em 2000–2010 e 276,31 km² em 2010–2018) [p. 21–22] contextualizam mudanças de estoque de carbono na região.
- Serve com ressalva: a silvicultura aparece só agregada à pastagem, na classe de proteção média que ocupa 58,31% da área [p. 9, 17]; área de silvicultura discriminada: não informado.
- Não serve: o artigo não estima biomassa, estoque de carbono, índices de vegetação nem emprega sensoriamento multissensorial; o produto é fragilidade ambiental em escala de microrregião (1:100.000), sem dados de campo de biomassa [p. 5].

## 8. Frases citáveis (literais)

- "Esse aspecto demonstra que mesmo com o uso intenso por pastagens não altera significativamente a fragilidade do ambiente." [p. 20]
- "A avaliação realizada para atribuição dos diferentes pesos a cada variável é dotada de subjetividade para determinar o quanto cada uma contribui para o estabelecimento do grau de fragilidade do ambiente, podendo levar a divergências, pois constituem em abstrações da realidade baseados em conceitos." [p. 24]
