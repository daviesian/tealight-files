from tealight.robot import (move, turn, look, touch, smell, leftSide, rightSide)

# Add your code here!
while True:
  while leftSide()=="wall":
    move()
  turn(-1)