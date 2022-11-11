import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
  """Testing the employee function"""
  
  def setUp(self):
    """Make an employee to use in tests."""
    self.samed = Employee('samed', 'walker', 80_000)
  
  def test_give_default_raise(self):
    """Testing the dafault function"""
    self.samed.give_raise()
    self.assertEqual(self.samed.salary, 85000)
    
  def test_give_custom_raise(self):
    """Testing the custom raise function"""
    self.samed.give_raise(10000)
    self.assertEqual(self.samed.salary, 90000)

if __name__ == '__main__':
  unittest.main()