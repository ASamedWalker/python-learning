# CREATING AND USING A CLASS
# creating the Dog Class: dog.py
class Dog:
  """A simple attempt to model a dog."""

  # information or constructor
  def __init__(self, name, age):
    """Initialize name and age attributes."""
    self.name = name
    self.age = age

  # attributes
  def sit(self):
    """Simulate a dog sitting in response to a command."""
    print(f"{self.name} is now sitting.")

  def roll_over(self):
    """Simulate rolling over in response to a command."""
    print(f"{self.name} rolled over!")

# MAKING AN INSTANCE FROM A CLASS
# my_dog = Dog('Willie', 6)
# your_dog = Dog('Lucy', 3)
# my_dog.sit()
# my_dog.roll_over()
# print(f"My dog's name is {my_dog.name.title()}.")
# print(f"My dog is {my_dog.age} years old.")



# # CREATING MULTIPLE INSTANCES
# print(f"My dog's name is {your_dog.name.title()}.")
# print(f"My dog is {your_dog.age} years old.")
# your_dog.sit()

# WORKING WITH CLASSES AND INSTANCES
# Most of time working with classes, you will spend more time 
# modifying attributes which are equal to variables
# car.py
class Car:
  """A simple attempt to represent a car."""

  def __init__(self, make, model, year):
    """Initialize attributes to describe a car."""
    self.make = make
    self.model = model
    self.year = year
    # A default value which are defined wihtout being passed in as parameters
    self.odometer_reading = 0

  def get_descriptive_name(self):
    """Return a neatly formatted descriptive name."""
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()
  
  def read_odometer(self):
    """Print a statement showing the car's mileage."""
    print(f"This car has {self.odometer_reading} miles on it.")

  def update_odometer(self, mileage):
    """Set the odometer reading to the given value.
       Reject the change if it attempts to roll the odometer back.
    """
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You can't roll back an odometer!")
  
  def increment_odometer(self, miles):
    """Add the given amount to the odometer reading."""
    self.odometer_reading += miles

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# Setting a Default Value for an Attribute
# The default value assigned in the __init__() method are defined 
# without being passed in as parameters.

# MODIFYING ATTRIBUTE VALUES
# Three ways to change an attribute's value:
# - change the value directly through an instance
# - set the value through a method
# - increment the value through a method

# - Modifying an Attribute's Value Directly
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# - Modifying an Attribute's Value through a Method
# my_new_car.update_odometer(55)
# my_new_car.read_odometer()

# - Incrementing an Attribute's Value Through a Method
# Sometimes rather than changing the value by a certain amount
# you would rather increment the current value or attribute
# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()



# INHERITANCE
class Car:
  """A simple attempt to represent a car."""

  def __init__(self, make, model, year):
    """Initialize attributes to describe a car."""
    self.make = make
    self.model = model
    self.year = year
    # A default value which are defined wihtout being passed in as parameters
    self.odometer_reading = 0

  def get_descriptive_name(self):
    """Return a neatly formatted descriptive name."""
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()
  
  def read_odometer(self):
    """Print a statement showing the car's mileage."""
    print(f"This car has {self.odometer_reading} miles on it.")

  def update_odometer(self, mileage):
    """Set the odometer reading to the given value.
       Reject the change if it attempts to roll the odometer back.
    """
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You can't roll back an odometer!")
  
  def increment_odometer(self, miles):
    """Add the given amount to the odometer reading."""
    self.odometer_reading += miles

class Battery:
  """A simple attempt to model a battery for an electric car."""

  def __init__(self, battery_size=75):
    """Initialize the battery's attributes."""
    self.battery_size = battery_size

  def describe_battery(self):
    """Print a statement describing the battery size."""
    print(f"This car has a {self.battery_size}-kWh battery.")

  def get_range(self):
    """Print a statement about the range this battery provides."""
    if self.battery_size == 75:
      range = 260
    elif self.battery_size == 100:
      range = 315

    print(f"This car can go about {range} miles on a full charge.")

  def upgrade_battery(self):
    if self.battery_size == 75:
      self.battery_size = 100
      print("Upgraded the battery to 100 kWh.")
    else:
      print("The battery is already upgraded.")

class ElectricCar(Car):
  """Represent aspects of a car, specific to electric vehicles."""

  def __init__(self, make, model, year):
    """Initialize attributes of the parent class.
       Then initialize attributes specific to an electric car.
    """
    super().__init__(make, model, year)
    self.battery = Battery()

  def fill_gas_tank(self):
    """Electric cars don't have a gas tanks."""
    print("This car doesn't need a gas tank!")

# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())

# my_tesla = ElectricCar('tesla', 'model s', 2022)
# print(my_tesla.battery.battery_size)
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.describe_battery()

# print("\nTry upgrading the battery a second time.")
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.describe_battery()




# Defining Attributes and Methods for the Child Class
# Once a child class is established, you can define methods and attributes for that class

# Overriding Methods from the Parent Class
# One way to override from the P
# .arent class
# you can make the child classes retain what they need and 
# override anything you don't need from the parent class.


# INSTANCES AS ATTRIBUTES
# Creating a Battery Class
# class Battery:
#   """A simple attempt to model a battery for an electric car."""

#   def __init__(self, battery_size=75):
#     """Initialize the battery's attributes."""
#     self.battery_size = battery_size

#   def describe_battery(self):
#     """Print a statement describing the battery size."""
#     print(f"This car has a {self.battery_size}-kWh battery.")

# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()


# IMPORTING CLASSES
# Importing a Single Class


# Storing Multiple Classes in a Module
# Importing Multiple Classes from a Module
# Importing an Entire Module
# Importing All Classes from a Module
# You can use the syntax "from module_name import *"
# But it is stil not recommended


# IMPORTING A MODULE INTO A MODULE
# USING ALIASES

# THE PYTHON STANDARD LIBRARY
# Using already existing modules including in the python 
# library in your program
# This module randomly generates numbers
# from random import randint
# randint(1, 6)

# Another module is the choice() function which list or tuple 
# returns a randomly chosen element
# from random import choice
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# first_up = choice(players)
# first_up


# 9-13 Dice
from random import randint, choice

class Die:
  """A simple dice game."""

  def __init__(self) -> None:
    # self.sides = 6  #This is a 6 sided die
    # self.sides = 10 #This is a 10 sided die
    self.sides = 20 #This is a 20 sided die

  def roll_die(self):
    return randint(1, self.sides)

my_dice = Die()
results = []
for roll_num in range(10):
  result = my_dice.roll_die()
  results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

# 9-14 Lottery:
# lottery_tickets = [3, 4, 5, 6, 9, 7, 2, 10, 8, 1, 'r', 'g', 'h', 'z', 'e']

# winning_ticket = []
# print("Let's see what the winning ticket is...")

# We use a while loop because we don't want to keep repeating the
# winning numbers or letters

# while len(winning_ticket) < 4:
#   pulled_item = choice(lottery_tickets)

#   if pulled_item not in winning_ticket:
#     print(f"We pulled a {pulled_item}! ")
#     winning_ticket.append(pulled_item)
    
# print(f"The final winning ticket is: {winning_ticket}")

# 9-15 Lottery Analysis:
def get_winning_ticket(lottery_tickets):
  """Return a winning ticket from a set of lottery tickets"""
  winning_ticket = []
  while len(winning_ticket) < 4:
    pulled_item = choice(lottery_tickets)
    
    if pulled_item not in winning_ticket:
      print(f"We pulled a {pulled_item}! ")
      winning_ticket.append(pulled_item)
  return winning_ticket

def check_ticket(played_ticket, winning_ticket):
  # Check all elements in the player ticket
  # If any are not in winning ticket, return False
  for element in played_ticket:
    if element not in winning_ticket:
      return False

  # We must have a winning ticket!
  return True

def make_random_ticket(lottery_tickets):
  """Return a random ticket from a set of lottery tickets"""
  tickets = []
  while len(tickets) < 4:
    pulled_item = choice(lottery_tickets)

    if pulled_item not in tickets:
      tickets.append(pulled_item)

  return tickets

lottery_tickets = [3, 4, 5, 6, 9, 7, 2, 10, 8, 1, 'r', 'g', 'h', 'z', 'e']
winning_ticket = get_winning_ticket(lottery_tickets)

plays = 0
won = False

MAX_TRIES = 1_000_000

while not won:
  new_ticket = make_random_ticket(lottery_tickets)
  won = check_ticket(new_ticket, winning_ticket)
  plays += 1
  if plays >= MAX_TRIES:
    break

if won:
  print("We have a winning ticket!")
  print(f"Your ticket: {new_ticket}")
  print(f"Winning ticket: {winning_ticket}")
  print(f"It only took {plays} tries to win!")
else:
  print(f"Tried {plays} times, without pulling a winner. :(")
  print(f"Your ticket: {new_ticket}")
  print(f"Winning ticket: {winning_ticket}")