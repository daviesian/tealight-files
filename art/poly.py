from tealight.art import polygon, fill_polygon, test_polygon

c = [(100,100), (50,200), (200,300), (200, 50)]
fill_polygon(c)

print test_polygon(120,150,c)