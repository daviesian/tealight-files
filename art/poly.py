from tealight.art import *

c = [(100,100), (50,200), (200,300), (270, 50), (270, 400), (290,20)]
fill_polygon(c)

color("red")
line(50,200,1000,200)
#spot(283,150,5)
print test_polygon(49,200,c)

def handle_mousedown(x,y):
  if test_polygon(x,y,c):
    color("red")
  else:
    color("blue")
  circle(x,y,10)