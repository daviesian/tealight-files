from tealight.art import (color, line, spot, circle, box, image, text, background)

def handle_mousedown(x,y):
  color("blue")
  spot(x,y,10)
  
def handle_mousemove(x,y,button):
  print button
  if button == "left":
    color("red")
    spot(x,y,10)