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
