# 8-8 Starting my program from 8-7
def make_album(artist_name, album_title, tracks=None):
  """Display a dictionary of the artist_name and album_title"""
  album_dict = {
    'artist': artist_name.title(),
    'album': album_title.title(),
  }
  if tracks:
    album_dict['tracks'] = tracks
    
  return album_dict
  

# Using while loop to ask users about their favorite musicians records
print("Recognize your favorite's artist and album's name")

while True:
  artist_name= input("\nEnter your artist name(or enter 'quit' to exit the program): ")
  if artist_name == 'quit':
    break
  
  album_title= input("Enter your album title(or enter 'quit' to exit the program): ")
  if album_title == 'quit':
    break
  
  prompt = "Can you count the number of songs on the album if any? (else enter 'quit' to exit the program): "
  
  count_songs = input(prompt)
  
  if count_songs == 'quit':
    break
  
  collection_of_info = make_album(artist_name, album_title, count_songs)
  
  print(collection_of_info)

print("Thank you for responding")