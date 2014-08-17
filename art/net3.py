from tealight.art import line

from tealight.net import connect, send

pos = {
       "x": 0,
       "y": 0
      }

def go(x,y):
  line(pos["x"], pos["y"], x,y)
  pos["x"] = x
  pos["y"] = y
  

def handle_mousemove(x,y):
  #go(x,y)
  send(pos)
  
def handle_message(message):
  go(message["x"], message["y"])
  
connect("my_thing")