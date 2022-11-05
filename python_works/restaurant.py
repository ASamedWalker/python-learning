# This is a tuple of a basic buffet food served in a restaurant
# basic_foods = ('buffet salads', 'roast duck', 'glazed ham')

# print("The buffet served at the restaurant near me are:")
# for buffet in basic_foods:
#   print(f" - {buffet.title()}")

# print("\n")

# basic_foods = ('palava source', 'bread and honey', 'glazed ham')
# print("The revised new menu:")
# for new_buffet in basic_foods:
#   print(f" - {new_buffet.title()}.")

# 9-1 Restaurant:
class Restaurant:
  def __init__(self, restaurant_name, cuisine_type) -> None:
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    
  def describe_restaurant(self):
    print(f"This restaurant {self.restaurant_name} has lots of various cuisines like {self.cuisine_type}.")
    
  def open_restaurant(self):
    print(f"{self.restaurant_name} is open 24/7.")
    
my_restaurant = Restaurant("Mommy's Kitchen", "Jollof & Waakye")

# print(my_restaurant.restaurant_name)
# print(my_restaurant.cuisine_type)

# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()


# 9-2 Three Restaurants:
restaurant = Restaurant('Lick your hands', 'Banku and Tilapia')
restaurant.describe_restaurant()
restaurant = Restaurant('Pop eaters', 'Rice and Tilapia')
restaurant.describe_restaurant()
restaurant = Restaurant('Dinners Spot', 'Salads and full Chicken')
restaurant.describe_restaurant()