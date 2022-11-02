#8-3 Defining a function called t_shirt
# def make_shirt(size):
#   """print a text sumarize the size of a shirt..."""
#   print(f"The size of the t-shirt is {size}")
  
# # Calling the function based on positional arguments
# make_shirt('medium')

# # Calling the function based on keyword arguments
# make_shirt(size='medium')

# 8-4 Large Shirts:
# Modifying the initial t-shirt code
def make_shirt(message = "I love python", size='large'):
  """print a text sumarize the size of a shirt..."""
  print(f"The size of the t-shirt is {size}, and its written on it '{message}'!")
  
# Calling the function based on positional arguments
# make_shirt("I love Python")

# # Calling the function based on keyword arguments
# make_shirt(message="I love python")

# Default message
make_shirt()

# Meidum t-shirt
def make_shirt(message = "I love python", size='medium'):
  """print a text sumarize the size of a shirt..."""
  print(f"The size of the t-shirt is {size}, and its written on it '{message}'!")
  
make_shirt()

