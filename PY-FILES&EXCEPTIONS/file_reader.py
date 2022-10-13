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
# filename = 'text_files\pi_million_digits.txt'

# with open(filename) as file_object:
#   lines = file_object.readlines()

# pi_string = ''
# for line in lines:
#   pi_string += line.strip()

# print(f"{pi_string[:52]}...")
# print(len(pi_string))

# Is Your Birthday Contained in Pi
# birthday = input("Enter your birthday. in the form mmddyy: ")
# if birthday in pi_string:
#   print("Your birthday appears in the first million digits of pi!")
# else:
#   print("Your birthday does not appear in the first million digits of pi.")

# WRITING TO A FILE
# Writing to an Empty File
# filename = 'text_files/programming.txt'

# with open(filename, 'w') as file_object:
#   file_object.write("I love programming.\n")
#   file_object.write("I love creating new games.\n")


# # WRITING MULTIPLE LINES

# # filename = 'text_files/programming.txt'

# # with open(filename, 'w') as file_object:
# #   file_object.write("I love programming.\n")
# #   file_object.write("I love creating new games.\n")

# # APPENDING TO A FILE
# filename = 'text_files/programming.txt'

# with open(filename, 'a') as file_object:
#   file_object.write("I also love finding meaning in large datasets.\n")
#   file_object.write("I love creating apps that can run in a browser.\n")


# EXCEPTIONS:
# USING TRY-EXCEPT BLOCKS
try:
  print(5/0)
except ZeroDivisionError:
  print("You can't divide by zero!")

# USING EXCEPTIONS TO PREVENT CRASHES
# The else Block
# division_calculator.py
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
  first_number = input("\nFirst number: ")
  if first_number == 'q':
    break
  second_number = input("Second number: ")
  if second_number == 'q':
    break
  try:
    answer = int(first_number) / int(second_number)
  except ZeroDivisionError:
    print("You can't divide by 0!")
  else:
    print(answer)