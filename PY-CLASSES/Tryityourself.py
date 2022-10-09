# 9-1 Restaurant:
class Restaurant:
  def __init__(self, restaurant_name, cuisine_type):
    """Initializing restaurant_name and cuisine_type"""
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
  

  def describe_restaurant(self):
    """Printing restaurant information"""
    print(f"The restaurants name is {self.restaurant_name} and we serve our favorite dish known as {self.cuisine_type}")

  def open_restaurant(self):
    """Printing availability of the restaurant"""
    print(f"{self.restaurant_name} is open 24/7 - Mondays - Saturdays")


# restaurant = Restaurant('Smash', 'Waakye and Jollof')
# print(restaurant.restaurant_name.title())
# print(restaurant.cuisine_type)
# restaurant.describe_restaurant()

# 9-2 Three Restaurant:
# restaurant1 = Restaurant('ChopandLick', 'Banku and Tilapia')
# restaurant2 = Restaurant("Mama's kitchen", 'Fufu')
# restaurant3 = Restaurant("Amazing Run", "rice and beans")

# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()

# 9-3 Users:
class User:
  def __init__(self, first_name, last_name, relationship, employed):
    self.first_name = first_name
    self.last_name = last_name
    self.relationship = relationship
    self.employed = employed

  def describe_user(self):
    print(f"\nSummary of the user's information: ")
    print(f"First Name: {self.first_name}")
    print(f"last Name: {self.last_name}")
    print(f"Relationship: {self.relationship}")
    print(f"Employment: {self.employed}")

  def greet_user(self):
    print(f"Welcome to programming {self.first_name} {self.last_name}")


# information = User("Abdul Samed", "Walker", "Married", "yes")
# information.describe_user()

# 9-4 Number Served:
class Restaurant:
  def __init__(self, restaurant_name, cuisine_type):
    """Initializing restaurant_name and cuisine_type"""
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    self.number_served = 0
  

  def describe_restaurant(self):
    """Printing restaurant information"""
    print(f"The restaurants name is {self.restaurant_name} and we serve our favorite dish known as {self.cuisine_type}")

  def open_restaurant(self):
    """Printing availability of the restaurant"""
    print(f"{self.restaurant_name} is open 24/7 - Mondays - Saturdays")

  def set_number_served(self, number):
    """Setting number of customers in a restaurant."""
    self.number_served = number

  def increment_number_served(self, customers):
    """Increasing number of customers who haven't been served"""
    self.number_served += customers


restaurant = Restaurant('Chop&Lick', 'Banku & Tilapia')
# print(restaurant.number_served)
# - Modifying the attributes directly
# restaurant.number_served = 15
# print(restaurant.number_served)

# - Modifying the attributes in a method by setting a new number
# restaurant.set_number_served(25)
# print(restaurant.number_served)

# - Modifying the attributes in a method by increasing 
# already existing number
# restaurant.increment_number_served(100)
# print(restaurant.number_served)

# 9-5 Login Attempts:
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

persons = User('Sam', 'Walker', 'Married', 'yes')
# print(persons.login_attempts)
# persons.increment_login_attempts()
# print(persons.login_attempts)
# persons.increment_login_attempts()
# print(persons.login_attempts)
# persons.increment_login_attempts()
# print(persons.login_attempts)
# persons.increment_login_attempts(1)
# print(persons.login_attempts)
# persons.increment_login_attempts(2)
# print(persons.login_attempts)
# persons.increment_login_attempts(3)
# print(persons.login_attempts)

# persons.reset_login_attempts(0)
# print(persons.login_attempts)

# persons.reset_login_attempts()
# print(persons.login_attempts)


# 9-6. Ice Cream Stand:
# Modeling a real world scenario using the ice cream stand
class IceCreamStand(Restaurant):
  """Inheriting attributes and methods of the restaurant class"""
  def __init__(self, restaurant_name, cuisine_type):
    super().__init__(restaurant_name, cuisine_type)
    self.flavors = ['vanilla', 'chocolate', 'banana', 'mango']

  def get_icecream_flavors(self):
    """Printing out ice cream flavors from a list of flavors"""
    print(f"We have all kinds of ice cream falvors: ")
    for flavor in self.flavors:
      print(f" - {flavor.title()}")

# my_flavors = IceCreamStand('Lickyourhands', 'Icecream')
# my_flavors.get_icecream_flavors()

# 9-7 Admin:
# Creating an admin class
class Admin(User):
  """A simple attempt to model a admin"""

  def __init__(self, first_name, last_name, relationship, employed):
    """Initializing the parent class"""
    # attributes
    super().__init__(first_name, last_name, relationship, employed)
    self.privileges = Privileges()



# 9-8 Privileges:
# Creating a seperate privilege class
class Privileges:
  """A simple model of an Admin Privileges"""
  def __init__(self):
    self.privileges = ['can add post', 'can delete post', 'can ban user']
  
    # Methods
  def show_privileges(self):

    print(f"Privileges granted to the admin are: ")
    for privilege in self.privileges:
      print(f" - {privilege}")


admin_user = Admin('Mike', 'Joe', 'Manager', 'yes')
admin_user.privileges.show_privileges()

# 9-9 Battery Update:
# 9-10 Imported Restaurant
# 9-11 Imported Admin
# 9-12 Multiple Modules
