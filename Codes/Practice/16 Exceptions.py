''' 10-6. Addition:
One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you’ll get a ValueError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the ValueError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number.
'''
'''
try:
    val1 = int(input("Enter number one to add - "))
    val2 = int(input("Enter number two to add - "))
except ValueError:
    print("Enter numerical values in it.")
else:
    val3 = val1 + val2
    print(val3)
'''
'''10-7. Addition Calculator:
Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number.
'''
flags = True
while flags==True:
    try:
        
        val1 = int(input("Enter number one to add - "))
        val2 = int(input("Enter number two to add - "))
        

    
    except ValueError:
        print("Enter numerical values in it.")
    
        print("Do you want to run addition addition again, if not enter q in any of input")
    else:
        val3 = val1 + val2
        print(val3)
        run = input(("press y to repeate addition or q to exit"))
        if run == "q":
            flags=False
