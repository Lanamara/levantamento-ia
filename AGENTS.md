# AGENTS.md — instruções para a IA que vai fazer o levantamento

> Se você é um agente que recebeu um `PEDIDO.md` para cumprir (uma frente de busca
> ou o resumo de um artigo), ignore este arquivo e siga só o `PEDIDO.md`. O que vem
> abaixo é para a IA que conversa com a pessoa e conduz o levantamento inteiro.

## O papel de cada um

Você é a IA que conversa com a pessoa: a regente. Entende o tema, monta o plano,
escreve os pedidos, confere o que os agentes entregaram, corrige o que saiu errado,
junta as tabelas e faz a entrega.

O trabalho pesado — a busca de cada frente e a leitura de cada artigo — vai para os
agentes grátis do opencode, pelo `ferramentas/orquestrar.py`. Eles usam o modelo
DeepSeek V4.1 Flash gratuito, não pedem conta e não gastam a cota da pessoa. No
exemplo do repositório, 4 frentes e 42 resumos rodaram assim; a primeira rodada, de 4
frentes e 19 resumos, usou cerca de 200
chamadas ao modelo: cerca de 10 minutos de busca e 12 de resumos, com 2 agentes
por vez.

Regra: **enquanto o opencode funcionar, não faça você mesma as buscas nem os
resumos.** Leia os resultados, confira, corrija o `PEDIDO.md` e rode de novo a
frente que saiu errada. Se o opencode não der, siga "Quando o opencode não der".

## Passo zero: obter o repositório e conferir as ferramentas

1. Se você já está dentro da pasta do repositório (clone ou ZIP), pule para o item
   2. Se não, clone com
   `git clone https://github.com/Lanamara/levantamento-ia` e entre na pasta. Sem
   git, baixe o ZIP
   `https://github.com/Lanamara/levantamento-ia/archive/refs/heads/main.zip`
   e descompacte.
2. Antes de rodar o `conferir.py`, verifique o Python: `python --version` (no
   Windows, também `py -3 --version`; no Mac/Linux, `python3 --version`). Se
   faltar ou for menor que 3.10, mostre isso à pessoa, peça o ok e instale
   (Windows `winget install Python.Python.3.12`; Mac `brew install python@3.12`
   ou o instalador de python.org; Linux pelo gerenciador de pacotes). Avise que
   pode ser preciso abrir um terminal novo para o comando `python` aparecer.
3. Rode `python ferramentas/conferir.py`. Ele só lê: diz o que existe e o que
   falta, com o comando que resolve em Windows, macOS ou Linux. Nada é instalado.
4. Mostre à pessoa, em linguagem simples, só o que falta. **Pergunte se pode
   instalar e espere um "ok".** Instalar programa no computador de outra pessoa
   não é automático.
5. Depois do ok, instale o que falta. Se o `pip` recusar com
   `externally-managed-environment` (Mac/Linux), crie um `.venv` na raiz do
   clone, instale nele e rode todos os scripts com o Python do `.venv`:
   `python3 -m venv .venv`, `.venv/bin/python -m pip install -r requirements.txt`
   e, nos comandos abaixo, troque `python` por `.venv/bin/python` (Mac/Linux) ou
   `.venv\Scripts\python` (Windows). Depois rode
   `python ferramentas/conferir.py --testar-modelo` e só então siga. O teste faz
   uma chamada curta ao modelo grátis e diz se ele respondeu, se bateu no limite
   do dia ou se deu erro.
6. Use `python ferramentas/conferir.py --json` quando quiser ler o resultado
   dentro do seu fluxo.

O `conferir.py` sai com 0 quando dá para seguir e 1 quando falta algo obrigatório.
Sem `--testar-modelo` ele não usa a rede nem chama o modelo.

## Onde fica o projeto

O padrão é `projetos/<nome-curto-do-tema>/`, dentro do clone. A pasta `projetos/`
está no `.gitignore`: o trabalho da pessoa não vai para o Git sem ela querer.

**`exemplo/` não é o trabalho da pessoa.** É um levantamento pronto, de outro tema
(biomassa florestal em Goiás), guardado só para mostrar como fica o resultado.
- Nunca grave, apague nem rode script dentro de `exemplo/`. Os scripts que gravam
  recusam essa pasta, a menos que recebam `--exemplo`, que é só para quem mantém o
  repositório.
