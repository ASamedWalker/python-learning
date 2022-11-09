import json

filename = 'python_works/text_files/username.json'

with open(filename) as f:
  username = json.load(f)
  print(f'Welcome back, {username}')