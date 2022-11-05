class Restaurant:
  def __init__(self, restaurant_name, cuisine_type) -> None:
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    self.number_served = 0
    
  def describe_restaurant(self):
    print(f"This restaurant {self.restaurant_name} has lots of various cuisines like {self.cuisine_type}.")
    
  def open_restaurant(self):
    print(f"{self.restaurant_name} is open 24/7.")
    
  def set_number_served(self, number):
    self.number_served = number
    
  def increment_number_served(self, number_served):
    self.number_served += number_served
    
restaurant = Restaurant("Mommy's Kitchen", "Jollof & Waakye")

# order = restaurant.number_served
# print(f"The {restaurant.restaurant_name} has served {order} enough people this afternoon.")

# restaurant.number_served = 15
# print(f"The {restaurant.restaurant_name} has served {restaurant.number_served} enough people this afternoon.")
# print(restaurant.number_served)

# restaurant.set_number_served(20)
restaurant.increment_number_served(100)
print(f"The {restaurant.restaurant_name} has increased customers to {restaurant.number_served}.")
