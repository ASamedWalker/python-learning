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

my_new_car = Car('audi', 'a4', 2009)
my_new_car = Car('subaru', 'outback', 2015)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# print("\n")

# # Modifying an attribute's values directly
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
# print("\n")
# # Modifying an attribute's value through a method
# my_new_car.update_odometer(-1)
# my_new_car.read_odometer()

# Incrementing an attribute's value through a method
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23_500)
my_new_car.read_odometer()
print("\n")
my_new_car.increment_odometer(100)
my_new_car.read_odometer()