from tealight.art import (color, line, spot, circle, box, image, text, background)

def handle_mousedown(x,y):
  spot(x,y,10)
  
def handle_mousemove(x,y,button):
  print button=="left"
  #if button == "left":
  #  spot(x,y,10)