from tealight.art import *

c = [(100,100), (50,200), (200,300), (270, 50), (270, 400), (290,20)]
fill_polygon(c)

color("red")
line(50,200,1000,200)
#spot(283,150,5)
print test_polygon(50,200,c)