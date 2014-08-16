from tealight.logo import (move, turn,
                           pen_down, pen_up,
                           show_turtle, hide_turtle,
                           color, speed)

from tealight.utils import github_import

github_import()

#import lib

print lib.lib_func()
print "This is logo mode!"

print 5/2
colors = ["red", "blue", "green"]

for i in range(10,200,5):
  move(i)
  turn(83)
  c = colors[(i / 5)%3]
  color(c)
