from tealight.robot import (move, turn, look, touch, smell, leftSide, rightSide)

# Add your code here!

while True:
  move()
  
  if touch() == "wall":
    turn(2)