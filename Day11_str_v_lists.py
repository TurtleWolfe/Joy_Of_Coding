# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge

# Day 11
# List v Strings
# What is output?

list = ["M", "T", "W", "R", "F"]
str = "days of the week"

print(len(list))
# 5
print(len(str))
# 16
list[-2] = "Th"
#  False
str.upper()
# DAYS OF THE WEEK

print(list)
# M T W R F
print(str)
# days of the week

str = "dow"
str = str.upper()
print(str)
# DOW

def main():
  print("Day 11 Lists & Strings")
  print()

  # Testing Template

    
main()