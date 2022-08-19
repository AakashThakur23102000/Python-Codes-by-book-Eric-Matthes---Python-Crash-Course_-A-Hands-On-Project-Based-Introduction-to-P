"""https://pynative.com/python-object-oriented-programming-oop-exercise/"""
#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
Car = Vehicle(50, 100)
print(f"Car max speed is {Car.max_speed} and gives a milage of {Car.mileage}!")
        
        
#OOP Exercise 2: Create a Vehicle class without any variables and methods.
class Vehicle:
    def __init__():
        #Here we use pass statement as a placeholder for future code.
        pass

#
