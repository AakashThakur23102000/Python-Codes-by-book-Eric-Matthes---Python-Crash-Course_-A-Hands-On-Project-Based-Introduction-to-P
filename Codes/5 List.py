


# list uses [] and comas to seperate them.. it is  ordered collections od items

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])

#using of string methods in list
print(bicycles[0].title())

## pyhton special cases of index reading --where -1 is considerd as last and -2 as secondlast

print(bicycles[-1])
print(bicycles[-2])

##using f string in list with method title
byec = f"Hii, i ride {bicycles[2].title()}"
print(byec)
