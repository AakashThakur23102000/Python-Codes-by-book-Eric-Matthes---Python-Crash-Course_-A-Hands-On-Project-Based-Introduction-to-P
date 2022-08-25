'''
Write a program that prompts the user for their name.
When they respond, write their name to a file called guest.txt.'''
'''
for i in range(5):
    name = input("Enter you name - ")
    with open("15data.txt","a") as file:
        file.write(name)
'''

'''
10-5. Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
'''
#first save response in list 
responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break
print(responses)

#then append it to a file
with open("15data.txt","a") as file:
    for i in responses:
        file.write(i + "\n")
    
    
