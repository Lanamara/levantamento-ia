# RELATÓRIO — Rosana Márcia da Costa Silva Herculano (2023)

## 1. Referência

- Autores: Rosana Márcia da Costa Silva Herculano; José Carlos de Souza [p. 1].
- Ano: 2023 (conforme DOI informado no pedido; o ano não aparece no corpo do texto).
- Título: "Fragilidade ambiental da bacia hidrográfica do rio Uru (Goiás): comparação entre modelos" [p. 1].
- Revista: não nomeada no `TEXTO.txt`; o DOI 10.5016/estgeo.v20i3.16799 indica *Estudos Geográficos*, v. 20, n. 3. O texto ocupa as páginas 305–323 [p. 1–19].
- DOI: 10.5016/estgeo.v20i3.16799.
- O arquivo está completo (vai do resumo às referências, terminando em VALLE et al.) e corresponde ao artigo do DOI; não há truncamento.

## 2. Pergunta do estudo

Comparar a fragilidade ambiental da bacia hidrográfica do rio Uru (GO) obtida pelo modelo tradicional de álgebra de mapas (média dos atributos) e pelo método multicritério AHP, avaliando se a ponderação distinta das variáveis altera a distribuição das classes de fragilidade [p. 3].

## 3. Área e dados

- Local: bacia hidrográfica do rio Uru (BHRU), Goiás, entre 16°16'00" e 15°20'00" de latitude Sul e 49°36'00" e 50°08'00" de longitude Oeste; 3.868,91 km² [p. 3]; território de 13 municípios [p. 3]; elevações de 500 m a 1.104 m, média de 724 m [p. 4].
- Clima: tropical úmido (Aw de Köppen), série do INMET para Itaberaí de 1981 a 2010, chuvas anuais médias entre 1.535 mm e 1.425 mm; máximas de 30 °C a 33 °C e mínimas de 15 °C a 20 °C [p. 4].
- Sensores e fontes: base vetorial de solos da EMATER (2017) [p. 4]; imagem OLI/Landsat 8 de 07/05/2021, resolução de 30 m, composição R2 G5 B6 [p. 4]; MDE SRTM de 30 m [p. 4]; processamento em QGIS 3.16 com o plugin SCP [p. 4].
- Período: dados de campo ou campanha de validação: não informado. A análise usa uma única data de imagem (07/05/2021) [p. 4].
- Número de amostras: não informado. Há validação da classificação por coeficiente kappa e exatidão global (0,81 e 85,43%), mas o texto não informa quantas amostras foram usadas [p. 8].

## 4. Método

- Reclassificação das três variáveis em cinco níveis de fragilidade (1 a 5) segundo Ross (1994), Spörl e Ross (2004) e Amaral e Ross (2009): solos, declividades (0–6% a > 30%) e grau de proteção do uso e cobertura [p. 4–5].
- Modelo 1 (tradicional): álgebra de mapas na calculadora raster, valores normalizados de 0 a 1 e soma dos pixels, com classes a cada 0,2 (0,0–0,2 muito baixa até 0,8–1 muito alta), ou seja, pesos iguais [p. 5].
- Modelo 2 (AHP): hierarquia das variáveis, pesos definidos por revisão de literatura e agregação por Combinação Linear Ponderada (WLC), FA = (Us × Pw1) + (De × Pw2) + (Pe × Pw3) [p. 5].
- Pesos adotados no AHP: uso do solo 0,45; declividade 0,35; solo 0,20 (soma 1,00) [p. 5].

## 5. Resultados principais

