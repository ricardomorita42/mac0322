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


#Metodo de Euler adotado para Projetil
#Assumir:   y = vy_0 * t +  g *t^2/2
#               logo:
#           dy/dt = vy_0 + g*t

#           x = vx_0 * t
#               logo:
#           dx/dt = vx_0
def simula_euler(lista_pontos, dados_experimento, arquivo_saida):

    print "Preparando %s..." %arquivo_saida

    f = open(arquivo_saida, 'w')
    f.write("Instante(s),Pos_x(m),Pos_y(m)\n")
    
    t_subida = lista_pontos[-1]/2

    #Preparando para o loop
    #vx e constante
    #vy varia
    #Assumiremos que o nazista nao passara de 0.90m
    vy_inicial = (dados_experimento[0] / t_subida) - (constantes.G * t_subida)/2  #valor inicial teorico de vy
    vx_inicial = dados_experimento[1] / lista_pontos[-1]                                        #valor inicial teorico de vx
    vy_atual = vy_inicial
    vx_atual = vx_inicial

    t_atual = lista_pontos.pop(0)
    a_atual = 0
    d_atual = 0

    f.write(str(round(t_atual, 3)) + ',' + str(round(d_atual, 3)) + ',' + str(round(a_atual, 3)) + '\n')

    #Atribuindo nomes novamente para ficar mais claro
    t_anterior = t_atual
    vy_anterior = vy_atual
    vx_anterior = vx_atual
    a_anterior = a_atual
    d_anterior = d_atual

    for ponto_atual in lista_pontos:
        delta_t = ponto_atual - t_anterior
        
        #calculos relativos ao eixo y
        vy_atual = vy_anterior + constantes.G * delta_t                             #vy_incial * contantes.G * ponto_atual = dy/dt
        a_atual = a_anterior + (vy_anterior + constantes.G * ponto_atual) * delta_t   #y_n+1 = vy_n + dy/dt * delta_t
        
        #calculos relativos ao eixo x                                                vx_incial = dx/dt
        vx_atual = vx_anterior + vx_anterior * delta_t
        d_atual = d_anterior + vx_anterior * delta_t                                  #x_n+1 = x_n + dx/dt * delta t


        f.write(str(round(ponto_atual, 3)) + ',' + str(round(d_atual, 3)) + ',' + str(round(a_atual, 3)) + '\n')
        t_anterior = ponto_atual
        a_anterior = a_atual
        d_anterior = d_atual
    
    f.close()

    #Dá um output neste arquivo que é usado no relatório na parte de
    #verificação do programa.
    f2 = open("resumo_projetil.txt", 'a')
    f2.write("(xf, yf) de %s: (%f , %f)\n" %( arquivo_saida, a_atual, d_atual))
    f2.close()

    print "Arquivo %s criado.\n\n" %arquivo_saida



def simula_euler_cromer(lista_pontos, dados_experimento, arquivo_saida):

    print "Preparando %s..." %arquivo_saida

    f = open(arquivo_saida, 'w')
    f.write("Instante(s),Pos_x(m),Pos_y(m)\n")
    
    t_subida = lista_pontos[-1]/2

    vy_inicial = (dados_experimento[0] / t_subida) - (constantes.G * t_subida)/2  #valor inicial teorico de vy
    vx_inicial = dados_experimento[1] / lista_pontos[-1]

    vy_atual = vy_inicial
    vx_atual = vx_inicial
    
    t_atual = lista_pontos.pop(0)
    a_atual = 0
    d_atual = 0

    f.write(str(round(t_atual, 3)) + ',' + str(round(d_atual, 3)) + ',' + str(round(a_atual, 3)) + '\n')

    t_anterior = t_atual
    vy_anterior = vy_atual
    vx_anterior = vx_atual
    a_anterior = a_atual
    d_anterior = d_atual

    for ponto_atual in lista_pontos:
        delta_t = ponto_atual - t_anterior
        
        #calculos relativos ao eixo y
        vy_atual = vy_anterior + constantes.G * delta_t                     
        a_atual = a_anterior + (vy_atual + constantes.G * ponto_atual) * delta_t  
        
        #calculos relativos ao eixo x                 
        vx_atual = vx_anterior + vx_anterior * delta_t
        d_atual = d_anterior + vx_atual * ponto_atual                          


        f.write(str(round(ponto_atual, 3)) + ',' + str(round(d_atual, 3)) + ',' + str(round(a_atual, 3)) + '\n')
        t_anterior = ponto_atual
        a_anterior = a_atual
    
    f.close()
    
    print "Arquivo %s criado.\n\n" %arquivo_saida
