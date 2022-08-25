'''9-13. Dice:
Make a class Dice with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll it
10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
'''
'''
from random import randint
class Dice:
    def __init__(self,sides = 6):
        self.sides = sides
    def roll_die(self):
        for i in range(6):
            print(f"Your Number is = {randint(1,self.sides)}")


dice = Dice()
dice.roll_die()
'''

'''9-14. Lottery:
Make a list or tuple containing a series of 10 numbers and
five letters. Randomly select four numbers or letters from the list and print a
message saying that any ticket matching these four numbers or letters wins a
prize.
'''
from random import choice
list1 = [0,1,2,3,4,5,6,7,8,9,"RAM","SHYAM","SITA","GITA","AAKASH"]
print("Generating your lottery \nIf integer comes you lose and if string comes you win")
lott = choice(list1)
if type(lott) == int:
    print(f"\nYou loss your number is {lott}")
elif type(lott) == str:
    print(f"\nYou win your number is {lott}")
