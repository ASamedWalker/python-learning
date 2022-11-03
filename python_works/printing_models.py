# Start with some designs that need to be printed.
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # Simulare printing each design, until none are left.
# # Move each design to completed_models after printing.
# while unprinted_designs:
#   current_design = unprinted_designs.pop()
  
#   print(f"Printing model: {current_design}")
#   completed_models.append(current_design)
  
# #Display all completed models
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#   print(completed_model)

# Including the code inside a function
def print_models(unprinted_designs, completed_models):
  """
  Simulate printing each design, until none are left.
  Move each design to completed_models after printing.
  """
  while unprinted_designs:
    current_design = unprinted_designs.pop()
  
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

def show_completed_models(completed_models):
  """Show all the models that were printed."""
  print("\nThe following models have been printed:")
  for completed_model in completed_models:
    print(completed_model)
    
    
def unprinted_copy(unprinted):
  print(unprinted)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
unprinted_copy = unprinted_designs[:]
completed_models = []

print_models(unprinted_copy, completed_models)
print(unprinted_designs)
show_completed_models(completed_models)

