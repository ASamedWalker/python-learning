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
filename = 'text_files/poll_result.txt'

active = True

content = []
print("Enter 'n' to exit the poll survey")

while active:

  prompt = input("\nWhy do you like programming? ")

  content.append(prompt)

  continue_poll = input("Would you like to let someone else respond? (y/n) ")

  if continue_poll != 'y':
    
    break
  
with open(filename, 'a') as f:
  for response in content:
    f.write(f"{response}\n")


