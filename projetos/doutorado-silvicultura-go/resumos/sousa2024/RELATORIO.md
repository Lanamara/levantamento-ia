# RELATÓRIO — Roneide dos Santos Sousa (2024)

## 1. Referência

Sousa, Roneide dos Santos; Rocha, Glairton Cardoso. **Fragilidade ambiental da paisagem da bacia hidrográfica do Rio Camurupim, Piauí, Brasil.** *Caderno de Geografia*, v. 34, n. 77, p. 396–425, 2024. DOI 10.5752/p.2318-2962.2024v34n77p396. Artigo original recebido em 22.03.2023 e aceito em 23.02.2024; o `TEXTO.txt` está completo (30 páginas, incluindo referências) e corresponde ao DOI informado.

## 2. Pergunta do estudo

Quais os níveis de fragilidade ambiental potencial (FAP) e emergente (FAE) da paisagem da Bacia Hidrográfica do Rio Camurupim (BHRC), no norte do Piauí, frente a processos de degradação? [p. 398]

## 3. Área e dados

- Local: BHRC, litoral do baixo curso do rio Parnaíba, entre 2º54'49"S e 41º30'26"W; abrange parte de Luís Correia, Cajueiro da Praia, Bom Princípio do Piauí e Cocal; cerca de 820 km², altitude de 0 m a mais de 300 m [p. 401].
- Período: uso e cobertura da terra em 1985 e 2021 [p. 410–411]; precipitação média de 1981–2020 [p. 402]; trabalho de campo com fotos de outubro de 2022 [p. 412–413].
- Fontes: MDE TOPODATA (30 m, INPE) [p. 407]; MapBiomas coleção 7 [p. 408]; geologia e solos do BDiA/IBGE (base RADAMBRASIL) [p. 405]; clima Köppen de Alvares et al. (2014) do IPEF [p. 407]; precipitação CHIRPS [p. 402]; dados de ANA, CPRM, EMBRAPA, IPEF [p. 405].
- Amostras: campo com câmera fotográfica e GPS Garmin para pontos de coordenadas, mas **número de amostras/pontos não informado** [p. 405].

## 4. Método

- Método empírico de Ross (1994; 2012): pesos de 1 (muito baixa) a 5 (muito alta) por classe de geologia, solos, clima, relevo e uso e cobertura da terra, com base em literatura e avaliação técnica [p. 405].
- Estruturação de banco de dados geográficos em QGIS 3.22.9 e ArcGIS Pro, SIRGAS 2000 e UTM zona 24S, escala 1:200.000 e célula de 30 m [p. 405, 409].
- Relevo por Geomorphons (10 unidades, classificadas no SAGA GIS a partir do MDE TOPODATA de 30 m) e por Índice de Dissecação do Relevo (IDR) [p. 407–408].
- Álgebra de mapas (raster calculator): FAP = ([G]+[S]+[C]+[R]+[IDR])/5 e FAE = ([FAP]+[UT])/2 [p. 409].

## 5. Resultados principais

- FAP: muito baixa 2,07%, baixa 6,62%, média 15,32%, alta 28,41% e muito alta 47,58% [p. 414]. Alta + muito alta somam 75,99% da bacia [p. 416].
- FAE: muito baixa 6,05%, baixa 74,36%, média 15,22%, alta 4,34% e muito alta 0,03% [p. 414]. Apenas 19,59% da área tem FAE de média a alta, sobretudo planícies fluviais e fluviomarinhas [p. 415].
- Uso e cobertura em 2021: formação florestal 61,23%, formação savânica 29,56%, mangue 1,73%, apicum 1,42%, agropecuária 1,65%, rio 1,44%, duna 0,91%, aquicultura 0,82%, áreas não vegetadas 0,81%, formação natural não florestal 0,28%, área urbanizada 0,15% [p. 410].
- Mudanças 1985–2021: formação florestal +7,89% e formação savânica −9,32% de área; agropecuária +1,13%; aquicultura +4,82% (texto) e +0,58 ponto percentual (Tabela 2); apicum −0,29%; área urbanizada +0,10% [p. 410–411].
- IDR na bacia restrito a duas classes, forte e muito forte [p. 408]; solos hierarquizados apenas em Alta e Muito Alta [p. 406].
- População da sede de Bom Princípio do Piauí: 5.670 habitantes, 68,82% rural [p. 404, 410].
- Clima As (tropical quente e úmido), peso 4 (alta) [p. 407]; precipitação de 1.200 a 1.400 mm e temperatura de 28 °C a 30 °C [p. 401–402].
- Conclusão dos autores: a cobertura vegetal conservada atenua os processos erosivos e rebaixa a FAE, apesar da fragilidade natural alta [p. 419–420].

## 6. Limitações que os próprios autores reconhecem

- O artigo não tem seção de limitações; as ressalvas aparecem no texto. A principal é metodológica: modelos distintos de fragilidade geram impactos distintos e "a escolha de um fator de ponderação em detrimento de outro também pode influenciar nos resultados", exigindo adaptação das variáveis à área [p. 399].
- A FAE é uma fotografia do uso da terra de 2021: "as futuras alterações do uso da terra podem dinamizar essas mudanças", gerando nova FAE [p. 419].
- O mapeamento é estático e Indicado para monitoramento futuro, sem projeção de cenários [p. 420].
- Inconsistências internas não comentadas pelos autores: as considerações finais trocam as classes da FAE ("baixa (6,62%) e muito baixa (74,36%)") em relação ao resultado apresentado [p. 419 vs p. 414]; o texto atribui +4,82% à aquicultura, mas a Tabela 2 registra +0,58 [p. 410–411]; não há validação estatística nem teste de acurácia dos mapas, apenas conferência em campo [p. 405, 420].

## 7. O que serve ao projeto e o que não serve

- Serve: o encadeamento operacional (banco de dados em SIG, reclassificação por pesos, álgebra de mapas em raster de 30 m) é replicável para integrar camadas multissensor de biomassa e carbono em escala de bacia [p. 409].
- Serve: o uso de atributos derivados de MDE (Geomorphons e IDR) como covariáveis de terreno, e a série MapBiomas 1985–2021 como camada de uso/cobertura para estratificar a silvicultura [p. 407–408, 410].
- Serve parcialmente: a lógica de FAP/FAE é útil como camada de contexto ambiental, mas mede suscetibilidade à degradação, não biomassa ou estoque de carbono — que o artigo não quantifica.
- Não serve: não há sensoriamento remoto multissensorial (nenhum radar, LiDAR ou série multiespectral própria), nenhum dado de biomassa, carbono ou equação alométrica; a área é Caatinga/costeira do Piauí, não silvicultura em Goiás, e a escala 1:200.000 é grossa para talhões [p. 401, 405].

## 8. Frases citáveis (literais)

- "Para o mapa da FAP, que analisou a integração dos condicionantes da paisagem, obtiveram-se as seguintes classes: muito baixa (2,07%), baixa (6,62%), média (15,32%), alta (28,41%) e muito alta (47,58%)." [p. 414]
- "As geotecnologias foram fundamentais para a realização da modelagem dos atributos físico-naturais e determinação das classes de fragilidade ambiental potencial e emergente, bem como as inspeções de campo para a conferência das classes de fragilidade e validação dos mapeamentos." [p. 420]
