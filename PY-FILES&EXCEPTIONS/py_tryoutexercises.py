# 10-1 Learning Python:
# Storing the file object in a list
# with open("text_files/learning_python.txt") as file_Object:
  # spams = file_Object.readlines()
  # print(spams)
# emptyString = ''
# for spam in spams:
#   emptyString += spam
# print(emptyString)
# print(emptyString)
# print(emptyString)


# By reading the content of the file
# with open("text_files/learning_python.txt") as file_Object:
#   content = file_Object.read()
#   print(content)

# By using for loop to loop the content of the file
# with open("text_files/learning_python.txt") as file_Object:
#   for content in file_Object:
#     print(content.strip())

# 10-2 Learning C:
# with open("text_files/learning_python.txt") as file_Object:
#   replaceContent = ''
#   activeListening = True
  
#   while activeListening:
#     for content in file_Object:
#       replaceContent += content.replace('python', 'Go')
#       activeListening = False
#   print(replaceContent)

# Alternative
# with open("text_files/learning_python.txt") as file_Object:
#   contents= file_Object.readlines()
#   print(contents)
# for content in contents:
#   print(content.replace('python', 'Go').strip())

# 10-3 Guest:
# filename = 'text_files/guest.txt'

# with open(filename, 'w') as f:
#   prompt = input("Enter your name to my party: ")
#   f.write(prompt)

# 10-4 Guest Book:
# filename = 'text_files/guest_book.txt'

# active = True

# print("Enter 'quit' when you are finished")

# while active:

#   prompt = input("\nEnter your name: ")

#   if prompt == 'quit':

#     break

#   else:

#     with open(filename, 'w') as f:

#       f.write(f'{prompt}\n')

#       print(f"Welcome {prompt} to the python land. u've been added to the guest book.")


# 10-5 Programming Poll:
# filename = 'text_files/poll_result.txt'

# active = True

# content = []
# print("Enter 'n' to exit the poll survey")

# while active:

#   prompt = input("\nWhy do you like programming? ")

#   content.append(prompt)

#   continue_poll = input("Would you like to let someone else respond? (y/n) ")

#   if continue_poll != 'y':
    
#     break
  
# with open(filename, 'a') as f:
#   for response in content:
#     f.write(f"{response}\n")

# 10-6. Addition:
# print("Enter two numbers to know their addition.")
# try:
#   input_one = int(input("Enter your first number: "))
#   input_two = int(input("Enter your second number: "))
# except ValueError:
#   print("Enter a valid numerical values")
# else:
#   print(f"The sum input of {input_one} and {input_two} is {input_one + input_two}")


# 10-7 Addition Calculator with while loop:
# print("Enter 'q' to end game.")
# activation = True
# while activation:
#   try:
#     input_one = input("Enter your first number: ")
#     if input_one == 'q':
#       break
#     x = int(input_one)
#     input_two = input("Enter your second number: ")
#     if input_two == 'q':
#       break
#     y = int(input_two)
#   except ValueError:
#     print("Enter a valid numerical values")
#   else:
#     sum = x + y
#     print(f"The sum input of {x} and {y} is {sum}")

# 10-8 Cats and Dogs:
# filenames = ['text_files/movers_files/cats.txt', 'text_files/dogs.txt']
# for filename in filenames:
#   try:
#     with open(filename) as f:
#       contents = f.read()
#       print(contents)
#   except FileNotFoundError:
#     print('sorry the file you are trying to locate cannot be found!!!')

# 10-9 Silent Cats and Dogs:
"""Modifying the previous file"""
# filenames = ['text_files/movers_file/cats.txt', 'text_files/dogs.txt']
# for filename in filenames:
#   try:
#     with open(filename) as f:
#       contents = f.read()
# 
#   except FileNotFoundError:
#    pass
#   else:
#     print("\nReading file: {filename}")
#     print(contents)

# 10-10 Common Words:
def count_words(filename, word):
  """Printing how many times the appears in a text."""
  try:
    with open(filename, encoding='utf-8') as f:
      contents = f.read()
  except FileNotFoundError:
    pass
  else:
    word_count = contents.lower().count(word)

    msg = f"{word}' appears in {filename} about {word_count} times."

    print(msg)
    
filename = 'text_files/ebooks.txt'
count_words(filename, 'the')
