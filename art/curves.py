from tealight.art import (color, line, spot, circle, box, image, text, background)

for x in range(0,54):
  for y in range(0,39):
    
    x = x / 10
    y = y / 10
    
    if y > x*x:
      color("red")
    elif y > x:
      color("green")
    elif y*y < x:
      color("yellow")
    else:
      color("blue")
    
    box(x,y,1,1)