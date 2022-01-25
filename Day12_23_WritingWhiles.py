# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge

# Day 12
# While Loops (2 hours)
#################################################
# Practice: Writing While Loops

# Write python code to print the following using while loops:

# i=1
# while i < 6:
#   print(i)
#   i+=1
# 1
# 2
# 3
# 4
# 5

# i=2
# while i < 12:
#   print(i)
#   i+=3
# 2
# 5
# 8
# 11

# i=-10
# while i < 1:
#   print(i, end='')
#   i+=2
# print()
# print()
# -10 -8 -6 -4 -2 0


# i=1
# while i < 5:
#   print("****")
#   i+=1
# ****
# ****
# ****
# ****



 
# Write a while loop that prints the letters in “CSCI 150” on separate lines.
                    # i=1
                    # while i in "CSCI 150":
                    #   print("****")
                    #   i+=1
                    # print()


# Create a program that allows the user to enter in a list of numbers, prints them out in sorted order, and prints the sum and average of the numbers. Prompt the user to continue entering numbers, and enter the number ‘0’ when finished.
i=1
numbers=[]
while i != 0:
  # a = float(input("Please enter a number: "))
  a = eval(input("Please enter a number: "))
  # input = input.append.eval
  i=a
  # numbers = numbers.append(a)
  # numbers = numbers.extend(a)
  # numbers = numbers.insert(0,a)

  print(a)
  print(numbers)
  

#################################################

def main():
  print("Day12_23_WritingWhiles")
  print()
  print("Day 12 While Loops")
  print()

  # # Testing Template
  # test_input = ["hellothere", "42 degrees Celsius", "eeeeeee"]
  # test_output = ["HELOTHRE", "42DEGREES CELSUS", "EEEEE"]
  # for i in range(len(test_input)):
  #   print("Testing: ", test_input[i] +":", mangle(test_input[i]) == test_output[i])
    
main()