#we use split() method to split a string into words list.
line = "Hii my name is Aakash"
print(line)
list1 = line.split()
print(list1)


''' counting the words in a file with exception handeling while file calling'''
filename= "63data.txt"
try:
    with open(filename) as file:
        files = file.read()
except FileNotFoundError:
    print(f"There is no file as {filename}")
else:
    file_word_count = files.split()
    print(f"the file {filename} has total words - ", len(file_word_count))
