print("never said it had to be all at once")
import turtle
import time

t = turtle.Turtle()


def Q():
    t.penup()
    t.goto(-20, -7)
    t.pendown()
    t.circle(30)
    t.penup()
    t.home()
    t.pendown()
    t.right(45)
    t.forward(20)
    t.back(40)



def U():
    t.circle(30, 100, 100)
    t.forward(20)
    t.penup()
    t.home()
    t.pendown()
    t.circle(30, -100, 100)
    t.back(20)


def I():
  t.left(90)
  t.forward(50)
  t.right(90)
  t.forward(20)
  t.back(40)
  t.penup()
  t.home()
  t.pendown()
  t.right(90)
  t.forward(10)
  t.left(90)
  t.forward(20)
  t.back(40)
  t.penup()
  t.home()
  t.pendown()


def N():
  t.left(90)
  t.forward(40)
  t.right(135)
  t.forward(60)
  t.left(135)
  t.forward(40)
  

def T():
  t.left(90)
  t.forward(50)
  t.right(90)
  t.forward(20)
  t.back(40)
  
Q()
time.sleep(2)
t.clear()
t.reset()
U()
time.sleep(2)
t.clear()
t.reset()
I()
time.sleep(2)
t.clear()
t.reset()
N()
time.sleep(2)
t.clear()
t.reset()
T()
time.sleep(2)
t.clear()
t.reset()
I()
time.sleep(2)
t.clear()
t.reset()
N()
time.sleep(2)
t.clear()
t.reset()

turtle.getscreen()._root.mainloop()