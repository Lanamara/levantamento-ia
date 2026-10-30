# RELATÓRIO — Thiara Messias de Almeida Teixeira (2024)

## 1. Referência

Thiara Messias de Almeida Teixeira; Amom Chrystian de Oliveira Teixeira; Elton Souza Oliveira (2024). *Avaliação da vulnerabilidade natural à perda de solo e fragilidade ambiental da Bacia Hidrográfica do Ribeirão Santa Rita (DF-GO)*. Revista Cerrados (Montes Claros – MG), v. 22, n. 01, p. 217-236, jan./jul. 2024. DOI: 10.46551/rc24482692202409.

O `TEXTO.txt` está íntegro (artigo completo, das referências aos dados de submissão) e corresponde ao DOI acima. Observação de leitura: a numeração abaixo usa as marcas `[página N]` do próprio arquivo, que estão deslocadas em relação à paginação impressa da revista (a marca `[página 7]` traz o número impresso 218).

## 2. Pergunta do estudo

Qual é a distribuição espacial da vulnerabilidade natural à perda de solo e da fragilidade ambiental da Bacia Hidrográfica do Ribeirão Santa Rita, e como os métodos de Crepani et al. (2001) e Ross (1994) se comparam ao aplicá-los à mesma bacia?

## 3. Área e dados

- Local: Bacia Hidrográfica do Ribeirão Santa Rita (BHRSR), ~10.000 ha [p. 4], na Alta Bacia do Rio Preto, entre a Região Administrativa de Planaltina (DF) e o município de Formosa (GO), em área de Cerrado [p. 4]; clima Aw de Köppen-Geiger [p. 12]; altitudes médias de 900 a 1.200 m na Superfície Regional de Aplainamento II A [p. 11] e desnível de ~318 m [p. 12].
- Período: uso e cobertura da terra em 1985 e 2018 [p. 5]; trabalho de campo em janeiro, abril, julho e outubro de 2019 [p. 5].
- Fontes: bases vetoriais do SIEG (geologia, geomorfologia, clima, classes de solos) [p. 5]; Projeto MapBiomas, Coleção 5, anos de 1985 e 2018 [p. 5]; MDE do projeto TOPODATA (folha 15S_48) derivado de SRTM, resolução espacial de 30 m [p. 5]. Sensor específico das imagens usadas pelo MapBiomas: não informado.
- Amostras: não informado — o estudo é de mapeamento por unidades territoriais básicas/classes, não por amostragem de campo. Área total mapeada: 10.178,51 ha [p. 19]; 8 classes de uso pontuadas no Quadro 4 (formação florestal, formação savânica, formação campestre, floresta plantada, pastagem, área urbana, cultura anual, área não vegetada) [p. 18].
- Processamento em ArcGIS 10.3 e QGIS 3.16, datum SIRGAS 2000 zona 23S [p. 5].

## 4. Método

- **Vulnerabilidade (Crepani et al., 2001)**: cada Unidade Territorial Básica recebe nota de 1,0 a 3,0 para geologia, geomorfologia, solos, vegetação e clima, e a vulnerabilidade final é a média aritmética simples dessas notas (Equação 1) [p. 6]; a componente geomorfológica é obtida por álgebra de mapas de dissecação do relevo, amplitude altimétrica e declividade (Equação 2) [p. 6–7].
- **Fragilidade (Ross, 1994)**: fragilidade natural pelo cruzamento de geomorfologia (Índice de Dissecação do Relevo), clima e solos (Equação 3) e fragilidade ambiental pela combinação da fragilidade natural com o uso e ocupação da terra (Equação 4) [p. 8], com pesos de 1 (muito baixa) a 5 (muito forte) [p. 9].
- **Automação**: obtenção automática em SIG dos mapas de vulnerabilidade geomorfológica e do Índice de Dissecação do Relevo conforme Guimarães et al. (2017) [p. 6, 8].
- **Checagem**: conferência topológica dos vetores e reconhecimento de campo com registro fotográfico e checagem de dados em 2019 [p. 5].

## 5. Resultados principais

