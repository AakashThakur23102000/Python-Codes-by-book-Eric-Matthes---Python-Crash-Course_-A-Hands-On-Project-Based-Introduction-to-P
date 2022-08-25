'''
The open() function automatically creates the file you’re writing to if
it doesn’t already exist.
'''
with open("empty.txt","w") as empty:
    empty.write("I Love Coading")
    empty.write("\nPlaying Chessssss too")
