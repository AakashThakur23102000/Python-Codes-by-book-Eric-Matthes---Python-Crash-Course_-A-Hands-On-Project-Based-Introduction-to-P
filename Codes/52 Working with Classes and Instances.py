'''
Our class will store information
about the kind of car we’re working with, and it will have a method that
summarizes this information:
'''

class Car:
    def __init__(self,name,model,year):
        self.name = name
        self.model = model
        self.year = year
        #creating own attribute and assigning its default value as 0
        self.speeds = 0
    def car_details(self):
        full_details = f"CAR NAME IS {self.name} OF YEAR {self.year} AND MODEL {self.model}."
        return full_details.title()
    def speed(self):
        print(f"This car has {self.speeds} miles on it.")

car1 = Car("ZEN","ZENXXX",2000)
print(car1.car_details())
car1.speed()        
