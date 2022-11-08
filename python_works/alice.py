filename = 'python_works/text_files/alice.txt'

try:
  with open(filename, encoding='utf-8') as f:
    contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exit.")
else:
  # Count the approximate number of words in the file.
  words = contents.split()
  num_words = len(words)
  print(f"The file {filename} has about {num_words} words.")