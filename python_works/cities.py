# Making a dictionary call Cities
cities = {
  'nairobi': {
    'country': 'kenya',
    'population': 48_397_527 ,
    'currency': 'kenyan Shilling',
    'language': 'Swahili, English',
  },
  'accra': {
    'country': 'ghana',
    'population': 31_486_000,
    'currency': 'cedis',
    'language': 'English',
  },
  'dakar': {
    'country': 'senegal',
    'population': 17_739_000,
    'currency': 'cfa',
    'language': 'french',
  },
}

for city, demography in cities.items():
  print(f"\nThe demograph of {city.title()} are:")
  infor_country = f"{demography['country'].title()}"
  infor_language = f"{demography['language'].title()}"
  infor_currency = f"{demography['currency'].title()}"
  infor_population = f"{demography['population']}"
  
  print(f" - Country: {infor_country}")
  print(f" - Language: {infor_language}")
  print(f" - Currency: {infor_currency}")
  print(f" - Population: {infor_population}")