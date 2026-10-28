# RELATÓRIO — Escleide Gomes Cabral (2019)

## 1. Referência

CABRAL, Escleide Gomes; BARREIRA, Sybelle; FERREIRA, Manuel Eduardo; ARAÚJO, Lázaro Gabriel de Oliveira. A silvicultura do eucalipto no estado de Goiás: um registro histórico via sensoriamento remoto. *Pesquisa Florestal Brasileira*, Colombo, v. 39, e201801649, p. 1–15, 2019. DOI: 10.4336/2019.pfb.39e201801649 [p. 1]. O arquivo `TEXTO.txt` está íntegro (15 páginas, de "Introdução" a "Referências") e corresponde ao DOI indicado.

## 2. Pergunta do estudo

Quantificar e mapear, por sensoriamento remoto, as áreas com silvicultura (sobretudo eucalipto) no estado de Goiás e sua evolução entre 2002 e 2015, discriminando-as pelas cinco mesorregiões goianas [p. 1; p. 3].

## 3. Área e dados

- Local: estado de Goiás, 340.110,38 km², dividido em cinco mesorregiões (Centro, Leste, Noroeste, Norte e Sul Goiano), entre 12°–20° S e 45°–54° W [p. 3].
- Período: 2002 a 2015, com três marcos de mapeamento — 2002 (Probio), 2013 (TerraClass Cerrado) e 2015 (mapa próprio) [p. 4].
- Sensores e fontes: Landsat-8 OLI, cenas Level 1T obtidas no USGS, resolução espacial de 30 m e temporal de 16 dias [p. 4]. Mosaico de 24 imagens cobrindo o estado, processadas em ArcGIS® e ENVI®, datum Sirgas 2000 [p. 4]. Mapas de uso da terra do Probio (2002) e do TerraClass Cerrado (2013), obtidos no portal do Lapig/UFG [p. 4]. Geomorfologia e solos do SIEG [p. 4].
- Amostras: o número de pixels amostrais **não informado**; a Tabela 2 traz apenas máximo, mínimo, média e desvio padrão por banda para as seis classes [p. 6]. Validação de campo com receptor GNSS/GPS portátil e checagem no Google Earth [p. 5].

## 4. Método

- Mosaico de 24 cenas Landsat-8 OLI de 2015, restritas à estação seca (abril a junho) e a cobertura de nuvens de até 10%, com composição falsa-cor RGB 654 (SWIR/NIR/Red) e recorte por mesorregião [p. 4–5].
- Separação em seis classes temáticas: agricultura, água, pastagem, silvicultura, solo exposto e vegetação nativa, com chave de interpretação baseada em cor, textura e forma [p. 5–6].
- Classificação digital supervisionada pelo Maximum Likelihood (Maxver), com amostras coletadas por análise visual da composição colorida e estatísticas descritivas por banda [p. 5].
- Validação por matriz de erro (comissão e omissão) e coeficiente Kappa, complementada por campo com GNSS e Google Earth; comparação das áreas de 2015 com os mapeamentos de 2002 e 2013 [p. 5; p. 7].

## 5. Resultados principais

- Área com floresta plantada em Goiás: 50.425,52 ha em 2002 (0,15% do estado) [p. 7–8]; 153.142,07 ha em 2013 (0,46%) [p. 7–8]; 162.516,69 ha em 2015 (0,48%) [p. 8].
- Por mesorregião em 2015: Sul 95.728,48 ha; Leste 27.404,45 ha; Norte 19.140,11 ha; Centro 19.023,81 ha; Noroeste 1.219,84 ha [p. 8].
- Coeficiente Kappa da classificação de 2015: 0,79, considerado "muito boa" [p. 8; p. 11].
- Série censitária da Ibá: 60.872 ha em 2005 e 135.770 ha em 2015, com queda de 2,15% em 2007 e picos de crescimento de 18,31% em 2006 e 3,68% em 2008 [p. 6–7].
- Crescimento absoluto de 75 mil ha entre 2005 e 2015, a maior parte em eucalipto [p. 11].
- Divergência entre fontes em 2015: 162.516 ha no mapeamento do estudo, 143.070 ha no IBGE e 135.770 ha na Ibá [p. 11].
- Entre 2013 e 2015 houve redução de 0,07% no Centro e 0,06% no Leste, e aumento de 0,04% no Norte e 0,05% no Sul, com cerca de 9 mil ha adicionais no estado [p. 7].
- Municípios sem quantificação de plantios na PEVS: 27 de 246 em 2013 e 9 em 2015 [p. 11].
- Cerca de 3% do território goiano (9 mil km²) é Mata Atlântica, não coberta pelos mapeamentos Probio e TerraClass [p. 7–8].

## 6. Limitações que os próprios autores reconhecem

- Nem o Probio nem o TerraClass Cerrado discriminam espécies dentro da classe silvicultura, e os plantios podem ser confundidos com culturas perenes de porte arbóreo [p. 4].
- As divergências de área entre os três mapeamentos decorrem de metodologias de classificação distintas e de recortes territoriais distintos (bioma Cerrado versus limite estadual) [p. 7].
- Nas imagens, os plantios florestais podem ser confundidos com cafeicultura, canavicultura, citricultura e heveicultura [p. 5].
- A ausência de dados municipais da PEVS é atribuída à falta de informantes locais no momento da visita, o que motivou a validação de campo [p. 11].
- Os autores recomendam novas pesquisas com sensores de maior resolução espacial (orbital e aéreo) para melhorar o detalhamento das áreas plantadas [p. 12].

## 7. O que serve ao projeto e o que não serve

- Serve: dá a linha de base de área plantada por mesorregião (2002, 2013, 2015) para recortar e contextualizar a área de estudo de biomassa e carbono no Cerrado goiano [p. 8].
- Serve: descreve um fluxo reprodutível (OLI 654, Maxver, Kappa) cujo 0,79 é o patamar mínimo de acurácia a ser superado por abordagens multissensoriais [p. 5; p. 8].
- Serve: lista municípios com plantios por mesorregião, útil para estratificar amostragem de campo e inventário florestal [p. 8–9].
- Não serve: não estima biomassa nem estoque de carbono, não usa dados multissensoriais (apenas OLI óptico, uma composição por marco temporal) e não apresenta a matriz de erro completa por classe [p. 4–5].

## 8. Frases citáveis (literais)

- "Verificou-se consideráveis avanços em termos de áreas plantadas em Goiás, constatando-se em 2002 aproximadamente 50.425 ha de floresta plantada, atingindo 162.516 ha em 2015." [p. 1]
- "A distribuição espacial dos plantios de eucalipto se caracteriza por sua atomização e por uma produção não verticalizada dos produtores, refletindo o potencial da atividade florestal na geração de renda em pequenas e médias propriedades." [p. 12]
