
'''
OOP Exercise 3: Create a child class Bus that will inherit all of the variables
and methods of the Vehicle class.
Create a Bus object that will inherit all of the variables and methods
of the parent Vehicle class and display it.

Vehicle Name: School Volvo Speed: 180 Mileage: 12
'''
'''
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

school = Bus("School Volvo",180,12)
print(school.name,school.max_speed,school.mileage)
'''



'''
Create a Bus class that inherits from the Vehicle class.
Give the capacity argument of Bus.seating_capacity() a default value of 50.
Use the following code for your parent Vehicle class.
'''
'''
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__( name, max_speed, mileage)
    # assign default value to capacity
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
        

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())
'''

'''
OOP Exercise 5: Define a property that must have the same value for every class instance (object).
Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
Use the following code for this exercise.
Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18
'''
'''
class Vehicle:

    def __init__(self, name, max_speed, mileage,color= " White"):
        self.color = color
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__( name, max_speed, mileage)
        print(f"Color:{self.color}  Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}")

class Car(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__( name, max_speed, mileage)
        print(f"Color:{self.color}  Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}")

bus = Bus("School Volvo",180,12)
car = Car("Audi",240,18)
'''







































