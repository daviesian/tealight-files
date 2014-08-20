from tealight.art import *

c = [(100,100), (50,200), (200,300), (200, 50)]
fill_polygon(c)

color("red")
line(120,150,1000,150)
spot(75,150,5)
print test_polygon(120,150,c)