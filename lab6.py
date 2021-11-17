'''
Lightning bug: To demonstrate your work, create a new file called lab6.py that will display a
single pixel whose position moves around the display based on a random walk with a time step of
0.1 s. In a random walk, at every time step the pixel will move by either -1, 0, or 1 (with equal
probability) in both x and y. The moving pixel should be prevented from moving beyond the edge of
the display. The result will look like a lightning bug trapped within the display
'''

from shifter import Shifter
from led8x8 import LED8x8
import time
import random
import multiprocessing

theDisplay = LED8x8()

def lightbug(theDisplay):

  row= random.randint(0,7)
  col= random.randint(0,7)

  newrow= 3
  newcol= 3

  #theDisplay = LED8x8()

  newrow = random.randint(-1, 1)
  newcol = random.randint(-1,1)

  if (newrow + row) not in range(0,7):
    pass
  else:
    row = row+newrow
  if (newcol+col) not in range(0,7):
    pass
  else: 
    col = col+newcol

  theDisplay.new(row,col)
  time.sleep(.25)

while True:
  lightbug(theDisplay)


'''p = multiprocessing.Process(name='lightningBug',target=lightbug)
p.daemon = True
p.start()'''
