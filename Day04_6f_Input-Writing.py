# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge
def movie_rating(i):
#movie_rating.py
# Day04_6f_Input-Writing
    #     2 hours
# Learning Activity:
# Writing Input/Output (I/O) Programs

# Write a program movie_rating.py
#  that asks the user to input a rating
#  (1-5 stars) for your favorite movie.
#  Print the difference between the user’s rating and yours.
#  You should store your movie rating in a different variable
#  from the rating that the user inputs.
  movieBoolean = input("Have you ever seen Star Wars? ")
  print()
  # if movieBoolean yes?:
    # else:
  # print("Do you rate it higher than a four?", Movie, "!")
  q2 = "On a scale of 1 to 5, what did you think of it? "
  rating = eval(input(q2))#crashes if 'text' input on 2nd question
  # rating = input(q2)#crashes if 'text' input on 2nd question
  myRating = 5
  print("  Cool!  I like it", myRating - rating, "more than you do\n  so I'm the bigger fan boy\n  because I never would finish all the PreQuels!")
  print(i)
  print()
  # movie_rating("movie_rating.py") 
  return(i)
  # movie_rating("movie_rating.py") 

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

def grandIose(i):
# Create a program grandiose.py
#  that asks the user to enter an adjective
#  that is a synonym for faster.
#   Use the adjective they input when you respond
#  that your laptop is so much faster than theirs,
#  you are surprised that their laptop can… (fill in the blank). 
  adjecTive = input("asks the user to enter an adjective? ")
  # rating = eval(input(q2))#crashes if 'text' input on 2nd question
  # rating = input(q2)#crashes if 'text' input on 2nd question
  print("  Cool!  I like it \n  that your laptop is so much faster than theirs, \n  you are surprised that their laptop can… \n  ", adjecTive)
  print()
  print(i)
  grandIose("grandIose is looping again!") 
  return(i)

def main():
  # print()
  print("Day04_6f_Input-Writing") 
  print("06-Input-Writing") 
  print()
  # movie_rating("CowBoy") 
  # print()
  movie_rating("movie_rating.py") 
  # print()
  # beta_Function(53.48,.07,.18) 
  grandIose("grandiose.py") 

# by, TurtleWolfe.com
# Day04_6f_Input-Writing

#################################
  print() # may duplicate blank line from main
main()  # end of Curled Main.. 
###########################
#######################################