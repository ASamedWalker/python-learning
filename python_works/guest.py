# Writing to a file by accepting inputs from a user
filename = 'python_works/text_files/guest.txt'

question = input("Enter your name on the guest list: ")

respond = f"My name is {question.title()}."

with open(filename, 'w') as fb:
  
  fb.write(respond)

