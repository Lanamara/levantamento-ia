# RELATÓRIO — Getúlio Fonseca Domingues (2023)

## 1. Referência

Getulio Fonseca Domingues; Guilherme Silverio Aquino de Souza; Rodolfo Alves Barbosa; Gustavo Eduardo Marcatti; Alexandre Simões Lorenzon; Helio Garcia Leite (2023). "Estimated volume of eucalyptus plantations through ALOS satellite images". TreeDimensional Journal (TREED), v. 11, e2023025, p. 1–8. DOI: 10.55746/treed.2023.09.025.

O `TEXTO.txt` está completo (8 páginas, incluindo referências) e corresponde ao DOI acima.

## 2. Pergunta do estudo

Testar diferentes configurações de redes neurais artificiais para estimar o volume de madeira de plantios comerciais de eucalipto a partir de dados multiespectrais (AVNIR-2) e de micro-ondas (PALSAR) do satélite ALOS [p. 2].

## 3. Área e dados

- Local: plantio comercial de eucalipto para celulose em Minas Gerais, Brasil, entre 19°14′–19°34′S e 42°32′–42°20′W; 83.712 ha; clones espaçados 3 × 2 m, idade de 4 a 8 anos, altura média de 26 m [p. 2].
- Clima Aw (temperado chuvoso-mesotérmico), precipitação média anual de 1.153 mm, temperatura média anual de 20 a 23 °C, solo Neossolo Flúvico Distrófico, relevo plano a suavemente ondulado [p. 2].
- Inventário florestal: 206 parcelas, realizado entre fevereiro e setembro de 2009; volume por parcela obtido por modelagem de altura e diâmetro [p. 2].
- Sensores: AVNIR-2 (multiespectral, 4 bandas) e PALSAR (radar L-band), ambos a bordo do ALOS; imagens de 2 e 27 de maio de 2009, respectivamente; PALSAR com ~12 m de resolução espacial e ângulo de incidência de 8° a 30° [p. 2].
- Bases de treino/teste/validação derivadas de 104, 84, 62 e 42 parcelas, conforme o cenário [p. 4–5].

## 4. Método

- Dados herdados de Oliveira (2011); variável dependente = volume por parcela; independentes = reflectância média das 4 bandas AVNIR-2 (AV1–AV4) e retroespalhamento das 4 polarizações PALSAR (LHH, LHV, LVV, LVH) [p. 3].
- Correção atmosférica das imagens AVNIR-2 pelo método de Chavez (1975); imagens PALSAR convertidas de 16 para 8 bits e usadas para calcular o coeficiente de retroespalhamento [p. 2–3].
- Redes Multilayer Perceptron (MLP) treinadas no Statistica 12 com o algoritmo Quasi-Newton BFGS; seleção de arquitetura pela ferramenta Intelligent Problem Solver (IPS): 1 a 20 neurônios na camada oculta, quatro funções de ativação (tangente hiperbólica, exponencial, logística, identidade) e 5.000 MLPs por combinação de amostras [p. 3].
- Partições aleatórias treino/teste/validação iniciando em 50/25/25 e reduzindo o treino até 10% (restante dividido igualmente entre teste e validação); melhor rede escolhida por coeficiente de correlação, distribuição de erros e RMSE% [p. 3].

## 5. Resultados principais

- Somente AVNIR-2, MLP 4-7-1 (tangente hiperbólica na oculta, logística na saída), 50% das parcelas no treino: resíduos de -4 a 20%, correlação de 0,96 e RMSE de 9,7 m³ ha⁻¹ [p. 3].
- Somente PALSAR, MLP 4-10-1 (logística em ambas as camadas): RMSE% de 7,93, correlação de 0,72 e resíduos de -12 a 16% [p. 4].
- AVNIR-2 + PALSAR, MLP 8-7-1, 104 parcelas: RMSE de 0,70 m³ ha⁻¹, correlação de 0,99 e resíduos de -1 a 0% [p. 4].
- 84 parcelas, MLP 8-4-1: resíduos de -1 a 2%, RMSE% de 0,81 e correlação de 0,99 [p. 4].
- 62 parcelas, MLP 8-4-1: resíduos de -10 a 12%, RMSE de 2,18% e correlação de 0,98 [p. 4].
- 42 parcelas, MLP 8-4-1: resíduos de -2 a 8%, RMSE de 1,65% e correlação de 0,98 — resultado melhor que o de 62 parcelas, atribuído à representatividade das amostras [p. 5].
- 22 parcelas, MLP 8-8-1: resíduos de -14 a 12%, RMSE de 6,43% e correlação de 0,81, com tendência a subestimar os volumes mais altos [p. 5].
- Ordem decrescente de importância das variáveis: AV2; LVH; LHV; LHH; AV1; LVV; AV3; AV4 — a banda do verde (AV2) foi a mais importante e o infravermelho (AV4), a menos importante [p. 5].
- Comparação com regressão linear prévia (Oliveira, 2011): R² de 0,71 para biomassa e 0,69 para volume, contra coeficientes de determinação superiores das redes, usando apenas 10% dos dados no treino [p. 6].
- Volume estimado com precisão usando entre 62 e 104 parcelas para treinar as redes, em área de 83.712 ha [p. 5].
- Observação: o resumo cita erro quadrático médio de 0,3% [p. 1], valor que não reaparece nos resultados (0,70 m³ ha⁻¹ e RMSE% de 0,81 a 6,43 conforme o cenário) [p. 4–5].

## 6. Limitações que os próprios autores reconhecem

- Dados ópticos apresentam saturação do sinal em dosséis densos, limitação que também ocorre em radares, ainda que ondas mais longas penetrem mais [p. 2].
- A análise de sensibilidade exige cautela porque as relações de causa e efeito modeladas pelas redes neurais são desconhecidas ("efeito caixa-preta"); a importância atribuída a cada variável vale apenas para o ajuste em questão [p. 5].
- A diferença de desempenho entre 62 e 42 parcelas é explicada pela provável diferença de representatividade entre as amostras que compuseram os conjuntos de treino [p. 5].
- Com apenas 22 parcelas no treino, a rede passou a subestimar os maiores valores de volume [p. 5].

## 7. O que serve ao projeto e o que não serve

- Serve: a arquitetura de fusão multissensorial (4 bandas ópticas + 4 polarizações SAR em um único MLP) como desenho metodológico replicável para volume/biomassa [p. 3–4].
- Serve: o protocolo de partições progressivas (50% → 10% de treino) e os critérios de seleção (correlação, resíduos, RMSE%) para testar o tamanho mínimo de amostra de campo [p. 3].
- Serve com ressalva: os resultados quantitativos vêm de um único talhão comercial em Minas Gerais, com clima Aw e imagens de maio de 2009 [p. 2]; a transferência para Goiás e para outras idades/sítios precisa de validação própria.
- Não serve diretamente: o estudo modela volume de madeira (m³ ha⁻¹), não biomassa nem estoque de carbono; não há fatores de conversão nem discussão de carbono no texto [p. 3, p. 6] — e a área é de eucalipto plantado, não de vegetação nativa.

## 8. Frases citáveis (literais)

- "Nevertheless, the best volume estimates observed in this work were obtained using multispectral and microwave data together." [p. 4]
- "The most important variables in decreasing order were: AV2; LVH; LHV; LHH; AV1; LVV; AV3; AV4." [p. 5]
