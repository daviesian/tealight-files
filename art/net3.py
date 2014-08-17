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
  
def handle_message(message):
  line(pos["x"], pos["y"], message.x, message.y)
  pos["x"] = x
  pos["y"] = y
  
connect("my_thing")