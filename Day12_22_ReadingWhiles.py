# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge

# Day 12
# While Loops (2 hours)
#################################################
# Learning Exercise: Basic While

# What is output by the following programs?



# j = 4
# while j > -4:
#    print(j)
#    j -= 1
# 43210-1-2-3


# string = “Hello” 
# builder = “”
# i = 0
# while i < len(string):
#    builder += string[i].swapcase() 
#    print(i, builder)
#    i += 1
# print(string, “->”, builder)



# x = 0
# i = 1
# while x < 20:
#   if x > 5:
#     x += 15
#   else:
#     x += 1
#   print(i, x)
#   i += 1

# Learning Exercise: Combining While

# What is output by the following programs?



# string = “HELLO”
# x = 0
# while string[x] != ‘L’:
#    print(string[x], end=”... “)
#    x += 1
# print(“\n”, string, “first L is at”, x)



# # Assume the user enters the following:
# # hello goodbye cat dog DONE done
# list = []
# prompt = “Please enter word, ‘done’ to finish ”
# response = input(prompt)
# while response != “done”:
#     list.append(response)
#     response = input(prompt)
# print(sorted(list))



# x = 0
# while x < 20:
#   if x > 5:
#     if x % 2 == 0:
#       x *= 2
#     else:
#       x *= -1
#   else:
#     x += 10
#   x += 1
# print(x)
#################################################


def main():
  print("Day12_22_ReadingWhiles")
  print()
  print("Day 12 While Loops")
  print()

  # # Testing Template
  # test_input = ["hellothere", "42 degrees Celsius", "eeeeeee"]
  # test_output = ["HELOTHRE", "42DEGREES CELSUS", "EEEEE"]
  # for i in range(len(test_input)):
  #   print("Testing: ", test_input[i] +":", mangle(test_input[i]) == test_output[i])
    
main()