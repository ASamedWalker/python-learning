# Storing a list of motorcylces in a list
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# modifying/changing the list with a new element
# motorcycles[0] = 'ducati'
# print(motorcycles)

# appending/adding a new element to the list
# It gets added to the end of the list
# motorcycles.append('ducati')
# print(motorcycles)

# building a list dynamically using the append method
# defining an empty list is the best way to give your users control
# motorcycles = []

# motorcycles.append('honda')
# motorcycles.append('suzuki')
# motorcycles.append('yamaha')
# motorcycles.append('Tesla')

# print(motorcycles)

# inserting provides another way of adding 
# a new element at any position in the list
# we do this by giving the insert method a index followed by the new element

# motorcycles.insert(0, 'ducati')
# print(motorcycles)

# you can remove an element in a list 
# via its position or via its value

# Using the del statement
# you ca no longer access the value that was removed from the list
# when you use the del statement

# del motorcycles[0]
# print(motorcycles)

# del motorcycles[1]
# print(motorcycles)

# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# Using the pop() method removes the last element in the list
# motorcycles = ['honda', 'yamaha', 'suzuki']

# last_owned = motorcycles.pop()
# print(f"The last motorcycle I owned was a {last_owned.title()}.")

# you can use the pop(index) method to 
# remove any element in a list and use the element
# first_owned = motorcycles.pop(0)
# print(f"The first motocycle I owned was a {first_owned.title()}.")

# We use the remove(value) method to remove an element in a list by value
# remove(value) method also allows you to use the element in a sentence
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)

# motorcycles.remove('ducati')
# print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")