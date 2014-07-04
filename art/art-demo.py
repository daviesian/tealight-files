from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import (screenWidth, screenHeight)

from tealight.utils import random

def expt():
  heads = 0
  for i in range(0,50,1):
    if random() > 0.5:
      heads = heads + 1

print expt()