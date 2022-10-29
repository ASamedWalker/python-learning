# Dictionaries of pets

animal1 = {
  'animal': 'wiley',
  'owner': 'yorkey'
}

animal2 = {
  'animal': 'lukey',
  'owner': 'francis'
}

animal3 = {
  'animal': 'bossy',
  'owner': 'joe'
}

pets = [animal1, animal2, animal3]

for pet in pets:
  print(f"My pets information are: ")
  for k, v in pet.items():
    print(f"\t{k}: {v}")