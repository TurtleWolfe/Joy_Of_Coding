# Joy of Coding Beginning Python Challenge
# from Prof. Emily Hill
# What does this program output 
# Day 9. Reading & Writing Functions
#                           (2 hours)

# What does this program do?

# What do you think def & return do?
# What’s the difference between return & print?
# In the code above, identify the following:
                        # Formal parameters
                        # Actual parameters
                        # Void functions
                        # Fruitful functions

def double(x):
    return 2 * x

def quad(x):
    return double(double(x))

def hello(name):
    print("Hello", name + ", how are you today?")

def repeat(string, n):
    return string * n

def square(string, n):
    for i in range(n):
        print(repeat(string, n))

print(double(5))
#             10
print(quad(4))
#             16
hello("Joe")
#             Hello Joe how are you today?
print(repeat("hi", 10))
#             hihihihihihihihihihihihi
square("*", 4)
#             ****
#             ****
#             ****
#             ****