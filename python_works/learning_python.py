# 10-1 Learning Python
# A program to open a text file on my computer
# For Looping
filename = 'python_works/text_files/learning_python.txt'
# with open(filename) as fb:
#   lines = fb.readlines()
#   for line in lines:
#     print(line)
    

# For reading the package off the file
# with open(filename) as fb:
#   lines = fb.read()
# print(lines)

with open(filename) as fb:
  
  lines = fb.readlines()
  
for line in lines:
  
  print(line.strip())