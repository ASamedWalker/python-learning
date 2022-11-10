def city_country(city_name, country, population=''):
  """A function to retrun the city_name and country"""
  if population:
    formatted_name = f"{city_name}, {country} - population={population}"
  else:
    formatted_name = f"{city_name}, {country}"
    
  return formatted_name.title()