#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Nomes:                              no. USP:
#       Bruno Guilherme Ricci Lucas         4460596
#       Lucas Hiroshi Hayashida             7557630
#       Ricardo Mikio Morita                5412562
#
import sys
sys.path.append('lib/') #para poder ler as funcoes de lib/


#Importando as funcoes de cada movimento
import calc_circular
import mov_inclinado
import queda_livre
import constantes
import projetil
import mov_pendular

#funcao para obter os instantes de tempo para a simulacao
def le_dados(filename):
    arquivo = filename + '.csv'
    with open(arquivo, "r") as f:
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
    if tipo_mov is "inclinado":
        mov_inclinado.simula(lista_pontos,dados_experimento,arquivo_saida)
    if tipo_mov is "queda":
        queda_livre.simula(lista_pontos,dados_experimento,arquivo_saida)
    if tipo_mov == 1:
        projetil.simula(lista_pontos, dados_experimento, arquivo_saida)
    if tipo_mov == "pendulo":
        mov_pendular.simula(lista_pontos, dados_experimento, arquivo_saida)

def main():

    ###Simulando Movimento Circular###
    raio = 0.6
    no_voltas = [0,5,6,6,5,6] #experimento 0 não existe
    #O arquivo abaixo é usado na parte de verificação do programa do
    #relatório. Cada vez que o programa é executado este arquivo é
    #refeito; os calculos estao em lib/mov_inclinado.py
    f = open('resumo_mov_circular.txt','w')
    f.write("Seguem abaixo dados que serão usadas para verificação do programa:\n")
    f.close()

    idx = 1
    while idx <= 5:
        dados_experimento = []
        dados_experimento.append(raio)
        dados_experimento.append(no_voltas[idx])

        dados_brutos_travessia= "entradasProcessadas/circular%d" %idx
        dados_travessia = le_dados(dados_brutos_travessia)
        simula_pontos("circular",dados_travessia,dados_experimento,"saidas/circular%d" %idx)
        idx += 1


    ###Simulando descida em Plano inclinado###
    angulo= 14.6            #graus
    altura_rampa = 0.6      #metros
    largura_rampa = 2.0     #metros, eixo referencial é o próprio plano

    dados_experimento = []
    dados_experimento.append(angulo)
    dados_experimento.append(altura_rampa)
    dados_experimento.append(largura_rampa)

    #O arquivo abaixo é usado na parte de verificação do programa do
    #relatório. Cada vez que o programa é executado este arquivo é
    #refeito; os calculos estao em lib/mov_inclinado.py
    f = open('resumo_mov_inclinado.txt','w')
    f.write("Seguem abaixo dados que serão usadas para verificação do programa:\n")
    f.close()

    idx = 1
    while idx <= 5:
        dados_brutos_travessia= "entradasProcessadas/mov_inclinado%d" %idx
        dados_travessia = le_dados(dados_brutos_travessia)
        simula_pontos("inclinado",dados_travessia,dados_experimento, "saidas/mov_inclinado%d" %idx)
        idx += 1

    ###Simulando Queda Livre###
    dados_experimento = constantes.alturaq
    f = open('resumo_queda_livre.txt', 'w')
    f.write("Seguem abaixo dados que serao usados para verificacao do programa:\n")
    f.close()
    idx = 1
    while idx <= 5:
        dados_brutos_travessia = "entradasProcessadas/queda_livre%d" %idx
        dados_travessia = le_dados(dados_brutos_travessia)
        simula_pontos("queda", dados_travessia, constantes.alturaq, "saidas/queda_livre%d" %idx)

        idx += 1

    ###Simulando Projetil###
    dados_experimento = []
    dados_experimento.append(constantes.alturap)
    dados_experimento.append(constantes.distancia)

    f = open('resumo_projetil.txt', 'w')
    f.write("Seguem abaixo dados que serao usados para verificacao do programa:\n")
    f.close()
    idx = 1
    while idx <= 5:
        dados_brutos_travessia = "entradasProcessadas/projetil%d" %idx
        dados_travessia = le_dados(dados_brutos_travessia)
        simula_pontos(1,dados_travessia,dados_experimento, "saidas/projetil%d" %idx)
        idx += 1

    f = open('resumo_pendulo.txt', 'w')
    f.write("Seguem abaixo dados que serao usados para verificacao do programa:\n")
    f.close()
    idx = 1
    while idx <= 5:
        dados_brutos_travessia = "entradasProcessadas/circular%d" %idx
        dados_travessia = le_dados(dados_brutos_travessia)
        simula_pontos("pendulo", dados_travessia, dados_experimento, "saidas/pendulo%d" %idx)
        idx += 1


if __name__ == "__main__":
    main()
