# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge
            # by, TurtleWolfe.com
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
# return(fourLoopz) // refactor for 2 more inputs

def csciOneFifty(str):
# Write a while loop that prints the letters in “CSCI 150” on separate lines.
  # i=1
  # while i in str:
  #   print(str[i])
  # print()
  # while i != 0:
  # return(str)
  # Python program to iterate over characters of a string
  
  # Code #2
  # str = "GEEKS"
    
  # Iterate over index
  for element in range(0, len(str)):
      print(str[element])
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
# https://www.geeksforgeeks.org/find-average-list-python/?ref=lbp
    print()
    print()
    srtd = sorted(numbers[:-1])
    print("Sort:    ", srtd)
    tot = sum(numbers[:-1])
    print("Sum:     ", tot)
    leng = len(numbers)-1
    print("length:  ", leng)
    if leng and tot > 0:
      averAge = (tot/leng)
      # print("Average: ", numbers[:-1])
      print("Average: ", averAge)
    # print(i)
    # print(numbers[:-1])
  # return(i)
  return(numbers)
# return(numList)
def main():
  print("Day12_23_WritingWhiles")
  print()
  countTo_i(5)#       count to i
  loop_leapThree(11)# by threes to i
  print()
  threeLoopz(-10)#    -10 -8 -6 -4 -2 0 
  print()
  fourLoopz(4)#       ****
  # print()
  # csciOneFifty("csciOneFifty")  
  # print("-"*20)
  csciOneFifty("CSCI 150")
  print()
  numList("9")
  # numList(9)
  # numList("0")
  # numList(0)
  print()
# main()  # end of Curled Main.. 