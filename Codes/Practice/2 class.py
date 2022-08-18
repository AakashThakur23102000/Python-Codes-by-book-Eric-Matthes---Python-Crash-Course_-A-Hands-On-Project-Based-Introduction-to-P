''' 9-1. Restaurant:
Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attri-
butes individually, and then call both methods.
'''

class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"THIS RESTAURANT NAME IS {self.restaurant_name} and uses {self.cuisine_type} cusine type.")
    def open_restaurant(self):
        print("This restaurant is currently opned!")

restaurant = Restaurant("haveli","soft")

print(f"HAVE YOU VISITED {restaurant.restaurant_name} ?")
print(f"DO THEY USE SOFT {restaurant.cuisine_type} CUISINE ?")

restaurant.describe_restaurant()
restaurant.open_restaurant()


print("\n")
'''
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
'''
restaurant1 = Restaurant("aakash","hard")
restaurant2 = Restaurant("vishal","soft")
restaurant3 = Restaurant("amit","none")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()



print("\n")
'''9-3. Users:
Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
'''
class User:
    def __init__(self,first_name,last_name,age,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old. {self.first_name} {self.last_name} gender is {self.gender}.")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")
user1 = User("aakash","thakur",21,"male")

user1.greet_user()
user1.describe_user()

user2 = User("sita","thakur",20,"female")

user2.greet_user()
user2.describe_user()











    
        
