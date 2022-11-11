class Employee():
  """A simple class to represent a employee."""
  
  def __init__(self, first_name, last_name, salary):
    """Initializes attributes for the class"""
    self.first_name = first_name
    self.last_name = last_name
    self.salary = salary
    
  def give_raise(self, amount=5000):
    """Increase the value of the annual salary."""
    self.salary += amount
    # print(f"{self.first_name} {self.last_name} annual is: ${self.annual_salary}")