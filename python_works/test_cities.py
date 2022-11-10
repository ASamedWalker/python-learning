import unittest
from city_function import city_country

class CityCountryTest(unittest.TestCase):
  """Test case for the function city and country."""
  
  def test_city_country(self):
    formatted_city_country = city_country('accra', 'ghana')
    self.assertEqual(formatted_city_country, 'Accra, Ghana')
    
  def test_city_country_population(self):
    formatted_city_country = city_country('accra', 'ghana', '7000000')
    self.assertEqual(formatted_city_country, 'Accra, Ghana - Population=7000000')
    
if __name__ == '__main__':
  unittest.main()