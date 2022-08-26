##basic code of function testing
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        new_name = get_formatted_name("Aakash","Thakur")
        self.assertEqual(new_name,"Aakash Thakur")

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')        
if __name__ == "__main__":
    unittest.main()


    
