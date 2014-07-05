from tealight.robot import (move, turn, look, touch, smell, leftSide, rightSide)

# Add your code here!

def go(): 
  moved = 0
  while touch() == "fruit":
    move()
    moved = moved + 1
    
  turn(-1)
  if leftSide() == "fruit"
    go()
  turn(2)
  if rightSide() == "fruit"
    go()
  
  turn(1)
  for i in range(0,moved):
    move()
  turn(2)
  
    
    
go()