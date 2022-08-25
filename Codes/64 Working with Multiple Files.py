#here to count the number of multiple files we create
#a function to count the no of words in a file.
def count_words(filename):
    try:
        with open(filename) as files:
            file = files.read()
    except FileNotFoundError:
        print(f"There is no file as {filename}")
    else:
        file_word_count = file.split()
        print(f"the file {filename} has total words - ", len(file_word_count))
        

#direct method to initalize value to function or
book1 = "63data.txt"
book2 = "64data.txt"
    #argument passing to a function 
count_words(book1)
count_words(book2)

#by using loops to pass values to a function
books = ["63data.txt","64data.txt"]
for book in books:
    count_words(book)
    
