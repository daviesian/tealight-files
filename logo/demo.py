from tealight.logo import (move, turn, color)

colors = ["red", "green", "blue"]

for i in range(0,500):
  move(i)
  turn(93)
  color(colors[i%3])
  print "%d %d" % (i, i%3)