import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
  """Test for the class Employee"""
  # The setUp method
  def setUp(self):
    """This setup creates instances"""
    self.my_employee = Employee('Samed', 'Walker', 65_000)
   
  # methods
  def test_give_default_raise(self):
    """First Method!!!"""
    self.my_employee.give_raise()
    self.assertEqual(self.my_employee.annual_salary, 70000)

  def test_give_custom_raise(self):
    """Second Method!!!"""
    self.my_employee.give_raise(10000)
    self.assertEqual(self.my_employee.annual_salary, 75000)

if __name__ == '__main__':
  unittest.main()