# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge

# Day 10
# Problem Solving with Functions

# # 4 is_even
# def is_even(num):
#   if (num % 2) == 0:
#       print("Even")
#   else:
#       print("Odd")
# print("### 4 is_even?")
# is_even(7)  
# is_even(12)  
# print()
def is_even(num):
  return num % 2 == 0

# # 5
# def calculate_total(meal, tax_rate, tip_rate):
#   mealTip = meal * tip_rate
#   mealTax = meal * tax_rate
#   total = meal + mealTax + mealTip
#   print("### 5 calculate_total")
#   print("$",total)
#   print()
# # 66.85
# calculate_total(53.48, .07, .18)

# # 6 hey
# def hey(num):
#   print(num * num)
# print("### 6 hey")
# hey(5)           # 25
# hey(0)           # 0
# hey(-3)          #  9
# print()

# # 7 there
# def there(n):
#   if (n >= 0):
#       print(2**n)
#   else:
#       print("0")
# print("### 7 there")
# there(5)         #   32
# there(0)         #   1
# there(3)         #   8
# there(-2)        #    0
# there(-6)        #    0
# print()

# # 8 are_we
# def are_we(num, str):
#   for i in range(num):
#     print("Are we",str,"yet?", end=' ')
#   print()
# print("### 8 are_we")
# are_we(2, "there")   # Are we there yet? Are we there yet?
# are_we(3, "50")   # Are we 50 yet? Are we 50 yet? Are we 50 yet?
# are_we(1, "")    # Are we  yet?
# are_we(0, "hey!")    
# print()

def main():
  print("4 is Even?: ", is_even(4))
  print("5 is Even?: ", is_even(5))
  print()
main()