# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge

# Day 12
# Practice: Writing While Loops (2 hours)
# print the following using while loops:
def countTo_i(loopZ):  
# 1
# 2
# 3
# 4
# 5
  i=1
  while i < loopZ+1:
    print(i)
    i+=1
  print()
  # print("countTo_i")
  print()
  return()
# return(countTo_i)

def loop_leapThree(maX_loopZ):  

# 2
# 5
# 8
# 11

  i=2
  # print("loop_leapThree")
  # print()
  while i < maX_loopZ+1:
    print(i)
    i+=3

  return(i)
# return(loop_leapThree)

def threeLoopz(i):  
# -10 -8 -6 -4 -2 0
  while i < 1:
    print(i, end=' ')
    i+=2
  print()
  return()
# return(threeLoopz)

def fourLoopz(i):  
# ****
# ****
# ****
# ****
  while i > 0:
    i-=1
    print("****")
  print()
  return(i)
# return(fourLoopz)

def csciOneFifty(str):
# Write a while loop that prints the letters in “CSCI 150” on separate lines.
  # i=1
  # while i in str:
  #   print(str[i])
  # print()
  # while i != 0:
  return(str)
# return(csciOneFifty)

def numList(i):
# Create a program that allows the user to enter in a list of numbers, prints them out in sorted order, and prints the sum and average of the numbers. Prompt the user to continue entering numbers, and enter the number ‘0’ when finished.
  numbers=[]
  while i != 0:
    i = float(input("enter a number, or '0' when done: "))
    numbers.append(i)
    # numbers = numbers.extend(a)
    # numbers = numbers.insert(0,a)
    # numbers = numbers.sort()
    print()
    print()
    print("Sort: ", numbers[:-1])
    print("Sum: ", numbers[:-1])
    print("Average: ", numbers[:-1])
    # print(i)
    # print(numbers[:-1])
  # return(i)
  return(numbers)
# return(numList)

def main():
  print("Day12_23_WritingWhiles")
  print()
  countTo_i(5) 
  # countTo_i(9) 
  # print()

  loop_leapThree(11)
  print()

  threeLoopz(-10) 
  print()

  fourLoopz(4) 
  print()

  print(csciOneFifty("csciOneFifty"))  
  print(csciOneFifty("CSCI 150"))
  # print()
  numList("9")
  # numList(9)
  # numList("0")
  # numList(0)
  print()
main()  # end of Curled Main.. 