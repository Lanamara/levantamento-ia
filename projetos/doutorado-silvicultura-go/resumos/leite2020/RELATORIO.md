# RELATÓRIO — Rodrigo Vieira Leite (2020)

## 1. Referência

- Rodrigo Vieira Leite; Cibele Hummel do Amaral; Raul de Paula Pires; Carlos Alberto Silva; Carlos Pedro Boechat Soares; Renata Paulo Macedo; Antonilmar Araújo Lopes da Silva; Eben North Broadbent; Midhun Mohan; Hélio Garcia Leite (2020).
- "Estimating Stem Volume in Eucalyptus Plantations Using Airborne LiDAR: A Comparison of Area- and Individual Tree-Based Approaches".
- *Remote Sensing*, 12(9), 1513. DOI: 10.3390/rs12091513 [p. 1].
- `TEXTO.txt` contém o artigo integral do DOI indicado (corpo, conclusões e referências), sem truncamento do conteúdo científico.

## 2. Pergunta do estudo

Comparar as abordagens area-based (ABA) e de detecção de árvores individuais (ITD) na estimativa de volume de fuste em plantios de *Eucalyptus*, verificando se uma supera a outra e propondo um método para melhorar a detecção de árvores em povoamentos homogêneos [p. 3].

## 3. Área e dados

- Local: Vale do Rio Doce, Minas Gerais, sudeste do Brasil, região montanhosa com forte variação de declividade [p. 3].
- Área total de 471,48 ha, dividida em 19 talhões clonais de *Eucalyptus urophylla* x *Eucalyptus grandis* para celulose, em três classes de idade: jovem (<4 anos), intermediária (4–6 anos) e madura (>6 anos) [p. 3].
- LiDAR aerotransportado (ALS): Cessna 206, altura média de 618 m, velocidade de 55 m/s, frequência de pulso de 300 kHz, ~5 pontos/m², footprint de 0,31 m, ângulo máximo de varredura de 30°, largura de faixa média de 713 m; voo em fevereiro de 2014 [p. 4].
- Inventário de campo: 33 parcelas retangulares de ~280 m², medidas em junho–agosto de 2014; dbh com suta e altura com clinômetro digital Haglof [p. 4].
- Estatísticas de campo por classe: madura 12 parcelas, 26,3 cm de dbh, 27,7 m de altura, 494,40 m³/ha, 1095 árvores/ha; intermediária 14 parcelas, 24,5 cm, 23,0 m, 324,74 m³/ha, 1042 árvores/ha; jovem 7 parcelas, 13,5 cm, 20,6 m, 133,11 m³/ha, 978 árvores/ha [p. 4].

## 4. Método

- **ABA**: cinco estimadores — regressão linear, modelo de Gompertz, ANN, Random Forest e SVM; 28 métricas LiDAR candidatas, com exclusão de colinearidade (|r| ≥ 0,9) seguida de Recursive Feature Elimination (RFE) para os não paramétricos e correlação de Spearman para os paramétricos [p. 4–5].
- **ITD**: três métodos de detecção de copas (dois Local Maxima Filters e watershed), combinados ao método proposto Tree Buffer Exclusion (TBE), gerando 35 possibilidades; dbh estimado por ANN e volume por árvore pelo modelo de Schumacher e Hall [p. 7, p. 9].
- Validação: divisão aleatória 60% treino / 40% teste, com r, RMSE, RMSE%, bias e bias%, e teste F de Graybill para comparar estimado vs. observado [p. 6, p. 9].
- Mapas de volume em tiles de 280 m² (mesmo tamanho das parcelas) para as duas abordagens [p. 9].

## 5. Resultados principais

