# The double asterisks before the variable('**user_info') cause 
# python to create a empty dictionary called 'user_info'
# Often times, parameter name **kwargs are 
# used to collect non-specific keyword arguments
def build_profile(first, last, **user_info):
  """Build a dictionary containing everything we know about a user."""
  user_info['first_name'] = first
  user_info['last_name'] = last
  return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field="physics")


print(user_profile)

# 8-13 User Profile:
def build_profile(first, last, **kwargs):
  """Build a dictionary containing everything we know about a user."""
  kwargs['first_name'] = first
  kwargs['last_name'] = last
  return kwargs

user_profile = build_profile('samed', 'walker',
                             location='boston',
                             field="computer science")


print(user_profile)