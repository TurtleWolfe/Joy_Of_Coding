# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge

# Day 12
# While Loops (2 hours)
# Learning Exercise: Basic While

# What is output by the following programs?
def alphaFunction(i):

# j = 4
# while j > -4:
#    print(j)
#    j -= 1
# 43210-1-2-3

  print(i)
  print()
  # alphaFunction("alphaFunction") 

def betaFunction(i):
  # string = “Hello” 
# builder = “”
# i = 0
# while i < len(string):
#    builder += string[i].swapcase() 
#    print(i, builder)
#    i += 1
# print(string, “->”, builder)
  print(i)
  print()
  # betaFunction("betaFunction") 

def charlieFunction(i):

# x = 0
# i = 1
# while x < 20:
#   if x > 5:
#     x += 15
#   else:
#     x += 1
#   print(i, x)
#   i += 1

  print(i)
  print()
  # charlieFunction("charlieFunction") 

# Learning Exercise: Combining While
# What is output by the following programs?
def deltaFunction(i):

# string = “HELLO”
# x = 0
# while string[x] != ‘L’:
#    print(string[x], end=”... “)
#    x += 1
# print(“\n”, string, “first L is at”, x)

  print(i)
  print()
  # deltaFunction("deltaFunction") 

def gammaFunction(i):

# # Assume the user enters the following:
# # hello goodbye cat dog DONE done
# list = []
# prompt = “Please enter word, ‘done’ to finish ”
# response = input(prompt)
# while response != “done”:
#     list.append(response)
#     response = input(prompt)
# print(sorted(list))
  
  print(i)
  print()
  # gammaFunction("gammaFunction") 

def hectorFunction(i):
  x = 0
  while x < 20:
    if x > 5:
      if x % 2 == 0:
        x *= 2
      else:
        x *= -1
    else:
      x += 10
    x += 1
  print(x)
  # print(i)
  print()
  # hectorFunction("hectorFunction") 

def indigoFunction(i):
  print(i)
  print()
  # indigoFunction("indigoFunction") 

def jdeltaFunction(i):
  print(i)
  print()
  # jdeltaFunction("jdeltaFunction") 

def main():
  # # Testing Template
  # test_input = ["hellothere", "42 degrees Celsius", "eeeeeee"]
  # test_output = ["HELOTHRE", "42DEGREES CELSUS", "EEEEE"]
  # for i in range(len(test_input)):
  #   print("Testing: ", test_input[i] +":", mangle(test_input[i]) == test_output[i])
  print("Day12_22_ReadingWhiles")
  print()
  print()
  alphaFunction("alphaFunction") 
  betaFunction("betaFunction") 
  charlieFunction("charlieFunction") 
  deltaFunction("deltaFunction")
  gammaFunction("gammaFunction") 
  hectorFunction("hectorFunction") 
  indigoFunction("indigoFunction") 
  jdeltaFunction("jdeltaFunction") 
  # epsilonFunction("epsilonFunction") 
  # omicronFunction("omicronFunction") 

# by, TurtleWolfe.com
# While Loops (2 hours)
# Day 12
#################################
  print()
main()  # end of Curled Main.. 
###########################
#################