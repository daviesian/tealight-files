from tealight.art import *

c = [(100,100), (50,200), (200,300), (270, 50), (270, 400), (290,20)]
fill_polygon(c)

color("red")
#line(50,60,1000,60)
#spot(287.89,60,5)
print test_polygon(50,60,c)



for i in range(0,500,4):
  for j in range(0,500,4):
    if test_polygon(i,j,c):
      color("red")
    else:
      color("blue")
    circle(i,j,2)    

