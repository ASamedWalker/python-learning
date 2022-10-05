# Introduction while Loops
# The while Loop in Action

# current_number = 1
# while current_number <= 5:
# 	print(current_number)
# 	current_number += 1

# Letting the User Choose When to Quit
# parrot.py
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
# 	message = input(prompt)
# 	if message != 'quit':
# 		print(message)

# Using a Flag
# active = True
# while active:
# 	message = input(prompt)

# 	if message == 'quit':
# 		active = False
# 	else:
# 		print(message)

# Using break to Exit a Loop
# cities.py
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "

# while True:
# 	city = input(prompt)

# 	if city == 'quit':
# 		break
# 	else:
# 		print(f"I'd love to go to {city.title()}!")

# Using continue in a Loop
# current_number = 0
# while current_number < 10:
# 	current_number += 1
# 	if current_number % 2 == 0:
# 		continue
	
# 	print(current_number)


# Using a while Loop with Lists and Dictionaries
# Moving Items from One List to Another
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
# confirmed_users.py
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
# while unconfirmed_users:
# 	current_user = unconfirmed_users.pop()

# 	print(f"Verifying user: {current_user.title()}")
# 	confirmed_users.append(current_user)
	
# 	# Display all confirmed users.
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
# 	print(confirmed_user.title())

# Removing All instances of Specific Values from a List
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
# 	pets.remove('cat')

# print(pets)

# Filling a Dictionary with User Input
# mountain_poll.py
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
	# Prompt for the person's name and response.
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")

	# Store the response in the dictionary
	responses[name] = response

	# Find out if anyone else is going to take the poll.
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat == "no":
		polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(f"{name} would like to climb {response}. ")