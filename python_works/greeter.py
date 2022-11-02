# Writing clear prompts
# name = input ("Please enter your name: ")


# Writing a prompt that is long
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "


# name = input(prompt)
# print(f"\nHello, {name}!")


# Defining a Function
# def greet_user():
#   """Display a simple greeting."""
#   print("Hello!")
  
# greet_user()

# # Modifying the function by passing it information
# def greet_user(username):
#   """Display a simple greeting."""
#   print(f"Hello, {username.title()}!")
  
# greet_user('jesse')

# Using a Function with a while Loop
# This is an infinite loop!

def get_formatted_name(first_name, last_name):
  """Return a full name, neatly formatted."""
  full_name = f"{first_name} {last_name}"
  return full_name.title()

#Inifite Loop
while True:
  print("\nPlease tell me your name:")
  print("(enter 'q' at any time to quit)")
  f_name = input("First name: ")
  if f_name == 'q':
    break
  l_name = input("Last name: ")
  if l_name == 'q':
    break
  
  formatted_name = get_formatted_name(f_name, l_name)
  print(f"\nHello, {formatted_name}!")