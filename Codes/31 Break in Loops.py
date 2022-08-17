#To exit a while loop immediately without running any remaining code in the
#loop, regardless of the results of any conditional test, use the break statement.

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == "quit":
        break
    else:
        print(f"i would love to visit {city.title()}")
