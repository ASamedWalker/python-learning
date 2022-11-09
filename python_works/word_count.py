def count_words(filename):
  """Count the approximate number of words in a file."""
  try:
    with open(filename, encoding='utf-8') as f:
      contents = f.read()
  except FileNotFoundError:
    # For try and exception to fail silently without letting the user know of the error
    pass
    # print(f"Sorry, the file {filename} does not exit.")
  else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
    
  
filenames = ['python_works/text_files/alice.txt', 'python_works/text_files/siddhartha.txt', 'python_works/text_files/moby_dick.txt', 'python_works/text_files/little_women.txt']
for filename in filenames:
  count_words(filename=filename)