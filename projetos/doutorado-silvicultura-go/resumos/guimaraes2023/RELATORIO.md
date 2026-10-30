# RELATÓRIO — ELIZA EMANOELLE SILVA GUIMARÃES (2023)

## 1. Referência

- Autores: Eliza Emanoelle Silva Guimarães; José Carlos de Souza (Universidade Estadual de Goiás — UEG, Anápolis/GO) [p. 1]
- Ano: 2023
- Título: Indicador de fragilidade ambiental para a bacia hidrográfica do Ribeirão João Leite (Goiás, Brasil)
- Revista: Revista Mirante, Anápolis (Goiás, Brasil), v. 16, n. 3, p. 18–33, 2023. ISSN 1981-4089. Dossiê especial "Questões ambientais contemporâneas: as realidades Moçambique–Brasil" [p. 1]
- DOI: 10.31668/mirante.v16i3.14377 (informado no pedido; o arquivo traz apenas o cabeçalho da revista)
- Integridade do texto: `TEXTO.txt` está completo — introdução, materiais e métodos, resultados, considerações finais e referências [p. 1–16]. Título e escopo conferem com o DOI indicado.
- Convenção de páginas: as marcas `[página N]` do arquivo correspondem às páginas impressas 18–33 (página 1 = p. 18).

## 2. Pergunta do estudo

Desenvolver um indicador de fragilidade ambiental para a bacia hidrográfica do Ribeirão João Leite a partir de modelagem de fragilidade potencial e emergente [p. 2].

## 3. Área e dados

- Local: bacia hidrográfica do Ribeirão João Leite, porção central de Goiás, entre 16°13' e 16°39' S e 48°57' e 49°11' O, área de 766 km², abrangendo Goiânia, Anápolis, Terezópolis, Goianápolis, Nerópolis e Ouro Verde; desde o Decreto nº 5.704/2002 é Área de Proteção Ambiental (APA), com o Parque Ecológico Altamiro de Moura Pacheco em seu interior [p. 3].
- Período: uso e cobertura da terra de 2021 [p. 4]; chuva de 1989 a 2019 [p. 4]; geologia com datações do Paleoproterozóico ao Quaternário [p. 5].
- Fontes e sensores:
  - Uso e cobertura: Projeto MapBiomas, Coleção 7, ano 2021 [p. 4].
  - Declividade: MDE SRTM, resolução espacial de 30 m, USGS [p. 4].
  - Solos: base cartográfica da EMATER-GO (SIEG) [p. 4].
  - Geologia: base da Superintendência de Geologia e Mineração de Goiás, de 2009 (SIEG) [p. 4].
  - Chuva: 4 estações pluviométricas da ANA (Hidroweb) — Goiânia, Anápolis, Goianápolis e Ouro Verde de Goiás —, interpoladas por Inverso do Quadrado da Distância no QGIS 3.22 [p. 4].
- Número de amostras: não informado (estudo de modelagem espacial, sem amostragem de campo); as bases vetoriais foram convertidas para raster com pixels de 30×30 m [p. 4].

## 4. Método

- Adaptação da proposta de Ross (1994, 2011, 2012), com cinco variáveis: unidades geológicas, declividade, tipo de solo, uso e cobertura do solo e totais de chuva; a inclusão da geologia é o incremento próprio dos autores [p. 3–4].
- Reclassificação de cada variável em cinco classes — muito baixa, baixa, média, alta e muito alta — segundo Ross (1994, 2011), Amaral e Ross (2009) e Moreira et al. (2008) [p. 4].
- Fragilidade potencial (FP) = média aritmética, na calculadora raster, das fragilidades de geologia, solos, declividade e chuva [p. 4].
- Fragilidade emergente (FE) = cruzamento da FP com o grau de proteção do uso e cobertura, reclassificado em sentido inverso (1 = maior proteção, 5 = menor proteção) [p. 5]; todo o geoprocessamento em QGIS 3.22 [p. 5].

## 5. Resultados principais

