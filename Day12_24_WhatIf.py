# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge
            # by, TurtleWolfe.com
# Day 12
# While Loops (2 hours)
#####################
def introduction():
  # prints welcome message
  #  & gets user's name
  print("> Greetings, my name is Eliza")
  name = input("> With whom am I speaking?\n")
  return name
  # //introduction..

def goodbye(name):
  # prints a farewell message
  print("> ... chatting with", name + ".")
  print("> I hope we can again soon!")
  print()

user = introduction()
question = "Nice to meet you, %s. How are you?" % user
print()
response = input("> " + question + "\n")
print()
  # | is that a pipe? continue statement through line break
while response.lower() != "goodbye" \
    and response.lower() != "exit" \
    and response.lower() != "quit" :
  if "today" in question:
    question = "Me to. \n> I love movies. What's your favorite?"
  elif "movies" in question:
    question = "marathon?"
  elif "marathon" in question:
    question = "marathon?"
  elif "like" in question:
    question = "marathon?"
  elif "quit" in question:
    question = "marathon?"
  else :
    question = "How does that make you feel?"
  response = input("> " + question + "\n")
# goodbye(user)  
  # //goodbye..

def numList(i):
# Given the following input entered by the user, what will be output?
# Henry Higgins
# Splendid. And you?
# Pygmalion
# Sure. Can we watch My Fair Lady as well?
# Watch Monty Python skits
# I especially like The Ministry of Silly Walks and Blackmail skits
# Wonderful, but I may have to quit soon. It takes too much of my time.
# Goodbye
  print(i)
  return(i)
# return(numList)

def main():
  print("Day12_24_   WhatIf, Eliza")
  print()
  # goodbye("Wonderful,\n   but it takes too much of my time.")
  goodbye("Eliza")
goodbye(user)  
main()  # end of Curled Main.. 