# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge

# Day 11
# Self-Assessment: Lists & Strings

# What is output by the following python program? For partial 
# credit, please include a manual walk through table.

def what(list):
    t = -3
    for i in list:
        if i < 2:
            t += i
            # 2, 5
        else:
            t -= i
            # -2, -3, -4
    return t

# print(what([5, 3, -7, 1, -1]))

# Assume the following variable is declared:
# movie = “Monty Python and the Holy Grail”
# What is the result of the following expressions?
# movie[1]  M
# movie[-2] i
# movie[-10:] H
# movie[4:7] y P


# Assume the following variable is declared:
# list = [36, “Madison”, “Ave”]
# What is the result of the following expressions?
# list[0] 36
# list[-2] Madison
# list[1:] Madison Ave
# “Ave” in list True
# “36” in list True


# Write a function total_positive that takes a list of numbers as parameters, and adds all the positive numbers (greater than 0) together and returns their sum. 

# Example function call:
# print(total_positive([-2, -3, -4, 0, 1, 2, 3, 4]))

# Outputs: 10

def total_positive(list):
  tot = 0
  for i in range(len(list)):
    # print(list[i])
    if (list[i] > 0):
      tot += list[i]
  return tot
# How are lists & strings different in terms of immutability? strings must be copied to be changed
def main():
  print("Day 11 More Practice: Writing Lists & Strings")
  print(total_positive([-2, -3, -4, 0, 1, 2, 3, 4]))
  # Testing Template
  # print(match("hello", "Healing"))#          3
  # print(match("Healing", "hello"))#          3
  # print(match("hellllllo", "Healllllling"))# 3
main()