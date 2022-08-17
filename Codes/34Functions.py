'''basic positional argument function'''
'''
def pets_details(pet_breed, pet_name):
    ''Pets Details''
    print(f"You have {pet_breed} and its name is {pet_name}")

pets_details("dog", "Vishal")
'''

'''input and loops in this function'''

def pets_details(pet_breed, pet_name):
    '''Pets Details'''
    print(f"You have {pet_breed} and its name is {pet_name}")

entry = int(input("Enter number of entries you want"))
types = "Enter you pet type"
name = "Enter your pets name"

for i in range(0,entry):
    typess = input(types)
    names = input(name)
    pets_details(typess, names)
