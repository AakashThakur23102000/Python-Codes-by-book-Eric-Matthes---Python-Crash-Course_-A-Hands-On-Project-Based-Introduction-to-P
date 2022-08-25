'''
#structure of read data to json file
import json

filename = "numbers.json"
with open(filename,"r") as f:
    numbers = json.load(f)

print(numbers)
'''

#calling users to welcome back them again
import json

filename = "users.json"
with open(filename) as f:
    user = json.load(f)
print(f"welcome back {user}")
