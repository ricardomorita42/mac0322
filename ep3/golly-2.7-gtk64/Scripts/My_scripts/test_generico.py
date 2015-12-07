#!/usr/bin/env python
# -*- coding: utf-8 -*-
#    Nomes:                                no. USP:
#        Bruno Guilherme Ricci Lucas           4460596
#        Diego Alvarez                         7557310
#        Lucas Hiroshi Hayashida               7557630
#        Ricardo Mikio Morita                  5412562
#        Sérgio Rosendo da Silva Júnior        6508702

from itertools import product
from time import time
import golly as g
import glife as gl
import oscar as o


#used to create cell lists
def gen_coordinates(n):
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
    coordinates = gen_coordinates(n)
    for i in cell_states(len(coordinates)/2):
        lista = []
        for y in range(len(i)):
            lista.append(coordinates[2*y])
            lista.append(coordinates[2*y+1])
            lista.append(i[y])

        if len(lista) % 2 == 0:
            lista.append(0)

        yield lista

#calculate density of cells
def calculate_density():
    bbox = gl.rect(g.getrect())
    if bbox.empty:
        d = 0
    else:
        d = float(g.getpop()) / float(bbox.wd*bbox.ht)
    return d


grid_size = int(g.getstring("Tamanho do tabuleiro:", "3"))
max_iter = grid_size * 500

number_of_tests = 2 ** (grid_size**2)
name = "%dx%d" % (grid_size, grid_size)
out_filename = "output/results_%s.csv" % (name)
patterns_filename = "patterns/patterns_%s.csv" % (name)
rlepatterns_filename = "patterns/patterns_" + name + "-%d.rle"

g.autoupdate(False)
f = open(out_filename, 'w')
f.write("id,number_of_iterations,initial_pop,final_pop,initial_density,final_density,end_status,elapsed_time\n")
#f2 = open(patterns_filename, 'w')
#f2.write("id, initial_cell_list\n")

trial_number = 1
for test_list in create_cell_list(grid_size):
    iterations = 0
    status = ''
    o.clear()
    g.new(name)
    g.reset()
    g.putcells(test_list)

    initial_pop = g.getpop()
    initial_d = calculate_density()

    start_time = time()
    while not o.oscillating() and iterations<max_iter:
        g.step()
        iterations += 1
    end_time = time()

    status = o.status

    if iterations >= max_iter:
        status = "timeout"
        #f2.write("%d, %s\n" % (trial_number, str(test_list)))
        #g.store(test_list, rlepatterns_filename%(trial_number))

    elif initial_pop<=g.getpop() and status == '':
        if iterations==0:
            status = "no_change"
        elif g.empty() == False:
            current_clist = g.hash(g.getrect())
            g.step()
            next_clist = g.hash(g.getrect())
            if current_clist == next_clist:
                status = "stable"
            else:
                status = "glider"

    #if status is 'glider':
    #    g.store(test_list, rlepatterns_filename%(trial_number))

    d = calculate_density()
    f.write("%d,%d,%s,%s,%f,%f,%s,%f\n" % (trial_number, iterations, initial_pop, g.getpop(), initial_d, d, status, end_time-start_time))

    progress = float(100*(trial_number+1)) / float(number_of_tests)
    g.show("progress: %.1f%%, iterations: %d, pop: %s, density: %6f, status: %s" % (progress, iterations, g.getpop(), d, status))
    trial_number += 1

g.update()
o.fit_if_not_visible()
f.close()
#f2.close()
