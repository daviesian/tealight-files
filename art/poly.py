from tealight.art import *

from github.daviesian.logo.lib import lib_func


c = [(100,100), (5,50), (200,300), (260, 50), (270, 400), (290,20), (280,50),(275,10)]
fill_polygon(c)

color("red")
#line(50,60,1000,60)
#spot(287.89,60,5)
print test_polygon(50,50,c)



for i in range(0,500,10):
  for j in range(0,500,10):  
    if test_polygon(i,j,c):
      color("red")
    else:
      color("blue")
    box(i,j,3,3)    

print __name__