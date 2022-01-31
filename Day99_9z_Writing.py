# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge
def alpha_Function(i):
# Day04_6f_Input-Writing
    #     2 hours
#movie_rating.py
  # print(i)
  # firstName = "TurtleWolfe"
  print("Hello,",i+"!")
  print()
# Learning Activity:
# Writing Input/Output (I/O) Programs

# Write a program movie_rating.py
#  that asks the user to input a rating
#  (1-5 stars) for your favorite movie.
#  Print the difference between the user’s rating and yours.
#  You should store your movie rating in a different variable
#  from the rating that the user inputs.
  color = input("What is your favorite color? ")
  print()
  print("Cool!  My favorite color is _light_", color, "!")

  q2 = "On a scale of 1 to 10, how much do you like Urban Fire? "
  rating = eval(input(q2))
  print("Cool!  I like it", rating*1.8, "!")
  print(i)
  return(i)
  # alpha_Function("movie_rating.py") 

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
# Create a program grandiose.py
#  that asks the user to enter an adjective
#  that is a synonym for faster.
#   Use the adjective they input when you respond
#  that your laptop is so much faster than theirs,
#  you are surprised that their laptop can… (fill in the blank). 
  print(i)
  print()
  return(i)
  # charlie_Function("charlie_Function") 

def main():
  # print()
  print("Day04_6f_Input-Writing") 
  print("06-Input-Writing") 
  print()
  # alpha_Function("CowBoy") 
  # print()
  alpha_Function("movie_rating.py") 
  print()
  # beta_Function(53.48,.07,.18) 
  charlie_Function("grandiose.py") 

# by, TurtleWolfe.com
# Day04_6f_Input-Writing

#################################
  print() # may duplicate blank line from main
main()  # end of Curled Main.. 
###########################
#######################################