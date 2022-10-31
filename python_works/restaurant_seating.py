restaurant_seat = "How many group of people are you bringing to the dinner?"

number_of_seat = int(input(restaurant_seat))

if number_of_seat > 8:
  print("You have to wait for an available table")
else:
  print("There is an available table waiting.")