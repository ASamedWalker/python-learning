filename = 'python_works/text_files/guest_book.txt'

activate_name = True

while activate_name:
  print("Enter 'quit' to exit the guest line.")
  
  question = input("\nEnter your name to be included in the guest book: ")
  
  if question == 'quit':
    
    break
  
  else:
    respond = f"{question.title()}"
    
    greeting = f"Welcome to the python award ceremony {respond}.\n"
  
  with open(filename, 'a') as fb:
    
    print("Your name is being recorded...")
    
    fb.write(greeting)
    
  activate_name = False
  
  
