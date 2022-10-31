# Dream Vacation Polling
vacation_responses = {}

vacation_polling = True

while vacation_polling:
  
  users = input("What is your name: ")
  
  responses = input("What is your dream vacation destionation? ")
  
  vacation_responses[users] = responses
  
  prompt = input("Would would like to name another dream destination: (yes/no)!")
  
  if prompt == "no":
    
    vacation_polling = False

print("\n")
print(" Dream Vacation Poll Results ".center(30, '='))
for name, response in vacation_responses.items():
  print(f"{name.title()} dream vacation destination is {response.title()}.")