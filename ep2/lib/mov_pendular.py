__author__ = 'Liron'
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Nomes:                              no. USP:
#       Bruno Guilherme Ricci Lucas         4460596
#       Lucas Hiroshi Hayashida             7557630
#       Ricardo Mikio Morita                5412562


import math
import constantes

g = constantes.G
L = constantes.comprimento
teta0 = constantes.teta0
w0 = constantes.w0

#Os padroes utilizados nessa biblioteca seguem os padroes utilizados no arquivo mov_inclinado.py

def teta(teta_ant,w_ant, dt):
    return teta_ant + omega(w_ant, teta_ant, dt)*dt

def omega(w_ant, teta_ant, dt):
    return w_ant - teta_ant*dt

def simula(lista_pontos, dados_experimento, arquivo_saida):
    arq_euler = arquivo_saida + "_euler.csv"
    #arq_euler_cromer = arquivo_saida + "_euler-cromer.csv"

    simula_euler(lista_pontos, arquivo_saida)
    #simula_euler_cromer(lista_pontos, dados_experimento, arq_euler_cromer)


#Metodo de Euler adotado para Movimento Pendular

def simula_euler(lista_pontos, arquivo_saida):

    print("Preparando %s..." %arquivo_saida)

    f = open(arquivo_saida,'w')
    f.write("Instante(s),Pos_ang(rad),Pos_x(m),Pos_y(m)\n")

    #Calculando Velocidade
    t_atual = lista_pontos.pop(0)
    teta_atual = omega(w0, teta0, 0) * t_atual
    x_atual = L * math.cos(teta_atual)
    y_atual = L * math.sin(teta_atual)

    f.write(str(round(t_atual,3)) + ',' +
            str(round(teta_atual,3)) + ',' +
            str(round(x_atual,3)) + ',' +
            str(round(y_atual,3)) + '\n')

    #Renomeando as variaveis para ficar mais claro no loop
    t_anterior = t_atual
    teta_anterior = teta_atual
    w_anterior = omega(w0, teta0, 0)

    x_atual = []
    y_atual = []

    for ponto_atual in lista_pontos:
        delta_t = ponto_atual - t_anterior
        w_atual = omega(w_anterior, teta_anterior, delta_t)
        teta_atual = teta(teta_anterior, w_anterior, delta_t)

        x_atual.append(L * math.cos(teta_atual))
        y_atual.append(L * math.sin(teta_atual))

        f.write(str(round(ponto_atual,3)) + ',' +
                str(round(teta_atual,3)) + ',' +
                str(round(x_atual,3)) + ',' +
                str(round(y_atual,3)) + '\n')

        #Renomeando as variaveis
        t_anterior = ponto_atual
        teta_anterior = teta_atual
        w_anterior = w_atual

    f.close()

    f2 = open("resumo_mov_circular.txt", 'a')
    f2.write("teta de %s: %f\n" %(arquivo_saida, teta_atual))
    f2.close()

    print("Arquivo %s criado.\n\n" %arquivo_saida)

    pyplot.figure(0)
    pyplot.plot(x_atual,y_atual,label='Euler',linestyle='',marker='o')
    #pyplot.plot(tempo,x_atual,label='Euler')
    pyplot.title('Pendulo')
    pyplot.show()

#Obs.: Como a velocidade angular é constante, o algoritmo de Euler-Cromer
#dá o mesmo resultado do que o de Euler.


#def simula_euler_cromer(lista_pontos, dados_experimento,arq_euler_cromer):
