#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Mais info no arquivo readme.txt

#Movimento Uniforme
travessia1 = ((3.42,3.5),(6.96,7.07),(10.71,11.64))
travessia2 = ((3.59,3.59),(7.31,7.23),(11.54,11.09)) #falha no sensor

#Movimento Uniformemente Variado
travessia3 = ((2.6,3.04),(4.78,4.48),(6.62,7.15))
travessia4 = ((1.88,2.19),(3.76,3.38),(4.38,5.06))

#funcao para obter os instantes de tempo para a simulacao
def le_dados(filename):
    with open(filename, "r") as f:
        content = f.readlines()

    content = [x.strip("\n") for x in content]
    content = [float(x) for x in content]
    ponto_zero = content[0]
    content = [(x - ponto_zero) for x in content]

    return content

#   Recebe uma tupla com os dados do cronometro, uma lista
#   com os pontos a simula e um nome de arquivo de destino.
#   Salva a saida em um .csv.
def simula_pontos(dados_cron,pontos,arquivo_saida):
    print "Preparando %s..." %arquivo_saida

    #calculando as velocidades
    tempo_medio = [(x[0] + x[1])/2 for x in dados_cron]
    tempo_ini = tempo_medio[0]
    tempo_medio = [y - x for x,y in zip(tempo_medio,tempo_medio[1:])]
    tempo_medio.insert(0,tempo_ini)
    print "tempo medio entre cada sensor: %s" %tempo_medio
    vel_media = [ 4 / x for x in tempo_medio]
    print "vel media: %s" %vel_media

    #calculando os instantes em que cada sensor e ativado
    #delta_t = delta_s / vel_media
    #calculando quanto tempo demorou para passar 4m com a-
    #quela velocidade media
    ativacao = [(4 / delta_v) for delta_v in vel_media]

    #tempo e cumulativo em cada etapa, portanto somamos
    ativacao[1] = ativacao[1] + ativacao[0]
    ativacao[2] = ativacao[2] + ativacao[1]
    print "tempo simulado para tocar sensor:\n%s" %ativacao

    #Agora calculamos ponto a ponto o delta_s de acordo
    #com a velocidade no trecho. Cada ponto eh calculado baseado
    #em relacao ao ponto anterior.

    f = open(arquivo_saida,'w')
    f.write("Instante,Posicao\n")

    ponto_anterior = 0.0
    posicao_anterior = 0.0

    for ponto_atual in pontos:
        delta_t = ponto_atual - ponto_anterior

        if ponto_atual <= ativacao[0]: #trecho de vel 1
            delta_s = vel_media[0] * delta_t
            s = (posicao_anterior + delta_s)

        elif ponto_atual <= ativacao[1]:#trecho de vel 2
            delta_s = vel_media[1] * delta_t
            s = (posicao_anterior + delta_s)

        else: #trecho de vel 3
            delta_s = vel_media[2] * delta_t
            s = (posicao_anterior + delta_s)

        f.write(str(round(ponto_atual,3)) + ',' + str(round(s,3)) + '\n')

        ponto_anterior = ponto_atual
        posicao_anterior = s

    f.close()
    print "Arquivo %s criado.\n\n" %arquivo_saida


dados_brutos_travessia1= "travessia1.txt"
dados_travessia1 = le_dados(dados_brutos_travessia1)
simula_pontos(travessia1,dados_travessia1,"projecao1.txt")

dados_brutos_travessia2= "travessia2.txt"
dados_travessia2 = le_dados(dados_brutos_travessia2)
simula_pontos(travessia2,dados_travessia2,"projecao2.txt")

