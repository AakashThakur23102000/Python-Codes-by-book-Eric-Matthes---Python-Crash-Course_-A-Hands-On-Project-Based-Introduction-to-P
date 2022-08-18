
class Car:
    def __init__(self,name,model,year):
        self.name = name
        self.model = model
        self.year = year
        self.speeds = 0
    def car_details(self):
        full_details = f"CAR NAME IS {self.name} OF YEAR {self.year} AND MODEL {self.model}."
        return full_details.title()
    def speed(self):
        print(f"This car has {self.speeds} miles on it.")

car1 = Car("ZEN","ZENXXX",2000)
print(car1.car_details())


#Here we first change the value of speed's default value from 0 to 10
car1.speeds = 10
car1.speed()        
