
class Privileges:
  """A simple model of an Admin Privileges"""
  def __init__(self):
    self.privileges = ['can add post', 'can delete post', 'can ban user']
  
    # Methods
  def show_privileges(self):

    print(f"Privileges granted to the admin are: ")
    for privilege in self.privileges:
      print(f" - {privilege}")
