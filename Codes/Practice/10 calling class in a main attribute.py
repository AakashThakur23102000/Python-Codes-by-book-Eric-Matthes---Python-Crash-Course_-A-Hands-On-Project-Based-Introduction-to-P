#main class
class Car:
    def __init__(self,model,year,fuel):
        self.model = model
        self.year = year
        self.fuel = fuel

    def print_main(self):
        print(f"This is main class items -- {self.model} {self.year} {self.fuel}.")

#child class / sub class
class Tesla(Car):
    def __init__(self,model,year,fuel):
        super().__init__(model,year,fuel)
        #battery class initalize
        self.bat = Battery()

    def print_child(self):
        print("This is Child class")

    

#new class to attach with child class
class Battery:
    def __init__(self,battery_size = 5):
        self.battery_size = battery_size

    def print_battery(self):
        print(f"your battery size is {self.battery_size}")

vehicle = Tesla("ZEN",2000,"45LTR")
vehicle.bat.print_battery()
