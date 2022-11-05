class User:
  """A simple attempt to represent a user."""
  
  def __init__(self, first_name, last_name, age) -> None:
    """Initializing attributes to describe a user."""
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.login_attempts = 0
    
    
  def describe_user(self):
    """Print a summary of the user information."""
    print(f"Here are the summary for the username information")
    print(f"first_name: {self.first_name}")
    print(f"last_name: {self.last_name}")
    print(f"Age: - {self.age}")
  
  def greet_user(self):
    """Print a personalized greeting to the user."""
    print(f"{self.first_name} {self.last_name}, Welcome to Python.")
    
  def increment_login_attempts(self):
    """Increment login attempts by 1."""
    self.login_attempts += 1
    
  def reset_login_attempts(self):
    """Reset login attempts to 0."""
    self.login_attempts = 0
    
member_user = User('Samed', 'Walker', 15)

member_user.increment_login_attempts()
print(f"Login attempts: {member_user.login_attempts}")

member_user.reset_login_attempts()
print(f"Login attempts: {member_user.login_attempts}")