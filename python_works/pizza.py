# Passing Arbitrary Arguments with the '*' star
# def make_pizza(*toppings):
#   """Print the list of toppings that have been requested.
#      Summarize the pizza we are about to make.
#   """
#   print("\nMaking a pizza with the following toppings:")
#   for topping in toppings:
#     print(f"- {topping}")
  
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


# Mixing Positional and Arbitrary Arguments
# You often see the generic parameter name *args, 
# that collects arbitrary positional arguments like this. 
def make_pizza(size, *args):
  """Print the list of toppings that have been requested.
     Summarize the pizza we are about to make.
  """
  print(f"\nMaking a {size}-inch pizza with the following toppings:")
  for topping in args:
    print(f"- {topping}")
  
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')