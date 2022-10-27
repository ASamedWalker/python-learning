# This is a tuple of a basic buffet food served in a restaurant
basic_foods = ('buffet salads', 'roast duck', 'glazed ham')

print("The buffet served at the restaurant near me are:")
for buffet in basic_foods:
  print(f" - {buffet.title()}")

print("\n")

basic_foods = ('palava source', 'bread and honey', 'glazed ham')
print("The revised new menu:")
for new_buffet in basic_foods:
  print(f" - {new_buffet.title()}.")
