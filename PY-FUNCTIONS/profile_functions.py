import profile_info as pi

username = pi.build_profile('Walker', 'Sam', location='NYC', field='CS')
print(username)

from profile_info import build_profile as bp

username_one = bp('doomer', 'joe', location='london', field='literature')
print(username_one)

from profile_info import *

username_two = build_profile('bob', 'spam', location='sydney', field='AI')

print(username_two)