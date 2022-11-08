filename = 'python_works/text_files/poll_result.txt'

active_poll = True

while active_poll:
  print("Enter 'quit' to exit the poll\n")
  question = input("\nWhy do you like programming? ")
  if question == 'quit':
    break
  else:
    responses = f"{question}"
  
  with open(filename, 'a') as fb:
    print("Recording your responses...")
    fb.write(f"{responses}\n")
    
  active_poll = False