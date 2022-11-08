
# Reading from afile and replacing a word Python to C
filename = 'python_works/text_files/learning_python.txt'

with open(filename) as fb: 
  lines = fb.readlines()
  
for line in lines:
  
  new_word = line.replace('Python', 'C')
  
  print(new_word.strip())