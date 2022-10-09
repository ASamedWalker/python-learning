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
