from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            leftSide, 
                            rightSide)

# Here is a fairly useless algorithm

while True:
  move()
  
  if touch() == "wall":
    turn(2)