# Refactoring
import json

try:
  filename = 'python_works/text_files/f_numbers.json'
  
  with open(filename) as f:

    contents = json.load(f)
  
except FileNotFoundError:
  number = input('What is your favorite number: ')

  responds = int(number)

  filename = 'python_works/text_files/f_numbers.json'

  with open(filename, 'w') as f:
    
    json.dump(responds, f)
    
    print("I will remember your number.")
else:
   print(f"I know your favorite number is : {contents}!")
  
  


