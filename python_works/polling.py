favorite_languages = {'jen': 'python',
                      'sarah':'c',
                      'edward': 'ruby',
                      'phil': 'python',
                      }

polling_users = ['edward', 'mike', 'joe', 'phil']

for person in polling_users:
  if person not in favorite_languages:
    print(f"{person.title()}, you are invited to take the poll.")
  else:
    print(f"{person.title()}, thank you for responding.")