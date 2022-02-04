# My First Variable Program!
# Joy of Coding Beginning Python Challenge

# What does this program output when it's ...
# 1. Monday?
# "Wake up at 7 am"

# 2. Saturday?
# "Wake up at 9 am"

# 3. Sunday?
# "Wake up at 10 am"

# 4. Raining?
# "Wake up at 7 am"

DoW = input("Enter a day: ")
# DoW = input().title()

if DoW == "Saturday":
	print("Wake up at 9 am")
elif DoW == "Sunday":
	print("Wake up at 10 am")
else:
	print("Wake up at 7 am")

  
# Learning Exercise: Reading Ifs 
# Try to predict what the code will do without running it… 
# code/dow2.py 

# Questions: 
# 1. Write what each line should print next to the code above for the 4  example inputs on lines 2—5. Consult with a neighbor before running  the example. Were your hypotheses correct? Why or why not? 
# 2. Revise the program above so that the user can also enter: a. saturday or sunday 
# b. satURday or SunDAY
