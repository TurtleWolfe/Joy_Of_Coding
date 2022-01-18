# Joy of Coding Beginning Python Challenge
# from Prof. Emily Hill
# What does this program output 
# Day 8. Ifs, Loops, & Functions (2 hours)

score = int(input("the Score?  "))
print()
print(score)

# A > 90
if score >= 90: 
  print("A") 

# B 80-89
elif score >= 80: 
  print("B")

# C 70-79
elif score >= 70: 
  print("C")

# D 65-70
elif score >= 65: 
  print("D")  

# F < 65
elif score < 65: 
  print("F")

# default 
else:
 print("F")
