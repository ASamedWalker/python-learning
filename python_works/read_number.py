import json

filename = 'python_works/text_files/f_numbers.json'

with open(filename) as f:
  
  contents = json.load(f)
  
  print(f"I know your favorite number is : {contents}!")