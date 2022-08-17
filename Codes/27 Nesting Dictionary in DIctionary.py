'''
For example, if you have several users
for a website, each with a unique username, you can use the usernames as
the keys in a dictionary. You can then store information about each user by
using a dictionary as the value associated with their username. In the fol
lowing listing, we store three pieces of information about each user: their
first name, last name, and location. We’ll access this information by looping
through the usernames and the dictionary of information associated with
each username:
'''

users = {
    "aakash":{"last":"Thakur",
              "age":21,
              "gender":"male"},
    "sapna":{"last":"Thakur",
             "age":30,
             "gender":"female"}
    }
for first, la in users.items():
    print(f"username - {first.title()} {la['last'].title()}")
    print(f"\t {la['age']}")
    print(f"\t {la['gender'].title()}")
    