- ABA com ANN foi o melhor resultado de volume por talhão: r = 0,95, RMSE = 14,41% e bias = −1,59% [p. 14].
- ITD por talhão: r = 0,94 e RMSE = 16,4%, mas bias = −9,55%, o maior valor absoluto, subestimando volumes baixos [p. 14].
- Na partição de teste (40%), r variou de 0,79 (linear) a 0,83 (ANN); RMSE% de 19,39 (ANN) a 24,71 (SVM); os métodos paramétricos diferiram significativamente do observado (p < 0,05) [p. 12].
- Seleção de variáveis: 15 das 28 métricas foram removidas por colinearidade, restando 13 para o RFE [p. 10]; as quatro mais importantes foram H.P95, Hmod, H.P50 e H.P10 [p. 11]; para os paramétricos, H.P95 teve a maior correlação com volume (ρ = 0,8361) [p. 11].
- Melhor detecção de árvores: LMF1 com janela de 2 m e raio TBE de 1,5 m, com o menor erro em 11 dos 19 talhões; watershed + 1,5 m foi o melhor em 7 dos 19 [p. 12].
- Todos os métodos de detecção melhoraram com a inclusão do TBE [p. 12, p. 19].
- Na validação por parcela, o ITD teve r = 0,80, RMSE% = 23,96 e bias% = −4,13 [p. 13].
- A estimativa de dbh por ANN no ITD atingiu r = 0,94, RMSE% = 5,52 e bias% = 0,0001 [p. 9].
- Altura média LiDAR subestimou a de campo nos plantios jovens (bias% = −11,17) e em declividades suaves (<25%) [p. 13].
- Erro geral dos métodos de volume em torno de 15% [p. 20]; cerca de 520 mil árvores detectadas no total [p. 21].
- Mapas: o ITD apresentou distribuição de volume com amplitude maior que a ABA, que concentrou estimativas em poucas classes [p. 14, p. 21].

## 6. Limitações que os próprios autores reconhecem

- Poucas parcelas (n = 33), o que pode ser apontado como limitante para treinar métodos não paramétricos, embora considerado consistente com a variabilidade de plantios homogêneos de *Eucalyptus* [p. 21].
- Apenas um ponto georreferenciado por parcela, com buffer de 9,44 m, devido à falta de posições adicionais; pequenas mudanças de posição afetam severamente a validação [p. 4, p. 21].
- Subestimativa de altura em plantios jovens e em terrenos suaves, atribuída à competição inicial e a erros no DTM por barreira da copa densa [p. 20].
- Classe de grande ângulo off-nadir (23°–30°) teve poucas observações para permitir inferências [p. 13].
- LMF e watershed não terão desempenho perfeito a menos que todas as árvores estejam no dossel superior; a direção e o início da janela móvel não foram explorados [p. 20].
- A janela ótima foi definida empiricamente pela relação com o espaçamento, por falta de informação para usar a rotina de janela variável do FUSION [p. 19].
- O ITD exige nuvens de pontos de alta densidade, implicando custo maior [p. 21].

## 7. O que serve ao projeto e o que não serve

- **Serve**: o desenho de validação (60/40, r, RMSE%, bias% e teste F de Graybill) e a comparação ABA vs. ITD no mesmo talhão são diretamente transferíveis para modelagem de biomassa e carbono [p. 6, p. 9].
- **Serve**: a cadeia de métricas LiDAR normalizadas (percentis de altura, Hmod, cobertura) e a seleção por RFE indicam variáveis candidatas enxutas para volume, base a partir da qual se pode modelar biomassa [p. 10–11].
- **Serve (com cautela)**: o TBE é uma correção simples e barata para erros de comissão em povoamentos homogêneos, útil onde o dossel é uniforme como na silvicultura goiana [p. 7, p. 21].
- **Não serve diretamente**: o artigo estima volume de fuste, não biomassa nem estoque de carbono; também não há sensoriamento multissensorial (só ALS), nem área em Goiás — a transposição para outro sítio e para equações de biomassa exige nova calibração [p. 3, p. 4].

## 8. Frases citáveis (literais)

- "The ABA was more accurate and precise especially with ANN for estimating stem volume as compared to the ITD approach." [p. 21]
- "From an operational standpoint, ABA is related to lower costs because it is possible to create models even with low-density point clouds [16]." [p. 21]
