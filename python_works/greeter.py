# Writing clear prompts
# name = input ("Please enter your name: ")


# Writing a prompt that is long
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "


name = input(prompt)
print(f"\nHello, {name}!")