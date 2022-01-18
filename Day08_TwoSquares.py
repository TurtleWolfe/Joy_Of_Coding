# Joy of Coding Beginning Python Challenge
# from Prof. Emily Hill
# What does this program output 
# Day 8. Ifs, Loops, & Functions (2 hours)
# Reading Ifs & Loops
import turtle
turtle.color("green")
# sides = 3
# size = 120
# angle = 90
# length = 23
def shApe(sides, size, angle):
# Repeat 3 times
  for i in range(sides):
    turtle.forward(size)
    turtle.left(angle)
#  shApe(sides, size, angle): 5 lines

def back(length):
# Repeat 3 times
    turtle.penup()
    turtle.back(length)
    turtle.pendown()
#  back(len): 5 lines

# triAngles
shApe(3, 10, 120)
shApe(3, 20, 120)
shApe(3, 30, 120)
shApe(3, 40, 120)
shApe(3, 50, 120)

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

back(15)
# try Squares
shApe(4, 210, 90)