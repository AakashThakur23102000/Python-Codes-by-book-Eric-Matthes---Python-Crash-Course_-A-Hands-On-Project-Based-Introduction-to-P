class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is sitting")
    def roll(self):
        print(f"{self.name} is rolling")

#creating an instance my_dog and using attributes which is name and age here.
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")


#using other method in a class by help of instance my_dog
my_dog.sit()
my_dog.roll()


##creating multiple instances
your_dog = Dog("Vishal",21)
print(f"Your dog name is {your_dog.name}")
your_dog.sit()