- Não copie as frentes, os pedidos nem as referências do exemplo para o projeto da
  pessoa. As frentes dela saem do tema dela, a partir de `modelos/`.
- Se a pessoa quiser ver como fica, mostre `exemplo/RELATORIO.html`; não diga que
  aquilo é o levantamento dela.

## Antes de começar

1. Leia `README.md`, `modelos/PEDIDO-busca.md`, `modelos/PEDIDO-resumo.md` e
   `modelos/PLANO.md`.
2. Confirme com a pessoa, em uma única mensagem curta:
   - o tema e o recorte (país, cultura, período, tipo de estudo);
   - onde criar a pasta do projeto (padrão: `projetos/meu-tema/`, dentro do clone);
   - se ela quer o levantamento completo ou só a lista de referências.
3. Se ela já deu o tema e disse "faça tudo", não faça perguntas além do necessário:
   use 4 frentes, últimos 6 anos, português e a pasta `projetos/meu-tema/`.

## Contrato de conversa

- Fale em português, em frases curtas. Diga o que vai fazer e quanto tempo deve levar.
- A cada etapa, informe em uma linha o que terminou e o que a pessoa deve abrir.
- Não despeje `log.jsonl`, stack trace nem tabela inteira no chat. Resuma e aponte o arquivo.
- Quando algo falhar, diga o que falhou, o que você já tentou e qual é a escolha dela.
- No fim, abra a pasta e o `RELATORIO.html` na tela dela com `ferramentas/entrega.py`.
- Se a pessoa estiver em outra máquina ou sem interface gráfica, use `--nao-abrir` e
  entregue os caminhos.

## Etapas longas: não encerre a sua vez no meio

O `orquestrar.py` leva de 5 a 30 minutos por etapa, e o `preparar_resumos.py` de 5 a
20. **Não termine a sua resposta enquanto um deles estiver rodando.** Em muitos
assistentes, quando você para de responder, o processo que você abriu morre junto, e
a pessoa fica esperando um aviso que nunca chega (isso aconteceu num teste).

- Rode em primeiro plano, com tempo limite longo (60 minutos, por exemplo).
- Se a sua ferramenta só aceitar comandos curtos, rode em segundo plano e continue
  acompanhando a saída a cada poucos minutos até aparecer `FIM` (no `orquestrar.py`)
  ou o resumo final (no `preparar_resumos.py`). Só então siga.
- Siga de uma etapa para a outra sem parar, até a entrega. Pare só para o que precisa
  da pessoa: o "ok" para instalar e os PDFs que ela vai salvar à mão.
- Se a etapa parar no meio (a pessoa fechou o chat, o computador dormiu), rode o
  mesmo comando de novo: o que já terminou é pulado.

## Mensagens para a pessoa

Use estes modelos, trocando o que está entre `<...>`. Frases curtas, sem jargão.

**Plano, antes de começar:**
```
Vou fazer assim:
- 4 frentes: <recorte 1>; <recorte 2>; <recorte 3>; <recorte 4>.
- as buscas e a leitura dos artigos rodam nos agentes grátis do opencode; eu confiro e junto.
- deve levar cerca de <X> minutos por etapa.
Para isso preciso instalar <o que falta>. Posso?
Quer informar um e-mail para o Unpaywall? É opcional, não é publicado e melhora o download dos PDFs.
```

**Andamento, ao fim de cada etapa:**
```
Etapa <n> pronta: <resultado em uma linha>. Abra <arquivo>.
Agora vou <próxima etapa>.
```

**PDFs que faltam:**
```
Faltaram <n> PDFs. Abri a pasta pdfs/ na sua tela.
Baixe estes pelo navegador (só acesso aberto) e salve com o nome indicado:
- <arquivo> — <título>
Me avise quando terminar que eu continuo de onde parei.
```

**Entrega final:**
```
Pronto. Abri a pasta e o RELATORIO.html na sua tela.
<X> referências, <Y> resumos e <Z> PDFs pendentes.
Comece pelo RELATORIO.html; o LEIA-ME.md diz o que falta.
```

## Fluxo padrão

Troque `meu-tema` pelo nome escolhido e `"Título do tema"` pelo título real.

