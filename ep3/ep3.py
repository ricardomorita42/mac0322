#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Nomes:                              no. USP:
#       Bruno Guilherme Ricci Lucas         4460596
#       Diego Alvarez                       7557310
#       Lucas Hiroshi Hayashida             7557630
#       Ricardo Mikio Morita                5412562
#       Sérgio Rosendo da Silva Júnior      6508702
#
#   Referencias:
#      https://jakevdp.github.io/blog/2013/08/07/conways-game-of-life/

from collections import deque
import sys
sys.path.append('lib/') #permite ler as funcoes de lib/

#importando as funcoes dentro de lib/
import draw_board

#Cada vez que é chamada, devolve um dos vizinhos
def neighbors(cell):
    x, y = cell
    yield x - 1, y - 1
    yield x    , y - 1
    yield x + 1, y - 1
    yield x - 1, y
    yield x + 1, y
    yield x - 1, y + 1
    yield x    , y + 1
    yield x + 1, y + 1

#Cada chamada itera em um passo o board
def apply_iteration(board):

    new_board = set([])

    #analisa os candidatos a serem povoados
    candidates = board.union(set(n for cell in board for n in neighbors(cell)))

    #notar que a morte celular esta sendo levada em consideracao aqui
    for cell in candidates:
        count = sum((n in board) for n in neighbors(cell))
        if count == 3 or (count == 2 and cell in board):
            new_board.add(cell)
    
    return new_board


def run_glife(board, number_of_iterations):
	
    pop_size= len(board)

    print "estado inicial: " + str(board)
    print "numero de iterações: " + str(number_of_iterations)
    print "tamanho pop: " + str(pop_size)

    #draw_board.draw(board)

    for _ in xrange(number_of_iterations):
        board = apply_iteration(board)

    pop_size= len(board)

    print "\n"
    print "estado final: " + str(board)
    print "tamanho pop: " +  str(pop_size)



    if __name__ == "__main__":
    #https://docs.python.org/2/library/collections.html#collections.deque

        board = {(1,0), (1,2), (2,0), (2,1), (2,2)}
        number_of_iterations = 10

        run_glife(board, number_of_iterations)
        #draw_board.draw(board)
