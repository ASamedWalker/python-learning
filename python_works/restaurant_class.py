class Restaurant:
  def __init__(self, restaurant_name, cuisine_type) -> None:
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    
  def describe_restaurant(self):
    print(f"This restaurant {self.restaurant_name} has lots of various cuisines like {self.cuisine_type}.")
    
  def open_restaurant(self):
    print(f"{self.restaurant_name} is open 24/7.")