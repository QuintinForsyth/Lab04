import turtle
import time



t = turtle.Turtle()
def teleports (size, count):
    t.penup()
    t.home() # uses home to warp back
    t.right(90)
    t.forward(size*count) # moves down by a size times count of lines
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

  
def chess_board(size, total_to_loop,two_per_row): # does two rows 
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


        







