#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Nomes:                              no. USP:
#       Bruno Guilherme Ricci Lucas         4460596
#       Lucas Hiroshi Hayashida             7557630
#       Ricardo Mikio Morita                5412562
#
#   circular.py
#
#       Recebe uma lista com os pontos a simular, uma lista
#   com os dados do experimento (o raio e o numero de voltas)
#   e um nome para dar para o arquivo de saida (em .csv)
#
#   Referencias:
#       https://en.wikipedia.org/wiki/Circular_motion

import math

def simula(lista_pontos, dados_experimento, arquivo_saida):

    #dados do experimento contêm raio e número de voltas dadas.
    raio = dados_experimento[0]
    voltas = dados_experimento[1]

    tempo = lista_pontos[-1]            #Tempo total do experimento
    periodo = tempo / voltas            #Tempo de uma volta
    vel_ang = 2 * math.pi / periodo     #Velocidade Angular

    print "Preparando %s..." %arquivo_saida

    f = open(arquivo_saida,'w')
    f.write("Instante(s),PosicaoAngular(graus)\n")

    for ponto_atual in lista_pontos:
        teta = vel_ang * ponto_atual                    #calculado em radianos
        teta_em_graus = 180 * teta / math.pi
        #print "t: " + str(ponto_atual) + " vel: " + str(vel_ang) + " teta: " + str(teta)

        f.write(str(round(ponto_atual,3)) + ',' + str(round(teta_em_graus,3)) + '\n')

    f.close()

    print "Arquivo %s criado.\n\n" %arquivo_saida
