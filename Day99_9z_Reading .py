# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge
def alpha_Function(i):
# Day04_6e_Input-Reading
    #     2 hours
#hello_me.py
  # print(i)
  # firstName = "TurtleWolfe"
  print("Hello,",i+"!")
  print()
######################################
# What will this program do?
# Try to predict what the code will do without running it…
# 06.code/input_demo.py
# Questions:
# What do you think the input function does?
# On line 9, what is the purpose of the eval function?

# In the code above, identify the following:
# Comments
# Variables
# Function calls
#  Expressions
# Assignments
# Literals 

######################################
# Demonstrate numeric and string input
# What do you think happens when this program is run?

  color = input("What is your favorite color? ")
  print()
  print("Cool!  My favorite color is _light_", color, "!")

  q2 = "On a scale of 1 to 10, how much do you like Urban Fire? "
  rating = eval(input(q2))
  print("Cool!  I like it", rating*1.8, "!")
  print(i)
  return(i)
  # alpha_Function("hello_me.py") 

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
  # print()
# 
  print("Day04_6e_Input-Reading") 
  print("input_demo.py") 
  print()
  alpha_Function("CowBoy") 
  print()
  print()
  beta_Function(53.48,.07,.18) 

# by, TurtleWolfe.com
# Day04_6e_Input-Reading

#################################
  print() # may duplicate blank line from main
main()  # end of Curled Main.. 
###########################
#####################################