from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import (screen_width, screen_height)

from random import random

def handle_frame():
  background("paper.jpg")
  for i in range(0,100):
    image(0,i,"bird.png")
    
    
    
spot(8,4,5)
def expt():
  heads = 0
  for i in range(0,50,1):
    if random() >= 0.6666667:
      heads = heads + 1
     
  return heads

bins = [0] * 51

numTrials = 1000

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
  
#text(0,620,"0 heads")
#text(0 + barWidth * 51/2,620,"25 heads")
#text(0 + barWidth * 51,620,"50 heads")

lastx = 0
lasty = 0

def handle_mousemove(x,y):
  global lastx, lasty
  line(lastx,lasty, x, y)
  lastx = x
  lasty = y
  print "%d,%d" % (x,y)
  
def handle_mousedown(x,y,b):
  print b
  spot(x,y,10)
  color("hsl(%d,100%%,50%%)" % int(random()*255))
  circle(x,y,10)
