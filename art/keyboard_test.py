from tealight.art import line, spot, screen_width, screen_height

x = screen_width / 2
y = screen_height / 2

def handle_keydown(keychar, keyval):
  global x,y
  x += 10
  y += 10
  
  spot(x,y,5)
  print keychar

