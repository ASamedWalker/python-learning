# 5-8 Hello Admin:
# usernames = ['admin', 'sam', 'eric', 'walker', 'jane']

# for username in usernames:
#   if username == 'admin':
#     print(f"Hello {username}, would you like to see a status report?")
#   else:
#     print(f"Hello {username}, thank you for logging again.")

# print("Welcome to the brand new day developers.")

# 5-9 No Users:
# usernames = []

# if usernames:
#   for username in usernames:
#     if username == 'admin':
#       print(f"Hello {username}, would you like to see a status report?")
#     else:
#       print(f"Hello {username}, thank you for logging again.")
# else:
#   print("We need to find some users")

# 5-10 Checking Usernames:
# Simulating a website users whom has a unique username
# current_users = ['joe', 'mick', 'bob', 'sam', 'jane']

# # To make sure something is case insentitive 
# # kindly make a copy of the original list

# current_users_lower = [user.lower() for user in current_users]

# new_users = ['bob', 'luck', 'PHIL', 'joe', 'king']

# for user in new_users:
#   if user.lower() in current_users_lower:
#     print(f"{user} kindly enter a new username")
#   else:
#     print(f"{user} is available")

# 5-11. Ordinal Numbers:
# numbers = list(range(1, 10))

# for number in numbers:
#   if number == 1:
#     print(f"{number}st")
#   elif number == 2:
#     print(f"{number}nd")
#   elif number == 3:
#     print(f"{number}rd")
#   else:
#     print(f"{number}th")

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
    
  
admin = Admin('Jason', 'Walter', 32)
# admin.greet_user()
# admin.describe_user()
# admin.show_privileges()

admin.describe_user()
admin.privileges.show_privileges()

print("\nAdding privileges...")
admin_privileges = ['can delete post', 'can ban user', 'can add post']

admin.privileges.privileges = admin_privileges
admin.privileges.show_privileges()