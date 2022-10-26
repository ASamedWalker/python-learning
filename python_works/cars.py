# The sort() method rearranges the list permanently
cars = ['bmw', 'audi', 'toyota', 'subaru']
# this sort the list in alphabetical order permanently
# we can never revert to the original order
# cars.sort()
# print(cars)

# this reverse the list in alphabetical order permanently
# cars.sort(reverse=True)
# print(cars)

# The sorted() method allows to maintain the 
# original order of the list but rearranges the method in another a different way
# It sorts the list temporarily
# print("Here is the original list:")
# print(cars)

# print("\nHere is the sorted list:")
# print(sorted(cars))

# print("\nHere is the original list again:")
# print(cars)

# print("\nHere is sorted reverse of the list in alphabetical order:")
# print(sorted(cars, reverse=True))

# Reversing the list in chronological order using the 
# reverse() method
print(cars)
# reverse method simply reverses the order of the list
# not in alphabetical order, but permanently.
cars.reverse()
print(cars)

# You can revert the list to it's original 
# state by calling the reverse() method again
cars.reverse()
print(cars)