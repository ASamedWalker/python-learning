# # 3-8 Seeing the World
# # A list of favorite places to visit
# favorite_places = ['brazil', 'japan', 'madrid', 'chile', 'peru']

# print(favorite_places)

# # Using the sorted() method to print the list in alphabetical order
# print(sorted(favorite_places))

# # List is still in it original order after sorted
# print(favorite_places)

# # Printing the list in a reverse alphabetical order
# print(sorted(favorite_places, reverse=True))

# # list still in it's original order
# print(favorite_places)

# # Now, printing the list in a reverse order 
# favorite_places.reverse()
# print(favorite_places)

# # reversing the list for the second time back
# favorite_places.reverse()
# print(favorite_places)

# # using the sort method to print 
# # the list in alphabetical order
# favorite_places.sort()
# print(favorite_places)

# # printing the list in sort method
# # reversely in alphabetical order
# favorite_places.sort(reverse=True)
# print(favorite_places)

# # 3-9 Dinner Guests:
# dinner_guest = ['jowe', 'angi', 'bob']
# print(f"We have {len(dinner_guest)} guest attending the dinner party.")

# 3-10 Every Function:
# mountains = ['look', 'fair', 'lky']

# mountains.reverse()
# print(mountains)

# mountains.sort()
# print(mountains)

# print(sorted(mountains, reverse=True))
# print(sorted(mountains))

# 6-9. Favorite Places:
favorite_places = {
  'joe': {
    'desti_1': 'london, united kingdom',
    'desti_2': 'new york, usa',
    'desti_3':'accra, ghana',
  },
  
  'alex': {
    'desti_1':'nairobi, kenya',
    'desti_2':'rio, brazil',
    'desti_3':'osaka, japan',
  },
  
  'monique': {
    'desti_1':'cape town, south africa',
    'desti_2':'lome, togo',
    'desti_3':'abuja, nigeria',
  },
}

for name, info in favorite_places.items():
  print(f"\nFavorite places of {name.title()} are: ")
  
  location1 = f"{info['desti_1'].title()}"
  location2 = f"{info['desti_2'].title()}"
  location3 = f"{info['desti_3'].title()}"
  
  print(f"\t - {location1.title()}")
  print(f"\t - {location2.title()}")
  print(f"\t - {location3.title()}")
  