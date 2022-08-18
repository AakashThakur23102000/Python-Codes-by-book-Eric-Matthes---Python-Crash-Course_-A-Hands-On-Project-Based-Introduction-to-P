'''9-5. Login Attempts:
Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 162).

Write a method called increment_login
_attempts() that increments the value of login_attempts by 1. Write another
method called reset_login_attempts() that resets the value of login_attempts
to 0.


Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
'''

class User:
    def __init__(self,first_name,last_name,age,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old. {self.first_name} {self.last_name} gender is {self.gender}.")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

    #new code
    #printing login attempt
    def login_print(self):
        print(f"Your Login Attempt was - {self.login_attempts}")

    #increments the value of login_attempts by 1.
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        
user1 = User("aakash","thakur",21,"male")

user1.greet_user()
user1.describe_user()

user2 = User("sita","thakur",20,"female")

user2.greet_user()
user2.describe_user()

#new code
user1.login_print()  #printing default login attempt
user1.increment_login_attempts()  #increment logins
user1.increment_login_attempts()  #increment logins
user1.increment_login_attempts()  #increment logins
user1.increment_login_attempts()  #increment logins
user1.increment_login_attempts()  #increment logins
user1.increment_login_attempts()  #increment logins
user1.increment_login_attempts()  #increment logins
user1.login_print()  #printing new login attempt
user1.reset_login_attempts() #reseting login back to 0
user1.login_print()
