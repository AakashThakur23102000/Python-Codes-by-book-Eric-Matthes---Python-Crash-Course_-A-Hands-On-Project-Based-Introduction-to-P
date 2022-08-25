loc = "14data.txt"
with open(loc) as loves:
    lovers = loves.readlines()
for i in range(3):
    for lover in lovers:
        print(lover.replace("Love","Hate"))
    
