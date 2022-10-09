class User:
  def __init__(self, first_name, last_name, relationship, employed):
    self.first_name = first_name
    self.last_name = last_name
    self.relationship = relationship
    self.employed = employed
    self.login_attempts = 0

  def describe_user(self):
    print(f"\nSummary of the user's information: ")
    print(f"First Name: {self.first_name}")
    print(f"last Name: {self.last_name}")
    print(f"Relationship: {self.relationship}")
    print(f"Employment: {self.employed}")

  def greet_user(self):
    print(f"Welcome to programming {self.first_name} {self.last_name}")

  def increment_login_attempts(self):
    """Increasing login attempts by 1"""
    self.login_attempts += 1

  def reset_login_attempts(self):
    """Resets the value of login_attempts to 0"""
    self.login_attempts = 0



class Privileges:
  """A simple model of an Admin Privileges"""
  def __init__(self):
    self.privileges = ['can add post', 'can delete post', 'can ban user']
  
    # Methods
  def show_privileges(self):

    print(f"Privileges granted to the admin are: ")
    for privilege in self.privileges:
      print(f" - {privilege}")


class Admin(User):
  """A simple attempt to model a admin"""

  def __init__(self, first_name, last_name, relationship, employed):
    """Initializing the parent class"""
    # attributes
    super().__init__(first_name, last_name, relationship, employed)
    self.privileges = Privileges()

