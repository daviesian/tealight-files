from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import (screenWidth, screenHeight)

from random import random

def expt():
  heads = 0
  for i in range(0,50,1):
    if random() >= 0.5:
      heads = heads + 1
     
  return heads

bins = [0] * 51

for i in range(0,1000,1):
  print "Trial %d" % i
  result = expt()
  bins[result] += 1
  
  
print bins

barWidth = 10

for i in range(0,51,1):
  box(i * barWidth,600,barWidth, -bins[i]*2)