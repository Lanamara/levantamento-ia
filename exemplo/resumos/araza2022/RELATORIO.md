# RELATÓRIO — Araza et al. (2022)

## 1. Referência

ARAZA, A.; DE BRUIN, S.; HEROLD, M.; QUEGAN, S.; LABRIERE, N.; RODRIGUEZ-VEIGA, P. et al. **A comprehensive framework for assessing the accuracy and uncertainty of global above-ground biomass maps**. *Remote Sensing of Environment*, v. 272, 112917, 2022. DOI: 10.1016/j.rse.2022.112917. (Recebido em 22/03/2021; aceito em 17/01/2022; 30 autores, os três primeiros de Wageningen University.) [p. 1]

## 2. Pergunta do estudo

Como estimar de forma objetiva, consistente e espacialmente explícita o viés e a incerteza de mapas globais de biomassa acima do solo (AGB), comparando-os com inventários florestais e parcelas de pesquisa que têm incerteza conhecida? [p. 2]

## 3. Área e dados

- **Local:** global, com estudo detalhado do pantropical (25°N–25°S); parcelas distribuídas em todos os biomas, com sub-representação de parte do boreal e da floresta tropical úmida. [p. 4; p. 7]
- **Período:** parcelas medidas entre 1996 e 2018 [p. 4]; épocas dos mapas avaliados: Baccini 2000, GEOCARBON 2007–2010, GlobBiomass 2010 e CCI Biomass 2017 [p. 5].
- **Sensores/fontes:** inventários florestais nacionais (NFI) e parcelas de redes de pesquisa; mapas globais de AGB derivados de LiDAR espacial + reflectância Landsat (Baccini), fusão de mapas pantropicais e mapa boreal de radar (GEOCARBON) e imagens SAR de intensidade de retroespalhamento convertidas em volume de madeira e depois em AGB (GlobBiomass e CCI Biomass). [p. 4; p. 5] Covariáveis do modelo de viés: AGB do mapa, SD do mapa, declividade e aspecto (SRTM) e cobertura arbórea Hansen 30 m; clima, bioma, longitude e latitude foram testados e descartados. [p. 6; p. 7, Tabela 1]
- **Amostras:** até 116.181 parcelas (de 225.698 possíveis) como referência [p. 4]; 8.457 parcelas com dados de árvores individuais, somando 267.907 árvores, o que é 7,4% do total de parcelas [p. 5]; 38.727 parcelas (um terço do total) na avaliação do modelo de erro de amostragem [p. 6]. Células de 0,1° com pelo menos 5 parcelas (média de 15 parcelas e 2,3 ha por célula) [p. 6]: Baccini 6.561, GEOCARBON 6.521, GlobBiomass 6.201 e CCI Biomass 2.612 células [p. 9, Fig. 4].

## 4. Método

1. **Harmonização das parcelas:** filtros de qualidade (não usadas na calibração do mapa, coordenadas com 4 casas decimais, medição até 10 anos da época do mapa, DAP ≥ 10 cm, não desmatadas, metadados completos), correção temporal por taxas de crescimento e correção areal pela fração florestal (cobertura arbórea > 10%). [p. 4; p. 5]
2. **Incerteza da parcela:** soma em quadratura de três fontes — erro de medição + modelo alométrico (propagação por 1.000 simulações Monte Carlo, pacote BIOMASS, com modelo altura–diâmetro de Weibull), erro temporal e erro de amostragem (CV previsto por random forest em função do tamanho da parcela e do pixel). [p. 5; p. 6]
3. **Comparação parcela–mapa em 0,1°:** média ponderada de variância mínima (MVLU) das parcelas por célula contra a média dos pixels do mapa; métricas RMSD e viés (MD) por classes de 50 Mg ha⁻¹; métrica de conformidade do erro do mapa (otimista/pessimista). [p. 6]
4. **Modelagem espacial:** random forest para prever o viés com 5 covariáveis (AGB do mapa, SD do mapa, declividade, aspecto, cobertura arbórea) e correção só onde o IC95% do viés não inclui zero; variogramas dos resíduos escalonados pela SD para estimar a correlação espacial e a variância do total pantropical; comparação com o FRA 2020. [p. 7]

## 5. Resultados principais

