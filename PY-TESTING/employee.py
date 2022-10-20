# Writing a class called employee
class Employee:
  """A class modeling an employee"""
  def __init__(self, f_name, l_name, annual_salary):
    # attributes
    self.f_name = f_name
    self.l_name = l_name
    self.annual_salary = annual_salary

    # methods
  def give_raise(self, addition=5000):
    # Give an employee a raise
    self.annual_salary += addition



    