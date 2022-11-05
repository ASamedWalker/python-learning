class User:
  """A simple attempt to represent a user."""
  
  def __init__(self, first_name, last_name, age) -> None:
    """Initializing attributes to describe a user."""
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    
    
  def describe_user(self):
    """Print a summary of the user information."""
    print(f"Here are the summary for the username information")
    print(f"first_name: {self.first_name}")
    print(f"last_name: {self.last_name}")
    print(f"Age: - {self.age}")
  
  def greet_user(self):
    """Print a personalized greeting to the user."""
    print(f"{self.first_name} {self.last_name}, Welcome to Python.")
    
    
user1 = User('Samed', 'Walker', 15)
user2 = User('Joe', 'Rogan', 20)
user3 = User('Bob', 'Steven', 17)


print(user1.first_name)
print(user1.last_name)
user1.describe_user()
user1.greet_user()

print("\n")
print(user2.first_name)
print(user2.last_name)
user2.describe_user()
user2.greet_user()

print("\n")
print(user3.first_name)
print(user3.last_name)
user3.describe_user()
user3.greet_user()
