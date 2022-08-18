'''9-4. Number Served:
Start with your program from Exercise 9-1 (page 162).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.

Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.

Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any num-
ber you like that could represent how many customers were served in, say, a
day of business.
'''
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"THIS RESTAURANT NAME IS {self.restaurant_name} and uses {self.cuisine_type} cusine type.")
    def open_restaurant(self):
        print("This restaurant is currently opned!")

    #printing no of served
    def number_served_print(self):
        print(f"The numbers of customers served are {self.number_served}")
    #set number of served by method
    def set_number_served(self, number):
        self.number_served = number
    #
    def increment_number_served(self,new_number):
        self.number_served += new_number
        

restaurant = Restaurant("haveli","soft")

print(f"HAVE YOU VISITED {restaurant.restaurant_name} ?")
print(f"DO THEY USE SOFT {restaurant.cuisine_type} CUISINE ?")

restaurant.describe_restaurant()
restaurant.open_restaurant()

#new code
restaurant.number_served = 50
restaurant.number_served_print()

restaurant.set_number_served(100)
restaurant.number_served_print()

restaurant.increment_number_served(10)
restaurant.number_served_print()
