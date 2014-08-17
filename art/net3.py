from tealight.art import line

from tealight.net import connect, send

pos = {
       "x": 0,
       "y": 0
      }

def handle_mousemove(x,y):
  line(pos["x"], pos["y"], x,y)
  pos["x"] = x
  pos["y"] = y
  send(pos)
  
def handle_message(new_pos):
  line(pos["x"], pos["y"], new_pos["x"], new_pos["y"])
  pos["x"] = x
  pos["y"] = y
  
connect("my_thing")