- Desde a década de 1980 a bacia já havia perdido aproximadamente 60% da cobertura original de Cerrado [p. 1; p. 15].
- Em 2018 a pastagem era o uso predominante: mais de 4.155 ha, 41,23% do total [p. 15].
- Entre 1985 e 2018 as áreas de pastagem caíram ~30% e as de cultura anual cresceram 36,59%; floresta plantada não aparecia em 1985 e chegou a 3,76% da bacia em 2018; a área urbana de Formosa expandiu 120 ha [p. 16].
- Vulnerabilidade natural: 82,42% da bacia (8.307,10 ha) em "moderadamente estável/vulnerável", 8,03% (909,80 ha) "moderadamente vulnerável", 9,29% (936,41 ha) "moderadamente estável" e 0,25% (25,20 ha) "estável"; nenhuma área na classe "vulnerável"; total 10.178,51 ha [p. 19]. O texto arredonda: ~80% moderadamente estável/vulnerável e 8% moderadamente vulnerável [p. 19].
- Notas atribuídas: Paraopeba 2,8; Coberturas Detrito-Lateríticas 3,0; Depósitos aluvionares 3,0; Paranoá 1,0; intensidade pluviométrica 1,9; Latossolo 1,0; Cambissolo 2,5; Plintossolo 3,0; formação florestal 1,0; pastagem 2,0; cultura anual 3,0 [p. 18].
- Fragilidade ambiental: média (3) em 4.841,00 ha (48,03%), forte (4) em 2.485,70 ha (24,66%), baixa (2) em 2.750,04 ha (27,29%), muito baixa (1) em 1,78 ha (0,02%) e nenhuma área em muito forte (5); total 10.078,51 ha [p. 20].
- A fragilidade natural da bacia é de média a alta, agravada pela ação antrópica [p. 19]; a classe forte está associada sobretudo a cultura anual de grãos, quase 25% da bacia [p. 19].
- Comparação dos modelos: ambos convergem para predomínio do grau médio, mas divergem nas classes, porque Crepani et al. (2001) incorpora o substrato rochoso e Ross (1994) não, e porque o tratamento do relevo difere [p. 20–21]. As classes extremas (muito baixa e muito alta) foram suavizadas pela média aritmética, restando três classes: baixa, média e alta [p. 21].
- Inconsistência interna: a área total é 10.178,51 ha na Tabela 2 [p. 19] e 10.078,51 ha na Tabela 3 [p. 20].

## 6. Limitações que os próprios autores reconhecem

- Modelos podem mascarar a realidade, o que revela a complexidade da modelagem de sistemas ambientais [p. 21].
- As classes de vulnerabilidade/fragilidade muito baixa e muito alta foram suavizadas pela média aritmética dos temas, restando apenas três classes [p. 21].
- Os dois modelos deram resultados distintos para as classes em razão de diferenças nos procedimentos técnico-operacionais, nas variáveis ambientais e nos valores empíricos adotados [p. 22].
- A modelagem reflete diretamente as informações utilizadas e sofre forte influência da escala dos dados [p. 22].
- Os autores afirmam que a questão não é determinar qual modelo é melhor, mas considerar as especificidades de cada bacia e o conjunto de dados disponível [p. 22].

## 7. O que serve ao projeto e o que não serve

- **Serve**: a classe "floresta plantada", que passa de ausente em 1985 a 3,76% da bacia em 2018 [p. 16], é o único indício de silvicultura no texto e um possível ponto de partida para localizar talhões no DF-GO.
- **Serve**: o recorte territorial (bacia no DF-GO, Cerrado, forte pressão agropecuária) e a série temporal 1985–2018 via MapBiomas [p. 5] são diretamente reutilizáveis como máscara de área e linha de base de uso da terra.
- **Serve parcialmente**: o arcabouço de álgebra de mapas e de pesos por classe (Quadro 4) [p. 18] pode ser adaptado como etapa de estratificação ambiental, mas não foi concebido para estimar biomassa ou carbono.
- **Não serve**: não há estimativa de biomassa, estoque de carbono, dados de campo dendrométricos, inventário florestal nem uso combinado de sensores (óptico, SAR, LiDAR); o sensoriamento remoto aparece apenas como base cartográfica (SRTM/Topodata 30 m e MapBiomas) [p. 5].

## 8. Frases citáveis (literais)

- "Desde a década de 1980, a Bacia já perdeu aproximadamente 60% da sua cobertura original de Cerrado." [p. 1]
- "A modelagem reflete diretamente as informações utilizadas, sofrendo forte influência da escala dos dados." [p. 22]
