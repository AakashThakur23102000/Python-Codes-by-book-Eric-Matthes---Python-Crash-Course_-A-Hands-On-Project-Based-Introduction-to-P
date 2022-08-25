'''
with open('pi_digits.txt') as file_object:
    #for loop in file
    for i in file_object:
        print(i)
    contents = file_object.read()
print(contents)
'''

'''
#using file path
with open("files/name.txt") as name:
    names = name.read()
print(names)
'''

'''
#Making a list of lines from Files
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
print(type(lines))
'''
'''
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
string = ""
for line in lines:
    string = string + line.strip()
print(string)
'''

#printing a large value in short
with open("pi100.txt") as file_object:
    lines = file_object.readlines()
string = ""
for line in lines:
    string = string + line.strip()
print(string)
#main logic
print("\n",string[:10])


































