filename = 'python_works/text_files/programming.txt'

# with open(filename, 'w') as fb:
#   fb.write("I love programming.\n")
#   fb.write("I love creating new games.\n")
  
  
with open(filename, 'a') as fb:
  fb.write("I also love finding meaning in large datasets.\n")
  fb.write("I love creating apps that can run in a browser.\n")