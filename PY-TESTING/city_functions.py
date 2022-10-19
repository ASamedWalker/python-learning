# 11-1 City, Country:
def city_and_country(city, country, population=''):
  """Displaying information of a city and country"""
  information = f'{city.title()}, {country.title()}'
  if population:
    information += f' - population {population}'
  return information

# 11-2 Population: