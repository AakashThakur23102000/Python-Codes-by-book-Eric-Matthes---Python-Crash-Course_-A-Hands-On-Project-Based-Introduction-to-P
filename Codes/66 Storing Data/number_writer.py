'''
#structure of writing data to json file
import json

numbers = [2,4,5,6,8,9]

filename = 'numbers.json'
with open(filename, "w") as f:
    json.dump(numbers, f)
'''


#store users their name in a file
import json

users = input("Enter your Name - ")

filename = 'users.json'
with open(filename, "w") as f:
    json.dump(users, f)
print(f"Hii {users}")
