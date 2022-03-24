import turtle
import time


t = turtle.Turtle()


def stairs_down1(x):
  t.forward(x)
  t.right(90)
  t.forward(x)
  t.left(90)    
  t.forward(x)
  t.right(90)
  t.forward(x)
  t.left(90)    
  t.forward(x)
  t.right(90)
  t.forward(x)
  t.left(90)    
  t.forward(x)
  t.right(90)
  t.forward(x)
  t.left(90)
  time.sleep(2)
  t.home()
  t.clear()

stairs_down1(20)