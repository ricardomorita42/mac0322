#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Mais info no arquivo readme.txt


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
def simula_pontos(tipo_mov, dados_cron,pontos,arquivo_saida):
    print "Preparando %s..." %arquivo_saida

    tempo_medio = [(x[0] + x[1])/2 for x in dados_cron]
    tempo_ini = tempo_medio[0]
    tempo_medio = [y - x for x,y in zip(tempo_medio,tempo_medio[1:])]
    tempo_medio.insert(0,tempo_ini)
    print "tempo medio entre cada sensor: %s" %tempo_medio

    vel_media = [ 5 / x for x in tempo_medio]
    print "vel media: %s" %vel_media

    #calculando as velocidades

    if tipo_mov == 0: #MOVIMENTO UNIFORME
        #Se o movimento é retilíneo uniforme, calculamos a
        #velocidade média de cada um dos dois trechos e com esta
        #podemos plotar qual a posicao no espaco naquele instante.

        #calculando os instantes em que cada sensor e ativado
        #delta_t = delta_s / vel_media
        #calculando quanto tempo demorou para passar 5m com a-
        #quela velocidade media e salvamos em ativacao
        ativacao = [(5 / delta_v) for delta_v in vel_media]

        #tempo e cumulativo em cada etapa, portanto somamos
        ativacao[1] = ativacao[1] + ativacao[0]
        print "tempo simulado para tocar sensor:\n%s" %ativacao


    else: #MOVIMENTO UNIFORMENTE VARIADO
        #Caso o movimento seja uniformente variado, podemos obter
        #a aceleração média de cada trecho e assim calcular a posição
        #instante a instante, recalculando a velocidade atual para
        #cada instante que estamos plotando.
        acel_media = [ 5 / x for x in vel_media]
		
        print "acel. media: %s" %acel_media

        ativacao = [(5 / delta_v) for delta_v in vel_media]

        #tempo e cumulativo em cada etapa, portanto somamos
        ativacao[1] = ativacao[1] + ativacao[0]
        print "tempo simulado para tocar sensor:\n%s" %ativacao


    #Agora calculamos ponto a ponto o delta_s de acordo
    #com a velocidade no trecho. Cada ponto eh calculado baseado
    #em relacao ao ponto anterior.

    f = open(arquivo_saida,'w')
    f.write("Instante,Posicao\n")

    ponto_anterior = 0.0
    posicao_anterior = 0.0
	
	
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
                delta_s = acel_media[0] * (delta_t * delta_t) / 2
                s = (posicao_anterior + delta_s)

            else: #trecho de acel 2
                    delta_s = acel_media[1] * (delta_t * delta_t) / 2
                    s = (posicao_anterior + delta_s)


            f.write(str(round(ponto_atual,3)) + ',' + str(round(s,3)) + '\n')

            ponto_anterior = ponto_atual
            posicao_anterior = s
	
	
	
    f.close()
    print "Arquivo %s criado.\n\n" %arquivo_saida

def main():
    #Dados obtidos no experimento
    mu1 = ((4.05,4.12),(8.02,7.90))
    mu2 = ((3.33,4.08),(7.70,9.01))
    mu3 = ((4.08,4.12),(7.89,9.29))
    mu4 = ((3.79,5.01),(8.41,9.59))
    mu5 = ((3.50,3.50),(7.63,7.62)) # falha no sensor
    mu6 = ((3.09,3.49),(8.02,6.65))
    mu7 = ((3.84,3.46),(7.49,7.35))
    mu8 = ((3.56,4.23),(7.63,8.06))
    mu9 = ((4.16,4.11),(7.97,8.07))
    mu10= ((3.11,2.27),(6.33,5.73))
    mu11= ((2.27,2.92),(5.67,5.67)) # falha no sensor
    mu12= ((3.67,3.67),(7.05,7.05)) # falha no sensor

    muv1 =((1.93,2.02),(4.83,4.33))
    muv2 =((3.36,3.26),(5.09,4.70))
    muv3 =((3.65,3.86),(7.54,6.08))
    muv4 =((2.61,2.71),(5.30,4.93))
    muv5 =((2.33,2.83),(4.64,4.92))
    muv6 =((2.79,2.52),(3.79,3.44))
    muv7 =((1.62,1.43),(2.68,2.47))
    muv8 =((2.54,2.58),(3.52,3.78))
    muv9 =((2.38,2.35),(3.61,3.70))
    muv10=((1.90,2.55),(3.38,3.99))
    muv11=((1.50,2.07),(2.92,3.61))
    muv12=((2.73,3.11),(4.00,4.36))

    dados_brutos_travessia1= "travessia1.txt"
    dados_travessia1 = le_dados(dados_brutos_travessia1)
    simula_pontos(0,mu1,dados_travessia1,"projecaoMu1.csv")

    dados_brutos_travessia2= "travessia2.txt"
    dados_travessia2 = le_dados(dados_brutos_travessia2)
    simula_pontos(1,muv1,dados_travessia2,"projecaoMu2.csv")

    travessia1 = ((3.42,3.5),(6.96,7.07),(10.71,11.64))
    travessia2 = ((3.59,3.59),(7.31,7.23),(11.54,11.09)) #falha no sensor

    #Movimento Uniformemente Variado
    travessia3 = ((2.6,3.04),(4.78,4.48),(6.62,7.15))
    travessia4 = ((1.88,2.19),(3.76,3.38),(4.38,5.06))

    dados_brutos_travessia1= "travessia1.txt"
    dados_travessia1 = le_dados(dados_brutos_travessia1)
    simula_pontos(1, travessia1,dados_travessia1,"projecaoMuv1.csv")

    dados_brutos_travessia2= "travessia2.txt"
    dados_travessia2 = le_dados(dados_brutos_travessia2)
    simula_pontos(1, travessia2,dados_travessia2,"projecaoMuv2.csv")

if __name__ == "__main__":
    main()
