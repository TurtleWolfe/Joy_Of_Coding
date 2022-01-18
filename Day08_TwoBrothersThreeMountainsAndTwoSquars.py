# Joy of Coding Beginning Python Challenge
# from Prof. Emily Hill
# What does this program output 
# Day 8. Ifs, Loops, & Functions (2 hours)
# Reading Ifs & Loops
import turtle
def shApe(sides = 3, size = 120, angle = 90):
# Repeat 3 times
  for i in range(sides):
    turtle.forward(size)
    turtle.left(angle)
#  shApe(sides, size, angle): 5 lines

def back(length = 23):
# Repeat 3 times
    turtle.penup()
    turtle.back(length)
    turtle.pendown()
#  back(len): 5 lines
turtle.color("green")

# triAngles
# shApe(3, 10, 120)
# shApe(3, 20, 120)
# shApe(3, 30, 120)
# shApe(3, 40, 120)
# shApe(3, 50, 120)

for i in range(10,51, 10):
  shApe(3, i, 120)
  print(i)

back(100)
shApe(3, 70, 120)
shApe(3, 90, 120)
shApe(3, 110, 120)
shApe(3, 130, 120)

back(120)
shApe(3, 150, 120)
shApe(3, 190, 120)
shApe(3, 230, 120)

back(-75)
# try Squares
shApe(4, 210, 90)

back(20)
# try Squares
shApe(4, 210, 90)