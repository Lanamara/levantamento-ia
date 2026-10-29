# RELATÓRIO — Raiany Cristina Ribeiro Santos (2023)

## 1. Referência

SANTOS, Raiany Cristina Ribeiro; SANTOS, Amiel Araujo Soares; ROMÃO, Patrícia de Araújo; OLIVEIRA, Ivanilton José de. **Vulnerabilidade ambiental e a potencialidade à perda de solos no entorno de atrativos turísticos em paisagens do Cerrado, na bacia hidrográfica do rio Caiapó, Caiapônia (GO) – Brasil.** *Agua y Territorio*, n. 23, p. 123–135, jan.–jun. 2024. DOI 10.17561/at.23.7325.

- O DOI confere com o pedido e o `TEXTO.txt` está completo (p. 123–135, incluindo referências). Não há truncamento.
- O texto recebeu o artigo em 29/09/2022 e o aceitou em 14/07/2023; o fascículo em que foi publicado é de 2024. O rótulo "2023" do pedido corresponde ao ano de aceite.
- As páginas citadas abaixo seguem as marcas `[página N]` do `TEXTO.txt`; a página impressa do fascículo é N + 122.

## 2. Pergunta do estudo

Qual é a vulnerabilidade ambiental à perda de solos e a potencialidade à erosão laminar na alta bacia do rio Caiapó (Caiapônia, GO), incluindo o entorno de nove atrativos turísticos?

## 3. Área e dados

- Local: alta bacia do rio Caiapó, porção coincidente com o município de Caiapônia (sudoeste de Goiás), a ~318 km de Goiânia; altitudes de 476 a 1.044 m [p. 3].
- Período: não informado para o estudo como um todo; o uso e cobertura vem do MapBiomas 5.0 referente a 2020 [p. 10].
- Sensores/fontes: SRTM (30 m) via SIEG/IMB e USGS para MDE, declividade, HAND e densidade de drenagem [p. 5–6]; pedologia vetorial da Emater [p. 4]; geologia da SIC [p. 6]; uso e cobertura do MapBiomas 5.0 [p. 6]; drenagem vetorial do IBGE em 1:100.000 [p. 7].
- Amostras: não informado — não há amostragem de campo nem pontos de treinamento; o trabalho é de álgebra de mapas em ArcGIS 10.3 e TerraViewHidro 0.0.4 [p. 6–7].
- Área total: não informada; a soma das classes do Quadro 11 é de aproximadamente 4.273 km² [p. 11].

## 4. Método

- Mapa de potencialidade à erosão laminar (Salomão et al., 2012): erodibilidade (tipos de solo), declividade (0–6%, 6–12%, 12–20%, >20%), suscetibilidade e uso e cobertura; classes de potencial alto, médio e baixo [p. 4–5].
- Mapa de vulnerabilidade ambiental à perda de solos (Crepani et al., 2001): média de cinco temas — geologia, geomorfologia, solos, uso e cobertura (no lugar de vegetação) e clima [p. 5–6].
- Geomorfologia obtida pela média de declividade, HAND (substituindo amplitude altimétrica) e densidade de drenagem (substituindo dissecação horizontal) [p. 7].
- Produtos em SIG por união de vetores, reclassificação e "Calculadora de campo"; clima fixado em 1,6 para toda a bacia [p. 5–8].

## 5. Resultados principais

- 74,47% da área na classe "Medianamente Estável/Vulnerável" (médias 1,8–2,2), o que corresponde a "mais de 70% de ocorrência" [p. 11; p. 1].
- 15,03% em "Moderadamente Vulnerável" (2,3–2,5), 10,41% em "Moderadamente Estável" (1,4–1,7) e 0,09% em "Estável" (1,2–1,3) [p. 11].
- Amplitude altimétrica de 476 a 1.044 m; predomínio de relevo plano (0–6%), com declividades >20% em pequenas porções [p. 8].
- Desníveis do modelo HAND predominantes até 48,5 m, associados à classe medianamente estável/vulnerável [p. 10].
- Erodibilidade muito alta expressiva, em Cambissolo e Neossolo Quartzarênico; Latossolos ao noroeste como baixa erodibilidade [p. 8].
- "Expressiva parte da área" com classes muito a extremamente suscetíveis, abrangendo quase metade da área no entorno dos atrativos [p. 8].
- A maior parte dos atrativos turísticos está em área de alto potencial à erosão laminar [p. 8].
- Vulnerabilidade cresce com pastagem, cana, soja, outras lavouras temporárias e infraestrutura urbana; os menores graus ficam nos pequenos remanescentes de vegetação natural [p. 11].

## 6. Limitações que os próprios autores reconhecem

- A densidade de drenagem "aparentemente não refletiu a dissecação existente na área, talvez por causa da escala da fonte dos dados" [p. 10].
- O tema clima foi representado por um único valor (1,6, correspondente a 175–200 mm), adotado de estudo da bacia vizinha do rio do Peixe [p. 5; p. 8].
- Os autores ressalvam que, onde os Latossolos têm textura média, a erodibilidade é maior e a resistência ao processo diminui [p. 8].
- Concluem que são necessários mais estudos na região [p. 12].

## 7. O que serve ao projeto e o que não serve

- **Serve:** o encadeamento em SIG (SRTM 30 m + MapBiomas + pedologia + geologia, por álgebra de mapas) é replicável para áreas de silvicultura em Goiás com dados gratuitos e sem trabalho de campo.
- **Serve:** a tabela de pesos de uso e cobertura distingue "Floresta Plantada" (1) de "Pastagem" (3) e de "Soja" (3), útil para separar silvicultura de pasto e de lavoura em modelos de fragilidade [p. 6].
- **Serve:** o diagnóstico de fragmentação e expansão agropecuária no sudoeste goiano e o recorte por entorno de atrativos, como contextualização regional.
- **Não serve:** não há biomassa, estoque de carbono, dados espectrais multissensoriais nem validação de campo; os pesos são ordinais definidos por literatura, sem calibração estatística ou medida de acurácia.

## 8. Frases citáveis (literais)

- "Os resultados mostraram a maior parte da área composta por pastagens, associadas à extrema suscetibilidade à erosão, em coincidência espacial com a classe vulnerabilidade ambiental “Medianamente Estável/Vulnerável”, com mais de 70% de ocorrência." [p. 1]
- "Quanto aos atrativos, a maior parte encontra-se em área de alto potencial à erosão laminar." [p. 8]
