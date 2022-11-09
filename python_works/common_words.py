# A program to find how many times a word appear in a text
def common_words(filename, word):
  """Counting how many times a word 'the' appears in the text"""
  try:
    with open(filename, encoding='utf-8') as fb:
      contents = fb.read()
  except FileNotFoundError:
    print("Loading....file is missing")
  else:
    words = contents.lower().count(word)
    print(f"The number of 'the ' in the file is: {words}")

filenames = 'python_works/text_files/common_word.txt'
common_words(filenames, 'the ')
  
# filename = 'python_works/text_files/common_word.txt'

# with open(filename, encoding='utf-8') as fb:
  
#   contents = fb.read()

#   word = contents.lower().count('the ')
  
#   print(word)
  
  