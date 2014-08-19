from tealight.net import connect, send

def handle_connected():
  print "Connected"
  
def handle_message(message):
  print "Message!"
  
  print message["x"]

def handle_mousemove(x,y):
  print "MM"
  send({"x":x, "y":y}, True)

connect("net_test")
send({"x":1, "y":2})
