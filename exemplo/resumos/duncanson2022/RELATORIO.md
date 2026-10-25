# RELATÓRIO — Duncanson et al. (2022)

## 1. Referência

DUNCANSON, L.; KELLNER, J. R.; ARMSTON, J.; DUBAYAH, R.; MINOR, D. M.; HANCOCK, S. *et al.* **Aboveground biomass density models for NASA's Global Ecosystem Dynamics Investigation (GEDI) lidar mission.** *Remote Sensing of Environment*, v. 270, 112845, 2022. DOI: 10.1016/j.rse.2021.112845. (Disponível online em 7 jan. 2022; ~90 autores.)

## 2. Pergunta do estudo

Quais preditores (métricas RH), transformações e nível de estratificação geográfica geram os modelos paramétricos de densidade de biomassa acima do solo (AGBD) por *footprint* (~25 m) mais acurados e transferíveis entre regiões para o produto GEDI04_A?

## 3. Área e dados

- **Local:** global, domínio do GEDI (≈ ±51,6° de latitude), com estratificação em 4 tipos funcionais de planta (PFT: EBT, ENT, DBT, GSW) e 6 regiões geográficas (América do Norte, América do Sul, Europa, África, Ásia, Oceania) [p. 3; p. 11]. Nenhum estrato específico para Cerrado ou para plantios florestais.
- **Período:** GEDI lançado em 5/12/2018, dados científicos desde abril de 2019; modelos aplicados ao arquivo 2019–2021 [p. 4]. Período das campanhas de campo: não informado (cada conjunto tem data própria, Tabela S1); o ALS usado tinha de ser de estação com folhas e coletado até 2 anos do dado de campo [p. 7].
- **Sensores/fontes:** lidar de forma de onda completa do GEDI (1064 nm, footprint ~25 m, 8 trilhas, espaçamento de 60 m ao longo da trilha) [p. 4]; ALS (Airborne Laser Scanning) de diversos instrumentos, simulado como GEDI por um simulador de forma de onda [p. 7]; MODIS MCD12Q1 V006 para classe PFT [p. 10]; parcelas de campo harmonizadas na base FSBD [p. 6].
- **Amostras:** 74 sítios de campo, selecionados de 142 sítios/projetos contribuintes [p. 6]; parcelas de ~25 m de diâmetro [p. 7]; 11 estratos PFT×região, com 65 a 3.441 amostras de treino por estrato (≈ 8.525 somando a Tabela 2) [p. 11]; densidade mínima de ALS de > 4 pulsos m⁻² [p. 7].

## 4. Método

1. **Base de calibração "crowd-sourced":** pareamento de parcelas de campo com ALS coincidente, geração de formas de onda tipo GEDI simuladas (peso gaussiano σ = 5,5 m; convolução com pulso FWHM = 15,6 ns) e cálculo das métricas RH em relação ao solo [p. 7].
2. **Modelos OLS paramétricos** com transformações identidade/log/raiz da resposta e dos preditores, correção de viés após retrotransformação (método de razão, Snowdon), filtros de multicolinearidade (r < 0,9; VIF ≤ 10) e offset de +100 m nas métricas RH [p. 8–9].
3. **Conjunto exaustivo de candidatos:** todas as combinações de 1 a 4 preditores (RH10–RH98 e termos de interação de duas vias), 4 níveis de restrição (livre, RH98 forçado, sem métricas < RH50, ambos) e 4 transformações → mais de 100.000 modelos [p. 3; p. 8–10].
4. **Seleção por validação cruzada de transferibilidade geográfica:** aplicação do modelo a áreas fora do treino mas dentro do estrato, com ranking por MRE, %RMSE (em faixas de 5%), maior métrica RH, número de coeficientes e número de métricas RH [p. 10].

## 5. Resultados principais

