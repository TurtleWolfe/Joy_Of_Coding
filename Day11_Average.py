# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge

# Day 11
# Lists & Strings (2 hours)

# Write a program that creates a list of 20 numbers input by the user and prints the average (mean) of the list.
def average(txm):
  total = 0
  for i in range(txm):
    n = float(input("Input: "))
    total += n
  return total/txm

# Write a function mangle that takes a string as a parameter and returns the string after performing the following operations: 
# Converting the string to all upper case letters
# Removing the third character
# Removing the third to last character
# Test that your function works. 

# Hint: Think about how you can remove from a string by creating a new string, adding characters to it, and omitting the characters you don’t want?

# Example function calls:    Output:
# print(mangle(“hellothere”))    HELOTHRE
# print(mangle(“42 degrees Celsius”))    42DEGREES CELSUS
# print(mangle(“eeeeeee”))    EEEEE
def mangle(str):
  str = str.upper()
  first = str[:2]
  # print(first)
  middle = str[3:-3]
  # print(middle)
  last = str[-2:]
  # print(last)
  str2= first+middle+last
  return(str2)

# Write a function, count_e, that takes a list of strings as a parameter and returns the total number of upper and lower case e’s (“E” and “e”) in all the strings in the list. Test that your function works with multiple examples.


# Example function call:    Output:
# print(count_e([“hi”, “hello”, “EEK!”]))    3

def count_e(list):
    tot = 0
    for string in list:
        tot += string.count("e")
        tot += string.count("E")
    return tot

# Write a function, count_vowels, that takes a list of strings as a parameter and returns the total number of upper and lower case vowels (A, E, I, O, U) in all the strings in the list.

# Example function call:    Output:
# print(count_vowels([“hi”, “hello”, “OOF!”]))    5
def count_vowels(list):
    tot = 0
    for string in list:
        for letter in string:
            if letter in "AEIOUaeiou":
                tot += 1
    return tot

def main():
  print("Day 11 Lists & Strings")
  print()
  # average()
  # print("Average: ", average(3))
  # print("Mangle:")#HELOTHRE
  # print(mangle("hellothere"))#HELOTHRE
  # print(mangle("42 degrees Celsius"))#  42DEGREES CELSUS
  # print(mangle("eeeeeee"))#    EEEEE
  print(count_e(["hi", "hello", "EEK!"]))#    3
  # print(count_e(["a", "b", "c"]))
  print(count_vowels(["hi", "hello", "OOF!"]))#    5

  # Testing Template
  test_input = ["hellothere", "42 degrees Celsius", "eeeeeee"]
  test_output = ["HELOTHRE", "42DEGREES CELSUS", "EEEEE"]
  for i in range(len(test_input)):
    print("Testing: ", test_input[i] +":", mangle(test_input[i]) == test_output[i])
    
main()