class Restaurant:
  def __init__(self, restaurant_name, cuisine_type) -> None:
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    
  def describe_restaurant(self):
    print(f"This restaurant {self.restaurant_name} has lots of various cuisines like {self.cuisine_type}.")
    
  def open_restaurant(self):
    print(f"{self.restaurant_name} is open 24/7.")


class IceCreamStand(Restaurant):
  """Respresent aspects of a ice cream joint, specific to restaurant."""
  
  def __init__(self, restaurant_name, cuisine_type) -> None:
    """
    Initialize attributes of the parent class
    Then initialize attributes specific to an electric car.
    """
    super().__init__(restaurant_name, cuisine_type)
    self.flavors = ['chocolate', 'ginger', 'strawberry']
    
  
  def display_flavors(self):
    """Display the ice cream flavors."""
    print(f"The {self.restaurant_name} has different flavors of {self.cuisine_type} like: ")
    for flavor in self.flavors:
      print(f"\n - {flavor} flavor.")
  
cream = IceCreamStand("Lick'n'Pop", "Ice Cream")

cream.display_flavors()