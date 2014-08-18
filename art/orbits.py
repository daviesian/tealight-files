from tealight.art import (color, line, spot, circle, box, image, text, background)

x = 600
y = 400
vx = 0
vy = 0
ax = 0
ay = 0

power = 0.1

def handle_keydown(keyval):
  global ax, ay
  
  if keyval == 37: # Left
    ax = -power
  elif keyval == 39: # Right
    ax = power
  elif keyval == 38: # Up
    ay = -power
  elif keyval == 40: # Down
    ay = power

def handle_keyup(keyval):
  global ax, ay
  
  if keyval == 37 or keyval == 39:
    ax = 0
  elif keyval == 38 or keyval == 40:
    print "STOP"
    ay = 0
    
def handle_frame():
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)
  vx = vx + ax
  vy = vy + ay
  
  x = x + vx
  y = y + vy
  
  color("blue")
  
  spot(x,y,8)
  
  