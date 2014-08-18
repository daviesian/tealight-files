from tealight.art import (color, line, spot, circle, box, image, text, background)

for x in range(54):
  for y in range(39):
    if y > x*x:
      color("red")
      box(x*30,y*30,1,1)