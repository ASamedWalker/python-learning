# print("Give me two numbers, and I'll add them.")
# print("Enter 'q' to quit")

# while True:
#   num_one = input("Enter your first number: ")
#   if num_one == 'q':
#     break
#   num_two = input("Enter your second number: ")
#   if num_two == 'q':
#     break
#   try:
#     result = int(num_one) + int(num_two)
#   except ValueError:
#     print("Pls enter a number.")
#   else:
#     print(f"The number {num_one} and {num_two} =", result)
    

def addition():
  """Adding two numbers together"""
  print("Give me two numbers, and I'll add them.")
  print("\nEnter 'q' to quit") 
  while True:
    num_one = input("\nEnter your first number: ") 
    if num_one == 'q':
      break
    num_two = input("Enter your second number: ")
    if num_two == 'q':
      break
    try:
      result = int(num_one) + int(num_two)
    except ValueError:
      print("Pls enter a number.")
    else:
      print(f"The number {num_one} and {num_two} =", result)
      
addition()