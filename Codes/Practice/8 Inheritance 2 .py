'''9-7. Admin:
An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.
'''
#old code
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
#New Code
class Admin(User):
    def __init__(self,first_name,last_name,age,gender,privileges):
        super().__init__(first_name,last_name,age,gender)
        self.privileges = privileges
    def pri(self):
        for i in self.privileges:
            print(i)

        
user1 = User("aakash","thakur",21,"male")

user1.greet_user()
user1.describe_user()

user2 = User("sita","thakur",20,"female")

user2.greet_user()
user2.describe_user()

#new code
task = ["can add post", "can delete post", "can ban user"]
user3 = Admin("sita","thakur",20,"female",task)
user3.pri()
