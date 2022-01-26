# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge

# Day 12
# Practice: Writing While Loops (2 hours)
# print the following using while loops:
def oneLoopz(i):  
# i=1
  while i < 6:
    print(i)
    i+=1
# 1
# 2
# 3
# 4
# 5
  print()
  print("oneLoopz")
  print()
  return()

def twoLoopz(i):  
# i=2
  # print("twoLoopz")
  # print()
  while i < 11:
    print(i)
    i+=3
# 2
# 5
# 8
# 11
  return(i)
# return(twoLoopz)

def threeLoopz(i):  
  print("threeLoopz")
  while i < 1:
    print(i, end=' ')
    i+=2
  # print()
# -10 -8 -6 -4 -2 0
  print()
  return()
# return(threeLoopz)

def fourLoopz(i):  
  while i > 0:
    i-=1
    print("****")
# ****
# ****
# ****
# ****
  print()
  print("fourLoopz")
  # print()
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
    i = float(input("Please enter a number: "))
    numbers.append(i)
    # numbers = numbers.extend(a)
    # numbers = numbers.insert(0,a)
    print(i)
    print(numbers)
  return(i)
# return(numList)

def main():
  print("Day12_23_WritingWhiles")
  print()
# why this one print ()?
  # print(oneLoopz(1)) 
  # print()

# why this one clean?
  # print(twoLoopz(1)) 
  # print()
  # print(twoLoopz(2)) 
  # # print()

# why this one print ()?
  # print(threeLoopz(-10)) 
  # print()

# why this one print zero?
  # print(fourLoopz(4)) 
  # print()

  # print(csciOneFifty("csciOneFifty"))  
  # print(csciOneFifty("CSCI 150"))

  # print()
  # numList("9")
  numList(9)
  # numList("0")
  # numList(0)
  # numList()
  # print(numList("0"))  
  print()
main()  # end of Curled Main.. 