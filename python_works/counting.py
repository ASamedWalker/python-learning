#4-3 Counting twenty using list comprehension:
# counting_twenty = [print(twenty) for twenty in range(1, 21)]

# 4-4 One Million:
# counting_one_million = [print(million) for million in range(1, 1_000_001)]
import numbers


million = list(range(1, 1_000_001))
# print(million)

# 4-5 Summing a Million
# print(min(million))
# print(max(million))
# print(sum(million))

# 4-6 Odd Numbers:
# for odd_numbers in range(1, 21, 2):
#   print(odd_numbers)

# # 4-7 Threes:
# multiples_of_three = [value * 3 for value in range(3, 31)]
# print(multiples_of_three)

# # 4-8 Cubes:
# cubes = []
# for value in range(1, 11):
#   cubes.append(value**3)
# print(cubes)

# # OR 

# cubes = list(range(1, 11))
# new_cubes = []
# for cube in cubes:
#   new_cubes.append(cube**3)
# print(new_cubes)

# # 4-9 Cube Comprehension
# cubes = [value**3 for value in range(1, 11)]
# print(cubes)


# Using while loop to count numbers
# current_number = 1
# while current_number <= 5:
#   print(current_number)
#   current_number += 1

# Using continue in a Loop
# current_number = 0
# while current_number < 10:
#   current_number += 1
  
#   if current_number % 2 == 0:
#     continue
  
#   print(current_number)
  
# Avoiding Infinite Loops
x = 1
while x <= 5:
  print(x)
  # x += 1