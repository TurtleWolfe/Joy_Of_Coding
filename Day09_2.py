# Joy of Coding Beginning Python Challenge
# from Prof. Emily Hill
# What does this program output 
# Day 9. Reading & Writing Functions
#                           (2 hours)

# 1. h(4)
# 2. h(5)

def f(x): 
	x = x-1
	return g(x)+1

def g(x):
	return x*2

def h(x):
	if x%2 == 1:      # x odd
		return f(x) + x
	else:             # x even
		return f(f(x))

print(h(3)) # 8
print(h(4))
print(h(5))