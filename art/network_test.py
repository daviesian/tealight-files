from tealight.net import connect, send

def handle_connected():
  print "Connected"
  
def handle_message(message):
  print "Message: %s" % message

def handle_mousemove(x,y):
  send({"x":x, "y":y})

connect("net_test")

