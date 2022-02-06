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

    # Writes content from a user to a file
    PROMPT = "Enter the new line in the file: "

    outfilename = input("What is the name of your output file? ")
    numLines = eval(input("How many lines do you want to write? "))

    # create a new file object, in "write" mode
    # dataFile = open(outfilename, "a")  # a to append
    dataFile = open("add.txt", "a")  # a to append
    # dataFile = open(outfilename, "w")  # w to write

    for x in range(numLines):
        userinput = input(PROMPT)
        # write the user's input to the file
        print(userinput, file=dataFile)

    # close the file with the method "close"
    dataFile.close()


main()
#################################################
# Your program should be ordered as follows:
#  leading comment, any imports, function definitions,
#  then lastly a main
# When testing your functions (by calling them in main),
#  make sure to also include some descriptive output
#  to determine if your test passed or failed
