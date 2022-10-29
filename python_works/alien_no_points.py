# One subtle problem of using the key to retrieve a value
# in the dictionary is trying to get a key which doesn't exit
# in the dictionary would result in a error
alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])

# To avoid this situation we can use the get() method 
# the get() method has a key as a first argument and default value as the 
# second argument in case the key does not exist in the dictionary

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)