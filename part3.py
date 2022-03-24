import turtle
import time


t = turtle.Turtle()
def stairs_down2(x): 
  t.forward(x)
  for i in range(4): # will loop 4 times
    t.forward(x)
    t.right(90)
    t.forward(x)
    t.left(90)
    
  time.sleep(2)
  t.home()
  t.clear()


stairs_down2(20)
turtle.getscreen()._root.mainloop()