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
#   Recebe uma lista com os pontos a simular
#   e um nome de arquivo de destino.
#   Salva a saida em um .csv.

def simula(lista_pontos, dados_experimento, arquivo_saida):
    print "cheguei no circular"
    print dados_experimento
    print lista_pontos[-1]
    print "\n"

'''
def simula(dados_cron,arquivo_saida):
    print "Preparando %s..." %arquivo_saida

    tempo_medio = [(x[0] + x[1])/2 for x in dados_cron]
    tempo_ini = tempo_medio[0]
    tempo_medio = [y - x for x,y in zip(tempo_medio,tempo_medio[1:])]
    tempo_medio.insert(0,tempo_ini)
    print "tempo medio entre cada sensor: %s" %tempo_medio

    vel_media = [ DELTA_INTERVALO / x for x in tempo_medio]
    print "vel media: %s" %vel_media

    #calculando as velocidades

    if tipo_mov == 0: #MOVIMENTO UNIFORME
        for idx,t in enumerate(tempo_medio):
            acel = 2 *(DELTA_INTERVALO - vel_inicial_trecho[idx] * t)/(t**2)
            vel_final = vel_inicial_trecho[idx] + acel*t
            acel_media.append(acel)
            vel_inicial_trecho.append(vel_final)

        #t = (v - v0)/a
        #ativacao[] guarda os instantes em que cada trecho é alcançado

        ativacao = []

        for idx,acel in enumerate(acel_media):
            if idx is 0:
                t = vel_inicial_trecho[idx+1] / acel
            else:
                t = (vel_inicial_trecho[idx+1] - vel_inicial_trecho[idx]) / acel
            ativacao.append(t)

        print "acel_media: %s" %acel_media
        print "vel no fim de cada trecho: %s" %vel_inicial_trecho


    #tempo e cumulativo em cada etapa, portanto somamos
    for idx,val in enumerate(ativacao):
        if idx != 0:
            ativacao[idx] = ativacao[idx] + ativacao[idx - 1]

    print "tempo simulado para tocar sensor:\n%s" %ativacao

    #Agora calculamos ponto a ponto o delta_s de acordo
    #com a velocidade no trecho. Cada ponto eh calculado baseado
    #em relacao ao ponto anterior.

    f = open(arquivo_saida,'w')
    f.write("Instante,Posicao\n")

    ponto_anterior = 0.0
    posicao_anterior = 0.0
    s = 0
    velocidade = 0


    if tipo_mov == 0:	#caso seja MU, precisamos usar S = Vo * t

        for ponto_atual in pontos:
            delta_t = ponto_atual - ponto_anterior

            if ponto_atual <= ativacao[0]: #trecho de vel 1
                delta_s = vel_media[0] * delta_t
                s = (posicao_anterior + delta_s)

            else: #trecho de vel 2
                delta_s = vel_media[1] * delta_t
                s = (posicao_anterior + delta_s)


            f.write(str(round(ponto_atual,3)) + ',' + str(round(s,3)) + '\n')

            ponto_anterior = ponto_atual
            posicao_anterior = s

    else:	#caso seja MUV, precisamos apenas usar S = a * t²/2

        for ponto_atual in pontos:
            delta_t = ponto_atual - ponto_anterior

            if ponto_atual <= ativacao[0]: #trecho de acel 1
                velocidade = velocidade + acel_media[0] * delta_t
                delta_s = acel_media[0] * (delta_t * delta_t) / 2
                s = (posicao_anterior + delta_s)
                #print s

            else: #trecho de acel 2 mas precisamos usar S = Vo * t a * t²/2
                velocidade = velocidade + abs(acel_media[1] * delta_t)
                delta_s = velocidade * delta_t + acel_media[1] * (delta_t * delta_t) / 2
                s = (posicao_anterior + delta_s)
                #print velocidade


            f.write(str(round(ponto_atual,3)) + ',' + str(round(s,3)) + '\n')

            ponto_anterior = ponto_atual
            posicao_anterior = s



    f.close()
    print "Arquivo %s criado.\n\n" %arquivo_saida
    '''
