#8-9 Describing a list of sentences
# def show_messages(items):
#   """
#   Simulating printing a series of text 
#   from a list.
#   """
#   for item in items:
#     print(f"{item}", end=" ")


# list_of_text = ['How', 'are', 'doing', 'today', "?"]
# show_messages(list_of_text)


# 8-10. Sending Messages:
def show_messages(display_messages):
  """Displaying received text messages """
  print("\nMessages sent from the customer to the receivers are:")
  for display_message in display_messages:
    print(f" - {display_message} ")
   
    
    
    
def send_messages(messages, received):
  """
  Simulate printing series of text messages which is 
  sent and recieved!!!
  """
  while messages:
    current_text = messages.pop()
    
    print(f"{current_text}")
    
    received.append(current_text)
    
    
list_of_text = ['How are you?', 'Hello there!']
sent_text= []

send_messages(list_of_text, sent_text)
show_messages(sent_text)

print("\nFinal Lists:")
print(list_of_text)
print(sent_text)