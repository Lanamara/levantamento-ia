# RELATÓRIO — Elia Vangi (2021)

## 1. Referência
- Autores: Elia Vangi, Giovanni D'Amico, Saverio Francini, Francesca Giannetti, Bruno Lasserre, Marco Marchetti, Gherardo Chirici [p. 1]
- Ano: 2021 (recebido 31/12/2020, aceito 02/02/2021, publicado 08/02/2021) [p. 1]
- Título: The New Hyperspectral Satellite PRISMA: Imagery for Forest Types Discrimination [p. 1]
- Revista: Sensors (MDPI), vol. 21, artigo 1182 [p. 1]
- DOI: 10.3390/s21041182 [p. 1]
- O TEXTO.txt contém o artigo completo (19 de 19 páginas, incluindo referências), não está truncado.

## 2. Pergunta do estudo
O sensor hiperespectral PRISMA discrimina melhor tipos florestais do que o Sentinel-2 MSI, medido por análise de separabilidade espectral par a par em dois níveis de nomenclatura e quatro métricas?

## 3. Área e dados
- Local: duas áreas de 900 km² cada, na Itália central (42°53′N 11°6′E — Grosseto/Toscana; 43°17′N 12°13′E — Arezzo/Perugia, Toscana-Umbria) [p. 5]
- Período: cenas PRISMA L2D de 16/06/2019 e 04/06/2019; cenas Sentinel-2A L2A de 18/06/2019 e 13/06/2019 [p. 7]
- Sensores: PRISMA (239 bandas, 402–2497 nm, 30 m; 230 bandas usadas após remover a sobreposição VNIR/SWIR) [p. 7]; Sentinel-2A MSI (13 bandas, 440–2190 nm; bandas b1, b9 e b10 descartadas, demais reamostradas para 30 m) [p. 7]
- Referência: 161 polígonos digitalizados sobre imagens pancromáticas de 5 m do próprio PRISMA [p. 6]; 250 ha (78 polígonos) na Área 1 e 220 ha (83 polígonos) na Área 2 [p. 6]; identificação das espécies via base de uso e cobertura da Toscânia (malha de 250 × 250 m, 367.760 pontos) [p. 6]
- Contexto de disponibilidade: de 64.504 imagens PRISMA, com nuvem <10% e período vegetativo, só 23 estavam disponíveis na Itália (todas de 2019) [p. 4]

## 4. Método
- Conversão dos cubos PRISMA em formato adequado via pacote R `prismaread` e extração da reflectância de todos os pixels dentro dos 161 polígonos, para cada uma das 230 bandas (mesmo procedimento para Sentinel-2) [p. 8]
- Análise de separabilidade espectral par a par, banda a banda, com pacote R `spatialEco`, para todos os pares de classes [p. 8]
- Quatro métricas de separabilidade: M-statistic (M), Bhattacharyya distance (B), Jeffries–Matusita distance (JM) e transformed divergence (TD) [p. 8]
- Repetição em dois níveis de nomenclatura (nível 3 e nível 4 do Corine Land Cover, com dois grandes grupos e cinco tipos florestais) e cálculo do incremento percentual de PRISMA sobre Sentinel-2 pela métrica de melhor resultado em cada par de classes [p. 7–9]

