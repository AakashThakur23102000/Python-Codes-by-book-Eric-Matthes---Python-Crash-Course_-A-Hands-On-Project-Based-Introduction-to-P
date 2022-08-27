import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp = Employee("Aakash","Thkaur",5000)

    def test_default(self):
        self.emp.give_raise()
        self.assertEqual(self.emp.salary, 10000)
    def test_new(self):
        self.emp.give_raise(500)
        self.assertEqual(self.emp.salary, 5500)

if __name__ == "__main__":
    unittest.main()
