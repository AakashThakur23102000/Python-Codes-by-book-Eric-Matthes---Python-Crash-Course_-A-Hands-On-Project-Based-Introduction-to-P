'''middle names aren’t always needed, and this function as written
would not work if you tried to call it with only a first name and a last name.
To make the middle name optional, we can give the middle_name argument
an empty default value and ignore the argument unless the user provides a
value. '''

def enter_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name=f"{first_name} {middle_name} {last_name}"
    else:
        full_name=f"{first_name} {last_name}"
    return full_name.title()

name = enter_name("Aakash","Thakur")
name2 = enter_name("Aakash","Thakur","Prakash")
print(name)
print(name2)


