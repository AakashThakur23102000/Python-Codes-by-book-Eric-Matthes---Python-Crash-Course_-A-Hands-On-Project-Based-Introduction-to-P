'''11-3. Employee:
Write a class called Employee. The __init__() method should
take in a first name, a last name, and an annual salary, and store each of these
as attributes. Write a method called give_raise() that adds $5,000 to the
annual salary by default but also accepts a different raise amount.
Write a test case for Employee. Write two test methods, test_give_default
_raise() and test_give_custom_raise(). Use the setUp() method so you don’t
have to create a new employee instance in each test method. Run your test
case, and make sure both tests pass'''

class Employee:
    def __init__(self,first,last,salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self,raisee=5000):
        #new variable declare
        self.raisee = raisee
        #adding rasiee in salary
        self.salary = self.salary + raisee
        #printing salary after raisee
        print(self.salary)

emp = Employee("Aakash","Thkaur",5000)
emp.give_raise(100)
        
