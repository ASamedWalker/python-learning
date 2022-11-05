# Describing a an album function
def make_album(artist_name, album_title, number_of_songs=None):
  """Display a dictionary of the artist_name and album_title"""
  return {
    'artist': artist_name,
    'album': album_title,
    'total_songs': number_of_songs
  }
  
records1 = make_album('Dejon', 'The Blue Skies')
records2 = make_album('Milk', 'Run away')
records3 = make_album('Nas', 'Thug')
records4 = make_album('Lupe', 'long gone', 5)
print(records1)
print(records2)
print(records3)
print(records4)


