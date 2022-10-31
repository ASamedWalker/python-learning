#7-8 Making list of deli sandwich orders
# sandwich_orders = ['chicken', 'egg', 'seafood', 'roast beef']

# finished_sandwiches = []

# while sandwich_orders:
#   making_sandwish = sandwich_orders.pop()
  
#   print(f"I am working on your {making_sandwish} sandwich.")
  
#   finished_sandwiches.append(making_sandwish)
  
#   prompt = "Would like to order more sandwiches. (yes/no)!"
#   repeat_order = input(prompt)
#   if repeat_order == 'no':
#     break

# print(" Finished Sandwiches ".center(30, '=')) 
# for finished_sandwich in finished_sandwiches:
#   print(f" - {finished_sandwich}")
  
# 7-9 No Pastrami:
sandwich_orders = ['chicken','pastrami', 'egg', 'pastrami', 'seafood', 'roast beef', 'pastrami']

print("The Deli has run out of Pastrami".center(30, '='))

finished_sandwiches = []

while 'pastrami' in sandwich_orders:
  
  sandwich_orders.remove('pastrami')
    
print("\n")
    
while sandwich_orders:
    
  making_sandwich = sandwich_orders.pop()
  
  print(f"Your {making_sandwich} will be on it's way.")
  
  finished_sandwiches.append(making_sandwich)
  
  prompt = "Would you like to re-order another sandwich: (yes/no)! "
  
  repeat = input(prompt)
  
  if repeat == 'no':
    
    break

print(" Finished Sandwiches ".center(30, '=')) 
for finished_sandwich in finished_sandwiches:
  print(f" - {finished_sandwich.title()}")