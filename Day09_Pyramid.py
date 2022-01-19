# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge

# Day 09
# Reading & Writing Functions

def pyramid(str, num):
  for i in range(num + 1):
    print(str * i)

pyramid("*", 2)
pyramid("+", 5)
pyramid("X", 10)