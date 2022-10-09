from user import User
from privileges import Privileges

class Admin(User):
  """A simple attempt to model a admin"""

  def __init__(self, first_name, last_name, relationship, employed):
    """Initializing the parent class"""
    # attributes
    super().__init__(first_name, last_name, relationship, employed)
    self.privileges = Privileges()