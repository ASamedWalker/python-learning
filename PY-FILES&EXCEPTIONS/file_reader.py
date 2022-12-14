# Sometimes your file would be in a folder file path
# So in that case you provide a file path like file_path/pi_digits.txt
from turtle import title


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
# try:
#   print(5/0)
# except ZeroDivisionError:
#   print("You can't divide by zero!")

# # USING EXCEPTIONS TO PREVENT CRASHES
# # The else Block
# # division_calculator.py
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")

# while True:
#   first_number = input("\nFirst number: ")
#   if first_number == 'q':
#     break
#   second_number = input("Second number: ")
#   if second_number == 'q':
#     break
#   try:
#     answer = int(first_number) / int(second_number)
#   except ZeroDivisionError:
#     print("You can't divide by 0!")
#   else:
#     print(answer)

# Handling the FileNotFoundError Exception
"""Trying to read a file that doesn't exist in the file.
   The open() function produced the error, so to handle it, 
   we use the try block
"""
# filename = 'text_files/alice.txt'

# try:
#   with open(filename, encoding='utf-8') as f:
#     contents = f.read()
# except FileNotFoundError:
#   print(f"Sorry, the file {filename} does not exist.")
# else:
#   # Count the approximate number of words in the file.
#   words = contents.split()
#   num_words = len(words)
#   print(f"The file {filename} has about {num_words} words.")


# ANALYZING TEXT
# title = "Alice in Wonderland"
# now = title.split()
# print(now)

# WORKING WITH MULTIPLE FILES
"""Working with multiple books would require the
  use of a function to make our code compact. 
"""
# def count_words(filename):
#   """Count the approximate number of words in a file."""
#   try:
#     with open(filename, encoding='utf-8') as f:
#       contents = f.read()
#   except FileNotFoundError:
#     print(f"Sorry, the file {filename} does not exist.")
#   else:
#   # Count the approximate number of words in the file.
#     words = contents.split()
#     num_words = len(words)
#     print(f"The file {filename} has about {num_words} words.")
# filenames = ['text_files/alice.txt', 'text_files/siddhartha.txt', 'text_files/moby_dick.txt', 'text_files/little_women.txt']
# for filename in filenames:
#   count_words(filename)

# FAILING SILENTLY
# def count_words(filename):
#   """Count the approximate number of words in a file."""
#   try:
#     with open(filename, encoding='utf-8') as f:
#       contents = f.read()
#   except FileNotFoundError:
#     """To make a code fail silently python uses the pass statement.
#     The pass statement acts as a placeholder.
#     """
#     pass
#   else:
#   # Count the approximate number of words in the file.
#     words = contents.split()
#     num_words = len(words)
#     print(f"The file {filename} has about {num_words} words.")
# filenames = ['text_files/alice.txt', 'text_files/siddhartha.txt', 'text_files/moby_dick.txt', 'text_files/little_women.txt']
# for filename in filenames:
#   count_words(filename)

# DECIDING WHICH ERRORS TO REPORT
# STORING DATA
"""Using json.dump() and json.load().
  json.dump() function takes two arguments: a piece of data to store
  and a file object it can use to store the data.
  it is use to store the set of data.
"""
# This are simple ways to share data between two programs
# This is a json.dump() function
# import json

# numbers = [2, 3, 5, 7, 11, 13]

# filename = 'text_files/numbers.json'
# with open(filename, 'w') as f:
#   json.dump(numbers, f)

# This is a json.load() function
# import json

# filename = 'text_files/numbers.json'
# with open(filename) as f:
#   numbers = json.load(f)

# print(numbers)

# Saving and Reading User-Generated Data
# It is useful when you're working with user-generated data
# The user's name was stored in the json format
# import json

# username = input("What is your name? ")

# filename = 'text_files/username.json'
# with open(filename, 'w') as f:
#   json.dump(username, f)
#   print(f"We'll remember you when you come back, {username}!")

# Now, lets read the json saved data with python
# import json

# filename = 'text_files/username.json'

# with open(filename) as f:
#   username = json.load(f)
#   print(f"Welcome back, {username}!")


# remember_me.py Example
# import json

# # Load the username, if it has been stored previously.
# # Otherwise, prompt for the username and store it.
# filename = 'text_files/username.json'

# try:
#   with open(filename) as f:
#     username = json.load(f)
# except FileNotFoundError:
#   username = input("What is your name? ")
#   with open(filename, 'w') as f:
#     json.dump(username, f)
#     print(f"We'll remember you when you come back, {username}!")
# else:
#   if username:
#     correct = input(f"Are you {username}: (y / n)")
#     if correct == 'y':
#       print(f"Welcome back, {username}!")
#     else:
      

# REFACTORING CODE
"""Refactoring involves breaking up code into series of functions 
   that have specific jobs.
"""
import json

def greet_user():
  """Greet the user by name."""
  username = get_stored_username()

  if username:
    correct = input(f"Are you {username}: (y/n)")
    if correct == 'y':
      print(f"Welcome back, {username}!")
  else:
    username = get_new_username()
    print(f"We'll remember you when you come back, {username}")
greet_user()

def get_new_username():
  """Prompt for a new username."""
  username = input("What is your name? ")
  filename = 'text_files/username.json'
  with open(filename, 'w') as f:
    json.dump(username, f)
  return username

def get_stored_username():
  """Get stored username if available."""
  filename = 'text_files/username.json'

  try:
    with open(filename) as f:
      username = json.load(f)
  except FileNotFoundError:
    return None
  else:
    return username

