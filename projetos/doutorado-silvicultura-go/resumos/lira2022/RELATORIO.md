# RELATÓRIO — Karen Carrilho da Silva Lira (2022)

## 1. Referência

LIRA, Karen Carrilho da Silva; FRANCISCO, Humberto Rodrigues; FEIDEN, Aldi. Classificação de fragilidade ambiental em bacia hidrográfica usando lógica Fuzzy e método AHP. *Sociedade & Natureza* (Soc. Nat.), Uberlândia, v. 34, e62872, 2022. ISSN 1982-4513. DOI: 10.14393/SN-v34-2022-62872.

O `TEXTO.txt` corresponde ao artigo do DOI informado e está integral (páginas 1 a 17, incluindo referências e contribuição dos autores).

## 2. Pergunta do estudo

Classificar a fragilidade ambiental da bacia hidrográfica do Arroio Marreco combinando lógica Fuzzy e AHP em SIG, e verificar se a forma de ponderação do mapa de declividade altera o mapa final de fragilidade [p. 2].

## 3. Área e dados

- **Local:** bacia hidrográfica do Arroio Marreco, entre os municípios de Toledo, Quatro Pontes, Marechal Cândido Rondon e Pato Bragado, oeste do Paraná, com 338,8 km² [p. 2–3]. Clima Cfa [p. 3].
- **Período:** não informado (o artigo não define recorte temporal de análise; as fontes são citadas com anos de acesso de 2019 e 2020) [p. 4].
- **Relevo:** MDE SRTM, resolução de 1 Arc-Second (30 m), duas cenas (SRTM1S25W054V3 e SRTM1S25W055V3) obtidas na USGS; delimitação da bacia pelo TauDEM [p. 4].
- **Solos:** vetor da EMBRAPA, escala 1:250.000, classes de segundo nível categórico [p. 4].
- **Uso/ocupação:** Projeto MapBiomas, coleção 5, formato matricial, escala 1:100.000 e resolução média de 30 m [p. 4].
- **Amostras:** rasters padronizados em 30 m, 16 bit, 464 linhas por 1564 colunas [p. 4]; grade regular de pontos espaçados em 30 m gerou 845.209 pontos por mapa, totalizando 2.535.627 [p. 12].
- **Software:** QGIS Las Palmas 2.18.28; R para estatística [p. 4; p. 9].

## 4. Método

- **Critérios e escala:** quatro planos de informação (declividade, tipo de solo, uso/ocupação do solo e altitude), reclassificados em 5 graus de fragilidade (muito fraca a muito forte) em intervalo [0,10], adaptados de Crepani et al. (2001) e Ross (1994) [p. 3; p. 5].
- **Fuzzy:** solo e uso/ocupação receberam pesos discretos (2, 4, 6, 8, 10); declividade e altitude receberam funções de pertinência contínuas — f(x) linear por trechos para declividade (0 a 51,46%) e g(x) = −0,025x + 15,4 para altitude (596 m → 216 m), aplicadas na calculadora raster [p. 5–7].
- **AHP:** comparação pareada com escala de Saaty (1 a 9 e recíprocos), julgamento baseado em literatura e opinião dos autores, com checagem de consistência (RC < 0,1); sobreposição linear ponderada no complemento Easy AHP [p. 7–8; p. 11].
- **Comparação de métodos:** três formas de ponderar a declividade — Fuzzy (FZ), Fuzzy modificada (FZmodificada) e Ross modificada (Rmodificada) —, com extração de valores por *point sampling* e 999 análises de variância de efeitos principais (999 pontos por planilha, α = 5%) no R [p. 8–9; p. 12].

## 5. Resultados principais

