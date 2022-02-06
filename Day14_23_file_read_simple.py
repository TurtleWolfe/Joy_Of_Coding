# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge

# Day 14
# Reading & Writing Files (2 hours)
#################################################
# Read in a file called add.txt & display it to the screen
# Make sure add.txt is in the same project
#################################################
def main():

  dataFile = open("add.txt")
  for line in dataFile:
    print(line.rstrip())
  dataFile.close()

main()
#################################################
# Your program should be ordered as follows: leading comment, any imports, function definitions, then lastly a main
# When testing your functions (by calling them in main), make sure to also include some descriptive output to determine if your test passed or failed