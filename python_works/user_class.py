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