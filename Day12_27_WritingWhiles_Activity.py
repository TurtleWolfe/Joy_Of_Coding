# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge

# Day 12
# While Loops (2 hours)
#################################################
# Activity: Strings, Lists & Whiles (40 min)
# No Due Date Points 10 Submitting a file upload
#################################################
# Please complete the following

def average_neg_evens(str):
  #     Write a function average_neg_evens that takes a list of numbers as a parameter, and adds all the negative even numbers (less than 0 and divisible by 2) together and returns their average.
  #     Example function call:
  #     print(average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4]))
  #     Outputs: -3
  
  # str=eval(input("Word Me: "))
  # str=str.lower()
  # if str.count('e')>=1:
  #   print(str, ":first (e) occurs at index ? position")
  #   # first E or e
  # else:
  print(str)

def count_letter(str, char):
#     Write a function count_letter that takes a list of strings and a string letter as parameters and returns the number of times this letter occurs, both upper- & lower-cased.
#     Example function call:
#     list = ["HELLO", "goodbye", "1234 Oooh!"]
#     print(count_letter(list, "o"))
#     Outputs: 6

  # str=eval(input("Word Me: "))
  str=str.lower()
  # if str.count('e')>=1:
  #   print(str, ":first (e) occurs at index ? position")
  #   # first E or e
  # else:
  print(str)

def main():
  print("Day12_27_WritingWhiles_Activity")
  # print()
  # print("Day 12 While Loops")
  print()
  # print()
  list = ["HELLO", "goodbye", "1234 Oooh!"]
  # print(count_letter(list))
  # print(count_letter(list, "o"))
  #  Outputs: 6
  count_letter("count_letter", "a") # count_letter
  count_letter("count_letter() takes 1 positional argument but 2 were given", "a") # count_letter  
  print()
  average_neg_evens("average_neg_evens") # average_neg_evens
  average_neg_evens("average_neg_evens() 'list' object has no attribute 'lower'") # average_neg_evens
  # print(average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4]))

  # Testing Template
  # test_input = ["hellothere", "42 degrees Celsius", "eeeeeee"]
  # test_output = ["HELOTHRE", "42DEGREES CELSUS", "EEEEE"]
  # for i in range(len(test_input)):
  #   print("Testing: ", test_input[i] +":", mangle(test_input[i]) == test_output[i])
  print()
main()

# Things to remember when submitting:
# For full credit, you must use a while loop once somewhere in your program.
# Your program should be ordered as follows: leading comment, any imports, function definitions, then lastly a main
# When testing your functions (by calling them in main), make sure to also include some descriptive output to determine if your test passed or failed