# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge

# Day 11
# Lists & Strings (2 hours)

# Write a function average_evens that takes a list of numbers as parameters, and adds all the even numbers together and returns their average using a list. 

# Example function call:
# print(average_evens([-2, -3, -4, 0, 1, 2, 3, 4]))

# Outputs: 0

def average_evens(list):
  tot = 0
  evenz = 0
  for i in range(len(list)):
    if(list[i]%2==0):
      tot += list[i]
      evenz += 1
      # print(tot)
      # print(evenz)
  return(tot/evenz)

def main():
  print("Day 11 More Practice: Writing Lists & Strings")
  print()


  # Testing Template
  test_input = [-2, -3, -4, 0, 1, 2, 3, 4]
  test_output = 0
  # for i in range(len(test_input)):
    # print("Testing: ", test_input[i] +":", mangle(test_input[i]) == test_output[i])
  # print(test_input)
  # print(test_output)
  # print()
  print("Testing: average_evens:",average_evens(test_input) == test_output)
  print(average_evens(test_input),"==",average_evens(test_input) == test_output)
  print()
main()