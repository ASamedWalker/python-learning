# Sometimes your file would be in a folder file path
# So in that case you provide a file path like file_path/pi_digits.txt
with open('text_files\pi_digits.txt') as file_object:
  contents = file_object.read()
# print(contents.rstrip())

# Reading Line by Line
# filename = 'text_files\pi_digits.txt'

# with open(filename) as file_object:
#   for line in file_object:
    # print(line.rstrip())

# Making a List of Lines from a File
filename = 'text_files\pi_digits.txt'

with open(filename) as file_object:
  lines = file_object.readlines()
  # print(lines)
# for line in lines:
#   print(line.rstrip())

# Working with a File's Contents
# pi_string.py
filename = 'text_files\pi_digits.txt'

with open(filename) as file_object:
  lines = file_object.readlines()

pi_string = ''
for line in lines:
  pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

# Is Your Birthday Contained in Pi
