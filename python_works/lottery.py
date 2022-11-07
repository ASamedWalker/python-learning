# 9-14 Lottery tickets
from random import randint, choice

possibilities = [5,6,4,8,3,2,1,7,9,0,'a', 'b', 'c', 'd', 'e']

winning_tickets = []


while len(winning_tickets) < 4:
  
  pulled_item = choice(possibilities)
  
  if pulled_item not in winning_tickets:
    
    print(f"We pulled a {pulled_item}!")
    
    winning_tickets.append(pulled_item)

message = f"The final winning tickets are: {winning_tickets}."

print(message)