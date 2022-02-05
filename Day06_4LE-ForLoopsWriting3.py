# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge
def alpha_Function(starT, stoP, steP):
# Day06_4LE-ForLoopsWriting3
    #     2 hours
# Using the range function,
#   print the multiples of 4 from -16 through 16 (inclusive).
#   The numbers should each be separated by a dash.
#   There should not be a dash after the final number (16).
  for i in range(starT,stoP,steP):
    print(i, end="/")
  print(stoP)
  # print(numBer)
  return(starT,stoP,steP)
  # alpha_Function("starT, stoP, steP") 

def beta_Function(starT,stoP,steP):
# Using the range function,
#  print the multiples of 10 from -10 to 100 (inclusive).
#  Each number should be separated by “...” and a space.
  for i in range(starT,stoP,steP):
    print(i, end="... ")
  print(stoP)
  # print(numBer)
  return(starT,stoP,steP)
  # beta_Function(starT,stoP,steP)
   
def sumTenPy(averageInputs):
# Create a program sum10.py
#  that calculates and prints the sum
#  of 10 real (i.e., decimal) numbers
#  entered by the user. Make sure you ask
#  (i.e., prompt) the user to enter each number
#  (the user will hit enter after each number). 
  sum = 0
  for i in range(averageInputs):
    print('Enter a number:')
    x = input()
    # print('Hello, ' + x) 
    sum = sum + int(x)
  print()
  print('The average\n of the numbers\n  you entered is', sum/averageInputs)
  return(averageInputs)
  # sumTenPy("namE") 

def main():
  print("Day06_4LE-ForLoopsWriting3.py") 
  alpha_Function(-16,16,4) 
  beta_Function(10,100,10) 
  sumTenPy(3)
# Day06_4LE-ForLoopsWriting3

#################################
  print() # may duplicate blank line from main
main()  # end of Curled Main.. 
###########################
#####################################