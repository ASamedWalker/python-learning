# 6-2 Favorite Numbers
favorite_numbers = {
  'sam': 15,
  'joe': 5,
  'julia': 10,
  'bob': 12,
  'spam': 16,
}

views = favorite_numbers.get('sam')
print(f"Sam's favorite number is {views}.")

views = favorite_numbers.get('joe')
print(f"Joe's favorite number is {views}.")

views = favorite_numbers.get('julia')
print(f"Julia's favorite number is {views}.")

views = favorite_numbers.get('bob')
print(f"Bob's favorite number is {views}.")

views = favorite_numbers.get('spam')
print(f"Spam's favorite number is {views}.")