# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge
def alpha_Function(numBer):
# Day06_2LE-ForLoopsWriting1
    #     2 hours
  for i in range(numBer):
    print(i+1)
  # print(numBer)
  return(numBer)
  # alpha_Function("namE") 

def beta_Function(numBer):
  for i in range(2,numBer+3,3):
    print(i)
  # print(numBer)
  return(numBer)
  # beta_Function("namE")
   
def charlie_Function(numBer):
  for i in range(numBer,1,2):
    print(i, end=" ")
  # print(numBer)
  return(numBer)
  # charlie_Function("namE") 

def delta_Function(char,brK,roW):
  for i in range(roW):
    print(char * brK)
  # print(numBer)
  return(char, brK, roW)
  # delta_Function("namE") 

def epsilon_Function(numBer):
  # Write a for loop that prints the letters
  #  in “CSCI 150” on separate lines.
  for i in numBer:
    print(i)
  # print(numBer)
  return(numBer)
  # alpha_Function("namE") 

def feta_Function(firsT, lasT):
  # Using the range function,
  #  print the numbers from 1 to 10 (inclusive).
  #  Each number should be on a separate line.
  for i in range(firsT,lasT+1):
    print(i)
  # print(numBer)
  return(firsT, lasT+1)
  # beta_Function("namE")

def main():
  print("Day06_2LE-ForLoopsWriting1.py") 
  # alpha_Function(5) 
  # beta_Function(11) 
  # charlie_Function(-10) 
  # delta_Function("*",4,4) 
  # delta_Function("TurtleWolfe.com ",4,4) 
  # epsilon_Function("CSCI 150") 
  feta_Function(1,10) 
  # feta_Function(7,14) 
  # gamma_Function(-10) 
  # hector_Function("*",4,4) 
# by, TurtleWolfe.com
# Day06_2LE-ForLoopsWriting1

#################################
  print() # may duplicate blank line from main
main()  # end of Curled Main.. 
###########################
#####################################