# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge

# Day 11
# Lists & Strings (2 hours)

# Write a function match that takes two strings as a parameter and returns how many letters the strings have in common. You should treat upper and lower case letters as the same letter (‘A’ == ‘a’, etc). Test that your function works. 

# Example function calls:                        Output:
# print(match(“hello”, “Healing”))            3
# print(match(“Healing”, “hello”))            3
# print(match(“hellllllo”, “Healllllling”))    3

def match(str, str2):
  matches = 0
  str = str.upper()
  print(str)
  str2 = str2.upper()
  print(str2)
  for i in range(len(str)):
    if (str[i] == str2[i]):
      matches += 1
  return matches

def main():
  print("Day 11 More Practice: Writing Lists & Strings")
  print()
  # Testing Template
  # print(match("hello", "Healing"))#          3
  # print(match("Healing", "hello"))#          3
  # print(match("hellllllo", "Healllllling"))# 3
main()