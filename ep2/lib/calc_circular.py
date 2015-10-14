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
#       https://en.wikipedia.org/wiki/Centripetal_force
#       https://en.wikipedia.org/wiki/Small-angle_approximation

import math

def simula(lista_pontos, dados_experimento, arquivo_saida):
    arq_analitico = arquivo_saida + "_analitico.csv"
    arq_euler = arquivo_saida + "_euler.csv"

    simula_analitico(lista_pontos, dados_experimento, arq_analitico)
    simula_euler(lista_pontos, dados_experimento,arq_euler)


def simula_analitico(lista_pontos, dados_experimento,arquivo_saida):

    #dados do experimento contêm raio e número de voltas dadas.
    raio = dados_experimento[0]
    voltas = dados_experimento[1]

    tempo = lista_pontos[-1]            #Tempo total do experimento
    periodo = tempo / voltas            #Tempo de uma volta
    vel_ang = 2 * math.pi / periodo     #Velocidade Angular

    print "Preparando %s..." %arquivo_saida

    f = open(arquivo_saida,'w')
    f.write("Instante(s),Pos_x(m),Pos_y(m)\n")

    for ponto_atual in lista_pontos:
        teta = vel_ang * ponto_atual
        x = raio * math.cos(teta)
        y = raio * math.sin(teta)

        f.write(str(round(ponto_atual,3)) + ',' +
                str(round(x,3)) + ',' +
                str(round(y,3)) + '\n')

    f.close()

    print "Arquivo %s criado.\n\n" %arquivo_saida

def simula_euler(lista_pontos, dados_experimento,arquivo_saida):
    #dados do experimento contêm raio e número de voltas dadas.
    raio = dados_experimento[0]
    voltas = dados_experimento[1]

    tempo = lista_pontos[-1]            #Tempo total do experimento
    periodo = tempo / voltas            #Tempo de uma volta
    vel_ang = 2 * math.pi / periodo     #Velocidade Angular

    print "Preparando %s..." %arquivo_saida

    f = open(arquivo_saida,'w')
    f.write("Instante(s),Pos_x(m),Pos_y(m)\n")

    #Calculando Velocidade e Aceleração atual para começar a usar Euler
    t_atual = lista_pontos.pop(0)
    teta = vel_ang * t_atual
    x_atual = raio * math.cos(teta)
    y_atual = raio * math.sin(teta)

    vel_x_atual = -1 * raio * vel_ang * math.sin(vel_ang*t_atual)
    vel_y_atual =      raio * vel_ang * math.cos(vel_ang*t_atual)

    #   A formula da aceleracao não é linear. Entretanto, para valores
    #pequenos de teta, estamos considerando:
    #
    #   sen(teta) = teta
    #   cos(teta) = 1 - teta**2/2
    #

    acel_x_atual = -1 * vel_ang ** 2 * raio * (1 - teta**2/2)
    acel_y_atual = -1 * vel_ang ** 2 * raio * teta

    f.write(str(round(t_atual,3)) + ',' +
            str(round(x_atual,3)) + ',' +
            str(round(y_atual,3)) + '\n')

    #Renomeando as variaveis para ficar mais claro no loop
    t_anterior = t_atual
    vel_x_anterior = vel_x_atual
    vel_y_anterior = vel_y_atual
    acel_x_anterior = acel_x_atual
    acel_y_anterior = acel_y_atual
    x_anterior = x_atual
    y_anterior = y_atual

    for ponto_atual in lista_pontos:
        delta_t = ponto_atual - t_anterior
        teta = vel_ang * delta_t

        x_atual = x_anterior + vel_x_anterior * delta_t
        y_atual = y_anterior + vel_y_anterior * delta_t

        vel_x_atual = vel_x_anterior + acel_x_anterior*delta_t
        vel_y_atual = vel_y_anterior + acel_y_anterior*delta_t

        acel_x_atual = -1 * vel_ang ** 2 * raio * (1 - teta**2/2)
        acel_y_atual = -1 * vel_ang ** 2 * raio * teta

        f.write(str(round(ponto_atual,3)) + ',' +
                str(round(x_atual,3)) + ',' +
                str(round(y_atual,3)) + '\n')

        #Renomeando as variaveis
        t_anterior = ponto_atual
        vel_x_anterior = vel_x_atual
        vel_y_anterior = vel_y_atual
        acel_x_anterior = acel_x_atual
        acel_y_anterior = acel_y_atual
        x_anterior = x_atual
        y_anterior = y_atual

    f.close()

    print "Arquivo %s criado.\n\n" %arquivo_saida
