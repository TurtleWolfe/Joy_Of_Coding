# Joy of Coding Beginning Python Challenge
# from Prof. Emily Hill
# What does this program output 
# Day 9. Reading & Writing Functions
#                           (2 hours)

import turtle
turtle.color("green")
sides = 3
size = 120
angle = 90
length = 23
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

back(75)
# two Squares
shApe(4, 210, 90)
back(25)
shApe(4, 225, 90)