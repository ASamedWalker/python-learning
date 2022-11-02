#8-6 Describing a city name called city_country

def city_country(city, country):
  """Display a printed format of city and country"""
  city_and_country = f"{city.title()}, {country.title()}"
  return city_and_country

display_info1 = city_country("abuja", "nigeria")
display_info2 = city_country("accra", "ghana")
display_info3 = city_country("osaka", "japan")
print(display_info1)
print(display_info2)
print(display_info3)

