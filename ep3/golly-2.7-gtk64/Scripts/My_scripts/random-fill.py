# Randomly fill cells in the current selection.
# Author: Andrew Trevorrow (andrew@trevorrow.com), March 2011.

import golly as g
from glife import rect, validint
from time import time
from random import randint

r = rect( g.getselrect() )
if r.empty: g.exit("There is no selection.")

maxlive = g.numstates() - 1

# use previous values if they exist
inifilename = g.getdir("data") + "random-fill.ini"
previousvals = "50 1 " + str(maxlive)
try:
   f = open(inifilename, 'r')
   previousvals = f.readline()
   f.close()
except:
   # should only happen 1st time (inifilename doesn't exist)
   pass

result = g.getstring(
   "Enter percentage minstate maxstate values\n" +
   "where the percentage is an integer from 0 to 100\n" +
   "and the state values are integers from 1 to "+str(maxlive)+"\n" +
   "(maxstate is optional, default is minstate):",
   previousvals, "Randomly fill selection")

# save given values for next time this script is called
try:
   f = open(inifilename, 'w')
   f.write(result)
   f.close()
except:
   g.warn("Unable to save given values in file:\n" + inifilename)

# extract and validate values
pmm = result.split()
if len(pmm) == 0: g.exit()
if len(pmm) == 1: g.exit("You must supply min and max states.")
if not validint(pmm[0]): g.exit("Bad percentage value: " + pmm[0])
if not validint(pmm[1]): g.exit("Bad minstate value: " + pmm[1])
perc = int(pmm[0])
minlive = int(pmm[1])
if perc < 0 or perc > 100:
   g.exit("Percentage must be from 0 to 100.")
if minlive < 1 or minlive > maxlive:
   g.exit("Minimum state must be from 1 to "+str(maxlive)+".")
if len(pmm) > 2:
   if not validint(pmm[2]): g.exit("Bad maxstate value: " + pmm[2])
   i = int(pmm[2])
   if i < minlive: g.exit("Maximum state must be >= minimum state.")
   if i > maxlive: g.exit("Maximum state must be <= "+str(maxlive)+".")
   maxlive = i
else:
   maxlive = minlive

oldsecs = time()
for row in xrange(r.top, r.top + r.height):
   for col in xrange(r.left, r.left + r.width):
      if randint(0,99) < perc:
         if minlive == maxlive:
            g.setcell(col, row, minlive)
         else:
            g.setcell(col, row, randint(minlive,maxlive))
      else:
         g.setcell(col, row, 0)
   # if large selection then give some indication of progress
   newsecs = time()
   if newsecs - oldsecs >= 1.0:
      oldsecs = newsecs
      g.update()
