'''
Here in first argument we use [:] which is a copy of orignal list and name it as notc in parameters 
'''
def machine(notc,changed,notchanged):
    while notc:
        deletednotchanged = notc.pop()
        changed.append(deletednotchanged)
        print("This is chnaged list", changed)
        print("This is notchnaged copy list", notc)
        print("This is notchnaged orignal list ", notchanged, "\n" )
        


notchanged = ["Aakash","Ankita","Sapna","Jyoti"]
changed=[]
machine(notchanged[:],changed,notchanged)

print(notchanged)
print(changed)
