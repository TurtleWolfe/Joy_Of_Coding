# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge
def alpha_Function(i):
# Day 03
    # Arithmetic
    #     2 hours
    
  # Evaluate the following expressions:
  print("1. Evaluate these expressions:") 
      # 17 % 3
  print(17 % 3)
      # 17 // 3
  print(17 // 3)
      # 7 / 2
  print(7 / 2)
      # 7 // 2
  print(7 // 2)
      # 5 + 3 * 2
  print(5 + 3 * 2)
      # 2 * 3 ** 2
  print(2 * 3 ** 2)
      # -3 ** 2
  print(-3 ** 2)
      # (2 ** 3) ** 2
  print((2 ** 3) ** 2)
      # 2 ** 4 - 2 + 2 * 3
  print(2 ** 4 - 2 + 2 * 3)
      # 5 - 6 * (1 + 4)
  print(5 - 6 * (1 + 4))
  # print(i)
  print()
  return(i)
  # alpha_Function("1. Evaluate these expressions:") 

def beta_Function(i,dir):
# If the following statements are executed in order, what will be the value of each variable?
  a = 5
  b = 3
  y = a + -1 * a
  z = a + y / 2
  c = a + 3
  # d = (7 + x) * z
  x = z * 2
  e = x % b
  f = 5 + c ** 2 - e
  b += 1
  a -= b
  # a += g
  g = 5

  # print(i)
  # print(dir)
  print("beta function, commented lines are out of order")
  return(i)
  # beta_Function("executed in order?") 
  # beta_Function("commented lines are out of order")

def charlie_Function(i):
  print("Tricky ones.. try to predict the output!")
  # print(type('True'))             # string
  # print(type("8.9"))              # string
  # print(type(2+4j))               # complex number
  print("num:",i)
  return(i)
  # Tricky ones... try to predict the output!
  # charlie_Function("types-tricky.py") 

def delta_Function(i):
  print()
  # Try to predict what the following program will print...
  #  ... then run it to find out!
  # print("Challenge: Make a prediction….")
  print("Try to predict what the following program will print...\n  ... then run it to find out!")
  # print()
  num = i
  oof = num + -1 * num
  nip = num + oof / 2
  num += 3
  # print("num:",num," oof:",oof," nip:",nip,"")

  # x equals nip 4 times 2 
  # 8
  x = nip * 2
  #  red equals
  #  (7+8) x 4
  #  15 x 4
  #  60
  red = (7 + x) * nip
  # print("red:",red,"  X:", x)             # string
  # print(.1 + .1 + .1)  
  # print()
  print("num:",i)
  return(i)
  # Tricky ones... try to predict the output!
  # delta_Function("variable-arithmetic.py") 


def main():
  print("Day03...")
  print("Learning Exercise: Arithmetic") 
  print()  
  alpha_Function("Day03...") 
  beta_Function(60,"left") 
  print()
  print("Challenge: Make a prediction….")
  print(" Try to predict what these programs will output\n  without running them first!")
  print()
  charlie_Function(3)
  # charlie_Function(8)
  delta_Function(4)

# by, TurtleWolfe.com
# Arithemitec (2 hours)
# Day 03
#################################
  print() # may duplicate blank line from main
main()  # end of Curled Main.. 
##########################
########################################