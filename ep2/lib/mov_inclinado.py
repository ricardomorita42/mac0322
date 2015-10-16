#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Nomes:                              no. USP:
#       Bruno Guilherme Ricci Lucas         4460596
#       Lucas Hiroshi Hayashida             7557630
#       Ricardo Mikio Morita                5412562
#
#   mov_inclinado.py
#
#       Recebe uma lista com os pontos a simular, uma lista
#   com os dados do experimento (o raio e o numero de voltas)
#   e um nome para dar para o arquivo de saida (em .csv)
#
#   Referencias:

import math

def simula(lista_pontos, dados_experimento, arquivo_saida):
    arq_analitico = arquivo_saida + "_analitico.csv"
    arq_euler = arquivo_saida + "_euler.csv"
    arq_euler_cromer = arquivo_saida + "_euler-cromer.csv"

    simula_analitico(lista_pontos, dados_experimento, arq_analitico)
    simula_euler(lista_pontos, dados_experimento,arq_euler)
    simula_euler_cromer(lista_pontos, dados_experimento,arq_euler_cromer)


def simula_analitico(lista_pontos, dados_experimento,arquivo_saida):

    #dados do experimento contêm a inclinação, altura e largura da rampa.
    angulo_rampa = dados_experimento[0]
    altura_rampa = dados_experimento[1]
    largura_rampa= dados_experimento[2]

    inclinacao = angulo_rampa * math.pi / 180   #conversao para rads
    tempo = lista_pontos[-1]                    #Tempo total do experimento

    #aceleracao é calculada empiricamente pq tem atrito no experimento
    acel = largura_rampa * 2 / tempo**2

    print "Preparando %s..." %arquivo_saida

    f = open(arquivo_saida,'w')
    f.write("Instante(s),Pos_x(m)\n")

    for ponto_atual in lista_pontos:
        s = acel * ponto_atual**2/2

        f.write(str(round(ponto_atual,3)) + ',' +
                str(round(s,3)) + '\n')

    f.close()

    print "Arquivo %s criado.\n\n" %arquivo_saida

def simula_euler(lista_pontos, dados_experimento,arquivo_saida):

    #dados do experimento contêm a inclinação, altura e largura da rampa.
    angulo_rampa = dados_experimento[0]
    altura_rampa = dados_experimento[1]
    largura_rampa= dados_experimento[2]

    inclinacao = angulo_rampa * math.pi / 180   #conversao para rads
    tempo = lista_pontos[-1]                    #Tempo total do experimento

    #aceleracao é calculada empiricamente pq tem atrito no experimento
    acel = largura_rampa * 2 / tempo**2

    print "Preparando %s..." %arquivo_saida

    f = open(arquivo_saida,'w')
    f.write("Instante(s),Pos_x(m)\n")

    #Preparando para o loop
    t_atual = lista_pontos.pop(0)
    v_atual = acel * t_atual
    s_atual = t_atual*v_atual

    f.write(str(round(t_atual,3)) + ',' +
            str(round(s_atual,3)) + '\n')

    #Atribuindo nomes novamente para ficar mais claro
    t_anterior = t_atual
    v_anterior = v_atual
    s_anterior = s_atual

    for ponto_atual in lista_pontos:
        delta_t = ponto_atual - t_anterior
        v_atual = v_anterior + acel*delta_t
        s_atual = s_anterior + v_anterior*delta_t

        f.write(str(round(ponto_atual,3)) + ',' +
                str(round(s_atual,3)) + '\n')

        t_anterior = ponto_atual
        v_anterior = v_atual
        s_anterior = s_atual

    f.close()

    f2 = open("resumo_mov_inclinado.txt", 'a')
    f2.write("Vf de %s: %f\n" %( arquivo_saida, v_atual))
    f2.close()

    print "Arquivo %s criado.\n\n" %arquivo_saida

def simula_euler_cromer(lista_pontos, dados_experimento,arquivo_saida):

    #dados do experimento contêm a inclinação, altura e largura da rampa.
    angulo_rampa = dados_experimento[0]
    altura_rampa = dados_experimento[1]
    largura_rampa= dados_experimento[2]

    inclinacao = angulo_rampa * math.pi / 180   #conversao para rads
    tempo = lista_pontos[-1]                    #Tempo total do experimento

    #aceleracao é calculada empiricamente pq tem atrito no experimento
    acel = largura_rampa * 2 / tempo**2

    print "Preparando %s..." %arquivo_saida

    f = open(arquivo_saida,'w')
    f.write("Instante(s),Pos_x(m)\n")

    #Preparando para o loop
    t_atual = lista_pontos.pop(0)
    v_atual = acel * t_atual
    s_atual = t_atual*v_atual

    f.write(str(round(t_atual,3)) + ',' +
            str(round(s_atual,3)) + '\n')

    #Atribuindo nomes novamente para ficar mais claro
    t_anterior = t_atual
    v_anterior = v_atual
    s_anterior = s_atual

    for ponto_atual in lista_pontos:
        delta_t = ponto_atual - t_anterior
        v_atual = v_anterior + acel*delta_t
        s_atual = s_anterior + v_atual*delta_t

        f.write(str(round(ponto_atual,3)) + ',' +
                str(round(s_atual,3)) + '\n')

        t_anterior = ponto_atual
        v_anterior = v_atual
        s_anterior = s_atual

    f.close()

    print "Arquivo %s criado.\n\n" %arquivo_saida
