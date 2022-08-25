''' #wrong way
filename = 'alice.txt'
with open(filename, encoding='utf-8') as f:
    contents = f.read()
'''
#correct way
filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()

except FileNotFoundError:
    print(f"This {filename} dosen't exist.")

