# 8-12 Sandwiches:
def sandwiches_list(*args):
  """Printing sandwiche items from a single individual."""
  print("Summarize the items from the list of sandwiches are: ")
  for item in args:
    print(f"- {item} sandwiches")

sandwiches_list('chicken')
sandwiches_list('chicken', 'beef', 'tilapia')
sandwiches_list('chicken', 'beef', 'tilapia', 'fish') 