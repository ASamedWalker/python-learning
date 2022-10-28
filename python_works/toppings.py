# toppings.py

# requested_topping = 'mushrooms'

# if requested_topping != 'anchovies':
#   print("Hold the anchovies!")

# requested_toppings = ['mushrooms', 'onions', 'pineapple']

# if 'mushrooms' in requested_toppings and 'pepperoni' in requested_toppings:

#   print(True)

# else:

#   print(False)

# requested_toppings = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_toppings:
#   print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#   print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#   print("Adding extra cheese.")

# print("\nFinished making your pizza!")

# Running an if-statement in a List
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
#   if requested_topping == 'green peppers':
#     print("Sorry, we are out of green peppers right now.")
#   else:
#     print(f"Adding {requested_topping}.")

# print("\nFinished making your pizza!")

# Checking that a list is not empty
# requested_toppings = []

# if requested_toppings:
#   for requested_topping in requested_toppings:
#     print(f"Adding {requested_topping}.")
#   print("\nFinished making your pizza!")
# else:
#   print("Are you sure you want a plain pizza?")

# Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
  if requested_topping in available_toppings:
    print(f"Adding {requested_topping}.")
  else:
    print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")