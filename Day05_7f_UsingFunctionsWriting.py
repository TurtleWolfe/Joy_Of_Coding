# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge
def alpha_Function(i):
# Day05_7f_UsingFunctionsWriting
    #     2 hours
#mad.py

# Write a program mad.py that asks the user to enter a phrase, and then prints out the following:

# The “mad” version of the phrase in all caps.
# A confused (i.e., mad) version of the phrase where all letter e’s are replaced by x’s.
# The maddest of all: print whether the phrase is printable.

# Hint: To find how you can print if something is printable, do the following:
# Convert your input to a string with str(input(“…”)) so that PyCharm “knows” that your input variable is a string
# Type the name of your variable
# Type dot (“.”)
# Scroll through the list of functions & see if any look promising
  print()
  # phraseMadLib = input("please enter a phrase? ")
  phraseMadLib = i
  # print("Mad Phrase: ", phraseMadLib)
  print(phraseMadLib.upper())
  print(phraseMadLib.replace("e", "x"))
  print(phraseMadLib.isprintable())

  # print()
  # print(i)
  print()
  return(i)
  # alpha_Function("mad.py") 

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
  # Write a program maths.py that takes a number as input from the user and prints out the following information:
# The absolute value of the number.
# The floor of the number using the math module (e.g., floor(3.75) is 3).
# The number rounded to 2 decimal places.
  # response = input("please enter a numberic value? ")  # crashes with text or "string"
  response = i
  # if response type numeric == true?
    
  mathNumBer = float(response)  # crashes with text or "string"
# absolute Value
  print("absolute: ",abs(mathNumBer))

# Import math library
  import math

# Round numbers down to the nearest integer
  # print           (math.floor(0.6))
  print("floored:  ",math.floor(mathNumBer))
  limit_float = round(mathNumBer, 3)
  print("rounded:  ",limit_float)
# float = 2.154327
  format_float = "{:.3f}".format(mathNumBer)
  print("2decimal: ",format_float, )
  # print(math.floor(mathNumBer), " :The number rounded to 2 decimal places.")

  print(i)
  # print()
  return(i)
  # charlie_Function("maths.py") 

def main():
  print("Day05_7f_UsingFunctionsWriting.py") 
  alpha_Function("beekeeper") 
  # beta_Function(53.48,.07,.18) 
  charlie_Function(-3.456789) 
  # print()
  # charlie_Function(3.456789) 
  # print()
  # charlie_Function(-3.4563789) 

# by, TurtleWolfe.com
# Day05_7f_UsingFunctionsWriting
  # print() # may duplicate blank line from main
main()  # end of Curled Main.. 
###########################
#####################################