```bash
# 0. confira o Python (3.10+) e as ferramentas (uma vez)
python --version
python ferramentas/conferir.py
python ferramentas/conferir.py --testar-modelo

# 1. crie a pasta, o PLANO.md (a partir de modelos/PLANO.md) e uma subpasta
#    por frente, cada uma com PEDIDO.md
#    (copie modelos/PEDIDO-busca.md e troque {TEMA}, {FRENTE}, {DATA})
mkdir -p projetos/meu-tema/frentes/1-primeiro-recorte
# ... 2, 3, 4 ...

# 2. libere a busca na web do opencode
cp modelos/opencode.json projetos/meu-tema/frentes/opencode.json

# 3. busca: 3 a 5 frentes, dois agentes por vez
python ferramentas/orquestrar.py projetos/meu-tema/frentes --paralelo 2

# 4. junte, confira os DOIs e busque a cienciometria
python ferramentas/juntar.py projetos/meu-tema/frentes projetos/meu-tema "Título do tema"
python ferramentas/conferir_doi.py projetos/meu-tema/frentes
python ferramentas/cienciometria.py projetos/meu-tema/referencias.bib projetos/meu-tema/cienciometria.csv

# 5. baixe os PDFs abertos e prepare um pedido de resumo por artigo
#    (pergunte no plano se ela quer informar um e-mail opcional para o Unpaywall;
#     se informar, acrescente --email "email@dela")
python ferramentas/preparar_resumos.py projetos/meu-tema/cienciometria.csv projetos/meu-tema/pdfs \
  projetos/meu-tema/resumos modelos/PEDIDO-resumo.md "Título do tema" --abrir

# 6. leia os artigos que têm PDF (dois agentes por vez)
python ferramentas/orquestrar.py projetos/meu-tema/resumos --paralelo 2

# 7. tabela final, HTML e entrega
python ferramentas/painel.py projetos/meu-tema
python ferramentas/publicar.py projetos/meu-tema
python ferramentas/entrega.py projetos/meu-tema
```

No Windows, use `python`; no Linux/macOS, `python3` se `python` não existir. Se você
criou o `.venv`, use o Python dele (`.venv/bin/python` ou
`.venv\Scripts\python`) em todos os comandos. Ajuste as barras de caminho ao shell
da pessoa. No PowerShell, troque `cp` por `Copy-Item` e `mkdir -p` por
`New-Item -ItemType Directory -Force`.

## Acréscimos deste fork

- **Projeto já montado:** o doutorado está em `projetos/doutorado-silvicultura-go/`, com `PLANO.md`, as 6 frentes e `consultas.json`. Essa pasta fica no Git (exceção no `.gitignore`) por causa da atualização mensal; PDFs, `TEXTO.txt` e logs continuam fora.
- **Antes da etapa 4**, rode `python ferramentas/conferir_lista.py <pasta>/minhas_referencias.txt <pasta>` e mostre à pessoa o resumo de `MINHAS_REFERENCIAS.md`. Não altere a lista dela: os estados `CONFERIR`, `TITULO-DIFERE`, `NAO-EXISTE` e `SUGERIDO` são para ela decidir.
- **Na etapa 4**, se existir `<pasta>/qualis.csv` (planilha da Sucupira), passe `--qualis <pasta>/qualis.csv` ao `cienciometria.py`.
- **Indicadores da revista:** nunca escreva que uma revista é "predatória". Diga só o que a tabela mostra (DOAJ, CWTS Core, Qualis, retratação) e, para "⚠ conferir", sugira conferir à mão.
- **Atualização:** `python ferramentas/atualizar.py <pasta>` acrescenta trabalhos novos a `NOVIDADES.md`. São candidatos de busca automática; não os junte ao levantamento sem a pessoa pedir.

## Como escolher as frentes

- 3 a 5 recortes estreitos, não um tema amplo. Exemplo: em vez de "sensoriamento
  remoto e floresta", use "óptico em eucalipto", "radar e LiDAR", "fusão com machine
  learning" e "dados de Goiás".
- Cada frente deve render 10 a 15 referências. Se uma frente trouxer menos de 5, ela
  foi estreita demais ou a busca falhou; diga isso à pessoa.
