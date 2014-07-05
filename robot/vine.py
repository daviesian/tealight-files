from tealight.robot import (move, turn, look, touch, smell, leftSide, rightSide)

# Add your code here!

def go():  
  while touch() == "fruit":
    move()