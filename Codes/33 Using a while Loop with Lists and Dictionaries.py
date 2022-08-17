'''
Moving Items from One List to Another

Consider a list of newly registered but unverified users of a website. After
we verify these users, how can we move them to a separate list of confirmed
users? One way would be to use a while loop to pull users from the list of
unconfirmed users as we verify them and then add them to a separate list of
confirmed users. Here’s what that code might look like:
'''
'''
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print(confirmed_users)
print(unconfirmed_users)
'''


''' Say you have a list of pets with the value 'cat' repeated several times. To
remove all instances of that value, you can run a while loop until 'cat' is no
longer in the list, as shown here:
'''
'''
pets = ['dog', 'cats', 'dog', 'goldfish', 'cats', 'rabbit', 'cats']
print(pets)

while 'cats' in pets:
    pets.remove('cats')

print(pets)
'''



'''Filling a Dictionary with User Input'''
'''
keyy = "Enter you Name"
Value = "Enter you Gender"
empty_dict={}
working = True

while working == True:
    name = input(keyy)
    gender = input(Value)
    empty_dict[name]= gender

    repeate = input("DO YOU WANT TO ADD MORE .. PRESS YES OR NO - ")
    if repeate == "NO":
        working = False
print(empty_dict)
'''        
    

    
    
