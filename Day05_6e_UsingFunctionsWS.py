# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge
def alpha_Function(i):
# Day05_6e_UsingFunctionsWS
    #     2 hours
#hello_me.py
  # print(i)
  # firstName = "TurtleWolfe"
  print("Day05_6e_UsingFunctionsWS.py,",i+"!")
  print()
######################################
  # Fun with Functions!

  # Generally, you should only use ONE of the following
  # import lines in your program... They are included
  # here for reference
  import math
  from math import sqrt

  # Math fun
  print("The square root of 25 is", sqrt(25))
  print("The log10 of 100 is", math.log10(100))
  print("The absolute value of -5 is", abs(-5))

  # String fun
  phrase = "find your Yoda"

  print(phrase.upper())
  print(phrase.title())
  print(phrase.count("o"))
  print(phrase.lower().islower())
  print(phrase.isdecimal())
######################################
# Learning Exercise: What will this program do?
# Try to predict what the code will do without running it…
# 06.code/fun.py

# Questions:
# What do you think import does?

# What is the difference between the import on line 6 vs 7? Does it    change how the math functions are called? In what way?

# Why do you think we need to import math, but not abs?

# How are the math functions called differently from the string        functions as compared to other functions we’ve seen so far?

# In the code above, identify the following:
# Comments
# Variables
# Function calls
#  Expressions
# Assignments
# Literals
# How can you find more information about python functions?
######################################
  print(i)
  return(i)
  # alpha_Function("fun.py") 

def beta_Function(meal, tax, tip):
#tips.py
# meal = 53.48
  print("Meal: $",meal)
# tax = .07
  print("Tax:  $",tax)
# tip = .18
  print("Tip:  $",tip)
  print()
  
  mealTax = meal * tax
  mealTip = meal * tip
  total = meal + mealTax + mealTip
  print("the cost of your meal\n  with tax & tip would be ")
  print("$",total)
  print()
# 66.85
  return(total)
  # beta_Function("tips.py") 

def charlie_Function(i):
  print(i)
  print()
  return(i)
  # charlie_Function("charlie_Function") 

def main():
  # print("Day05_6e_UsingFunctionsWS") 
  alpha_Function("fun.py") 
  # beta_Function(53.48,.07,.18) 
  # charlie_Function(53.48) 

# by, TurtleWolfe.com
# Day05_6e_UsingFunctionsWS

#################################
  print() # may duplicate blank line from main
main()  # end of Curled Main.. 
###########################
#####################################