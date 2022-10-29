favorite_languages = {'jen': 'python',
                      'sarah':'c',
                      'edward': 'ruby',
                      'phil': 'python',
                      }

# Looping for both keys and values
# for name, language in favorite_languages.items():
#   print(f"{name.title()}'s favorite language is {language.title()}.")
# # language = favorite_languages['sarah'].title()
# # print(f"Sarah's favorite language is {language}.")

# # Looping through all keys
# # OR
# for name in favorite_languages.keys():
#   print(name.title())
  
# # Default behavior of looping through keys
# for name in favorite_languages:
#   print(name.title())

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#   print(name.title())
  
#   if name in friends:
#     language = favorite_languages[name].title()
#     print(f"\t Hi {name.title()}, I see you love {language}!")
    
#   if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# Using the sorted() method to sort the dictionary's key in a particular order
# for name in sorted(favorite_languages.keys()):
#   print(f"{name.title()}, thank you for taking the poll.")

# for primarily interested in the values of the dictionary you use the value() method
# To avoid repetitive values in dictionarys value.Use set() method, they make each item unique
# print("The ff languages have been mentioned:")
# for language in set(favorite_languages.values()):
#   print(language.title())
  

favorite_languages = {'jen': ['python', 'ruby'],
                      'sarah':['c'],
                      'edward': ['ruby', 'go'],
                      'phil': ['python', 'haskell'],
                      }

for name, languages in favorite_languages.items():
  print(f"\n{name.title()}'s favorite languages are:")
  for language in languages:
    print(f"\t{language.title()}")