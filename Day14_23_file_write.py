# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge

# Day 14
# Reading & Writing Files (2 hours)
#################################################
# Read in a file called add.txt & display it to the screen
# Make sure add.txt is in the same project
#################################################

def alpha_Function(i):
    # Writing Files Practice

    # Write a python program that reads in a text file
    #  and prints all the lines back out with a dash in front.

    # Example program run:
    # > python3 read_file.py

    # Input File contents:
    # hello
    # goodbye
    # 1234

    # Outputs:
    # -hello
    # -goodbye
    # -1234

    # create a new file object, in "read" mode
    file1 = open('text4.txt', 'r')
    # Using readlines()
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        # print("Line{}: {}".format(count, line.strip()))
        print("-{}".format(line.strip()))
    # print(i)
    print()
    return(i)
    # alpha_Function()


def beta_Function(i):
    # Write a python program that asks the user for the name of a file,
    #  and then repeatedly asks the user to enter a number,
    #  entering the number ‘0’ when finished.
    #  Output each of these numbers to the file on a separate line.

    # Example program run:
    # > python3 write_numbers.py

    # User inputs:
    # out.txt
    # 25
    # 34
    # 14
    # 0

    # Output file out.txt created with the following contents:
    # 25
    # 34
    # 14

    # create a new file object, in "write" mode
    outfilename = input("What is the name of your output file? ")
    outfilename = open(outfilename, "w")  # w to write

    # Writes content from a user to a file
    # outfilename = open("out.txt", "w")  # a to append
    while i != 0:
        i = int(input("enter a number, or '0' when done: "))
        # write the user's input to the file
        if i != 0:
            print(i, file=outfilename)
        # print(i, file=outfilename)
    # close the file with the method "close"
    outfilename.close()

#################################################
    file1 = open('out.txt', 'r')
    # Using readlines()
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        # print("Line{}: {}".format(count, line.strip()))
        print("{}".format(line.strip()))
#################################################
# read outFile.txt
    # print(str(outfilename))
#################################################

    # print(i)
    print()
    return(i)
    # beta_Function()


def charlie_Function(currentFile):
    # Write a python program that reads 3 files called
    #  test1.txt, text2.txt, and text3.txt,
    #  counts the number of lines in each file,
    #  and prints out the number of lines to a file counts.txt.

    # Example program run:
    # > python3 read3_files.py

    # text1.txt:            text2.txt:            text3.txt:
    # Hello                Goodbye            End of semester
    # how are you?        Number 5            approaches!
    # Good.                Nice knowing you
    # See you later.

    # Output file counts.txt created with the following contents:
    # text1.txt : 4
    # text2.txt : 3
    # text3.txt : 2

    # Hint: How to be DRY & not copy/paste the code 3 times?
    #  There are 2 approaches:
    # Create a function with the filename as a parameter & call it 3 times
    # Create a list of the file names and loop over the file names
    #################################################
    # currentFile = open("text1.txt", "r")
    file1 = open(currentFile, 'r')
    # Using readlines()
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        # print("Line{}: {}".format(count, line.strip()))
        # print("{}".format(line.strip()))
#################################################
    # print()
    print(currentFile, ":", count, "lines")
    return(currentFile)
    # charlie_Function()


def delta_Function(listOfFiles):
    # def delta_Function(currentFile):
    # Create a program similar to above
    #  that counts the number of words in the files as well.
    #  After printing out information about each file,
    #  this program should also print the total number of lines & words
    #  in all 3 files. You can use the string split function
    #  to split a line of input into a list of words
    #  by splitting the line on spaces.

    # Example program run:
    # > python3 read3_files2.py

    # text1.txt:            text2.txt:            text3.txt:
    # Hello                Goodbye            End of semester
    # how are you?        Number 5            approaches!
    # Good.                Nice knowing you
    # See you later.

    # Output file counts.txt created with the following contents:
    # text1.txt : 4 lines, 8 words
    # text2.txt : 3 lines, 6 words
    # text3.txt : 2 lines, 4 words
    # TOTAL: 9 lines, 18 words
    #################################################
    for currentFile in listOfFiles:
        # currentFile = open("text1.txt", "r")
        file1 = open(currentFile, 'r')
        # Using readlines()
        Lines = file1.readlines()

        # currentFile.close()

        count = 0
        # Strips the newline character
        for line in Lines:
            count += 1
        # print(currentFile, ":", count, "lines", ",", count*2, "words")
        # print(currentFile, ":", count, "lines", ",", count, "words")

        # data = file1.read()
        # words = data.split()

        # print('Number of words in text file :', len(words))

#################################################
# https://www.geeksforgeeks.org/python-program-to-count-words-in-text-file/
        # creating variable to store the
        # number of words
        number_of_words = 0

        # Opening our text file in read only
        # mode using the open() function
        # with open(r'text1.txt', 'r') as file:
        with open(currentFile, 'r') as file:

            # Reading the content of the file
            # using the read() function and storing
            # them in a new variable
            data = file.read()

            # Splitting the data into separate lines
            # using the split() function
            lines = data.split()

            # Adding the length of the
            # lines in our number_of_words
            # variable
            number_of_words += len(lines)

        # Printing total number of words
        # print(number_of_words)
        print(currentFile, ":", count, "lines", ",", number_of_words, "words")

#################################################
    return(currentFile)
    # delta_Function()


def epsilon_Function(i):
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

    print(i)
    return(i)
    # epsilon_Function()


def main():
    print()
    # alpha_Function("alpha_Function")
    # beta_Function("beta_Function")
    # charlie_Function("text1.txt")
    # charlie_Function("text2.txt")
    # charlie_Function("text3.txt")
    delta_Function(["text1.txt", "text2.txt", "text3.txt"])
    # epsilon_Function("epsilon_Function")


main()
#################################################
# Your program should be ordered as follows:
#  leading comment, any imports, function definitions,
#  then lastly a main
# When testing your functions (by calling them in main),
#  make sure to also include some descriptive output
#  to determine if your test passed or failed
