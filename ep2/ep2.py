#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Nomes:                              no. USP:
#       Bruno Guilherme Ricci Lucas         4460596
#       Lucas Hiroshi Hayashida             7557630
#       Ricardo Mikio Morita                5412562
#
import sys
sys.path.append('lib/')

import calc_circular

#Variaveis Globais

DELTA_INTERVALO = 5 #Tamanho do intervalo, em metros

#funcao para obter os instantes de tempo para a simulacao
def le_dados(filename):
    with open(filename, "r") as f:
        content = f.readlines()

    content.pop(0) #removendo a 1a linha do csv que contem o nome da coluna
    content = [x.strip("\n") for x in content]
    content = [float(x) for x in content]
    ponto_zero = content[0]
    content = [(x - ponto_zero) for x in content]

    return content

#   Recebe uma tupla com os dados do cronometro, uma lista
#   com os pontos a simula e um nome de arquivo de destino.
#   Salva a saida em um .csv.
def simula_pontos(tipo_mov, lista_pontos, dados_experimento, arquivo_saida):
    if tipo_mov is "circular":
        calc_circular.simula(lista_pontos,dados_experimento,arquivo_saida)

def main():

    #Simulando Movimento Circular
    raio = 0.6
    no_voltas = [0,5,6,6,5,6] #experimento 0 não existe
    idx = 1
    while idx <= 5:
        dados_experimento = []
        dados_experimento.append(raio)
        dados_experimento.append(no_voltas[idx])

        dados_brutos_travessia= "entradasProcessadas/circular%d.csv" %idx
        dados_travessia = le_dados(dados_brutos_travessia)
        simula_pontos("circular",dados_travessia,dados_experimento,"saidas/circular%d.csv" %idx)
        idx += 1

if __name__ == "__main__":
    main()
