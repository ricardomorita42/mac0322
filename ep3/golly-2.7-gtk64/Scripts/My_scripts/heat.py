# Golly Python script
# Written by Nathaniel Johnston (nathaniel@nathanieljohnston.com)
# March 28, 2009

''' Calculate the heat of the current oscillator/spaceship '''       

import golly as g
from glife import validint 

# Python versions < 2.4 don't have "set" built-in
try:
   set
except NameError:
   from sets import Set as set

def chunks(l,w):
   for i in xrange(0, len(l), 2):
      yield l[i]+(w*l[i+1])

if g.empty(): g.exit("The pattern is empty.")
s = g.getstring("Enter the period:","", "Heat calculator")

if not validint(s): 
  g.exit('Bad number: %s' % s)
numsteps = int(s)
if numsteps < 2:
  g.exit('Period must be at least 2.')

g.show('Processing...')

heat = 0;
maxheat = 0;
minheat = 9*g.getpop();

for i in range(0, numsteps):
  bb = g.getrect()
  clist = list(chunks(g.getcells(bb), bb[2]+2))
  g.run(1)
  dlist = list(chunks(g.getcells(g.getrect()), bb[2]+2))
  theat = (len(clist)+len(dlist)-2*len([x for x in set(clist).intersection( set(dlist) )]))
  heat += theat
  maxheat = max(theat, maxheat)
  minheat = min(theat, minheat)

g.show('Heat: %.4f, Max change: %d, Min change: %d' % ((float(heat)/numsteps), maxheat, minheat))