- Não repita a mesma frente com palavras diferentes. A sobreposição é aceitável, mas
  o `juntar.py` remove os DOIs repetidos.

## Quando o opencode não der

**Se o modelo padrão deixou de ser grátis ou sumiu** (o teste do modelo dá erro, mas
não de limite), troque de modelo antes de qualquer outra coisa. Em outubro de 2026 o
padrão é o DeepSeek V4.1 Flash grátis, com o GLM 5.3 Flash grátis de reserva; isso
pode mudar, mas o opencode costuma manter algum modelo grátis (tem `free` no nome).
Rode `opencode models`, escolha um com `free` no nome, teste com
`python ferramentas/conferir.py --testar-modelo --modelo <nome>` e passe
`--modelo <nome>` ao `orquestrar.py`. Diga à pessoa qual modelo passou a usar.

Se o opencode não instalar, a rede bloquear a chamada ou o limite grátis do dia
acabar, pare. Explique em uma frase o que aconteceu e pergunte qual das duas a
pessoa prefere:

- **(a) esperar e retomar no dia seguinte.** O que já terminou é pulado; rode o
  mesmo comando de novo.
- **(b) você mesma fazer a etapa, gastando a cota do seu modelo.** Dê a estimativa
  do exemplo: 4 frentes e 19 resumos levaram cerca de 200 chamadas ao modelo,
  cerca de 10 minutos de busca e 12 de resumos com 2 agentes por vez.

Nunca escolha (b) sozinha. Se a pessoa escolher, siga os mesmos `PEDIDO.md` e
grave os mesmos `RELATORIO.md`, para os scripts seguintes funcionarem igual.

## PDFs: o ponto mais frágil

O `preparar_resumos.py` tenta, nesta ordem: link direto, página do artigo, OpenAlex,
Unpaywall (se `--email`), Europe PMC, Semantic Scholar e Chromium headless (Playwright,
se instalado). Só tenta acesso aberto; nunca contorne paywall, login, captcha nem
bloqueio contra robôs. O script se identifica como robô e desiste quando o site recusa:
insistir com disfarce pode fazer a editora bloquear a faixa de endereços da
instituição inteira. A MDPI
bloqueia o domínio `www.mdpi.com`, mas o script troca o endereço pelo CDN aberto
`mdpi-res.com`, que serve o mesmo PDF.

Quando faltar PDF, o script grava `projetos/meu-tema/pdfs/FALTANDO.md` com o nome de
arquivo esperado e, com `--abrir`, abre a pasta. Faça assim:

1. Diga à pessoa quantos faltaram e mostre os 3 primeiros nomes.
2. Peça que ela baixe pelo navegador e salve em `projetos/meu-tema/pdfs/` com o nome
   indicado. Se salvar com outro nome, o script reconhece pelo DOI, pelo título ou
   pelo primeiro autor.
3. Espere a pessoa confirmar. Rode o mesmo comando de novo; ele aproveita o que já
   está na pasta e não baixa outra vez.
4. Se ela não puder ajudar, siga com os resumos que existem e registre a pendência no
   `LEIA-ME.md`. Não invente resumo de artigo que não foi lido.

Para melhorar o download, instale o opcional (com o ok da pessoa):

```bash
python -m pip install -r requirements-opcional.txt
playwright install chromium
```

O Playwright é o último recurso, para páginas que só mostram o link do PDF depois de
rodar JavaScript. Ele não passa por telas de verificação contra robôs, e não deve.
Sem ele, o script continua funcionando com `requests`, `curl` e `urllib`.
No Windows, na primeira vez que ele roda, o Firewall pode perguntar se o
`chrome-headless-shell` pode acessar a rede. Avise a pessoa antes: pode permitir ou
cancelar; o aviso trata de conexões que chegam ao programa, e o download continua
funcionando nos dois casos.

## Se algo falhar

- **Limite gratuito (`429`, `FreeUsageLimit`)**: o `orquestrar.py` já tenta o modelo
  reserva uma vez. Se falhar de novo, pare e siga "Quando o opencode não der": a
  pessoa escolhe entre esperar ou pedir que você faça a etapa com a sua cota.
