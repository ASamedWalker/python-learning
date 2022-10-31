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
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
  pets.remove('cat')
  
print(pets)