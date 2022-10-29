# glossary's
glossarys = {
  'dictionary':'a collection of key-value pairs',
  'list':'a sequence of values',
  'variable': 'a data structure for storing data values',
}

# print(f"\nDictionary: {glossarys['dictionary']}")
# print(f"\nList: {glossarys['list']}")
# print(f"\nVariable: {glossarys['variable']}")

glossarys['comments'] = 'it gives a description of what your code does.'
glossarys['strings'] = 'they are series of characters.'
glossarys['tuple'] = 'A tuple is an unimmutable data structure.'

# Glossary 2
for k, v in glossarys.items():
  print(f"\n{k.title()}: {v[0].title()}{v[1:]}.")

