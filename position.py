import turtle


t = turtle.Turtle()  

def position_turtle(x,y):
  t.hideturtle()
  t.penup()
  t.goto(x,y)
  t.showturtle()
  t.pendown()

position_turtle(-100,100)
turtle.getscreen()._root.mainloop()