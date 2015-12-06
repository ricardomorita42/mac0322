#!/usr/bin/python
from itertools import product

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

coordenates = gen_coordenates(2)
test_generator = cell_states(len(coordenates)/2)

for i in test_generator:
    lista = []

    for y in range(len(i)):
        lista.append(coordenates[2*y])
        lista.append(coordenates[2*y+1])
        lista.append(i[y])

    print lista