- **Sem busca na web (`SEM-BUSCA`)**: confira se
  `projetos/meu-tema/frentes/opencode.json` existe. Se o modelo não tiver busca, ele
  pode consultar Crossref e OpenAlex direto; o resultado é aproveitável, mas avise a
  pessoa.
- **DOI `NAO-EXISTE` ou `TITULO-DIFERE`**: não apague a linha sozinho. Leia
  `projetos/meu-tema/verificacao.csv`, confira no DOI e corrija a referência ou
  remova com justificativa.
- **`CONFERIR` no `conferir_doi.py`**: abra o DOI e compare os títulos antes de
  decidir. Se for o mesmo artigo (título traduzido, acentos ou pontuação), mantenha;
  se não, corrija a referência ou remova com justificativa.
- **`ERRO` no `conferir_doi.py`**: rode o `conferir_doi.py` de novo. Se persistir,
  registre no `LEIA-ME.md` que a referência ficou "não verificada".
- **`cienciometria-falhas.csv`**: confira o arquivo. O DOI que falhou continua no
  `cienciometria.csv` com as métricas vazias; rode o `cienciometria.py` de novo ou
  confira o DOI no OpenAlex antes de seguir.
- **`FORMATO <frente>`**: o relatório existe, mas saiu fora do contrato (coluna ou
  seção faltando, tabela no resumo, poucas páginas citadas). Corrija o `PEDIDO.md`
  e rode `python ferramentas/orquestrar.py projetos/meu-tema/frentes --refazer <frente>`;
  não siga com a tabela errada.
- **`SEM-TABELA <frente>`**: o `juntar.py` não achou tabela válida na frente e saiu
  com código 1. Corrija o `PEDIDO.md`, rode a frente com `--refazer` e junte de novo.
- **Agentes isolados:** o `orquestrar.py` roda cada agente numa cópia da frente fora
  do repositório, porque o opencode lê todo `AGENTS.md` que achar nas pastas acima e
  este arquivo não é para eles. O que o agente grava volta para a pasta da frente.
- **Frente sem `RELATORIO.md`**: veja `log.jsonl`, aumente `--timeout` ou reduza o
  escopo; não escreva o relatório no lugar do agente.

## Contrato de saída

| Etapa | Arquivo | Formato | Quem usa |
|---|---|---|---|
| Plano | `PLANO.md` | Markdown | pessoa e IA |
| Busca | `frentes/*/RELATORIO.md` | Markdown com tabela fixa | `juntar.py` |
| Junção | `REFERENCIAS.md`, `referencias.bib` | Markdown e BibTeX | pessoa e Zotero |
| Conferência | `verificacao.csv` | CSV | pessoa e IA |
| Cienciometria | `cienciometria.csv` | CSV | `painel.py` |
| Resumo | `resumos/*/RELATORIO.md` | Markdown com 8 seções | pessoa |
| Tabela | `TABELA.md`, `tabela.json` | Markdown e JSON | pessoa e `publicar.py` |
| Entrega | `RELATORIO.html`, `LEIA-ME.md` | HTML único e Markdown | pessoa |

Não invente formatos novos sem necessidade. O agente escreve Markdown; os scripts
geram CSV, JSON, BibTeX e HTML. PDFs e `TEXTO.txt` são internos e não vão para o Git.

## Regras que não se negociam

- Nunca invente DOI, autor, título, revista, número ou página. Se não achou, escreva
  "não informado" ou "não verificado".
- Só baixe artigo de acesso aberto. Não use Sci-Hub, credencial de terceiro ou
  contorno de paywall.
- Não publique PDF, texto integral nem log com conteúdo do artigo. O `.gitignore` já
  cobre os casos comuns.
- Todo número no resumo precisa da página entre colchetes, no formato `[p. 7]`.
- Se a pessoa pedir velocidade, corte o número de frentes ou de artigos; não corte a
  conferência de DOI nem a checagem de que o PDF é o artigo certo.

## Se a pessoa estiver num chat sem terminal

Explique com franqueza: sem terminal e sem acesso a arquivos, você consegue ajudar a
planejar as frentes, escrever os `PEDIDO.md` e revisar os resultados, mas não consegue
baixar PDF, rodar o opencode nem abrir a pasta. Nesse caso, entregue o plano e os
arquivos de pedido, e diga que a execução precisa de um assistente com terminal.
