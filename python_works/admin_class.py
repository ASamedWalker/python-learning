class User:
  """A simple attempt to represent a user."""
  
  def __init__(self, first_name, last_name, age) -> None:
    """Initializing attributes to describe a user."""
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    
    
  def describe_user(self):
    """Print a summary of the user information."""
    print(f"\nHere are the summary for the username information: ")
    print(f"first_name: {self.first_name}")
    print(f"last_name: {self.last_name}")
    print(f"Age: {self.age}")
  
  def greet_user(self):
    """Print a personalized greeting to the user."""
    print(f"\n{self.first_name} {self.last_name}, Welcome to Python.")

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