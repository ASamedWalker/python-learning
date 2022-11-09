import json

number = input('What is your favorite number: ')

responds = int(number)

filename = 'python_works/text_files/f_numbers.json'

with open(filename, 'w') as f:
  
  json.dump(responds, f)
  
  print("I will remember your number.")