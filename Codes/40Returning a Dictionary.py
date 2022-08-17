'''Returning a Dictionary
he following function takes in parts of a name and returns a dictionary representing
a person:
'''
'''
def persons(first_name, last_name):
    person = {first_name:last_name}
    return person
personn = persons("Aakash","Thakur")
print(personn)
'''



'''Adding name in nested dictionary list using for loop'''
#function
def persons(first_name, last_name):
    person = {first_name:last_name}
    return person

#working
lists = []
working = True

while working == True:
    wor = input("DO you want to enter names.. Press Y or N")
    if wor=="Y":
        fir = input("Enter First Name")
        lst = input("Enter Last Name")
        personn = persons(fir,lst)
        lists.append(personn)
    elif wor=="N":
        working = False
    else:
        print("Enter a vadid input")
    
print(lists)
