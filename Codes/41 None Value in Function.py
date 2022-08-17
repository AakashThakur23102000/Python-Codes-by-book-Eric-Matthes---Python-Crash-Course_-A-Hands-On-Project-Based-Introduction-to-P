def full_name(first_name,last_name,age=None):
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"]= age
    return person
music = full_name("Aakash","Thakur",age=22)
print(music)