- Foram ajustados **> 100.000 modelos** no total, tipicamente **2.000–10.000 por estrato** [p. 10].
- O **%RMSE** dos 20 melhores modelos por estrato variou de **~28% a 66%**, com a maioria entre **30% e 50%**; o **MRE** ficou **< 25 Mg/ha** em todos os estratos, exceto **EBT Ásia** [p. 10].
- Melhor e pior desempenho na Tabela 2: **GSW Oceania** com R² = **0,90**, %RMSE = **58,60** e MRE = **11,41 Mg/ha**; **EBT Oceania** com o menor %RMSE (**28,66**); **EBT Ásia** com R² = **0,36**, %RMSE = **78,94** e MRE = **121,15 Mg/ha** [p. 11].
- Estrato amplo **Ásia**: R² = **0,46**, %RMSE = **98,83**, MRE = **142,98 Mg/ha** — o pior do conjunto [p. 11].
- **EBT América do Sul** (estrato tropical com mais dados): R² = **0,66**, %RMSE = **42,2**, MRE = **10,4 Mg/ha**, **3.441** amostras [p. 11].
- Predominância de **1 a 3 preditores** nos modelos escolhidos; os modelos da versão 1 tinham forma simples (só RH98, RH98+RH70 ou RH98+RH50), com **RH98 presente em todos** [p. 3; p. 13–14].
- A **raiz quadrada** da AGBD foi a transformação dominante (esquema sqrt-sqrt), com exceção de **EBT Ásia** e **Ásia** [p. 11].
- Restringir os modelos (forçar RH98 e remover métricas < RH50) elevou o %RMSE em **18,63 pontos** em EBT Ásia e **7,08** em GSW Oceania, e o MRE em **17,68 Mg/ha** (DBT Europa) e **15,21 Mg/ha** (DBT América do Norte), mas na maioria dos estratos o efeito foi pequeno [p. 16].
- A AGBD das parcelas de treino vai de **0 a mais de 1.000 Mg/ha** por footprint [p. 9].
- O simulador de formas de onda apresentou viés **< 25 cm** e RMSE de **5,7 m** para as métricas RH [p. 7].
- Requisito da missão que condiciona o erro aceitável: erro-padrão de **20% da AGBD média em pelo menos 80% das células de 1 km** [p. 4].

## 6. Limitações reconhecidas pelos autores

- **Incertezas não contabilizadas (seção 4.5):** erros de medição no inventário de campo, erros nas métricas RH do GEDI em órbita, erros dos modelos alométricos, erros de amostragem/representatividade do treino e erros da transposição de métricas simuladas para observadas **não** foram incluídos nas estimativas de incerteza do GEDI04_A [p. 16].
- **Dados escassos em alguns estratos:** EBT Ásia é o caso extremo (poucos sítios, em áreas de biomassa muito alta em Bornéu), com modelo "unreliable" e opção por um modelo mais genérico [p. 12]; a falta de dados de treino em parte dos estratos prejudicou o desempenho (ex.: Ásia continental) [p. 17].
- **Representatividade do treino:** garantir que a faixa de valores do treino seja semelhante à da população é difícil pela falta de dados de alta qualidade em todos os estratos de predição [p. 17].
- **Alometria:** os modelos alométricos usados para gerar a AGB de campo têm incertezas altas (ex.: árvores grandes) [p. 6].
- **Geolocalização e tamanho de parcela:** incerteza de ~10 m do GEDI e ~5 m das parcelas sob dossel denso dificulta o pareamento; parcelas pequenas aumentam a variância e os efeitos de borda [p. 4; p. 12].
- **Simulação vs. observação:** a forma de pulso em órbita não é perfeitamente gaussiana e a razão de reflectância copa/solo foi assumida constante, o que motivou excluir métricas RH baixas dos modelos finais [p. 8–9].
- **Classificação PFT:** onde o campo não informava o PFT, usou-se o MODIS, com risco de erros de classificação e de casamento espacial/temporal [p. 10].
- Os modelos descritos são a **versão 1 e 2** do produto e serão substituídos [p. 17].

## 7. O que serve ao projeto e o que não serve

- **Serve — desenho de validação:** o esquema de validação cruzada por transferibilidade geográfica (treinar em uma região, testar em outra dentro do estrato), com MRE por faixas de AGBD além de R² e %RMSE, é diretamente aplicável a Goiás (treinar em talhões/regiões e testar em outros) [p. 10].
- **Serve — referência metodológica:** justifica OLS paramétrico com 1–3 preditores de estrutura (altura máxima + métrica mediana) como linha de base parcimoniosa e comparável a modelos de aprendizado de máquina, além da correção de viés na retrotransformação [p. 8; p. 13].
- **Serve — argumento sobre estratificação e escala:** demonstra que modelos estratificados (por tipo de vegetação e região) superam o modelo global, evidência útil para defender calibração regional no Cerrado/goiano em vez de usar um modelo pantropical [p. 11; p. 15].
- **Não serve — domínio e alvos:** os estratos são PFTs naturais (EBT, ENT, DBT, GSW) do domínio GEDI, sem classe de **plantio comercial** (Eucalyptus/Pinus) nem de Cerrado stricto sensu, e o produto é AGBD, **não estoque de carbono** [p. 3; p. 9]; sensores: apenas lidar de forma de onda (GEDI/ALS) + MODIS para PFT, sem a fusão multissensorial óptica/SAR pretendida no projeto, e sem custo computacional/operacional de campo comparável.

## 8. Duas frases citáveis (literais)

> "Fourth, for the vast majority of strata, the best performing models were fit using square root transformation of field AGBD and/or height metrics." [p. 3]

> "The development of global biomass maps from GEDI rests upon the development of robust, transparent, and reproducible calibration models with well-known error structures." [p. 17]
