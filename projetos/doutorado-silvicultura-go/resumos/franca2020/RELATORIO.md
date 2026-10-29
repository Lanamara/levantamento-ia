# RELATÓRIO — Luciano Cavalcante de Jesus França (2020)

## 1. Referência

FRANÇA, L. C. J.; MUCIDA, D. P.; SANTANA, R. C.; MORAIS, M. S.; GOMIDE, L. R.; BATEIRA, C. V. M. AHP approach applied to multi-criteria decisions in environmental fragility mapping. **FLORESTA**, Curitiba, v. 50, n. 3, p. 1623–1632, jul/set 2020. DOI: 10.5380/rf.v50i3.65146.

O `TEXTO.txt` está íntegro (recebido em 25/02/2019, aceito em 23/04/2020; contém resumo, abstract, métodos, resultados, discussão, conclusões e referências) e corresponde ao DOI indicado. Observação: as marcas `[página N]` do arquivo vão de 1 a 10 e correspondem às páginas 1623–1632 da revista; as citações abaixo usam a numeração das marcas.

## 2. Pergunta do estudo

O método AHP pode apoiar a decisão multicritério no mapeamento de fragilidade ambiental potencial de uma bacia hidrográfica, produzindo uma hierarquia de pesos matematicamente consistente para uso em SIG?

## 3. Área e dados

- Local: Bacia Hidrográfica do rio Jequitinhonha, porção nordeste de Minas Gerais, com trecho na Bahia; 70.315 km² no total (66.319 km² em MG e 3.996 km² na BA), entre os paralelos 15°39' e 18°36'S e os meridianos 39°50' e 43°48'W, orientação SW-NE [p. 6].
- Período: levantamentos bibliográficos e diagnósticos de campo na bacia entre 2016 e 2017 [p. 4].
- Fontes: planos de informação em SIG — classes de solo, declividade do terreno, domínios geológicos, chuva e hierarquia de drenagem; base de referência IBGE (1997) [p. 6]. Não há sensores remotos citados; a fonte específica dos dados de chuva, do MDE/declividade e da geologia não é informada [p. 6].
- Amostras: 5 critérios ambientais avaliados e matriz de comparação par a par de dimensão n = 5 [p. 6–7]; número de pontos amostrais de campo: não informado. Pesos definidos por correlação binária com especialistas de cinco linhas (geomorfologia, geologia, pedologia, engenharia florestal e geoprocessamento) [p. 4].

## 4. Método

- Estruturação hierárquica do problema em objetivo, 5 critérios e alternativas, seguindo Saaty (Figuras 1 e 2) [p. 2–3].
- Matriz de comparação par a par n × n com escala contínua de 1 a 9 e recíprocos, preenchida por julgamento técnico e diagnóstico de campo [p. 4].
- Cálculo em quatro subetapas: normalização da matriz e autovetor (Eqs. 1 e 2), autovalor principal λMax (Eq. 3), Consistency Index (CI, Eq. 4) e Consistency Ratio (CR, Eq. 5, com RI = 1,12 para n = 5); planilhas Excel™ [p. 5–6].
- Integração dos pesos na equação PEF = (FD·X1) + (FS·X2) + (FDG·X3) + (FHF·X4) + (FCP·X5) (Eq. 6), por álgebra de mapas e *weighted overlay* em SIG (ArcGIS/QGIS) [p. 6].

## 5. Resultados principais

- Hierarquia de pesos: declividade (TS) 45,8% > chuva (R) 27,8% > hierarquia de drenagem (DH) 15,8% > classes de solo (CS) 7,7% > domínios geológicos (GD) 2,9% [p. 7].
- Autovetores: TS 0,4581; R 0,2778; DH 0,1580; CS 0,0770; GD 0,0291 [p. 7].
- Autovalor principal λMax = 5,35 (5,350), maior que n = 5, indicando matriz consistente [p. 7].
- CI = 0,0875 e CR = 0,0781, abaixo do limite de 0,1 (10%), com RI = 1,12 [p. 8].
- Justificativa da drenagem: predominância de canais de 1ª ordem em 11.058,10 km² e de 2ª ordem em 5.491,64 km² [p. 7].
- Comparação externa: outros estudos (Paraná e Alto Paranaíba/MG) também atribuíram à declividade ~40% do peso [p. 8].
- O artigo entrega a hierarquia de pesos e a validação da matriz; não apresenta o mapa final de fragilidade nem validação dos resultados do PEF contra dados de campo [p. 6–8].

## 6. Limitações que os próprios autores reconhecem

- As escalas de mapeamento de solos no Brasil são regionais, o que implica afirmações imprecisas sobre as fragilidades envolvidas [p. 8].
- O limite de tolerância de CR < 0,1 (10%) é uma restrição questionável pela margem de erro envolvida, com pouca discussão na literatura e sem consenso; citam a crítica de Bana e Costa et al. (2001) ao coeficiente de inconsistência de Saaty [p. 9].
- A entrada de dados é simples, mas a estruturação da matriz e a atribuição de pesos exigem atenção para evitar tendência ou viés dos especialistas [p. 9].
- Sugerem complementar o AHP com pesquisa operacional e programação computacional para reduzir incertezas na decisão [p. 9].

## 7. O que serve ao projeto e o que não serve

- Serve: o protocolo completo de AHP (matriz par a par, autovetor, λMax, CI e CR) é diretamente reaproveitável como camada de ponderação multicritério em modelos de biomassa/estoque de carbono, inclusive o critério de aceitação CR < 0,1 [p. 5–6, p. 8].
- Serve: a lógica de combinar pesos de especialistas com álgebra de mapas/weighted overlay em SIG (Eq. 6) é o mesmo arranjo operacional usado para integrar produtos de sensoriamento remoto multissensorial [p. 6].
- Não serve: não há biomassa, estoque de carbono, silvicultura, inventário florestal nem sensores remotos; os cinco critérios são atributos físicos da paisagem (declividade, solo, geologia, chuva, drenagem), sem variáveis espectrais ou estruturais da vegetação [p. 4, p. 6].
- Não serve: os pesos (declividade 45,8%) são específicos da bacia do Jequitinhonha (MG/BA) e não transferíveis para Goiás nem para plantios florestais; o artigo também não valida o mapa de fragilidade resultante [p. 7–8].

## 8. Frases citáveis (literais)

- "The terrain slope was a factor of greater relevance in the evaluation of potential environmental fragility in the Jequitinhonha river basin (45.8% value of importance)." [p. 7]
- "The CR found was 0.0781 within acceptable limits (0.1 or 10%) (SAATY, 1980)." [p. 8]
