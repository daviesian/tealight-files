from tealight.robot import (move, turn, look, touch, smell, leftSide, rightSide)

# Add your code here!
while True:
  while leftSide()=="wall":
    move()
    while touch()=="wall":
      turn(1)
      move()
  turn(-1)
  move()
  print touch()
  