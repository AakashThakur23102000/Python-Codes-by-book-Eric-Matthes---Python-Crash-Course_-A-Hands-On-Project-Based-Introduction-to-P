#here we gona need to combine these two programs into one file.
import json
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename="users.json"

try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("Whats your name ? - ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")
    
 
