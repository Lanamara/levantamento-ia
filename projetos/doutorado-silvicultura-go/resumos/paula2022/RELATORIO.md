# RELATÓRIO — Luiz Gustavo de Souza Paula (2022)

## 1. Referência

Paula, Luiz Gustavo de Souza; Ribeiro, Sônia Maria Carvalho. **Aptidão das áreas no entorno do Parque Estadual do Rio Doce para implementação de sistemas agroflorestais com base em análise multicritério**. *Ciência Florestal*, Santa Maria, v. 32, n. 1, p. 474-492, jan./mar. 2022. DOI: 10.5902/1980509839173. Nota Técnica. Submissão em 22/07/2019, aprovação em 02/03/2021, publicação em 25/03/2022 [p. 1]. O `TEXTO.txt` contém o artigo integral (páginas 1–19) e corresponde ao DOI informado.

## 2. Pergunta do estudo

Quais áreas no entorno do Parque Estadual do Rio Doce (PERD) apresentam maior aptidão para implementação de sistemas agroflorestais (SAF) voltados prioritariamente à preservação ambiental e, secundariamente, à geração de renda [p. 5]?

## 3. Área e dados

- **Local:** entorno do PERD, Vale do Aço, Minas Gerais, incluindo áreas dos municípios de Coronel Fabriciano, Timóteo, Ipatinga e Caratinga [p. 1; p. 15].
- **Período:** primeiro ciclo do projeto PELD entre junho de 2017 e novembro de 2018 (entrevistas e workshops); imagens de satélite de 14 a 22 de fevereiro de 2018 [p. 4; p. 9].
- **Sensores e fontes:** Landsat 8 para uso e cobertura da terra e NDVI; Base Hidrográfica Ottocodificada da Bacia do Rio Doce (ANA) para APPs ripárias; OpenStreetMap (OSM) para vias de acesso; processamento em QGIS 2.18 com o complemento EasyAHP [p. 9; p. 6].
- **Amostras:** não informado (não há amostragem de campo; a unidade de análise é o pixel de 30 m, com 900 m² por pixel) [p. 14]. Área total modelada: 1.677.033 ha [p. 15].

## 4. Método

- **Análise multicritério AHP** (*Analytic Hierarchy Process*, Saaty 1987): comparação par a par das variáveis em matriz, com escala de 1 a 9, gerando pesos, autovalor, índice de consistência (CI) e razão de consistência (CR) [p. 6; p. 9–10].
- **Quatro variáveis em camadas georreferenciadas:** uso e cobertura da terra (cinco classes: meio urbano, matas e florestas, silvicultura, água e meio rural antropizado); APPs de lagoas e cursos d'água; NDVI; proximidade de vias de acesso [p. 6–8].
- **Normalização e álgebra de mapas:** atributos receberam notas de 1 a 3 (muito baixo, moderado, muito elevado), combinadas pelos pesos AHP em cinco classes finais de aptidão [p. 12–13].
- **Análise complementar:** repetição da leitura do modelo excluindo as APPs, para identificar áreas aptas fora delas [p. 15–16].

## 5. Resultados principais

- Validação do AHP: autovalor λ = 4,08; índice de consistência CI = 0,027; razão de consistência CR = 0,03, abaixo do limite de 0,1 exigido pelo método [p. 13].
- Pesos atribuídos: uso e cobertura da terra 0,605; APPs de corpos d'água 0,185; proximidade de vias 0,132; NDVI 0,079 [p. 13].
- Área com aptidão "muito elevada": 5.580 ha, o que corresponde a 0,33% da área modelada de 1.677.033 ha [p. 15–16]. Essas áreas são rurais antropizadas, com baixo NDVI, dentro de APPs ripárias e próximas a rodovias [p. 15].
- As maiores manchas contínuas têm mais de 30 ha e situam-se às margens do rio Piracicaba, incluindo trechos próximos à foz no rio Doce; a imagem ampliada B destaca áreas às margens do rio Doce vizinhas ao PERD [p. 15].
- Fora das APPs, as concentrações de maior aptidão estão em áreas rurais de Coronel Fabriciano-MG, Ipatinga-MG (ao norte do PERD) e Caratinga-MG (a leste do PERD) [p. 15].
- Classes de aptidão do modelo: 1,000–1,599 nulo ou muito baixo; 1,600–1,999 baixo; 2,000–2,500 moderado; 2,501–2,900 elevado; 2,901–3,000 muito elevado [p. 13].
- Silvicultura recebeu nota 2 (aptidão moderada), abaixo das áreas rurais antropizadas (nota 3) e acima de água, áreas urbanizadas, florestas e matas (nota 1) [p. 12].
- Conclusão dos autores: existem mais de 5.500 ha aptos, extensão considerada significativa para implementação de SAF na região [p. 16].

## 6. Limitações que os próprios autores reconhecem

- O resultado é um ponto de partida: para implementação real, "podem e devem ser ainda mais refinados", com novas variáveis (disponibilidade de mão de obra local, APPs de topo de morro) e análises in loco das principais áreas [p. 16].
- A conclusão reforça que, para uso em decisões de programas de revegetação, "possivelmente ainda serão necessários outros filtros, com utilização de diferentes variáveis" [p. 16–17].
- O NDVI isolado pode gerar falsos positivos: áreas com pouca vegetação podem ser dunas, areais, cascalhos, afloramentos rochosos, corte recente de eucalipto, lavouras em entressafra ou pastagens produtivas [p. 11].
- APPs situadas em meio urbano ou sobre corpos d'água não são aptas, exigindo filtragem pela camada de uso e cobertura da terra para evitar anomalias no modelo [p. 10].

## 7. O que serve ao projeto e o que não serve

- **Não serve como referência de biomassa ou carbono:** o artigo não estima biomassa, estoque de carbono, produtividade nem volume de madeira, e não trabalha com silvicultura como alvo — silvicultura é apenas uma classe de uso com nota 2 [p. 12].
- **Não serve como referência multissensorial nem para Goiás:** usa apenas Landsat 8 (mais bases vetoriais ANA e OSM), no entorno do PERD, em Minas Gerais; não há fusão de sensores, LiDAR, radar ou dados de campo [p. 9].
- **Serve como protocolo metodológico para AHP em ambiente SIG:** detalha matriz de comparação par a par, escala 1–9, pesos, λ, CI e CR, com replicação gratuita em QGIS/EasyAHP [p. 6; p. 13].
- **Serve como cautela no uso de NDVI:** documenta a ambiguidade do índice em pastagens produtivas, entressafra e corte de eucalipto, argumento útil para justificar índices de vegetação complementares e validação de campo no projeto [p. 11].

## 8. Frases citáveis (literais)

- "As áreas de aptidão mais elevada para os SAF somam 5.580 hectares." [p. 1]
- "É pertinente ressaltar que, para o caso de implementação real de SAF na região, os resultados apresentados podem e devem ser ainda mais refinados." [p. 16]
