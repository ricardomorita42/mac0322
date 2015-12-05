#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Nomes:                              no. USP:
#       Bruno Guilherme Ricci Lucas         4460596
#       Lucas Hiroshi Hayashida             7557630
#       Ricardo Mikio Morita                5412562
#

#rodar easy_install prettytable no terminal para instalar esta lib
from prettytable import PrettyTable

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

def apply_iteration(board):
    new_board = set([])
    candidates = board.union(set(n for cell in board for n in neighbors(cell)))
    for cell in candidates:
        count = sum((n in board) for n in neighbors(cell))
        if count == 3 or (count == 2 and cell in board):
            new_board.add(cell)
    return new_board

#pega o set e desenha num table
def draw(board):
    max_row = 0
    max_col = 0

    for cell in board:
        if cell[0] > max_row:
            max_row = cell[0]
        if cell[1] > max_col:
            max_col = cell[1]

    drawn_board = [[0 for col in range(max_col+1)] for row in range(max_row+1)]

    for cell in board:
        drawn_board[cell[0]][cell[1]] = 1

    p = PrettyTable()
    for row in drawn_board:
        p.add_row(row)

    print p.get_string(header=False, border=False)

if __name__ == "__main__":
    board = {(0,1), (1,2), (2,0), (2,1), (2,2)}
    number_of_iterations = 2
    pop_size= len(board)

    print "estado inicial: " + str(board)
    print "numero de iterações: " + str(number_of_iterations)
    print "tamanho pop: " + str(pop_size)

    draw(board)

    for _ in xrange(number_of_iterations):
        board = apply_iteration(board)

    pop_size= len(board)

    print "\n"
    print "estado final: " + str(board)
    print "tamanho pop: " +  str(pop_size)
    draw(board)
