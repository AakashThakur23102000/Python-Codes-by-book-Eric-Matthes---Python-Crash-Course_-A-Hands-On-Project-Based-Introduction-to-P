#here flag variable is active which uses true to run the program and false to end the program#

pt = "\nTell me something, and I will repeat it back to you:"
pt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(pt)

    if message == 'quit':
        active = False
    else:
        print(message)

