"""A Class representing a simple dice game."""
from random import randint
x = randint(1, 6)

class Dice:
  """A simple class to represent a dice game."""
  
  def __init__(self, sides=6) -> None:
    """Initialize the die."""
    self.sides = sides
    
  def roll_die(self):
   return randint(1, self.sides)
    
d6 = Dice()

results = []
for roll_num in range(10):
  result = d6.roll_die()
  results.append(result)
print("\n10 rolls of a 6-sided die:")
print(results)

d10 = Dice(sides=10)

results = []
for roll_num in range(10):
  result = d10.roll_die()
  results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

d10 = Dice(sides=20)

results = []
for roll_num in range(10):
  result = d10.roll_die()
  results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)