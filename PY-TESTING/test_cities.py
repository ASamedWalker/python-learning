"""Test my city and country function"""
import unittest
from city_functions import city_and_country

class TestCityCountry(unittest.TestCase):
  """Test for 'city_functions.py'"""

  def test_city_country(self):
    infor_display = city_and_country('accra', 'ghana')
    self.assertEqual(infor_display, 'Accra, Ghana')

  def test_city_country_population(self):
    infor_modification = city_and_country('accra', 'ghana', population=5_000_000)
    self.assertEqual(infor_modification, 'Accra, Ghana - population 5000000')

if __name__ == '__main__':
  unittest.main()

