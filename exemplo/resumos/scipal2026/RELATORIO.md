# RELATÓRIO — Scipal et al. (2026), missão BIOMASS

> Observação: as páginas entre colchetes seguem as marcas `[página N]` do TEXTO.txt (página 1 = capa/folha de citação; página 2 = p. 220 da revista).

## 1. Referência

SCIPAL, K.; ALBINET, C.; CACCIA, M.; CARBONE, A.; CARVALHAIS, N.; CHAVE, J.; DALL, J.; FEHRINGER, M.; LEANZA, A.; LE TOAN, T.; MALIK, M.; NOVELLI, A.; PAILLOU, P.; PAPATHANASSIOU, K. P.; PATTERSON, J.; PINHEIRO, M.; QUEGAN, S.; REICHSTEIN, M.; ROMMEN, B.; SAATCHI, S.; SHUGART, H. H.; SIMON, T.; TEBALDINI, S.; ULANDER, L. M. H.; VALENTINO, A.; WILLEMSEN, P.; WILLIAMS, M. **BIOMASS: ESA's P-Band SAR Mission.** *Proceedings of the IEEE*, v. 114, n. 2, p. 220–235, fev. 2026. DOI: 10.1109/JPROC.2026.3687416. [p. 1]

## 2. Pergunta do estudo

Não é um estudo com pergunta experimental: o artigo descreve o status pré-lançamento e a arquitetura da missão BIOMASS, ou seja, como um SAR em banda P em órbita pode medir biomassa acima do solo, altura de floresta e distúrbio florestal com acurácia sem precedentes [p. 2].

## 3. Área e dados

- **Local:** global — florestas entre 75°N e 56°S [p. 9]. Nenhum sítio específico; Goiás, Cerrado ou silvicultura não são mencionados em nenhuma página.
- **Período:** satélite lançado em 29/04/2025 [p. 2]; comissionamento de ~6 meses [p. 7]; fase tomográfica (TOM) iniciada em 21/11/2025 por 18 meses, seguida da fase interferométrica (INT) de 42 meses, totalizando 5 anos de vida operacional [p. 8].
- **Sensores/fontes:** SAR de abertura sintética em banda P, 435 MHz, totalmente polarimétrico, 6 MHz de banda, refletor de 12 m [p. 5]; processamento Pol-InSAR e TomoSAR [p. 2]; Copernicus DEM como insumo do processador L1c [p. 10]; transponder de calibração BCT em solo [p. 6]–[p. 7]; validação prevista com o projeto GeoTrees (censo florestal, lidar aerotransportado e terrestre) [p. 11].
- **Número de amostras:** não informado (o artigo não apresenta amostra de campo própria). O único número de sítios citado é o planejamento de 100 sítios de referência do GeoTrees [p. 11].

## 4. Método

1. **Instrumento:** SAR de faixa (stripmap) olhando à esquerda, banda P (435 MHz), largura de banda de 6 MHz, cadeia completa de transmissão/recepção polarimétrica (H e V), refletor dobrável de ~12 m, potência de pico de 90 W [p. 5]; três faixas imageadas por rolagem da plataforma, com larguras de 51,1 / 54,5 / 52,0 km [p. 6].
2. **Aquisição em duas fases:** TOM (18 meses) com pilha interferométrica de 7 imagens por ponto; INT (42 meses) com pilha de 3 imagens; repetição temporal de 3 dias entre imagens da pilha, manobras de rolagem para as 3 faixas e manobra de reposicionamento (SRM) para cobrir o globo [p. 8]–[p. 9].
3. **Recuperação dos parâmetros:** altura de floresta por Pol-InSAR/TomoSAR em pilha de 3 imagens e biomassa (AGBD) por cancelamento do sinal de solo ("ground notch") a partir da pilha, com decomposição SKP e calibração de fase [p. 10]–[p. 11].
4. **Calibração e processamento:** calibração externa com o transponder BCT e alvos distribuídos, correção de rotação de Faraday e de distorções de fase ionosféricas, cadeia L1a/L1b/L1c/L2a/L2b/L3 com o BIOMASS Processing Suite (BPS), em código aberto [p. 6], [p. 9]–[p. 10].

## 5. Resultados principais

