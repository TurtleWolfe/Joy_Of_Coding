# Joy of Coding Beginning Python Challenge
# from Prof. Emily Hill
# What does this program output 
# Day 7. Loops & Ifs (2 hours)

x = 3
y = 7

# Exercise
print( not x == 5 )
# True
print( x > 0 and y > 0 )
# True
print( x < 0 or y < 0 )
# False
print( x*y > 20 or x*y < -20 )
# True
# Challenge

print( not (x == 0 or y == 5) )
# True
print( not  x == 0 or y == 5  )
# True
print( x == 3 and not y == 5 )
# True
print( not (x == 3 and y == 5) )
# True


# 3. What is output by the following code?

# 4. Consider the 3 programs below that all determine whether a number  input by the user is even or odd. Assuming the user enters an integer,  which program is more efficient?

# # Solution A: 
# x = eval(input("Enter a number: "))
# if x % 2 == 0:
#   print(x,"is even")
# elif x% 2 ==1:
#   print(x,"is odd")
  
# # Solution B: 
# x = eval(input("Enter a number: "))
# if x % 2 == 0:
#   print(x,"is even")
# if x% 2 ==1:
#   print(x,"is odd")

# Solution C:
x = eval(input("Enter a number: "))
if x % 2 == 0:
  print(x,"is even")
else:
  print(x,"is odd")

# Why? 