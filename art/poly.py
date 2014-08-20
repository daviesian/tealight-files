from tealight.art import line, color, polygon, fill_polygon, test_polygon

c = [(100,100), (50,200), (200,300), (200, 50)]
fill_polygon(c)

color("red")
line(120,150,0,150)
spot(75,150,2)
print test_polygon(120,150,c)