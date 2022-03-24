import turtle
import time


t = turtle.Turtle()

# question 1
# worlds ugliest car without tires
#front end
def ugly_car():
  t.forward(40)
  t.right(40)
  t.forward(20)
  t.left(40)
  t.forward(45)
  t.right(10)
  t.forward(5)
  t.right(80)
  t.forward(20) 

  #underside
  t.right(90)
  t.forward(20)
  t.right(45)
  t.forward(10)
  t.left(45)
  t.forward(10)
  t.left(45)
  t.forward(10)
  t.right(45)
  t.forward(80)
  t.right(45)
  t.forward(10)
  t.left(45)
  t.forward(10)
  t.left(45)
  t.forward(10)
  t.right(45)
  t.forward(20)
  
  #rear
  t.right(90)
  t.forward(20)
  t.right(90)
  t.forward(2)
  t.left(90)
  t.forward(15)
  t.left(90)
  t.forward(9)
  t.right(90)
  t.forward(7)
  t.right(100)
  t.forward(30)
  t.right(70)
  t.forward(10)
  t.right(110)
  t.forward(10)
  t.left(90)
  t.forward(10)
  t.left(100)
  t.forward(30)
  t.left(45)
  t.home()
  # very thin car
  time.sleep(2)
  t.home()
  t.clear()
  
# question 2
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
  t.forward(x)
  time.sleep(2)
  t.home()
  t.clear()

  # question 3
def stairs_down2(x,y):
  t.forward(x)
  for i in range(y):
    t.right(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    
  time.sleep(2)
  t.home()
  t.clear()
  
stairs_down1(20)
stairs_down2(20,4)

turtle.getscreen()._root.mainloop()