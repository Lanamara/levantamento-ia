# RELATÓRIO — PAULA L.G. OLIVEIRA (2024)

## 1. Referência

- Paula L.G. Oliveira, Eraldo A.T. Matricardi, Eder P. Miguel, Ben Hur Marimon Júnior & Alba Valéria Rezende (2024). *Artificial Neural Network and Remote Sensing combined to predict the Aboveground Biomass in the Cerrado biome*. Anais da Academia Brasileira de Ciências (An Acad Bras Cienc) 96(3): e20221041. DOI 10.1590/0001-3765202420221041.
- O `TEXTO.txt` corresponde a este DOI, está íntegro (23 páginas, de "INTRODUCTION" a "Author Contributions", com referências) e não apresenta truncamento.

## 2. Pergunta do estudo

É possível estimar com acurácia a biomassa acima do solo (AGB) de vegetação de Cerrado no Distrito Federal combinando índices de vegetação derivados de imagens RapidEye com redes neurais artificiais (ANN-MLP)?

## 3. Área e dados

- Local: Distrito Federal, Brasil, 578.919 ha dentro do bioma Cerrado, clima Aw, precipitação média anual de 1.500 mm; Cerrado *sensu stricto* com cobertura arbóreo-arbustiva de 10% a 60% [p. 3–4].
- Período: inventário de campo do Inventário Florestal Nacional (NFI) realizado em 2011 [p. 4]; dados de campo da Fazenda Água Limpa (FAL/UnB) de 2005 [p. 5]; imagens RapidEye de setembro e outubro de 2011 (uma cena de 09/10/2011 e outra de 22/06/2011) [p. 7].
- Sensores/fontes: RapidEye, 5 bandas (azul, verde, vermelho, red-edge 0,69–0,73 µm, NIR), resolução espacial de 5 m e temporal de 5 dias, reflectância de topo de atmosfera processada no ERDAS IMAGINE 2011 [p. 7]; dados de campo NFI e FAL [p. 4–5].
- Amostras: 42 parcelas em vegetação savânica, selecionadas de 15 conglomerados, com 4 subamostras de 0,1 ha (20x50 m) cada, subdivididas em 10 subparcelas de 10x10 m [p. 4–5]; 18 parcelas permanentes de 0,1 ha na FAL [p. 5]. Na modelagem, 42 parcelas (70%) para treinamento e 18 para validação [p. 10] — o texto fala em "sixty sample plots" [p. 10], o que não fecha com as 42 parcelas descritas na coleta [p. 4].

## 4. Método

- AGB por indivíduo (DB ≥ 5 cm) pela equação alométrica de Rezende et al. (2006): AGB = 0,4913 + 0,0291 × DB² × Ht (R² = 98,28%; Syx = 25,79%), sem densidade da madeira; soma por parcela e normalização em Mg.ha⁻¹ [p. 6–7].
- Cinco índices de vegetação (NDVI, NDRE, GNDVI, CIrededge, CIgreen) extraídos das imagens [p. 7–8]; teste de Shapiro-Wilk, correlação de Spearman (não paramétrica) e VIF para multicolinearidade, no RStudio 1.0.143 [p. 8, 10].
- Seleção de variáveis por stepwise regression, retendo GNDVI e NDRE [p. 11].
- Treinamento supervisionado de 500 redes MLP no Intelligent Problem Solver (Statistica 7), normalização 0–1 e algoritmo quasi-Newton BFGS; escolha por RMSE%, R e análise gráfica de resíduos, com validação por teste t de Student, diferença agregada (DA%) e função de autocorrelação (ACF) [p. 8–10, 13].

## 5. Resultados principais

- Inventário: DB médio 11,57 cm, Ht média 3,52 m, área basal 10,32 m².ha⁻¹, AGB média 16,55 Mg.ha⁻¹ (mínimo 5,12; máximo 39,46; DP 8,59; CV 51,89%) [p. 11]. O resumo traz 16,55 ± 8,6 Mg.ha⁻¹ [p. 1] e a discussão, 16,55 ± 8,5 Mg.ha⁻¹ [p. 14].
- Correlação de Spearman com AGB: GNDVI 0,77 e CIgreen 0,77 (as maiores), NDVI 0,71, NDRE 0,67, CIrededge 0,67, área basal 0,76; todas significativas a 1% [p. 11].
- VIF indicou multicolinearidade entre GNDVI e CIgreen (r = 1,00 entre si) [p. 11]; o stepwise reteve GNDVI e NDRE [p. 11].
- Das 500 redes, cinco selecionadas; a ANN 2 (MLP 2-8-1, ativação tangente nas duas camadas) teve RMSE de 16,52% e R = 0,908 no ajuste e RMSE de 13,36% e R = 0,914 na validação [p. 12]. As redes 2, 3 e 4 tiveram R > 0,84 e erros abaixo de 18% [p. 11].
- Validação: teste t com p = 0,893 (sem diferença significativa entre observado e estimado) e DA% = -0,65, leve superestimação [p. 13].
- ACF dos resíduos: -0,13, sem autocorrelação espacial significativa a 95% [p. 13].
- Poder preditivo de 90% e RMSE inferior a 17% [p. 1, 18]; erros concentrados entre -10% e 7% no treinamento [p. 17].
- Extrapolação: maiores estoques em áreas protegidas; a Estação Ecológica de Água Emendadas teve a maior média, 26,94 ± 8,41 Mg.ha⁻¹ [p. 18]; fragmentos pequenos próximos a áreas urbanas, 6 a 13 Mg.ha⁻¹ [p. 18].

## 6. Limitações que os próprios autores reconhecem

- Não usaram densidade da madeira nas estimativas, por variação entre espécies, indivíduos e dentro da árvore, e por indisponibilidade de dados [p. 5–6].
- Assumiram que não houve mudança significativa na biomassa entre 2005 (dados FAL) e 2011 (imagens), na ausência de fogo ou evento climático severo [p. 5].
- Correlações apenas médias entre índices e biomassa indicam desempenho moderado do modelo; atribuem isso a efeitos atmosféricos e de solo, saturação do sinal espectral, contribuição do sub-bosque e sombreamento [p. 16–17].
- O estudo se restringe a shrublands de Cerrado *sensu stricto* no DF; Random Forest, SVM, hyperspectral, SAR e LiDAR ficam como pesquisa futura [p. 18].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o encadeamento estatístico antes da modelagem — Shapiro-Wilk, Spearman, VIF e stepwise — para escolher índices sem redundância, replicável em povoamentos de eucalipto em Goiás [p. 8, 11].
- **Serve:** o desenho de treinamento/validação (70%/30%), com RMSE%, R, DA% e teste t, como protocolo de avaliação de modelos de biomassa [p. 10, 13].
- **Serve:** a evidência de que índices de red-edge (NDRE) combinados a um índice de banda verde (GNDVI) superam pares colineares, e o patamar de referência de R ≈ 0,91 e RMSE de 13–17% em vegetação nativa [p. 11–12, 15].
- **Não serve:** não há silvicultura (apenas Cerrado nativo), não há estoque de carbono em Mg.C.ha⁻¹ nem fator de conversão (o carbono é tratado só qualitativamente) [p. 18], e o sensoriamento é monossensor óptico (RapidEye, 2011), sem a fusão multissensorial que o projeto propõe [p. 18].

## 8. Frases citáveis (literais)

- "The best performing ANN showed a predictive power of 90% and RMSE less than 17%." [p. 1]
- "However, we observed multicollinearity between GNDVI and CIgreen, suggesting that one index does not substantially contribute additional information beyond the other." [p. 15]
