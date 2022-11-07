from random import choice

def get_winning_ticket(possibilities):
  
  winning_tickets = []


  while len(winning_tickets) < 4:
    
    pulled_item = choice(possibilities)
    
    if pulled_item not in winning_tickets:
      
      winning_tickets.append(pulled_item)
      
  return winning_tickets


def check_ticket(played_ticket, winning_ticket):
  
  for element in played_ticket:
    if element not in winning_ticket:
      return False
    
  return True

def make_random_ticket(possibilities):
  
  ticket = []


  while len(ticket) < 4:
    
    pulled_item = choice(possibilities)
    
    if pulled_item not in ticket:
      
      ticket.append(pulled_item)
      
  return ticket


possibilities = [5,6,4,8,3,2,1,7,9,0,'a', 'b', 'c', 'd', 'e']

winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

MAX_TRIES = 1_000_000

while not won:
  
  new_ticket = make_random_ticket(possibilities)
  won = check_ticket(new_ticket, winning_ticket)
  plays += 1
  if plays >= MAX_TRIES:
      break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")