- Geologia: seis unidades; Complexo granulítico Anápolis-Itauçu (classe baixa) com 514,45 km² (67,24%), Suíte Jurubatuba (moderada) com 184,22 km² (24,08%), coberturas detrito-lateríticas ferruginosas (muito baixa) com 42,89 km² (5,60%), Sequência metavulcanossedimentar Silvânia (alta) com 12,99 km² (1,69%) e depósitos aluvionares (muito alta) com 12,42 km² (1,36%) [p. 6].
- Solos: três classes — Latossolo Vermelho, fragilidade baixa, 520,21 km² (67,84%); Argissolos, moderada, 180,30 km² (23,53%); Cambissolos, alta, 66,29 km² (8,63%) [p. 7].
- Chuva: média dos totais de precipitação de 1989 a 2019 entre 1.472 mm e 1.525 mm, com toda a bacia (766,80 km², 100%) enquadrada na classe alta [p. 8]; a tabela cita volumes de 1.600 a 1.800 mm/ano e concentração de 70% a 80% do total entre novembro e abril [p. 9].
- Declividade: 0–6% em 195,08 km² (24,47%), 6–12% em 318,80 km² (42,71%), 12–20% em 172,36 km² (22,50%), 20–30% em 62,91 km² (8,21%) e >30% em 16,13 km² (2,11%) — cerca de 90% da área entre 6% e 20% [p. 10].
- Fragilidade potencial: predomínio das classes baixa (318,7 km²; 41,6%) e moderada (207,27 km²; 27,06%); os maiores níveis ocorrem nas bordas da bacia [p. 10–11].
- Uso e cobertura: treze classes identificadas; grau de proteção baixo em 533,35 km² (69,73%), muito alto em 174,27 km² (22,65%), muito baixo em 35,08 km² (4,58%), moderado em 19,21 km² (2,51%) e alto em 4,09 km² (0,53%) [p. 12–13].
- Fragilidade emergente: classe alta em 63,68% da bacia, ou 487,77 km² [p. 13]; classe muito baixa em 141,65 km² (18,5%), nas coberturas naturais de Cerrado (Cerradão e Mata Seca) [p. 14].
- Área total da bacia: 766,80 km² [p. 6].

## 6. Limitações que os próprios autores reconhecem

- Necessidade de aprimorar a escala das bases cruzadas, tornando-as maiores e mais detalhadas, para produtos cartográficos mais precisos e aplicáveis à gestão de pequenas áreas [p. 15].
- Restam poucas áreas de cobertura natural na bacia, o que limita a leitura da paisagem apenas pelos componentes do meio físico [p. 14].
- Observação metodológica dos autores: a variável uso e cobertura é reclassificada em sentido inverso das demais, pois mede potencial de proteção, e não fragilidade — inversão que precisa ser respeitada em replicações [p. 5].

## 7. O que serve ao projeto e o que não serve

- Serve: a estrutura de modelagem FP/FE em ambiente raster de 30 m (geologia + solos + declividade + chuva, depois uso e cobertura), replicável para bacias com silvicultura em Goiás [p. 3–5].
- Serve: o tratamento do uso e cobertura como grau de proteção invertido (1 = maior proteção, 5 = menor) via MapBiomas Coleção 7 e SRTM 30 m — insumos gratuitos e compatíveis com o fluxo de sensoriamento remoto do projeto [p. 4–5].
- Não serve: o artigo não trata de biomassa, estoque de carbono, índices de vegetação nem sensoriamento multissensorial; não há qualquer dado de campo ou de carbono [p. 1–16].
- Não serve: a silvicultura aparece apenas como uma classe dentro do grau de proteção moderado (grupo de 19,21 km², 2,51%, junto com formação campestre, cana e outras lavouras perenes), sem discriminação de espécie, idade ou manejo [p. 12].

## 8. Frases citáveis (literais)

- "Os resultados da fragilidade emergente indicaram predominância da classe alta, ocorrendo em 63,68% da área da bacia." [p. 1]
- "apesar de apresentar estabilidade quanto à Fragilidade Potencial, por seus componentes do meio físico, as atividades agropecuárias desenvolvidas na área maximizam a Fragilidade Emergente." [p. 14]
