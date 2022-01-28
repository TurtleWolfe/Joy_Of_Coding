# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge
def pick_A_Beatlez(str): 
    # John Lennon is my favorite beatle
    # Paul McCartney is my favorite beatle
    # George Harrison is my favorite beatle
    # Ringo Star is NOT my favorite beatle
  beatles = "John, Paul, George, Ringo Starr"
  list = beatles.split(", ")
  i=0
  while list[i] != "Ringo Starr":
    print(list[i], "is my favorite Beatle")
    i += 1
  print(list[i], "is NOT my favorite Beatle")
  print()
  return(str)

def rw2(x,i): 
  # x=-3
  # i=1
  while i > x:
    if x > 0:
      # odds
      if i % 2 == 1:
        x+= 3
      else:
        x *= 2
    # even
    elif i % 2 == 0:
      x += i
    else:
      x -= 1
    i += 1
    print(i,x)
  print()
  # print(str)
  return(str)

def rw3(list, tot, i):

  # list = [-3, 12, 4, -1, 2, 7, -5]
  # tot = 0
  # i = 0
  while list[i] % 2 == 0 or list[i] < 0:
    num = list[i]
    if num % 3 == 0:
      if num < 0:
        tot += e(num)
      else:
        tot += f(num)
    elif num % 2 == 0:
      tot -= g(num)
    elif num < 0:
      tot += h(num)
    else:
      tot -= h(num)
    i += 1
  print("what is this?:",i, num, tot, sep="\t")

  # print(tot)
  # print()
  print("list:",list)
  print("total:",tot)
  print("index:",i)
  print()  
  print()  
  return(list)

def e(x):
  return g(h(f(x)))

def f(x):
  return h(g(x))

def g(x):
  return 2 * x

def h(x):
  return x + 2

def main():
  print("Day12_25_ReadingWhilesEnrichment")
  print()
  # pick_A_Beatlez("John Lennon is my favorite beatle")
  # pick_A_Beatlez("Paul McCartney is my favorite beatle")
  # pick_A_Beatlez("George Harrison is my favorite beatle")
  # pick_A_Beatlez("Ringo Star is NOT my favorite beatle")
  # pick_A_Beatlez("The Beatles")
  # pick_A_Beatlez("John Lennon") 
  # pick_A_Beatlez("Ringo Star")
  # rw2(-3,1)  
  # rw2(-9,6)  
  # rw2(-9,3)  
  print()
  rw3([-3, 12, 4, -1, 2, 7, -5],0,0)
  rw3([-3, 12, 4, -1, 2, 7, -5],-6,-6)
  # print(rw3("rw3"))

# by, TurtleWolfe.com
# While Loops (2 hours)
# Day 12
#################################
  print()
main()  # end of Curled Main.. 
###########################
#################