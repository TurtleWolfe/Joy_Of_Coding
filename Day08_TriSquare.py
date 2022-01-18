# Joy of Coding Beginning Python Challenge
# from Prof. Emily Hill
# What does this program output 
# Day 8. Ifs, Loops, & Functions (2 hours)

# Reading Ifs & Loops

import turtle
turtle.color("green")

sides = 3
size = 120
angle = 90

def shApe(sides, size, angle):
# Repeat 3 times
  for i in range(sides):
    turtle.forward(size)
    turtle.left(angle)
#  return 2

# triAngle
shApe(3, 50, 120)

# try Square
shApe(4, 150, 90)

