#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Nomes:                              no. USP:
#       Bruno Guilherme Ricci Lucas         4460596
#       Lucas Hiroshi Hayashida             7557630
#       Ricardo Mikio Morita                5412562


import math
import constantes

#Os padroes utilizados nessa biblioteca seguem os padroes utilizados no arquivo mov_inclinado.py

def simula(lista_pontos, dados_experimento, arquivo_saida):
    arq_euler = arquivo_saida + "_euler.csv"
    arq_euler_cromer = arquivo_saida + "_euler-cromer.csv"

    simula_euler(lista_pontos, dados_experimento,arq_euler)
    simula_euler_cromer(lista_pontos, dados_experimento,arq_euler_cromer)


#Metodo de Euler adotado para Queda Livre (ql)
#Assumir: y = v * t +  g *x^2/2
#           logo:
#         dy/dx = v +  g*x

def simula_euler(lista_pontos, dados_experimento, arquivo_saida):

    #dados do experimento que contem a altura inicial do nazista antes de ser lançado abismo a baixo
    altura_inicial = dados_experimento

    print("Preparando %s..." %arquivo_saida)

    f = open(arquivo_saida, 'w')
    f.write("Instante(s),Pos_y(m)\n")


    #Preparando para o loop
    t_atual = lista_pontos.pop(0)
    v_atual = 0.0
    a_atual = altura_inicial 

    f.write(str(round(t_atual, 3)) + ',' + str(round(a_atual, 3)) + '\n')

    #Atribuindo nomes novamente para ficar mais claro
    t_anterior = t_atual
    v_anterior = v_atual
    a_anterior = a_atual

    for ponto_atual in lista_pontos:
        delta_t = ponto_atual - t_anterior
        v_atual = v_anterior + constantes.G * delta_t                       #v_atual +  constante.G * ponto_atual = dy/dx
        a_atual = a_anterior + (v_anterior + constantes.G * ponto_atual) * delta_t  # y_n+1 = y_n + dy/dy * delta_x     

        f.write(str(round(ponto_atual, 3)) + ',' + str(round(a_atual, 3)) + '\n')

        t_anterior = ponto_atual
        a_anterior = a_atual
    
    f.close()

    #Dá um output neste arquivo que é usado no relatório na parte de
    #verificação do programa.
    f2 = open("resumo_queda_livre.txt", 'a')
    f2.write("Af de %s: %f\n" %( arquivo_saida, a_atual))
    f2.close()

    print("Arquivo %s criado.\n\n" %arquivo_saida)





def simula_euler_cromer(lista_pontos, dados_experimento, arquivo_saida):

    #dados do experimento que contem a altura inicial do nazista antes de ser lançado abismo a baixo
    altura_inicial = dados_experimento

    print("Preparando %s..." %arquivo_saida)

    f = open(arquivo_saida, 'w')
    f.write("Instante(s),Pos_y(m)\n")


    #Preparando para o loop
    t_atual = lista_pontos.pop(0)
    v_atual = 0.0
    a_atual = altura_inicial

    f.write(str(round(t_atual, 3)) + ',' + str(round(a_atual, 3)) + '\n')

    #Atribuindo nomes novamente para ficar mais claro
    t_anterior = t_atual
    v_anterior = v_atual
    a_anterior = a_atual

    for ponto_atual in lista_pontos:
        delta_t = ponto_atual - t_anterior
        v_atual = v_anterior + constantes.G * delta_t
        a_atual = a_anterior + (v_atual + constantes.G * ponto_atual) * delta_t

        f.write(str(round(ponto_atual, 3)) + ',' + str(round(a_atual, 3)) + '\n')

        t_anterior = ponto_atual
        a_anterior = a_atual
    
    f.close()
    print("Arquivo %s criado.\n\n" %arquivo_saida)


