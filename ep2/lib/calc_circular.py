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
    arq_euler_cromer = arquivo_saida + "_euler-cromer.csv"

    simula_analitico(lista_pontos, dados_experimento, arq_analitico)
    simula_euler(lista_pontos, dados_experimento,arq_euler)
    simula_euler_cromer(lista_pontos, dados_experimento,arq_euler_cromer)


def simula_analitico(lista_pontos, dados_experimento,arquivo_saida):

    #dados do experimento contêm raio e número de voltas dadas.
    raio = dados_experimento[0]
    voltas = dados_experimento[1]

    tempo = lista_pontos[-1]            #Tempo total do experimento
    periodo = tempo / voltas            #Tempo de uma volta
    vel_ang = 2 * math.pi / periodo     #Velocidade Angular

    print "Preparando %s..." %arquivo_saida

    f = open(arquivo_saida,'w')
    f.write("Instante(s),Pos_ang(rad),Pos_x(m),Pos_y(m)\n")

    for ponto_atual in lista_pontos:
        teta = vel_ang * ponto_atual
        x = raio * math.cos(teta)
        y = raio * math.sin(teta)

        f.write(str(round(ponto_atual,3)) + ',' +
                str(round(teta,3)) + ',' +
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
    f.write("Instante(s),Pos_ang(rad),Pos_x(m),Pos_y(m)\n")

    #Calculando Velocidade
    t_atual = lista_pontos.pop(0)
    teta_atual = vel_ang * t_atual
    x_atual = raio * math.cos(teta_atual)
    y_atual = raio * math.sin(teta_atual)

    f.write(str(round(t_atual,3)) + ',' +
            str(round(teta_atual,3)) + ',' +
            str(round(x_atual,3)) + ',' +
            str(round(y_atual,3)) + '\n')

    #Renomeando as variaveis para ficar mais claro no loop
    t_anterior = t_atual
    teta_anterior = teta_atual

    for ponto_atual in lista_pontos:
        delta_t = ponto_atual - t_anterior

        #   Como é MCU, não há Acel. Angular e portanto vel.
        #angular é constante no algoritmo de Euler

        teta_atual = teta_anterior + vel_ang * delta_t

        x_atual = raio * math.cos(teta_atual)
        y_atual = raio * math.sin(teta_atual)

        f.write(str(round(ponto_atual,3)) + ',' +
                str(round(teta_atual,3)) + ',' +
                str(round(x_atual,3)) + ',' +
                str(round(y_atual,3)) + '\n')

        #Renomeando as variaveis
        t_anterior = ponto_atual
        teta_anterior = teta_atual

    f.close()

    f2 = open("resumo_mov_circular.txt", 'a')
    f2.write("teta de %s: %f\n" %(arquivo_saida, teta_atual))
    f2.close()

    print "Arquivo %s criado.\n\n" %arquivo_saida

#Obs.: Como a velocidade angular é constante, o algoritmo de Euler-Cromer
#dá o mesmo resultado do que o de Euler.
def simula_euler_cromer(lista_pontos, dados_experimento,arquivo_saida):
    #dados do experimento contêm raio e número de voltas dadas.
    raio = dados_experimento[0]
    voltas = dados_experimento[1]

    tempo = lista_pontos[-1]            #Tempo total do experimento
    periodo = tempo / voltas            #Tempo de uma volta
    vel_ang = 2 * math.pi / periodo     #Velocidade Angular

    print "Preparando %s..." %arquivo_saida

    f = open(arquivo_saida,'w')
    f.write("Instante(s),Pos_ang(rad),Pos_x(m),Pos_y(m)\n")

    #Calculando Velocidade
    t_atual = lista_pontos.pop(0)
    teta_atual = vel_ang * t_atual
    x_atual = raio * math.cos(teta_atual)
    y_atual = raio * math.sin(teta_atual)

    f.write(str(round(t_atual,3)) + ',' +
            str(round(teta_atual,3)) + ',' +
            str(round(x_atual,3)) + ',' +
            str(round(y_atual,3)) + '\n')

    #Renomeando as variaveis para ficar mais claro no loop
    t_anterior = t_atual
    teta_anterior = teta_atual

    for ponto_atual in lista_pontos:
        delta_t = ponto_atual - t_anterior

        #   Como é MCU, não há Acel. Angular e portanto vel.
        #angular é constante no algoritmo de Euler

        teta_atual = teta_anterior + vel_ang * delta_t

        x_atual = raio * math.cos(teta_atual)
        y_atual = raio * math.sin(teta_atual)

        f.write(str(round(ponto_atual,3)) + ',' +
                str(round(teta_atual,3)) + ',' +
                str(round(x_atual,3)) + ',' +
                str(round(y_atual,3)) + '\n')

        #Renomeando as variaveis
        t_anterior = ponto_atual
        teta_anterior = teta_atual

    f.close()

    print "Arquivo %s criado.\n\n" %arquivo_saida