- Área total da bacia: 338,8 km² [p. 3]. Declividade máxima: 51,46% [p. 6]. Altitudes entre 216 m e 596 m [p. 7].
- Solos: Nitossolo Vermelho 184,6 km² (54,5%), Latossolo Vermelho 93,5 km² (27,6%), Neossolo 60,7 km² (17,9%) [p. 10].
- Uso/ocupação: agricultura 193,3 km² (57,1%), formação florestal 63,9 km² (18,9%), mosaico agricultura-pasto 59,2 km² (17,5%), área urbana 14,3 km² (4,2%), pasto 8,1 km² (2,4%) [p. 10].
- Fragilidade por declividade (f(x)): fraca 50,4%, muito fraca 20,7%, média 19,4%, forte 7,3%, muito forte 2,3% [p. 11]. Por altitude (g(x)): fraca 25,7%, média 25,2%, forte 24,7%, muito forte 21,6%, muito fraca 2,8% [p. 11].
- Pesos AHP: declividade 51,42%, uso/ocupação 29,55%, solo 12,14%, altitude 6,89%; λmax = 4,02285, IC = 0,0076, IR = 0,90 e RC = 0,0085 [p. 11].
- Fragilidade final: média 241,6 km² (71,3%), fraca 51,2 km² (15,1%), forte 44,7 km² (13,2%), muito fraca 0,5 km² (0,2%) e muito forte 0,8 km² (0,2%) [p. 11–12].
- Comparação das ponderações: FZ manteve 71,3% na classe média e 15,1% na fraca; FZmodificada ficou com 57,2% média e 37,7% forte; Rmodificada com 63,1% média e 31,1% forte [p. 13].
- Médias do grau de fragilidade: FZ 5,94 (c), FZmodificada 6,80 (a) e Rmodificada 6,60 (b), com diferença significativa pelo teste de Tukey a 5% [p. 13].
- Estatística: F_posição = 8,807 (p = 1,383·10^-310) e F_método = 484,015 (p = 1,391·10^-146) [p. 12].

## 6. Limitações que os próprios autores reconhecem

- A subjetividade dos julgamentos baseados na experiência dos pesquisadores "pode resultar em inconsistências na matriz final", o que motivou o controle pela razão de consistência [p. 8].
- A escolha da função de pertinência "não é arbitrária, mas é subjetiva" e depende do contexto do problema; as funções escolhidas "dependem do conjunto de dados e em qual contexto são tratados" [p. 5; p. 13].
- A ponderação dos elementos foi feita "de forma empírica", com base em Crepani et al. (2001), Ross (1994) e Spörl (2001) [p. 5]; a importância dos critérios no AHP foi atribuída com base na "opinião profissional dos autores" e na literatura [p. 7].
- Não há menção a validação em campo nem a dados de biomassa, carbono ou inventário florestal — tal ausência não é discutida como limitação pelos autores [p. 13–14]. Os autores apenas sugerem "o aprofundamento e exploração da lógica fuzzy em análises a nível de planejamento ambiental" [p. 14].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o arranjo metodológico Fuzzy + AHP + SIG para variáveis contínuas (funções de pertinência para declividade e altitude) é diretamente reutilizável como camada de ponderação de preditores ambientais em modelos de biomassa, com pesos derivados de especialistas e checagem por RC [p. 7–8; p. 11].
- **Serve:** o protocolo de comparação entre esquemas de ponderação (três variantes, 999 reamostragens, ANOVA de efeitos principais e Tukey) é um modelo útil para testar a sensibilidade de índices e estimativas a escolhas de discretização [p. 12–13].
- **Serve parcialmente:** o uso exclusivo de dados públicos gratuitos (SRTM 30 m, MapBiomas, EMBRAPA) em QGIS mostra um caminho de baixo custo, mas com generalização compatível apenas com escalas regionais [p. 4].
- **Não serve:** o artigo não trata de silvicultura, biomassa, estoque de carbono, sensores multissensoriais (óptico/radar/LiDAR) nem de Goiás; o produto é um índice qualitativo-ordinal de fragilidade (0–10) em bacia do oeste do Paraná, sem calibração com dados de campo, e não pode ser transferido como estimador de carbono [p. 1; p. 3; p. 12].

## 8. Frases citáveis (literais)

- "O resultado desse cálculo indica que 71,3% da área da bacia tem fragilidade média, 15,1% tem fragilidade fraca e 13,2% tem fragilidade forte (Figura 7 e Tabela 8)." [p. 11]
- "Isso pode ser explicado pelo método FZ permitir representar a variação dos elementos do mapa enquanto FZmodificada e Rmodificada atribuem valores fixos a regiões com características diferentes." [p. 14]
