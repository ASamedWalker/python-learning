multiples_of_ten = "Provide a number that is a multiple of ten: "

number = int(input(multiples_of_ten))

if number % 10 == 0:
  print(f"{number} is a multiple of 10.")
else:
  print(f"{number} is not a multiple of 10.")