"""A class that can be used to represent a car."""

class Car:
  """A simple attempt  to represent a car."""
  
  def __init__(self, manufacturer, model, year) -> None:
    """Initialize attributes to describe a car."""
    self.manufacturer = manufacturer
    self.model = model
    self.year = year
    self.odometer_reading = 0
    
  def get_descriptive_name(self):
    """Return a neatly formatted descriptive name."""
    long_name = f"{self.year} {self.manufacturer} {self.model}"
    return long_name.title()
  
  def read_odometer(self):
    """Print a statement showing the car's mileage."""
    print(f"This car has {self.odometer_reading} miles on it.")
  
  def update_odometer(self, mileage):
    """
    Set the odometer reading to the given value.
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
  
  def __init__(self, battery_size=75) -> None:
    """Initialize the battery's attributes."""
    self.battery_size = battery_size
    
  def describe_battery(self):
    """Print a statement describing the battery size."""
    print(f"This car has a {self.battery_size}-kWh battery.")
  
  def get_range(self):
    """PRint a statement about the range this battery provides."""
    if self.battery_size == 75:
      range = 260
    elif self.battery_size == 100:
      range = 315
      
    print(f"This car can go about {range} miles on a full charge.")
    
  def uprade_battery(self):
    """Checking the battery size of the electric car."""
    if self.battery_size == 75:
      self.battery_size = 100
      print('Upgraded the battery to 100 kWh')
    else:
      print("The battery is already upgraded.")

    
class ElectricCar(Car):
  """
  Initialize attributes of the parent class.
  Then initialize attributes specific to an electric car.
  Represent aspects of a car, specific to electric vehicles.
  """
  
  def __init__(self, make, model, year):
    """Initialize attributes of the parent class."""
    super().__init__(make, model, year)
    self.battery = Battery()

# my_new_car = Car('audi', 'a4', 2009)
# my_new_car = Car('subaru', 'outback', 2015)
# # print(my_new_car.get_descriptive_name())
# # my_new_car.read_odometer()
# # print("\n")

# # # Modifying an attribute's values directly
# # my_new_car.odometer_reading = 23
# # my_new_car.read_odometer()
# # print("\n")
# # # Modifying an attribute's value through a method
# # my_new_car.update_odometer(-1)
# # my_new_car.read_odometer()

# # Incrementing an attribute's value through a method
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(23_500)
# my_new_car.read_odometer()
# print("\n")
# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()