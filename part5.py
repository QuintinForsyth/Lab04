import turtle
import time


t = turtle.Turtle()
def manipulated_stairs(hori,vert,loop): 
  for i in range(loop): # will loop y times
    t.forward(hori) # horizontal
    t.right(90)
    t.forward(vert) # verticle
    t.left(90)
    
  time.sleep(2)
  t.home()
  t.clear()

t = turtle.Turtle()  



manipulated_stairs(4,2,6)
t.penup()
t.home()
t.pendown()
manipulated_stairs(-40,5,6)
turtle.getscreen()._root.mainloop()