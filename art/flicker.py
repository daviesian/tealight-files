from tealight.art import *

sx = 0
sy = 0

def handle_mousemove(x,y):
  global sx, sy
  
  sx = x
  sy = y

def handle_frame():
  color("white")
  box(0,0,screen_width, screen_height)
  
  color("red")
  box(0,0,screen_width, screen_height)
  color("blue")
  spot(sx,sy,50)