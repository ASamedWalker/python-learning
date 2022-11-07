from user_class import User

class Privileges():
  """A simple attempt to represent privileges of an admin."""
  
  def __init__(self, privileges=[]) -> None:
    """Initialize attributes for the privileges class"""
    self.privileges = privileges
  
  def show_privileges(self):
    """Display the privileges admin has"""
    if self.privileges:
      for privilege in self.privileges:
        print(f"\n - {privilege}")
    else:
      print("- This user has no privileges.")
    
# 9-7 Admin class:
class Admin(User):
  """Represent aspect of admin class, specific to the user class."""
  
  def __init__(self, first_name, last_name, age) -> None:
    """
    Initialize attributes of the parent class
    Then initialize attributes specific to an electric car.
    """
    super().__init__(first_name, last_name, age)
    self.privileges = Privileges()