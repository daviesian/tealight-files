from tealight.robot import (move, turn, look, touch, smell, leftSide, rightSide)

# Add your code here!
while True:
  print touch()
  while touch()=="wall":
    turn(1)
    move()
  while leftSide()=="wall":
    move()
  turn(-1)
  move()
  