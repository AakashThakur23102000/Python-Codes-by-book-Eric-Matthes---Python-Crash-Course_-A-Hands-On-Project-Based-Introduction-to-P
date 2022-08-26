import unittest
from TestingCode import city_country

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        city_con = city_country("Santiago", "Chile")
        self.assertEqual(city_con, "Santiago, Chile")
    def test_city_country(self):
        city_con_pop = city_country("Santiago", "Chile", 5000000)        
        self.assertEqual(city_con_pop, "Santiago, Chile – population 5000000")
if __name__ == "__main__":
    unittest.main()
