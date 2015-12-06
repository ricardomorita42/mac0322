#!/usr/bin/python
from itertools import product

coordenates_dois= [0,0,0,1, \
                   1,0,1,1]

coordenates_tres=[0,0,0,1,0,2, \
                  1,0,1,1,1,2, \
                  2,0,2,1,2,2]


coordenates = coordenates_tres

def cell_states(n):
    for i in product([0,1], repeat=n):
        yield i

test_generator = cell_states(len(coordenates)/2)

for i in test_generator:
    #print(i)
    lista = []

    for y in range(len(i)):
        lista.append(coordenates[2*y])
        lista.append(coordenates[2*y+1])
        lista.append(i[y])

    print lista