## 5. Resultados principais
- Melhoria média declarada no resumo: +40% na discriminação coníferas vs. folhosas e +102% na discriminação entre cinco tipos florestais [p. 1]
- Nível 3, Área 1: par coníferas–folhosas separado por PRISMA com separabilidade média de 0.64 no azul (450–503 nm), contra 0.13 no SWIR (1613 nm, banda 11) do Sentinel-2 [p. 9]
- Nível 3, Área 2: coníferas e folhosas só distinguíveis em duas faixas (~1380 e 1830 nm) não sentidas pelo Sentinel-2; PRISMA atingiu 0.75 contra 0.43 do Sentinel-2 [p. 9]
- Nível 4, Área 1: separabilidade máxima de PRISMA entre 428 e 443 nm para o par Mediterranean coniferous–azonal formations (0.69), seguido de azonal formation–evergreen broadleaf (0.68); pares menos separáveis: Mediterranean coniferous–deciduous evergreen (0.40) e evergreen broadleaf–deciduous evergreen (0.39) [p. 9]
- Nível 4, Área 2: máxima separabilidade 0.74 para Mediterrâneas coníferas–folhosas sempre-verdes, em 1373/1822 nm (NIR/SWIR) [p. 9]
- Nas conclusões, os autores quantificam: PRISMA melhorou a separação coníferas vs. folhosas em 50% na Área 1 e 30% na Área 2; no nível 4, a separabilidade média foi 120% maior na Área 1 e 84% na Área 2 [p. 16]; na discussão citam melhorias médias >120% (Área 1) e 84% (Área 2), com máximos de 170% e 130% [p. 16]
- Dados hiperespectrais foram eficazes em discriminar tipos florestais nas duas áreas (separabilidade média normalizada >0.50 em 4 de 6 classes na Área 1 e em 9 de 10 pares de classes na Área 2) [p. 16]
- A zona SWIR foi a mais adequada para discriminação; também se destacaram o azul (Área 1, par folhosas–coníferas), o red edge e o NIR-plateau (Área 2) [p. 16]
- Única exceção: no nível 3 da Área 1, o Sentinel-2 MSI foi comparável ao PRISMA [p. 16]

## 6. Limitações que os próprios autores reconhecem
- Topografia complexa da Área 2 (encostas íngremes, até 120–140%) causou interferência de backscatter e aumentou a razão sinal-ruído das bandas estreitas [p. 15–16]
- Áreas de sombra, pela mistura de árvores altas e baixas, afetaram a análise de separabilidade e explicam parte das diferenças entre as áreas [p. 15]
- Efeitos de condições atmosféricas e de iluminação variáveis, pelo intervalo de tempo entre as aquisições das cenas dos dois sensores [p. 15]
- Baixo número de referências de campo, viés do observador e diferenças de tempo entre observação em campo e aquisição da imagem [p. 15]
- Complexidade estrutural da floresta mediterrânea e a fração de vegetação não fotossintética (casca, ramos, madeira) afetam a extração de assinaturas espectrais puras [p. 15]
- A limitação estatística do M-statistic, que vale zero quando as médias das duas classes são iguais [p. 8]

## 7. O que serve ao projeto e o que não serve
- Serve: a comparabilidade PRISMA vs. Sentinel-2 é um precedente direto para justificar o uso de dados hiperespectrais multissensoriais no projeto em Goiás — mostra quando o Sentinel-2 basta (classes agregadas) e quando o hiperespectral agrega (tipos por grupo de espécies) [p. 16]
- Serve: as quatro métricas de separabilidade (M, B, JM, TD) e o ganho percentual são uma estrutura replicável para pré-avaliar sensores antes da classificação de espécies; o artigo também indica que resolução espectral fina importa mais que resolução espacial fina [p. 8, 15]
- Não serve diretamente: o artigo não estima biomassa nem estoque de carbono — é análise de separabilidade de tipos florestais, sem modelos alométricos ou inventários de biomassa/carbono [não informado]
- Não serve diretamente: contexto é floresta mediterrânea (nativa e em talhadia) em duas cenas de 2019 na Itália central, com poucas imagens disponíveis na época (23 para toda a Itália com nuvem <10%) [p. 4]; aplicação a silvicultura comercial em Goiás não é tratada no artigo [não informado]

## 8. Frases citáveis (literais)
- "The PRISMA hyperspectral sensor, compared to Sentinel-2 MSI, allowed for a better discrimination in all forest types, increasing the performance when the complexity of the nomenclature system also increased." [p. 1]
- "The low number of field references, observer bias, and time differences between field observation and image acquisition could also influence the results." [p. 15]
