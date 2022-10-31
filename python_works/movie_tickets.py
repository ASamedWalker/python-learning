
prompt_age = "What is your age to purchase the movie tickets: "
prompt_age += "\n(Enter 'quit' to leave the ticket line)"

while True:
  movie_age = input(prompt_age)
  
  if movie_age == 'quit':
    break
  
  movie_age = int(movie_age)
  
  if movie_age < 3:
    price = 'free'
  elif movie_age < 13:
    price = '$10'
  else:
    price = '$15'
  
  print(f"The ticket is {price}")