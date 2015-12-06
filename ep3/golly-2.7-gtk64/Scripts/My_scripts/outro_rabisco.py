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
# Oscilation check is based on Oscar(OSCillation AnalyzeR) for use with Golly.

from itertools import product
from time import time

# --------------------------------------------------------------------
#used to create cell lists
def gen_coordenates(n):
    new_list = []
    for x in range(0,n):
        for y in range(0,n):
            new_list.append(x)
            new_list.append(y)
    return new_list

def cell_states(n):
    for i in product([0,1], repeat=n):
        yield i

def create_cell_list(n):
    coordenates = gen_coordenates(n)
    test_generator = cell_states(len(coordenates)/2)

    final_list =[]

    for i in test_generator:
        lista = []

        for y in range(len(i)):
            lista.append(coordenates[2*y])
            lista.append(coordenates[2*y+1])
            lista.append(i[y])

        yield lista

# --------------------------------------------------------------------

partial_cell_list = create_cell_list(2)

trial_number= 1
f = open('output/results_2x2.csv', 'w')
f.write("id,number of iterations,initial_pop,final_pop,initial_density,final_density,end_status, elapsed time\n")

for test_list in partial_cell_list:
    print test_list

f.close()
