from tealight.art import line

pos = {
       "x": 0,
       "y": 0
      }

def handle_mousemove(x,y):
  line(pos["x"], pos["y"], x,y)
  pos["x"] = x
  pos["y"] = y