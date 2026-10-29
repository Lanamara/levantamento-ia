# RELATÓRIO — Carlos Augusto Zangrando Toneli (2024)

## 1. Referência
- Toneli, C.A.Z.; Scardua, F.P.; Martins, R.d.C.C.; Matricardi, E.A.T.; Ribeiro, A.; Ferraz Filho, A.C. (2024). *Aerial Biomass Estimation in the Cerrado Biome Using Canopy Height Data*. Revista **Forests** (MDPI), v. 15, artigo 507. DOI: 10.3390/f15030507 [p. 1].
- Verificação: o `TEXTO.txt` contém o artigo integral (18 páginas, seções 1–5 e referências), e este corresponde ao DOI informado. Há pequenas duplicações de texto no arquivo (resquícios da versão "peer review"), mas o conteúdo está completo e não truncado.

## 2. Pergunta do estudo
Como estimar com acurácia a biomassa aérea e total (raízes, serapilheira e necromassa) das formações arbustivas, savânicas e florestais do Cerrado usando uma equação alométrica ajustada a partir da altura do dossel obtida por sensores ópticos e a laser?

## 3. Área e dados
- **Local:** todo o bioma Cerrado (Brasil), em altitudes de 300 a 1.600 m e precipitação anual de 600 a 2.000 mm [p. 5].
- **Período:** altura de dossel do ano de 2020 [p. 6]; revisão sistemática realizada em junho de 2023, com artigos publicados de 1998 a 2023 [p. 3]; medições de campo dos artigos datadas de 1988 a 2022 [p. 8].
- **Sensores/fontes:** modelo global de altura de dossel (canopy height model) de Lang et al. (2023), gerado com dados a laser orbital do programa GEDI fundidos a modelos de terreno e classificações de vegetação Sentinel-2, em pixels de 10 m [p. 4–5]; processamento na plataforma Google Earth Engine [p. 6]; fatores de expansão do 4º Relatório de Comunicação do Inventário Nacional de Gases de Efeito Estufa [p. 3].
- **Amostras:** 67 documentos revisados e 16 selecionados [p. 4]; validação com dois conjuntos: (1) inventário florestal de 77 sítios, 893 parcelas e 95.484 árvores [p. 6]; (2) 29 fragmentos florestais dos artigos (2 arbustivos, 14 de savana e 13 florestais) [p. 10]; no conjunto da revisão são identificados 37 fragmentos em sete fitofisionomias [p. 8].

## 4. Método
- Revisão sistemática de biomassa aérea publicada para o Cerrado (base CAPES, termos "forest AND aboveground AND biomass AND cerrado", artigos de 1998 a 2023) [p. 3].
- Classificação da vegetação por estratos de altura do dossel: campo (1–3 m), savana (4–7 m) e floresta (8–30 m) [p. 5].
- Conversão da altura do dossel em biomassa aérea pela equação alométrica linear AGB = 2,44 + 6,25 × CHM (canopy height model), implementada no Google Earth Engine [p. 6].
- Aplicação de fatores de expansão (raízes, serapilheira e necromassa) por estrato para obter a biomassa total; validação por análise de variância (teste F, 5%) contra os dois conjuntos de amostras [p. 3, 6].

