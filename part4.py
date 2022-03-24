import turtle
import time


t = turtle.Turtle()
def efficient_stairs(x,y): 
  for i in range(y): # will loop y times
    t.forward(x)
    t.right(90)
    t.forward(x)
    t.left(90)
    
  time.sleep(2)
  t.home()
  t.clear()


efficient_stairs(20,4)
turtle.getscreen()._root.mainloop()