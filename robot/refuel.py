from tealight.robot import (move, turn, look, touch, smell, leftSide, rightSide)

# Add your code here!
while True:
  while touch()=="None":
    turn(1)
    move()
  while leftSide()=="wall":
    move()
  turn(-1)
  move()
  print touch()
  