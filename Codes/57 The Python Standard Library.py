#use of randint from random module
from random import randint
print(randint(1,5))

'''Another useful function is choice(). This function takes in a list or tuple
and returns a randomly chosen element:'''
from random import choice
players = ["Aakash", "Thakur", "Vishal", "Random"]
print(choice(players))
