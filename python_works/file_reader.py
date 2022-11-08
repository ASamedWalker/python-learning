# Reading from a file

# with open('text_files/pi_digits.txt') as file_object:
#   contents = file_object.read()
# print(contents.rstrip())

# Reading Line by line
filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
  # This readlines returns the file in a list
  lines = file_object.readlines()
  
  for line in lines:
    print(line.rstrip())