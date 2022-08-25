'''10-11. Favorite Number:
Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate pro-
gram that reads in this value and prints the message, “I know your favorite
number! It’s _____.”
'''
'''
import json
try:
    fav = int(input("Enter you fav. num - "))
except ValueError:
    print("enter numeric value next time.")
else:
    filename = "17data.json"
    with open(filename, "w") as f:
        json.dump(fav,f)
#next code is read by 17readerjson.py
'''


'''10-12. Favorite Number Remembered:
Combine the two programs from
Exercise 10-11 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the user’s favorite number and store it in a
file. Run the program twice to see that it works.
'''
import json
try:
    filename = "17data.json"
    with open(filename) as f:
        files = json.load(f)
except FileNotFoundError:
    fav = int(input("enter your fav number - "))
    filename = "17data.json"
    with open(filename,"w") as f:
        json.dump(fav,f)
else:
    print(f"your fav number is {files}")


