- Erro de medição + alometria domina a incerteza da parcela: para parcelas < 0,3 ha, IQR da SD = 30–151 Mg ha⁻¹; erro de amostragem, SD = 16–44 Mg ha⁻¹. [p. 2; p. 7]
- Na média dos mapas, SD estimada de 93,9 Mg ha⁻¹ (medição), 51,6 Mg ha⁻¹ (amostragem) e 24,6 Mg ha⁻¹ (temporal), equivalentes a 73%, 22% e 5% da variância total. [p. 7]
- Modelo de predição do erro de medição: R² = 0,86 e RMSE = 22,1 Mg ha⁻¹ (validação com n = 2.819 parcelas); modelo de CV de amostragem: R² = 0,81 e RMSE = 0,07 (n = 38.727). [p. 5; p. 6]
- Todos os mapas superestimam AGB baixa e subestimam AGB alta; a inversão ocorre em ~150 Mg ha⁻¹ (Baccini) e ~200 Mg ha⁻¹ (demais). [p. 7]
- Conformidade do erro: GEOCARBON é otimista quanto à precisão; CCI Biomass é pessimista; Baccini e GlobBiomass são otimistas em AGB baixa e pessimistas em AGB alta. [p. 7]
- O RF de viés explica 24–36% da variância do viés; AGB do mapa e cobertura arbórea são os preditores mais importantes; em 4–15% das células o IC95% do viés incluiu 0 Mg ha⁻¹. [p. 7]
- Subestimação sistemática nas florestas úmidas da Amazônia, bacia do Congo e Sudeste Asiático insular; GEOCARBON tem a menor subestimação nos trópicos e GlobBiomass a maior superestimação nas regiões temperadas. [p. 8]
- Correlação espacial dos erros do mapa até 50–104 km, com sills dos variogramas de 0,11–0,38 e nugget = 0. [p. 2; p. 8]
- Total pantropical de AGB (Tabela 3): 2000 = 354,47 Pg (padrão), 406,38 Pg (ajustado por viés) e 302,69 Pg (FRA); 2010 = 279,35 / 314,20 / 290,97 Pg; 2017 = 277,60 / 296,20 / 283,78 Pg. IC95% do total: 5,83 e 0,88 Pg em 2000; 7,93 e 5,09 Pg em 2010; 14,10 e 1,57 Pg em 2017. [p. 12, Tabela 3]
- O ajuste por viés eleva o total em todos os anos; a diferença entre estimativas diminui de 2000 a 2017, mas o total ajustado ainda é 12,4 Pg maior que o FRA em 2017. [p. 8]
- Divergência entre passagens: a conclusão fala em diferença de "pelo menos 6,9 Pg" em 2017 [p. 13], valor que não bate com os 12,4 Pg do texto [p. 8] nem com a Tabela 3 (296,20 − 283,78 = 12,42 Pg) [p. 12].
- Subestimação de ao menos 60 Mg ha⁻¹ ocorre sobretudo com AGB > 300 Mg ha⁻¹ e cobertura de copa de 60–90%; viés dos mapas de radar é sensível a encostas íngremes de nordeste. [p. 10]

## 6. Limitações reconhecidas pelos autores

- A maioria das parcelas com dados de árvore não tem altura; a altura foi estimada pelo modelo de Weibull, que pode não se aplicar a todos os biomas (savanas arbóreas e manguezais). [p. 13]
- Falta de dados de árvore individuais fora dos trópicos, de modo que os erros de medição nessas regiões estão sujeitos a revisão; o conjunto boreal está concentrado em dois países, limitando a aplicação global. [p. 13]
- Viés de seleção das parcelas: parcelas de pesquisa são 4% do total, mas 24% nos trópicos, e podem superestimar a AGB da célula; o teste com filtragem estrita indicou efeito pequeno, mas o viés corrigido acima de 300 Mg ha⁻¹ pode estar exacerbado pela falta de dados representativos. [p. 13]
- As camadas de SD dos mapas precisam ser melhoradas: os sills dos variogramas se afastam de 1 e a conformidade do erro mostra SD otimistas ou pessimistas; falta camada de SD extra-tropical para o mapa Baccini, o que restringiu a análise aos trópicos. [p. 6; p. 12]
- O modelo de viés pode ser melhorado com covariáveis adicionais (textura da AGB, altura do dossel), mais parcelas grandes e validações cruzadas alternativas. [p. 13]

## 7. O que serve ao projeto e o que não serve

- **Serve:** o arcabouço de validação (incerteza da parcela → MVLU em célula → viés por RF → variograma → total com IC) é transplantável para validar mapas de biomassa da silvicultura goiana; a decomposição da incerteza em medição/alometria, amostragem e tempo, com medição + alometria respondendo por 73% da variância, indica onde investir esforço de campo (DAP, altura, modelo alométrico local). [p. 3; p. 6; p. 7; p. 9]
- **Serve:** a modelagem do viés em função de AGB, cobertura arbórea e declividade, e o uso de variogramas para agregar erros espacialmente correlacionados, são úteis para reportar estoque por talhão, fazenda ou município com IC honesto. [p. 7; p. 10]
- **Não serve:** o estudo não tem nenhum dado de Goiás, do Cerrado ou de floresta plantada (Eucalyptus/Pinus); as parcelas são florestas naturais e NFIs, e os modelos alométricos são genéricos tropicais, não específicos por clone/espécie. [p. 2; p. 4; p. 5]
- **Não serve (resolução):** os mapas avaliados são globais/pantropicais (pixels de 30 m a 1 km) e toda a análise é feita em células de 0,1° (~11 km); a escala é grossa demais para manejo de talhão, e a fusão multissensorial drone + óptico + SAR de alta resolução que o projeto pretende não é abordada. [p. 5; p. 6; p. 9]

## 8. Duas frases citáveis

> "All AGB maps tended to overestimate low AGB and underestimate high AGB." [p. 9]

> "Both map-based and FRA estimates of pantropical AGB show a decline from 2000 to 2017, and become increasingly close with time, despite the datasets and methods used being quite different for different map epochs." [p. 13]