- Alvo de acurácia: **20% para AGBD e altura de floresta em resolução de 4 ha** [p. 4]; a literatura de base da missão indica **20%–30%**, comparável a observações de campo [p. 4].
- Produtos: AGBD e altura em **200 × 200 m**; distúrbio florestal (FD) em **50 × 50 m**; produto L1b em **50 × 50 m** [p. 11]; síntese final em 200 × 200 m e 50 × 50 m [p. 12].
- Órbita: **666 km** de altitude média, inclinação **97,97°**, LTAN **06:00**, **14 + 2/3** revoluções/dia, ciclo quase-repetitivo de **3 dias**, trilha controlada em **10%** da linha de base crítica (**≈ ±480 m**) [p. 7].
- Pilhas: **7 imagens** (TOM) e **3 imagens** (INT), repetição de **3 dias**; linha de base de **0,87 km (15%)** no TOM, com altura de ambiguidade de **160 m** e resolução vertical de **25 m**; **1,49 km (30%)** no INT, com ambiguidade de **100 m** [p. 8].
- Ciclos: ciclo maior (MC) de **63 dias** (TOM) e **27 dias** (INT); ciclo global (GC) de **504 dias** (TOM) e **273 dias** (INT) [p. 8]–[p. 9].
- Cobertura: **uma** cobertura global com pilhas tomográficas e **cinco** com pilhas interferométricas nos 5 anos [p. 9].
- Desempenho: **todos os objetivos de desempenho foram atingidos e superados** ao fim do comissionamento [p. 6]; porém o PSLR entre faixas (requisito **−16 dB**) não é conforme na borda próxima do Swath 1 e o desequilíbrio de canal (requisito **−25 dB**) não é conforme a 3 sigma [p. 6].
- Aplicações secundárias: gelo de até **120 m** de espessura mapeado com TomoSAR aerotransportado em banda P [p. 12]; penetração no subsolo desértico **> 5 m** [p. 12]; ionosfera observada a cada **2 h** [p. 12].

## 6. Limitações reconhecidas pelos autores

- **Desequilíbrio de canal fora do requisito** de 3 sigma, crítico para o desempenho polarimétrico, mitigado por compensação via medidas sobre o BCT e alvos distribuídos; **PSLR** não conforme na borda do Swath 1, considerado não crítico [p. 6].
- **Restrição de cobertura:** a missão não pode operar na linha de visada dos radares SOTR do Departamento de Defesa dos EUA, o que exclui basicamente América do Norte e Europa; os autores avaliam que isso não compromete os objetivos [p. 9].
- **Plano de aquisição quase congelado:** o esquema de pilhas com repetição de 3 dias não permite inserir restrições adicionais, como observar alvos em janelas temporais ou estações específicas [p. 9].
- **Cobertura incompleta da Antártica** durante o comissionamento, por causa da necessidade de observar o BCT [p. 8].
- **Produto L3 ainda em desenvolvimento**, a ser validado com dados reais apenas ao fim da segunda cobertura global, por volta do fim de 2027 [p. 10]; o modelo de produção do L3 está "em consolidação" [p. 11].
- **Linhas de base definidas no equador**, reduzindo com a latitude [p. 8].

## 7. O que serve ao projeto e o que não serve

1. **Serve** como referência metodológica de ponta para estimar AGBD e altura por banda P (Pol-InSAR e TomoSAR), com a meta de 20% em 4 ha e produtos de 200 m / 50 m — parâmetros úteis para dimensionar o que esperar de sensores de baixa frequência [p. 4], [p. 11].
2. **Serve** pela política de dados: L1, L2 e L3 gratuitos e abertos no ESA Earth Observation Gateway, em COG/STAC, e processador BPS em código aberto — candidatos a fonte de dados e a base de código para o projeto [p. 10]–[p. 11].
3. **Não serve** como evidência empírica local: o artigo não traz Goiás, Cerrado, eucalipto, silvicultura plantada, estoque de carbono medido, nem qualquer amostra de campo; é descrição de missão, sem validação com dados reais [p. 2], [p. 11].
4. **Não serve** para desenho amostral ou aquisição sob demanda: a resolução de 200 m é grossa para talhão e o plano de aquisição é quase congelado, sem escolha de data ou estação, o que inviabiliza acompanhar ciclos silviculturais curtos [p. 9], [p. 11].

## 8. Frases citáveis

1. "BIOMASS will deliver estimates of FH and above-ground biomass at 200 × 200 m2 resolutions and loss dynamics at 50 × 50 m2 resolution for the largely underobserved and vulnerable forest areas worldwide." [p. 12]
2. "The science driver of BIOMASS is the role of forest in the Earth's carbon cycle, but this has naturally led to the mission using pioneering space technology, advanced instrumentation, and innovative methods." [p. 12]
