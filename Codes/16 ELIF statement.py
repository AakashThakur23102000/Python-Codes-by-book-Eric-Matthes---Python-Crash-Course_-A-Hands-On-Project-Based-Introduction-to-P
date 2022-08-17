'''
consider an amusement park that charges different rates for
different age groups:
• Admission for anyone under age 4 is free.
• Admission for anyone between the ages of 4 and 18 is $25.
• Admission for anyone age 18 or older is $40.
How can we use an if statement to determine a person’s admission rate?
'''

age = int(input("Enter your age - "))

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
