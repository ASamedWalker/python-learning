prompt = "What is you favorite pizza toppings:"
prompt += "\n(Enter 'quit' to exit out of the program): \n"



while True:
  
  name_toppings = input(prompt)
  
  if name_toppings == 'quit':
    
    break
  
  else:
    
    print(f"your favorite pizza toppings {name_toppings} has been added to your pizza.")
    