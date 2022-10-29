# # 6-2 Favorite Numbers
# favorite_numbers = {
#   'sam': 15,
#   'joe': 5,
#   'julia': 10,
#   'bob': 12,
#   'spam': 16,
# }

# views = favorite_numbers.get('sam')
# print(f"Sam's favorite number is {views}.")

# views = favorite_numbers.get('joe')
# print(f"Joe's favorite number is {views}.")

# views = favorite_numbers.get('julia')
# print(f"Julia's favorite number is {views}.")

# views = favorite_numbers.get('bob')
# print(f"Bob's favorite number is {views}.")

# views = favorite_numbers.get('spam')
# print(f"Spam's favorite number is {views}.")


# 6-10 Favorite Numbers:
favorite_numbers = {
  'sam': [15, 8, 10],
  'joe': [5, 3, 1],
  'julia': [10, 2, 4],
  'bob': [12, 13, 9],
  'spam': [16, 17, 20],
}

for name, numbers in favorite_numbers.items():
  print(f"\n{name.title()}'s favorite numbers are: ")
  for number in numbers:
    print(f" - {number}")