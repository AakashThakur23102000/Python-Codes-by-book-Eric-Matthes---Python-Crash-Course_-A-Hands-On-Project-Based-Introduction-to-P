#sorting of list 

#all lowercased
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

#using sort method to use it as assending order
cars.sort()
print(cars)

#using sort method to use it as assending order
cars.sort(reverse = True)
print(cars)



#temporary sorting of list through sorted method
carss = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(carss)

print("\nHere is the sorted list:")
print(sorted(carss))

print("\nHere is the original list again:")
print(carss)

print("\nHere is the temporary sorted list but in reverse order:")
print(sorted(carss, reverse=True))


#Printing a list in reverse order but not SOrted
print("THis is reverse of a list but not sorted ")
carsss = ['bmw', 'audi', 'toyota', 'subaru']
print(carsss)

carsss.reverse()
print(carsss)
