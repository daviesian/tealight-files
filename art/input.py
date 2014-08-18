from tealight.art import (color, line, spot, circle, box, image, text, background)

def handle_mousedown(x,y):
  spot(x,y,10)
  
def handle_mousemove(x,y,button):
  if button == "left":
    spot(x,y,10)