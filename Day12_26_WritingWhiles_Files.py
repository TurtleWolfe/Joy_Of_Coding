# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge

# Day 12
# While Loops (2 hours)
#################################################

# (WW1) Using a while loop, write a program that prints out the even numbers from 2 to 20.



















# (WW2) Write a program that gets a string as input from the user, and finds the index of the first occurrence of the letter ‘e’ (upper or lower case). Your program should define a function that takes a string as a parameter and returns the e index. If the string does not contain an e, the function should return -1.

# Example call        Returns
# find_e(“hello”)     1
# find_e(“how”)        -1













# (WW3) Create a program that allows the user to enter a list of strings, prints them out in sorted order, and prints the number of strings entered as well as the total number of characters in all the strings in the list. Prompt the user to continue entering phrases, and enter ‘Q’ when finished. If the user enters an empty string, output an informative error message. Test your program.

# Example program run:
# > python3 count_strings.py
# > Please enter a phrase (‘Q’ to finish) hello
# > Please enter a phrase (‘Q’ to finish) goodbye
# > Please enter a phrase (‘Q’ to finish) 
# > Please enter non-empty strings or ‘Q’ to quit.
# > Please enter a phrase (‘Q’ to finish) q
# > Please enter a phrase (‘Q’ to finish) Q
# > You entered 4 strings and 29 characters.
# (WF1) Write a program that reads in a file of strings (one per line), creates a new file, and prints out each line followed by the number of characters in each line. At the end of the new file your program should print the total and average number of characters per line. Test that your program works with the following file of strings (you need to create this file in PyCharm):


# Top 10 Movies of 2015
# Star Wars Episode VII: The Force Awakens
# Jurassic World
# The Avengers: Age of Ultron
# Inside Out
# Furious 7
# American Sniper
# Minions

# The Hunger Games: Mockingjay – Part 2
# The Martian
# Cinderella

# Creates the following output file:
# Top 10 Movies of 2015 : 21
# Star Wars Episode VII: The Force Awakens : 40
# Jurassic World : 14
# The Avengers: Age of Ultron : 27
# Inside Out : 10
# Furious 7 : 9
# American Sniper : 15
# Minions : 7
#  : 0
# The Hunger Games: Mockingjay – Part 2 : 37
# The Martian : 11
# Cinderella : 10
# 201 characters and 16.75 characters per line













# (WF2) Write a program that reads in a file of numbers (one per line) and prints out the sum, mean, and median of the numbers. Test that your program works with the following files of numbers (you will need to create these in PyCharm):





# 3
# 30
# 4
# 0
# 0
# 4
# 45
# 25
# 23
# 2

# 3
# 30
# 4
# 0
# 0
# 45
# 25
# 23
# 2



# Outputs for first file of numbers:
# Sum: 136
# Mean: 13.6
# Median 4.0

# Outputs for second file of numbers:
# Sum: 132
# Mean: 14.666666666666666
# Median 4











# Challenge Exercise

# (LC) Implement & test the function mix_lists(list1, str2) which returns a combined string. E.g.:
# # Using abbreviated list format below. Assume each letter
# # is it’s own list element: [he] = [‘h’, ‘e’]
# mix_lists([hello], [there])     returns [htehlelroe]
# mix_lists([1234], [abcd])     returns [1a2b3c4d]
# mix_lists([12], [abcd])         returns [1a2bcd]
# mix_lists([1234], [ab])         returns [1a2b34]






















# Hints:
# Just try to print the list/file in the right order, then worry about returning 
# What happens if one list/file is longer than the other? There are two approaches:
# Loop over the shortest list & then loop over the longest list
# Loop over the longest list & have an if inside the loop for the shorter list

# Challenge Exercise

# (FC) Implement & test the function 
# mix_files(fname1, fname2, outfile) which returns a combined string. E.g.:


        




















#################################################


def main():
  print("Day 12 While Loops")
  print()

  # # Testing Template
  # test_input = ["hellothere", "42 degrees Celsius", "eeeeeee"]
  # test_output = ["HELOTHRE", "42DEGREES CELSUS", "EEEEE"]
  # for i in range(len(test_input)):
  #   print("Testing: ", test_input[i] +":", mangle(test_input[i]) == test_output[i])
    
main()