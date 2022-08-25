'''
#basic try and except block syntax in exception handeling.
try:
    print(5/0)
except ZeroDivisionError:
    print("You cant divide it by 0.")

'''

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cant divide it by Zero.")
    #here we use else block.
    #Any code that depends on the try block executing successfully goes in the else block
    else:
        print(answer)
