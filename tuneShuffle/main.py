# imports
from display import print_menu, print_header, clear
from album import Album
from song import Song



# globals
#Homework
#declare a catalog variable (list)
catalog = []

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

  the_album = Album(1, title, genre, artist, release_year, price, album_art, related_artist, record_label)
  
  # push the album into the list
  catalog.append(the_album)

def print_albums():
  print_header("Albums")
  for album in catalog:
    print(f"ID: {album.id} | Title: {album.title}")
    

def register_song():
  #let the user choose an album
  print_albums()
  album_id = input("Please choose the album Id: ")

  print_header("Songs")
  title = input("Please provide Title: ")
  featured_artist = input("Please provide Featured Artist: ")
  song_duration = input("Please provide Song Duration: ")
  written_by = input("Please provide Writter: ")

  the_song = Song(1, title, featured_artist, song_duration, written_by)

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