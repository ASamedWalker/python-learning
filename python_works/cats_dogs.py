# 10-8 Cats and Dogs
# def cats_dogs(cats_and_dogs):
#   """A program to read a contents of the text in the files"""
#   print(f"\nReading file: {cats_and_dogs}")
#   try:
#     with open(cats_and_dogs) as fb:
#       contents = fb.read()
#   except FileNotFoundError:
#     print("Loading....")
#     print("The file you searching is missing.")
#   else:
#     print(f"{contents.title()}")

# filenames = ['python_works/text_files/cats.txt','python_works/text_files/dogs.txt']
# for filename in filenames:
#   cats_dogs(filename)
  
# 10-9 Silent Cats and Dogs:(Modifying to fail silently)
def cats_dogs(cats_and_dogs):
  """A program to read a contents of the text in the files"""
  print(f"\nReading file: {cats_and_dogs}")
  try:
    with open(cats_and_dogs) as fb:
      contents = fb.read()
  except FileNotFoundError:
    pass
  else:
    print(f"{contents.title()}")

filenames = ['python_works/text_files/cats.txt','python_works/text_files/dogs.txt']
for filename in filenames:
  cats_dogs(f" - {filename}")