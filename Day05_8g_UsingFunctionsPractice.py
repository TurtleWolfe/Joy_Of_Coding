# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge
def alpha_Function(nouN, adJecTive):
# Day05_8g_UsingFunctionsPractice
    #     2 hours
#poem.py
  # print(i)
  # firstName = "TurtleWolfe"
  # print("Day05_8g_UsingFunctionsPractice.py,",i+"!")
  print()
######################################

# Using Functions Practice

# Create a program poem.py that asks the user for 2 parts of speech as input (a plural noun and an adjective) and outputs the following:

# ______ are red, violets are blue
# Monty Python is _______, woo hoo!

# Make sure to convert the strings to the proper case so that the first blank is capitalized and the second blank is all lower case.

# An example run of this program might be:
# > Please enter a plural noun: LEGOS
# > Please enter an adjective: AWESOME
# > Legos are red, violets are blue
# > Monty Python is awesome, woo hoo!
  # String fun
  phrase = "Day05_8g_UsingFunctionsPractice.py"
  print(phrase)
  print()
  # r1 = input("Please enter a plural noun: ")
  # nouN = r1
  # r2 = input("Please enter an adjective: ")
  # adJecTive = r2
  # print("Please enter a plural noun: LEGOS ", nouN)
  # print("Please enter an adjective: AWESOME ", adJecTive)
  print(nouN.title(),"are red, violets are blue")
  print("Monty Python is", adJecTive+ ", woo hoo!")
  print()
  return()
  # alpha_Function("poem.py") 

def charlie_Function(i):
# Write a program madfun.py that takes a decimal number as input from the user and prints out the following:
# The absolute value of the number 
# The number rounded to 0 decimal places
# The square root of the rounded number’s absolute value

  response = i
  # if response type numeric == true?
  # response = input("please enter a decimal value? ")  # crashes with text or "string"
    
  mathNumBer = float(response)  # crashes with text or "string"
  
# absolute Value
  print("absolute: ",abs(mathNumBer))

# Import math library
  import math

# The number rounded to 0 decimal places
  rndMathInput = round(mathNumBer)
  print("rounded:  ",rndMathInput)

# The square root of the rounded number’s absolute value
  print("squared:  ", math.sqrt(abs(rndMathInput)))
  
  
  # print(math.floor(mathNumBer), " :The number rounded to 2 decimal places.")
# Example runs of this program might be:
# > Please enter a number: 8.88
# > 8.88
# > 9.0
# > 3.0

# > Please enter a number: -24.75
# > 24.75
# > -25.0
# > 5.0


# Don’t forget to use meaningful variable names and add comments.


# Once you’re satisfied that your programs are working correctly, please take screenshots using the test cases above & upload to canvas to get feedback!
  # print(i)
  print()
  return(i)
  # charlie_Function("madfun.py") 

def main():
  # print("Day05_8g_UsingFunctionsPractice") 
  alpha_Function("nouns","adjective") 
  # beta_Function(53.48,.07,.18) 
  # charlie_Function("madfun.py") 
  # charlie_Function(8.88) 
  charlie_Function(-24.75) 

# by, TurtleWolfe.com
# Day05_8g_UsingFunctionsPractice

#################################
  print() # may duplicate blank line from main
main()  # end of Curled Main.. 
###########################
#####################################