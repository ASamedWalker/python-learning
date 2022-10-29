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
people = {
  'sampy': {
    'first_name': 'Samed',
    'last_name': 'Walker',
    'age': 25,
    'city': 'New York',
  },
  'yorkey':{
    'first_name': 'york',
    'last_name': 'dwight',
    'age': 60,
    'city': 'California',
  },
}

for person, info in people.items():
  print(f"\nUsername: {person}")
  full_info = f"{info['first_name'].title()} {info['last_name'].title()}"
  age_info = f"{info['age']}"
  city_info = f"{info['city'].title()}"
  
  print(f"\tName: {full_info}")
  print(f"\tAge: {age_info}")
  print(f"\tCity: {city_info}")