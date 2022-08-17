def greet(names):
    """passing naam list in names"""
    '''Using for loops to access all items in a list'''
    
    for name in names:
        print(f"Hello {name.title()}, Good DAY")
naam = ["aakash","Ankita","Sapna","jYoti"]
greet(naam)