- Solos: Latossolo Vermelho em 2.222,91 km² (57,45%), fragilidade muito baixa; Argissolos em 1.247,0 km² (5,63% + 26,59%), fragilidade média; Cambissolo Háplico em 296,0 km² (7,65%), alta; Neossolo Litólico em 103,0 km² (2,68%), muito alta [p. 6]. Alta e muito alta somam cerca de 10,3% [p. 7].
- Declividades: 1.686,06 km² (43,6%) de 0–6%; 1.252,58 km² (32,4%) de 6–12%; 569,35 km² (14,7%) de 12–20%; 220,12 km² (5,7%) de 20–30%; 140,80 km² (3,6%) acima de 30%. Muito baixa e baixa juntas ocupam 76% e as demais 24% [p. 8].
- Uso e cobertura: pastagem 1.471,10 km² (38,0%) e agricultura 1.048,38 km² (27,1%), somando 65,10% [p. 8–9]; Cerrado florestal e hidrografia 482,97 km² (12,5%); savânica 575,83 km² (14,9%), 27,40% juntas [p. 9]; solo exposto e área urbana 290,63 km² (7,5%) [p. 9]. Kappa 0,81 e exatidão global de 85,43% [p. 8].
- Modelo tradicional: muito baixa 474,19 km² (12,3%); baixa 1.606,68 km² (41,5%); média 1.403,80 km² (36,3%); alta 363,01 km² (9,4%); muito alta 21,23 km² (0,5%); baixa e média somam 77,8% e alta e muito alta 9,9% [p. 11].
- Modelo AHP: muito baixa 265,12 km² (6,85%); baixa 1.645,13 km² (42,52%); média 1.850,71 km² (47,84%); alta 107,63 km² (2,78%); muito alta 0,318 km² (0,01%); baixa e média somam 90,36% [p. 12–13].
- Comparação: muito baixa cai de 12,3% para 6,85%; muito alta de 0,5% para 0,01%; alta de 9,4% para 2,78%; baixa praticamente estável (41,50% e 42,52%); média sobe de 36,3% para 47,84% [p. 14]. A redução das classes alta e muito alta é atribuída ao maior peso da variável uso e cobertura [p. 14].
- Inconsistência interna: o texto afirma que alta e muito alta "juntas ocupam 2,78%" no AHP [p. 13], valor que na Tabela 5 corresponde apenas à classe alta (2,78% + 0,01% = 2,79%) [p. 13].

## 6. Limitações que os próprios autores reconhecem

- Os modelos usam apenas três variáveis; os autores recomendam incluir geologia, chuvas, comprimento da encosta e proximidade de estradas e rodovias, com aplicação do AHP [p. 17].
- Os resultados são sensíveis à ponderação: só a classe baixa teve valores próximos entre modelos, e as demais "registraram resultados bem distintos", evidenciando "a importância da determinação de pesos distintos para as variáveis" [p. 17]; a divergência é explicada pelo peso dado ao uso e cobertura [p. 14].
- Os pesos do AHP foram obtidos "por revisão de literatura" [p. 5]; não há no texto matriz de comparação par a par nem razão de consistência (não informado).
- Não declarado pelos autores, mas verificável no texto: não há validação de campo dos mapas de fragilidade, apenas a acurácia da classificação de uso (Kappa 0,81) [p. 8].

## 7. O que serve ao projeto e o que não serve

- Serve: fluxo reprodutível de mapeamento de uso e cobertura no Cerrado goiano com OLI/Landsat 8 (30 m, composição R2 G5 B6, SCP no QGIS) e controle de qualidade por Kappa de 0,81 e exatidão de 85,43% [p. 4, p. 8].
- Serve: estrutura de ponderação por AHP e WLC (uso 0,45; declividade 0,35; solo 0,20) como referência metodológica para combinar variáveis derivadas de sensores distintos, e a constatação de que a escolha de pesos muda a área das classes [p. 5, p. 14, p. 17].
- Serve: contexto de uso do solo na região (65,10% de pastagem e agricultura; 7,5% de solo exposto e área urbana) para interpretar onde a silvicultura se insere e qual o baseline de fragilidade [p. 8–9].
- Não serve: o artigo não estima biomassa nem estoque de carbono, não usa dados de campo, não integra múltiplos sensores (apenas um imageamento óptico e o SRTM) e trabalha com uma só data; as classes de fragilidade são ordinais, não grandezas físicas mensuráveis [p. 4–5].

## 8. Frases citáveis (literais)

- "A fragilidade muito baixa ocupa uma área de 12,3% da BHRU, segundo o método tradicional, enquanto que pelo método AHP esse percentual é de 6,85%." [p. 14]
- "Sugerimos, para tornar o produto final mais robusto, o incremento de outras variáveis ambientais, que interferem diretamente nos níveis de fragilidade, como por exemplo: a geologia, os de chuva, o comprimento da encosta, a proximidade com as estradas e rodovias, dentre outras, sendo que nestes casos orienta-se a aplicação do método AHP." [p. 17]

(As duas citações preservam o texto; apenas os espaços quebrados pelo OCR foram reunidos.)
