# prompt = input("Tell me something, and I will repeat it back to you: ")
# prompt += "\nEnter 'quit' to end the program. "

# message = ""
# while message != 'quit':
#   message = input(prompt)
#   if message != 'quit':
#     print(message)
    
    
# Using the Flag Now
prompt = input("Tell me something, and I will repeat it back to you: ")
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
  message = input(prompt)
  
  if message == 'quit':
    active = False
  else:
    print(message)