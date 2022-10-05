#7-4 Pizza Toppings:
# prompt = "Enter your favorite pizza toppings: "
# prompt += "(Enter 'quit' when you feel you have enough)"

# pizza_topping = []

# activation = True
# while activation:
#   message = input(prompt)
#   pizza_topping.append(message)
#   print("you've added this toppings to your pizza")

#   if message == 'quit':
#     activation = False

# print(pizza_topping)

# 7-5 Movie Tickets:
# prompt = "Enter your age to determine the prices for the movie tickets:"

# activateAge = True
# while activateAge:
#   userAge = int(input(prompt))

#   if userAge <= 3:
#     print(f'Ticket is free for people of age {userAge}')
#   elif userAge == 3 or userAge == 12:
#     print("The ticket is $10")
#   elif userAge >= 12:
#     print("The ticket is $15")
#   else:
#     activateAge = False


# 7-6 Three Exits:
# 7-7 Infinity
# x = 1
# while x < 10:
#   print(x)

# 7-8 Deli:
# sandwich_orders = ['chicken', 'pastrami', 'fish', 'beef', 'pastrami', 'lamp', 'pastrami']
# # print(sandwich_orders)
# print("The deli has run out of pastrami:")
# while 'pastrami' in sandwich_orders:
#   sandwich_orders.remove('pastrami')

# print(sandwich_orders)

# finished_sandwiches = []

# while sandwich_orders:
#   popped_sandwiches = sandwich_orders.pop()
#   print(f"I made your {popped_sandwiches.title()} sandwich")
#   finished_sandwiches.append(popped_sandwiches.title())

# print("The list of sandwiches made are:")
# for finished_sandwich in finished_sandwiches:
#   print(f"{finished_sandwich} sandwich")

# 7-9 No Pastrami:
# print("The deli has run out of pastrami")
# while 'pastrami' in sandwich_orders:
#   sandwich_orders.remove('pastrami')

# print(sandwich_orders)

# 7-10 Dream Vacation:
# a vacation polling 
# vacation_destination = {}

# # set a flag to make the polling active
# prompt = "If you could visit a dream destination for your vacation, "
# prompt += "Where would you like to go? "

# active_poll = True

# while active_poll:

#   name = input("What is your name: ")
#   poll_message = input(prompt)

#   # Storing the poll responses in a dictionary
#   vacation_destination[name] = poll_message

#   # Finding out if someone would like to be asked about the polls
#   repeat = input("Would you want to continue working on the polls? (yes/no) ")

#   if repeat == "no":
#     active_poll = False

# print("\n--- Vacation Poll Results ---")
# for name, destination in vacation_destination.items():
#   print(f"{name.title()} wants to visit {destination.title()}")

# 8-1 Message:
# function name that prints out a message
# def display_message():
#   print("I am learning a chapter on python programming called functions")
# # function call
# display_message()

# # 8-2 Favorite Book:
# def favorite_book(title):
#   print(f"My favorite books is {title.title()}.")

# favorite_book("Alice in Wonderland")

# 8-3 T-Shirt: Positional Arguments


# def make_shirt(size, message):
#   print(f'{message} {size}')
# make_shirt('medium', 'The size of the is:')

# # Keyword - Arguments
# def make_shirt(size, message):
#   print(f'{message} {size}')
# make_shirt(size='extra-large', message='The size of the is:')

# # Default Value - Arguments
# def make_shirt(message, size='extra-small'):
#   print(f'{message} {size}')
# make_shirt('The size of the is:')
# make_shirt(message='The size of the is:')


# # 8-4 Large Shirts:
# # Default Value arguments for size
# def make_shirt(message, size='large'):
#   print(f'{message} {size}')
# make_shirt('I love Python:')
# make_shirt(message='I love Python:')

# # Default value arguments for message
# def make_shirt(size, message='I love Python'):
#   print(f'{message} {size}')
# make_shirt('medium')
# make_shirt(size='medium')

# 8-5 Cities:
# Positional Arguments
# def describe_city(city, country):
#   print(f'{city.title()} is in {country.title()}')
# describe_city('accra', 'ghana')

# Default Values
# def describe_city(city, country = 'ghana'):
#   print(f'{city.title()} is in {country.title()}')
# describe_city('accra')
# describe_city('tamale')
# describe_city(city='vancouver', country='canada')

# 8-6 City Names:
# def city_country(city, country):
#   return f"'{city.title()}, {country.title()}'"

# name_of_city_and_country = city_country("santiago", 'chile')
# name_city_and_country = city_country("accra", 'ghana')
# name_citycountry = city_country("new-york", 'usa')
# print(name_of_city_and_country)
# print(name_city_and_country)
# print(name_citycountry.upper())

# 8-7 Album:
# def make_album(artistName, albumTitle, makeAlbum=None):
#   return {artistName.title(), albumTitle.title(), makeAlbum}

# album1 = make_album('nas', 'little hope')
# album2 = make_album('samesh', 'party mood')
# album3 = make_album('surish', 'stone cast away')
# # print(album1)
# # print(album2)
# # print(album3)

# # 8-8 User Albums:
# while True:
#   artist_input = input("Enter name of your favorite artist: ")
#   if artist_input == 'q':
#     break

#   album_input = input("Enter artist album name: ")
#   if album_input == 'q':
#     break

#   album_number_input = int(input("Enter how many albums artist got: "))
#   if album_number_input == 0:
#     break;

#   finishedInformation = make_album(artist_input.title(), album_input.title(), album_number_input)
  
#   print(finishedInformation)

# 8-9 Messages:
# def short_message(text_messages):
#   for text_msg in text_messages:
#      print(f'Things i love doing: {text_msg} ')

# short_text = ['walker like swimming', 'sam likes hiking']
# short_message(short_text)


# # 8-10 Sending Messages:
# def send_messages(record_txt, recorded_txt):
#   while record_txt:
#     current_txt = record_txt.pop()

#     print(f'\nThings i love doing: {current_txt.title()}')
#     recorded_txt.append(current_txt)

# short_txt = short_text[:]
# sent_messages = []


# # 8-11 Archived Messages:
# send_messages(short_txt, sent_messages)
# print(short_text)
# print(sent_messages)

# 8-12 Sandwiches:
def make_sandwiches(*args):
  """Building list of items on sandwiches"""
  print("Summary of items ordered to be added on a sandwich: ")
  for arg in args:
    print(f"- {arg.title()}")

make_sandwiches("tomato", "avocado", "fried eggs", "toasted chicken")
make_sandwiches("salad", "mayo")
make_sandwiches("cheese", "onions", "butter")

# 8-13 User Profile:
def build_profile(first, last, **kwargs):
  """Build a dictionary containing everything we know about a user."""
  kwargs['first_name'] = first
  kwargs['last_name'] = last
  return kwargs

user_profile = build_profile('samed', 'walker',
                            location='new york',
                            field='computer science')

print(user_profile)

# 8-14 Cars:
def make_car(manufacturer, model, **kwargs):
  print("\nBuilding a new model electric car who's info are: ")
  kwargs['maufacturer'] = manufacturer
  kwargs['model'] = model
  return kwargs

car_info = make_car('subaru', 'outback', color="blue", tow_package=True)
print(car_info)

# 8-15 Printing Models
# 8-16 Imports

