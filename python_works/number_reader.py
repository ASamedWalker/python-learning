import json

filename = 'python_works/text_files/numbers.json'

with open(filename) as f:
  numbers = json.load(f)
print(numbers)