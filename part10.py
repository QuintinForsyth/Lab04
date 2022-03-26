#Create a chess/checkerboard 
#Use the fill feature for squares
#create a shapes.py and put the functions in there
#call those functions from main.py (import shapes)
#Use loops to create the board!
#Use docstrings for in shapes.py
import turtle
import time



t = turtle.Turtle()
def teleports (size, count):
    t.penup()
    t.home()
    t.right(90)
    t.forward(size*count)
    t.left(90)
    t.pendown()

def forward_right(size):
  t.forward(size)    
  t.right(90)
  
def draw_square(size):
  forward_right(size)
  forward_right(size)
  forward_right(size)
  forward_right(size)
  t.forward(size)

  
def chess_board(size, total_to_loop,two_per_row):
  count = 0
  for i in range(total_to_loop):
    count = count + 1
    
    for n in range(two_per_row):
      turtle.color("black")
      draw_square(size)
      t.begin_fill()
      draw_square(size)
      t.end_fill()

    teleports(size, count)
    
    for n in range(two_per_row):
        turtle.color("black")
        t.begin_fill()
        draw_square(size)
        t.end_fill()
        draw_square(size)
    count = count + 1  
    teleports(size,count)


        



t.
chess_board(20,4,4)
turtle.getscreen()._root.mainloop()

