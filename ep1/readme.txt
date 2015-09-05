Objetivo:
    Usar os dados do experimento com o cronometro para
criar uma projeçao para n pontos. Com esta projecao,
comparar com os resultados obtidos com o celular.

Detalhes:
    * Geral *
    - Travessia 1 e 2 sao simulacoes de MU e as
travessias 3 e 4 sao simulacoes de MUV.
    - Os pontos que serao usados na projecao serao
salvos na lista denominada "entrada"

    * Cronometro *
    - Cada travessia esta salva em uma tupla,
a qual foi digitada manualmente. Os nomes sao
"travessia1" e assim por diante.
    - Distancia entre cada sensor entre si e de
4m cada, totalizando 12m percorridos.
    - Caso haja um dado de valor -1, isto indica
que houve falha no sensor. Sera usado portanto o
valor do sensor do outro lado neste caso;
    (pensar em como fazer isso automaticamente)

    * Simulacao *
    - Cada simulacao recebe uma tupla com os dados
do cronometro e uma lista dos instantes dos pontos
a simular. Esta lista sera alterada em dois passos:
    1. Observando o grafico, anota-se o valor em que
o movimento foi observado e retiramos os pontos antes
deste instante; do mesmo modo retiramos os pontos
apos o final do movimento. Esta etapa e feita manual-
mente nos arquivos entrada1.txt e assim por diante.
    2.Subtrai-se o resultado da primeira celula em
todas as outras, de modo a tornar esta celular o
"instante zero" do experimento. Esta etapa e feita
no momento de captura dos dados na funcao le_dados().
