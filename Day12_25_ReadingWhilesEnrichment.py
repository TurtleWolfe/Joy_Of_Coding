# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge

# Day 12
# While Loops (2 hours)
def pick_A_Beatlez(str): 
  beatles = "John Lennon, Paul McCartney, Gearge Harrison, Ringo Starr"
  list = beatles.split(", ")
  i=0
  while list[i] != "Ringo Starr":
    print(list[i], "is my favorite Beatle")
    i += 1
  print(list[i], "is NOT my favorite Beatle")

# John Lennon is my favorite beatle
# Paul McCartney is my favorite beatle
# George Harrison is my favorite beatle
# Ringo Star is NOT my favorite beatle
  print()
  return(str)

def main():
  print("Day12_25_ReadingWhilesEnrichment")
  print()
  # print(pick_A_Beatlez("John Lennon is my favorite beatle"))
  # print(pick_A_Beatlez("Paul McCartney is my favorite beatle"))
  # print(pick_A_Beatlez("George Harrison is my favorite beatle"))
  # print(pick_A_Beatlez("Ringo Star is NOT my favorite beatle"))
  # print()
  # print(pick_A_Beatlez("The Beatles"))  
  # print(pick_A_Beatlez("John Lennon"))  
  print(pick_A_Beatlez("Ringo Star"))  
  print()
main()  # end of Curled Main.. 