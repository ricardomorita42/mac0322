__author__ = 'Liron'

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
import golly as g
from glife import rect, pattern
from time import time

# --------------------------------------------------------------------

# initialize lists
hashlist = []        # for pattern hash values
genlist = []         # corresponding generation counts
poplist = []         # corresponding population counts
boxlist = []         # corresponding bounding boxes

# --------------------------------------------------------------------


def show_spaceship_speed(period, deltax, deltay):
    # we found a moving oscillator
    if period == 1:
        g.show("Spaceship detected (speed = c)")
    elif (deltax == deltay) or (deltax == 0) or (deltay == 0):
        speed = ""
        if (deltax == 0) or (deltay == 0):
            # orthogonal spaceship
            if (deltax > 1) or (deltay > 1):
                speed += str(deltax + deltay)
        else:
            # diagonal spaceship (deltax == deltay)
            if deltax > 1:
                speed += str(deltax)
        g.show("Spaceship detected (speed = " + speed + "c/" +str(period) + ")")
    else:
        # deltax != deltay and both > 0
        speed = str(deltay) + "," + str(deltax)
        g.show("Knightship detected (speed = " + speed + "c/" + str(period) + ")")

# --------------------------------------------------------------------

def oscillating():
    # return True if the pattern is empty, stable or oscillating
    global status

    # first get current pattern's bounding box
    prect = g.getrect()
    pbox = rect(prect)
    if pbox.empty:
        g.show("The pattern is empty.")
        status = "empty"
        return True

    # get current pattern and create hash of "normalized" version -- ie. shift
    # its top left corner to 0,0 -- so we can detect spaceships and knightships
    ## currpatt = pattern( g.getcells(prect) )
    ## h = hash( tuple( currpatt(-pbox.left, -pbox.top) ) )

    # use Golly's hash command (3 times faster than above code)
    h = g.hash(prect)

    # check if outer-totalistic rule has B0 but not S8
    rule = g.getrule().split(":")[0]
    hasB0notS8 = rule.startswith("B0") and (rule.find("/") > 1) and not rule.endswith("8")

    # determine where to insert h into hashlist
    pos = 0
    listlen = len(hashlist)
    while pos < listlen:
        if h > hashlist[pos]:
            pos += 1
        elif h < hashlist[pos]:
            # shorten lists and append info below
            del hashlist[pos : listlen]
            del genlist[pos : listlen]
            del poplist[pos : listlen]
            del boxlist[pos : listlen]
            break
        else:
            # h == hashlist[pos] so pattern is probably oscillating, but just in
            # case this is a hash collision we also compare pop count and box size
            if (int(g.getpop()) == poplist[pos]) and \
               (pbox.wd == boxlist[pos].wd) and \
               (pbox.ht == boxlist[pos].ht):
                period = int(g.getgen()) - genlist[pos]

                if hasB0notS8 and (period % 2 > 0) and (pbox == boxlist[pos]):
                    # ignore this hash value because B0-and-not-S8 rules are
                    # emulated by using different rules for odd and even gens,
                    # so it's possible to have identical patterns at gen G and
                    # gen G+p if p is odd
                    return False

                if period == 1:
                    if pbox == boxlist[pos]:
                        g.show("The pattern is stable.")
                        status = "stable"
                    else:
                        show_spaceship_speed(1, 0, 0)
                elif pbox == boxlist[pos]:
                    g.show("Oscillator detected (period = " + str(period) + ")")
                    status = "oscillation (period = " + str(period) + ")"
                else:
                    deltax = abs(boxlist[pos].x - pbox.x)
                    deltay = abs(boxlist[pos].y - pbox.y)
                    show_spaceship_speed(period, deltax, deltay)
                return True
            else:
                # look at next matching hash value or insert if no more
                pos += 1

    # store hash/gen/pop/box info at same position in various lists
    hashlist.insert(pos, h)
    genlist.insert(pos, int(g.getgen()))
    poplist.insert(pos, int(g.getpop()))
    boxlist.insert(pos, pbox)

    return False

# --------------------------------------------------------------------

def fit_if_not_visible():
    # fit pattern in viewport if not empty and not completely visible
    r = rect(g.getrect())
    if (not r.empty) and (not r.visible()): g.fit()

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

partial_cell_list = create_cell_list(5)

number_of_tests = 2 ** (5 ** 2)

trial_number= 1
f = open('output/results_5x5.csv', 'w')
f.write("id,number of iterations,initial_pop,final_pop,initial_density,final_density,end_status, elapsed_time\n")

for test_list in partial_cell_list:

    iterations = 0
    status = ""

    g.new("")
    g.reset()
    g.putcells(test_list,0,0,1,0,0,1,"xor")

    g.show("Checking for oscillation... (hit escape to abort)")

    oldsecs = time()

    # --------------------------------------------------------------------
    bbox = rect( g.getrect() )
    if bbox.empty:
        initial_d = 0
    else:
        initial_d = float( g.getpop() ) / ( float(bbox.wd) * float(bbox.ht) )
    initial_pop = g.getpop()

    # --------------------------------------------------------------------

    while not oscillating() and iterations < 4000:
        g.run(1)
        iterations += 1

        newsecs = time()
        if newsecs - oldsecs >= 1.0:     # show pattern every second
            oldsecs = newsecs
            fit_if_not_visible()
            g.update()

    if iterations >= 4000
        status = "didn't stop"

    if (iterations is 0 and initial_pop == g.getpop()):
        status = "didn't change"

    bbox = rect( g.getrect() )
    if bbox.empty:
        d = 0
    else:
        d = float( g.getpop() ) / ( float(bbox.wd) * float(bbox.ht) )

    progress = 1.0 * trial_number / number_of_tests * 100

    g.show("progress: %.1f%%, iteration: %d, pop: %s, density: %6f, status: %s" %(progress,iterations,g.getpop(),d,status))
    endtime = time()
    f.write("%d,%d,%s,%s,%f,%f,%s,%f\n" %(trial_number,iterations,initial_pop,g.getpop(),initial_d,d,status,(endtime - oldsecs )))

    #g.store(test_list,"patterns/%d.rle" %loop)

    fit_if_not_visible()
    trial_number +=1
f.close()

