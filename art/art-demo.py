from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import (screenWidth, screenHeight)

from random import random

def expt():
  heads = 0
  for i in range(0,50,1):
    if random() >= 0.333333:
      heads = heads + 1
     
  return heads

bins = [0] * 51

numTrials = 100

for i in range(0,numTrials,1):
  print "Trial %d" % i
  result = expt()
  bins[result] += 1
  
  
print bins

maxPeak = max(bins)
barWidth = 10
line(0,600,51*barWidth,600)
for i in range(0,51,1):
  if bins[i] == maxPeak:
    text(i*barWidth,620, i)
  box(i * barWidth,600,barWidth, -bins[i]*2* 2000/numTrials)
  
text(0,620,"0 heads")
text(0 + barWidth * 51/2,620,"25 heads")
text(0 + barWidth * 51,620,"50 heads")
