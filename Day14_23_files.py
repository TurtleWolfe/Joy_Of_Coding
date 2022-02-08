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

    # Write a python program that reads in a text file and prints all the lines back out with a dash in front.

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
    print(i)
    return i


def beta_Function(i):
    # Write a python program that asks the user for the name of a file, and then repeatedly asks the user to enter a number, entering the number ‘0’ when finished. Output each of these numbers to the file on a separate line.

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
    print(i)
    return i


def charlie_Function(i):
    # Write a python program that reads 3 files called test1.txt, text2.txt, and text3.txt, counts the number of lines in each file, and prints out the number of lines to a file counts.txt.

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

    # Hint: How to be DRY & not copy/paste the code 3 times? There are 2 approaches:
    # Create a function with the filename as a parameter & call it 3 times
    # Create a list of the file names and loop over the file names
    print(i)
    return i


def delta_Function(i):
    # Create a program similar to above that counts the number of words in the files as well. After printing out information about each file, this program should also print the total number of lines & words in all 3 files. You can use the string split function to split a line of input into a list of words by splitting the line on spaces.

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

    print(i)
    return i
#################################################


def main():

    # Writes content from a user to a file

    PROMPT = "Enter the new line in the file: "

    outfilename = input("What is the name of your output file? ")
    numLines = eval(input("How many lines do you want to write? "))

    # create a new file object, in "write" mode
    dataFile = open(outfilename, "w")  # a to append

    for x in range(numLines):
        userinput = input(PROMPT)
        # write the user's input to the file
        print(userinput, file=dataFile)

        # close the file with the method "close"
    dataFile.close()
    print()
    alpha_Function("alpha_Function")
    beta_Function("beta_Function")
    charlie_Function("charlie_Function")
    delta_Function("delta_Function")


main()
#################################################
# Your program should be ordered as follows: leading comment, any imports, function definitions, then lastly a main
# When testing your functions (by calling them in main), make sure to also include some descriptive output to determine if your test passed or failed
