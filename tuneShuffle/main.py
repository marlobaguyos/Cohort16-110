# imports
from display import print_menu, print_header, clear
from album import Album
from song import Song



# globals
#Homework
#declare a catalog variable (list)
catalog = []
album_count = 0

# functions
def release_year():
  while True:
    try:
      num = int(input("Please provide release_year: "))
      return num
    except ValueError:
        print("Please enter release_year...")  
        continue

def price():
  while True:
    try:
      num = float(input("Please provide price: "))
      return num
    except ValueError:
        print("Please Enter price...")  
        continue

def register_album():
  global album_count
  print_header("Register a new Album")

  # title, genre, artist, release_year, price, album_art, related_artist, record_label = 8 total
  title = input("Please provide Title: ")
  genre = input("Please provide Genre: ")
  artist = input("Please provide Artist Name: ")
  release_year()
  price()
  album_art = input("Please provide Related Artist: ")
  related_artist = input("Please provide Related Artist: ")
  record_label = input("Please provide Record Label: ")

  album_count += 1

  the_album = Album(album_count, title, genre, artist, release_year, price, album_art, related_artist, record_label)
  
  # push the album into the list
  catalog.append(the_album)

def print_albums():
  print_header("Albums")
  for album in catalog:
    print(f"ID: {album.id} | Title: {album.title} | {album.artist}")
    

def register_song():
  #let the user choose an album
  print_albums()
  album_id = int(input("Please choose the album Id: "))

  #find the album with that ID
  found = False
  for album in catalog:
    if(album.id == album_id):
      found = True
      the_album = album
  
  if(not found):
    print("**Error: Wrong ID. Try again")
    return

  print_header("Songs")
  title = input("Please provide Title: ")
  featured_artist = input("Please provide Featured Artist: ")
  song_duration = input("Please provide Song Duration: ")
  written_by = input("Please provide Writter: ")

  the_song = Song(1, title, featured_artist, song_duration, written_by)

  the_album.add_song(the_song)

  print("** Song Registered")
  print(f"{the_song.title} | {the_song.featured_artist}")

# instructions
opc = ''
while(opc != 'q' and opc != 'x'):
  clear()
  print_menu()
  opc = input("Please select an option: ")
  if(opc == '1'):
    register_album()
  
  elif(opc == '2'):
    register_song()

  elif(opc == '3'):
    print_albums()

  input("press enter to continue...")