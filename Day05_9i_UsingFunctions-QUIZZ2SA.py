# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge
def alpha_Function(namE, agE):
# Day05_9i_UsingFunctions-QUIZZ2SA
    #     2 hours
#num.py
  # print(i)
  # firstName = "TurtleWolfe"
  # print("Day05_9i_UsingFunctions-QUIZZ2SA.py,",i+"!")
  # print()
######################################
  # Fun with Functions!
  # String fun
  phrase = "Day05_9i_UsingFunctions-QUIZZ2SA.py"
  # phrase = "Quiz 2 Self-Assessment: Using Functions Module"
  # print(phrase.upper())
  print(phrase)
  # print(phrase.title())
  # print(phrase.count("o"))
  # print(phrase.lower().islower())
  # print(phrase.isdecimal())
######################################
# Quiz 2 Self-Assessment: Using Functions Module

# Write a program num.py that asks the user for their name and their favorite number as input and outputs the following:
# The user’s name followed by “ ’s number” centered (assume 80 characters width) and all in title case. For the apostrophe to work, you may need to strip spaces from the right of the name.
# Whether or not the number is a decimal number
# The number of 1’s in the number
# The factorial of the absolute number rounded to 0 decimals
# The log base 5 of the absolute value of the number
# An example run of this program might be:
# > Please enter your name: EMILY
# > Please enter your favorite number: 17


# Don’t forget to use meaningful variable names and add comments.

# Once you’re satisfied that your programs are working correctly, please take screenshots using the test case above & upload to canvas.
 
  # print()
  # r1 = input("What is your name? : ")
  # namE = r1
  # r2 = input("and your age? : ")
  # agE = r2
  # print()

# The user’s name followed by “ ’s number” centered (assume 80 characters width) and all in title case. For the apostrophe to work, you may need to strip spaces from the right of the name.
# >             Emily’s Number
  # print(namE.title()+"'s ",agE)

  # str = "this is string example....wow!!!"
  strNG = str((namE.title()+"'s ",agE))
  strNG = namE.title()+"'s "+agE
  print (strNG.center(30, ' '))
                                 # str.center(width[, fillchar])


# > Is decimal? True
  print("Is decimal?: ",agE.isdecimal())
# > How many 1’s? 1
  print("How many 1s: ",agE.count("1"))

# Python code to demonstrate naive method
# to compute factorial
  n = int(agE)
  fact = 1
  
  for i in range(1,n+1):
      fact = fact * i
      
  # print ("The factorial of ", str(n)," is : ",end="")
  # print (fact)
# > Factorial: 355687428096000
  print("Factorial:   ",fact)

  import math
  agE = int(agE)
# > Log base 5: 1.7603744277225881
  print("Log base 5:  ",math.log(agE, 5))
  print("")
  # alpha_Function("EMILY", "17") 
  return(namE, agE)
  # alpha_Function("num.py") 

def main():
# print("Day05_9i_UsingFunctions-QUIZZ2SA") 
  alpha_Function("EMILY", "17") 
# by, TurtleWolfe.com
# Day05_9i_UsingFunctions-QUIZZ2SA

#################################
  print() # may duplicate blank line from main
main()  # end of Curled Main.. 
###########################
#####################################