# FUNCTIONS
# def greet_user():
#   """Display a simple greeting."""
#   print("Hello!")

# greet_user()

# # PASSING INFORMATION TO A FUNCTION
# def greet_user(username):
#   """Display a simple greeting with a name"""
#   print(f"Hello , {username.title()}!")

# greet_user('jesse')

# ARGUMENTS AND PARAMETERS
# Variables in a function definition is called a parameter
# Values in the function call is called an argument

# PASSING ARGUMENTS
# Positional Arguments
# egs. pets.py

# def describe_pet(animal_type, pet_name):
#   """Display information about a pet."""
#   print(f"\nI have a {animal_type}.")
#   print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

# ORDER MATTERS IN POSITIONAL ARGUMENTS
# KEYWORD ARGUMENTS
# When using keyword arguments, be sure to use the exact names
# of the parameters in the function's definition
# def describe_pet(animal_type, pet_name):
#   """Display information about a pet."""
#   print(f"\nI have a {animal_type}.")
#   print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet(animal_type='hamster', pet_name='harry')

# DEFAULT VALUES
# def describe_pet(pet_name, animal_type='hamster'):
#   """Display information about a pet."""
#   print(f"\nI have a {animal_type}.")
#   print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet(pet_name='harry')
# describe_pet('harry')

# AVOIDING ARGUMENT ERRORS
# AVOID MISSING MATCHING PARAMETERS WITH THE ARGUMENTS
# RETURN VALUES
# formatted_name.py
# def get_formatted_name(first_name, last_name):
#   """Return a full name, neatly formatted."""
#   full_name = f'{first_name} {last_name}'
#   return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# # Making an Argument Optional
# def get_formatted_name(first_name, last_name, middle_name=''):
#   """Return a full name, neatly formatted."""
#   if middle_name:
#     full_name = f'{first_name} {middle_name} {last_name}'
#   else:
#     full_name = f'{first_name} {last_name}'

#   return full_name.title()

# musician = get_formatted_name('john', 'hooker')
# print(musician)

# # RETURNING A DICTIONARY
# # person.py
# def build_person(first_name, last_name):
#   """Return a dictionary of information about a person"""
#   person = {'first': first_name, 'last': last_name}
#   return person

# musician = build_person('jimi', 'hendrix')
# print(musician)

# # Modifying person's dictionary
# def build_person(first_name, last_name, age=None):
#   """Return a dictionary of information about a person"""
#   person = {'first': first_name, 'last': last_name}
#   if age:
#     person['age'] = age
#   return person

# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

# # Using a Function with a while Loop
# def get_formatted_name(first_name, last_name):
#   """Return a full name, neatly formatted."""
#   full_name = f'{first_name} {last_name}'
#   return full_name.title()

# # This is an infinite loop!
# information_dictionary = {}

# while True:
#   print("\nPlease tell me your name:")
#   print("(enter 'q' at any time to quit)")
#   f_name = input("First name: ")
#   if f_name == 'q':
#     break
#   l_name = input("Last name: ")
#   if l_name == 'q':
#     break

#   # information_dictionary['first_name'] = f_name
#   # information_dictionary['last_name'] = l_name

#   formatted_name = get_formatted_name(f_name, l_name)
  
#   information_dictionary['full_name'] = formatted_name
#   print(f"\nHello, {formatted_name}!")


# print(information_dictionary)


# PASSING A LIST
# greet_users.py
# def greet_users(names):
#   """Print a simple greeting to each user in the list."""
#   for name in names:
#     msg = f'Hello, {name.title()}'
#     print(msg)

# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)

# printing_models.py
# Start with some designs that need to be printed.
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# while unprinted_designs:
#   current_design = unprinted_designs.pop()

#   print(f"Printing model: {current_design}")
#   completed_models.append(current_design)

# # Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#   print(completed_model)

# Moving printing_models.py into a function
# first function handles the printing of the design



# def print_models(unprinted_designz, completed_models):
#   """
#   Simulating printing each design, until none are left.
#   Move each design to completed_models after printing.
#   """
#   while unprinted_designz:
#     current_design = unprinted_designz.pop()

#     print(f"Printing model: {current_design.title()}")
#     completed_models.append(current_design)

# def show_completed_models(completed_models):
#   """Show all the models that were printed."""
#   print("\nThe following models have been printed:")
#   for completed_model in completed_models:
#     print(completed_model.title())

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# unprinted_designz = unprinted_designs[:]
# completed_models = []

# print_models(unprinted_designz, completed_models)
# show_completed_models(completed_models)
# print(unprinted_designs)

# PREVENTING A FUNCTION FROM MODIFYING A LIST
# To prevent a modifying list we use the slice syntax '[:]' to make 
# a copy of the original list. We later use the copied list to modifying

# PASSING AN ARBITRARY NUMBER OF ARGUMENTS
# pizza.py
# def make_pizza(*toppings):
#   # """Print the list of toppings that have been requested."""
#   # print(toppings)
#   """Summarize the pizza we are about to make."""
#   print("\nMaking a pizza with the following toppings:")
#   for topping in toppings:
#     print(f"- {topping}")
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# MIXING POSITIONAL AND ARBITRARY ARGUMENTS
# def make_pizza(size, *toppings):
#   print(f"\nMaking a {size}-inch pizza with the following toppings:")
#   for topping in toppings:
#     print(f"- {topping}")

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# OR 

def make_pizza(size, *args):
  print(f"\nMaking a {size}-inch pizza with the following toppings:")
  for topping in args:
    print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# USING ARBITRARY KEYWORD ARGUMENTS
# user_profile.py
# def build_profile(first, last, **user_info):
#   """Build a dictionary containing everything we know about a user."""
#   user_info['first_name'] = first
#   user_info['last_name'] = last
#   return user_info

# user_profile = build_profile('albert', 'einstein',
#                             location='princeton',
#                             field='physics')
# print(user_profile)

# OR 

def build_profile(first, last, **kwargs):
  """Build a dictionary containing everything we know about a user."""
  kwargs['first_name'] = first
  kwargs['last_name'] = last
  return kwargs

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')
print(user_profile)

# STORING YOUR FUNCTIONS IN MODULES
# syntax for calling modules
# module_name.function_name()

# IMPORTING SPECIFIC FUNCTIONS
# Syntax
# from module_name import function_name

# Importing many functions
# Syntax
# from module_name import function_0, function_1, function_2

# USING AS TO GIVE A FUNCTION AN ALIAS
# use alias short unique name 'as' to avoid naming conflictions
# syntax: 
# from module_name import function_name as fn

# USING 'as' TO GIVE A MODULE AN ALIAS
# syntax:
# import module_name as mn

# IMPORTING ALL FUNCTIONS IN A MODULE
# we use the * to import all functions in a module
# syntax:
# from module_name import *
