#parent class
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
#printing method
    def car_print(self):
        print(f"{self.make} {self.model} {self.year}")

    def car_fuel(self):
        print("This car uses fuel")

#new class #nstances as Attributes
class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    #range of battery
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
            print(f"YOUR BATTERY SIZE IS NOW {self.battery_size}")
        else:
            print("Your battery size is already 100")




#child class or sub class
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)

        #Defining Attributes and Methods for the Child Class
        #nstances as Attributes
        self.battery = Battery()


    #Overriding Fuel Methods from the Parent Class #
    def car_fuel(self):
        print("NO FUEL")



tesla = ElectricCar(2002,"TESLAG",23)
tesla.car_print()


#checking overriding of fuel
tesla1 = Car(2002,"TESLAG",23)
tesla1.car_fuel()
tesla2 = ElectricCar(2002,"TESLAG",23)
tesla2.car_fuel()
##nstances as Attributes
tesla.battery.describe_battery()
tesla.battery.get_range()
tesla2.battery.upgrade_battery()

