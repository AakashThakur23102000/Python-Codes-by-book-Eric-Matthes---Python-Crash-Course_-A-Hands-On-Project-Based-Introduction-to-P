'''9-6. Ice Cream Stand:
An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand
that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
'''
#old code
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        

    def describe_restaurant(self):
        print(f"THIS RESTAURANT NAME IS {self.restaurant_name} and uses {self.cuisine_type} cusine type.")
    def open_restaurant(self):
        print("This restaurant is currently opned!")
#new code
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors

    def print_flavors(self):
        for i in self.flavors:
            print(f"Flavors added are {i}")
    
        

#old code



#new code
list1 = [1,2,3,5,6]
restaurant2 = IceCreamStand("haveli","soft",list1)
restaurant2.print_flavors()
