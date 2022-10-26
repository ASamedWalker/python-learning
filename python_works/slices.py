# 4-10 Using slices
players = ['charles', 'martina', 'micheal', 'florence', 'eli', 'sam']
empty_players = []

# Printing the first three items in the list
# for player in players[:3]:
#   empty_players.append(player)
# print(f"The first three of the items in the list are:")
  

# for player in empty_players:
#   print(f" - {player.title()}")

# Priniting the three middle items in the list
# for player in players[2:4]:
#   empty_players.append(player)
# print(f"The three middle items in the list are:")
  

# for player in empty_players:
#   print(f" - {player.title()}")

# Printing the last three items in the list
# for player in players[3:]:
#   empty_players.append(player)
# print(f"The first three of the items in the list are:")
  

# for player in empty_players:
#   print(f" - {player.title()}")

# 4-11. My Pizzas, Your Pizzas:
pizzas = ['cheese', 'chicken', 'veges']

friend_pizzas = pizzas[:]

pizzas.append('banana')
friend_pizzas.append('meat')

# print(pizzas)
# print(friend_pizzas)


# new_pizza = []
# for pizza in pizzas:
#   new_pizza.append(pizza)
# print(f"My friend's favorite pizzas are:")

# for favorite_pizza in new_pizza:
#   print(f" - {favorite_pizza.title()} pizza")

# print("\n")
# newz_pizza = []
# for pizza in friend_pizzas:
#   newz_pizza.append(pizza)
# print(f"My friend's favorite pizzas are:")

# for favorite_pizza in newz_pizza:
#   print(f" - {favorite_pizza.title()} pizza")

# 4-12 More Loops
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

new_food = []
for favorite_food in my_foods:
  new_food.append(favorite_food)
print(f"My friend's favorite food are:")

for favorite_food in new_food:
  print(f" - {favorite_food.title()}.")

print("\n")
new_food2 = []
for favorite_foodz in friend_foods:
  new_food2.append(favorite_foodz)
print(f"My friend's favorite food are:")

for favorite_foodz in new_food2:
  print(f" - {favorite_foodz.title()}.")