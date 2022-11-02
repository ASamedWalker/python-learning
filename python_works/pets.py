# Dictionaries of pets

# animal1 = {
#   'animal': 'wiley',
#   'owner': 'yorkey'
# }

# animal2 = {
#   'animal': 'lukey',
#   'owner': 'francis'
# }

# animal3 = {
#   'animal': 'bossy',
#   'owner': 'joe'
# }

# pets = [animal1, animal2, animal3]

# for pet in pets:
#   print(f"My pets information are: ")
#   for k, v in pet.items():
    # print(f"\t{k}: {v}")
    
# Removing All instances of specific values from a list
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#   pets.remove('cat')
  
# print(pets)

# Positional Arguments
def describe_pet(pet_name, animal_type ='dog'):
  """Display information about a pet."""
  print(f"\nI have a {animal_type}.")
  print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet("hamster", 'harry')

# # Multiple Function Calls
# describe_pet("dog", 'willie')

# # Keyword Arguments
# describe_pet(animal_type='hamster', pet_name='harry')
# # Even wehn you mismatch keyword arguments works perfectly
# describe_pet(pet_name='harry', animal_type='hamster')

# Default Values
# describe_pet(pet_name='willie')

# To describe another animal type aside a dog explicitly
# Python ignores the default value for animal type parameter
# describe_pet(pet_name='harry', animal_type='hamster')

# Equivalent Function Calls
# A dog named Willie
# describe_pet('willie')
# describe_pet(pet_name='Willie')

# #A hamster named Harry
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')

# Avoiding Argument Errors
describe_pet()