## 5. Resultados principais
- Equação ajustada (de Bispo et al., 2020) com R² de 0,89, RMSE de 8,12 Mg·ha⁻¹ e bias de 0,43 Mg·ha⁻¹; alturas LIDAR de 1,7 a 38 m e biomassa aérea de 19 a 104 Mg·ha⁻¹ [p. 6].
- Conjunto do inventário (77 sítios): 12 locais excluídos por mudança de uso (2 por barragem, 9 para pastagem, 1 para agricultura); biomassa observada de 4,77 a 50,22 Mg·ha⁻¹ (média 24,54); estimada pelo modelo de 14,94 a 121,19 Mg·ha⁻¹ (média 62,93) — estimativas substancialmente maiores; F(1, 110) = 2,53, p < 0,05 [p. 10].
- Conjunto dos artigos (29 fragmentos): valores reportados de 3,9 a 184,10 Mg·ha⁻¹ (média geral 60,24); estimados de 14,94 a 152 Mg·ha⁻¹ (média 63,67), com alturas de 2 a 24 m; F(1, 54) = 0,77, p < 0,05, sem efeito significativo entre grupos — estimativas do modelo estatisticamente iguais às médias dos artigos [p. 10–11].
- Caso por fitofisionomia (mesma fazenda): Mata de Galeria observado 149,0 vs. estimado 152,44 Mg·ha⁻¹; Cerrado Típico observado 21,7 vs. estimado 39,9 Mg·ha⁻¹; arbustiva observado 17,6 vs. estimado 27,4 Mg·ha⁻¹ [p. 11–13].
- Fatores de expansão por estrutura (Tabela 4): arbustiva — AGB 4,4 ± 2,2 Mg·ha⁻¹, raízes 280% ± 94, serapilheira 93% ± 1,9, necromassa 1%, BGB:TotalAGB 2,36; savana — AGB 22,1 ± 6,2, raízes 60% ± 48, serapilheira 12% ± 0,1, necromassa 13%, BGB:TotalAGB 0,46; floresta — AGB 69,2 ± 25,1, raízes 27% ± 12, serapilheira 9% ± 0,1, necromassa 9%, BGB:TotalAGB 0,23 [p. 14].
- Exemplo de composição: floresta com 100 Mg·ha⁻¹ de biomassa aérea + 27 (raízes) + 9 (serapilheira) = 136 Mg·ha⁻¹ de biomassa total [p. 14].
- Resultados de raízes via fatores de expansão: 12,3 Mg·ha⁻¹ (arbustiva), 13,3 (savana) e 18,63 (floresta) [p. 14].
- Os fatores de expansão foram aplicados à biomassa aérea estimada para gerar mapas por compartimento (raízes, serapilheira e necromassa) e o somatório desses compartimentos gerou o primeiro mapa de biomassa total do Cerrado em pixels de 10 m [p. 1, 14–15].
- Formações arbustivas apresentaram maiores incertezas, por árvores isoladas e dossel baixo, em comparação com savanas e florestas [p. 1].

## 6. Limitações que os próprios autores reconhecem
- Amostragem insuficiente no norte do bioma (regiões de Alto Parnaíba e Paraná Guimarães), deixando lacunas [p. 15–16].
- Uso de altura de dossel do ano de 2020: as estimativas são mais indicadas para vegetação clímax de 2020; áreas com altura divergente (ex.: regeneração florestal) podem apresentar resultados viesados [p. 16].
- O modelo não distingue florestas nativas de plantadas e pode ser difícil de aplicar para estimar biomassa total por unidade de área contendo apenas vegetação nativa, pois foi calibrado para florestas nativas [p. 16].
- Variabilidade nas definições de diâmetro mínimo e de conceitos de árvore/arbusto nos estudos pode impactar a estimativa de biomassa aérea [p. 16].
- Parcelas medidas em datas antigas não mantiveram correlação linear com a estrutura estimada pelo modelo de 2020; fragmentos inventariados em 1993 diferiram significativamente do modelo [p. 16].
- Desvios de altura são mais influentes em dosséis de baixa altura: maiores incertezas e superestimações nas formações arbustivas [p. 1, 16].
- O compartimento subterrâneo de raízes foi o mais variável; a amostragem de necromassa não foi abordada nos inventários dos artigos revisados [p. 16].

## 7. O que serve ao projeto e o que não serve
- **Serve:** o método integral — canopy height model (GEDI + Sentinel-2, 10 m), equação alométrica com altura do dossel e fatores de expansão por estrato — é um caminho multisensorial replicável para estimar biomassa e estoque de carbono em pixels de 10 m no Cerrado, incluindo Goiás; o código no Google Earth Engine é aberto [p. 1, 6, 14, 17].
- **Serve:** as médias de biomassa aérea por fitofisionomia compiladas na revisão (ex.: Cerrado Típico de 12,88 a 108,40 Mg·ha⁻¹ e Cerradão de 18,40 a 131,40 Mg·ha⁻¹) e os fatores de expansão por estrato servem como valores de referência e validação para o levantamento em Goiás [p. 9–10, 14].
- **Não serve (diretamente):** o modelo distingue apenas formações nativas e não separa silvicultura de vegetação nativa; os próprios autores listam a distinção entre remanescentes nativos e atividades silviculturais como passo futuro [p. 16–17].
- **Não serve (para séries temporais):** a altura de dossel refere-se a 2020, limitando o monitoramento de mudanças e áreas em regeneração ou plantios recentes [p. 16].

## 8. Frases citáveis (literais)
- "This study presents, for the first time, the mapping of total biomass in 10 m pixels of all regions of the Cerrado biome." [p. 1]
- "A possible limitation of the methods employed in this study concerns the use of the canopy height information obtained from the year 2020, as described in [20]." [p. 16]
