'''
8-12. Sandwiches:
Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sand-
wich that’s being ordered. Call the function three times, using a different num-
ber of arguments each time.
'''
'''
def Sandwich(items):
    for i in items:
        print(f"Items that are added in your pizza is - {i}")


inc = ["RAT", "BAT", "HAT"]

Sandwich(inc)
'''


'''
8-14. Cars: Write a function that stores information about a car in a diction-
ary. The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the func-
tion with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was
stored correctly.'''


def Cars(manufacturer,model,**others):
    others["manufacturer_details"] = manufacturer
    others["model_name"] = model
    return others

Car = Cars("Honda",2022,
     Owner="Aakash",
     size="Large")

print(Car)
















