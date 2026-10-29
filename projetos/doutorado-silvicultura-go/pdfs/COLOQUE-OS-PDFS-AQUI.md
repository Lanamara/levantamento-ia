# Coloque os PDFs aqui

O script tenta baixar sozinho os artigos de acesso aberto. Quando o site bloqueia,
ele grava a lista do que faltou em `FALTANDO.md`, com o nome de arquivo que você deve usar.

1. Baixe o PDF pelo navegador (só artigos de acesso aberto).
2. Salve nesta pasta com o nome da coluna **Arquivo** de `FALTANDO.md`
   (ex.: `silva2020.pdf`). Se salvar com outro nome, o script tenta reconhecer
   pelo DOI, pelo título ou pelo primeiro autor.
3. Rode o mesmo comando do `preparar_resumos.py` de novo. Ele aproveita os PDFs
   que já estão aqui e não baixa de novo.

Os PDFs e o texto integral não vão para o Git; só os resumos são publicados.
