# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge
def alpha_Function(firsT,lasT):
# Day06_3LE-ForLoopsWriting2
    #     2 hours
# Using the range function, print the multiples of 5 from 10 through -25 (inclusive). The numbers should each be separated by a space. (Hint: use the end parameter to the print function like we did in for_range.py). Don’t forget to print a newline after this loop by calling print() with no parameters.
  for i in range(firsT,lasT-1,-5):
    if i > -1:
      print(" "+str(i))
    else:
      print(i)
  print()
  return(firsT, lasT+1)
  # alpha_Function("namE") 

def beta_Function(starT, stoP, steP):
# Using the range function, print the multiples of 3 from -3 to 21 (inclusive). Each number should be separated by a comma and a space. There should not be a comma after the final number (21).
  for i in range(starT,stoP,steP):
    print(i, end=", ")
  print(stoP)
  # print(numBer)
  return(starT,stoP,steP)
  # beta_Function("namE")
   
def avgPy(averageInputs):
  # Create a program avg.py that calculates and prints the average of 10 real (i.e., decimal) numbers entered by the user. Make sure you ask (i.e., prompt) the user to enter each number (the user will hit enter after each number). 
  sum = 0
  for i in range(averageInputs):
    print('Enter a number:')
    x = input()
    # print('Hello, ' + x) 
    sum = sum + int(x)
  print()
  print('The average\n of the numbers\n  you entered is', sum/averageInputs)
  return(averageInputs)
  # avgPy("namE") 

def main():
  print("Day06_3LE-ForLoopsWriting2.py") 
  # alpha_Function("Day06_3LE-ForLoopsWriting2.py") 
  alpha_Function(10,-25) 
  # alpha_Function(10,25) 
  beta_Function(-3,21,3) 
  avgPy(3) 
  # avgPy(10) 
# by, TurtleWolfe.com
# Day06_3LE-ForLoopsWriting2

#################################
  print() # may duplicate blank line from main
main()  # end of Curled Main.. 
###########################
#####################################