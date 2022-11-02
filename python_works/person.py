# Person dictionary
# person = {
#   'first_name': 'Samed',
#   'last_name': 'Walker',
#   'age': 25,
#   'city': 'New York',
# }

# first_name = person.get('first_name')
# last_name = person.get('last_name')
# age = person.get('age')
# city = person.get('city')

# print(first_name)
# print(last_name)
# print(age)
# print(city)

# 6-7 People
# people = {
#   'sampy': {
#     'first_name': 'Samed',
#     'last_name': 'Walker',
#     'age': 25,
#     'city': 'New York',
#   },
#   'yorkey':{
#     'first_name': 'york',
#     'last_name': 'dwight',
#     'age': 60,
#     'city': 'California',
#   },
# }

# for person, info in people.items():
#   print(f"\nUsername: {person}")
#   full_info = f"{info['first_name'].title()} {info['last_name'].title()}"
#   age_info = f"{info['age']}"
#   city_info = f"{info['city'].title()}"
  
#   print(f"\tName: {full_info}")
#   print(f"\tAge: {age_info}")
#   print(f"\tCity: {city_info}")

# Returning a Dictionary
# def build_person(first_name, last_name):
#   """Return a dictionary of information about a person."""
#   person = {'first': first_name, 'last': last_name}
#   return person

# musician = build_person('jimi', 'hendrix')
# print(musician)

# Expanding on the previous function
def build_person(first_name, last_name, age=None):
  """Return a dictionary of information about a person."""
  person = {'first': first_name, 'last': last_name}
  if age:
    person['age'] = age
  return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)