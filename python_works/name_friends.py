# 3-1. Names:
# Storing a collection of friends name in a list
from unicodedata import name


name_friends = ['bob', 'jake', 'doe', 'sam']

# Printing each person's name from the list
print(name_friends[0].title())
print(name_friends[1].title())
print(name_friends[2].title())
print(name_friends[3].title())


# 3-2 Greetings:
print(f"{name_friends[0].title()}, you are welcome to the python world!")
print(f"{name_friends[1].title()}, you are welcome to the python world!")
print(f"{name_friends[2].title()}, you are welcome to the python world!")
print(f"{name_friends[3].title()}, you are welcome to the python world!")


# 3-3 Your Own List:
transportation = ['train', 'bus', 'car', 'bicycle']

print(f"I would like to build a {transportation[0]} factory!")
print(f"I would like to own a {transportation[0]} building factory!")
print(f"I would like to buy my own {transportation[0]} in month time!")
print(f"I would like to buy a mini {transportation[0]} for my transportation!")
