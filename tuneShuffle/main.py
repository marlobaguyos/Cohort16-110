# imports
from display import print_menu, print_header, clear
from album import Album
from song import Song
import pickle



# globals
#Homework
#declare a catalog variable (list)
catalog = []
album_count = 0
song_track = 0

# functions

def serialize_data():
    try:
        writer = open('songMngr.data', 'wb')  # wb = write binary
        pickle.dump(catalog, writer)
        writer.close()
        print("** Data serialized!")
    except:
        print("** Error, data not saved")

def deserialize_data():
    global album_count

    try:
        reader = open('songMngr.data', 'rb')  # rb = read binary
        temp_list = pickle.load(reader)
        reader.close()

        for prod in temp_list:
            catalog.append(prod)

        # get the last used id, and increase by 1
        last = catalog[-1]
        album_count = last.id + 1

        how_many = len(catalog)
        print("** Read: " + str(how_many) + " albums")

    except:
        print("** Error, no data file found")

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
      num = float(input("Please provide price: $"))
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
  album_art = input("Please provide Album Art: URL")
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

def count_songs():
  print_header("Your total number of songs")

  total = 0
  for album in catalog:
    songs_catalog = len(album.songs)
    total += songs_catalog

  print(f"There are: {total} songs in the system")

def print_album_songs():
  global song_track
  print_albums()
  album_id = int(input("Please choose the album ID: "))

  #find the album with that ID
  found = False
  for album in catalog:
    if(album.id == album_id):
      found = True
      # the_album = album

      #print album songs
      for song in album.songs:
        print(f"Title: {song.title}")

  if(not found):
    print("**Error: Wrong ID. Try again")
    return

def total_value():
  print_header("Total Price in Catalog")
  for album in catalog:
    add

# instructions
deserialize_data()
input("press enter to continue...")

opc = ''
while(opc != 'q' and opc != 'x'):
  clear()
  print_menu()
  opc = input("Please select an option: ")
  if(opc == '1'):
    register_album()
    serialize_data()
  
  elif(opc == '2'):
    register_song()
    serialize_data()

  elif(opc == '3'):
    print_albums()

  elif(opc == '4'):
    print_album_songs()

  elif(opc == '5'):
    count_songs()

  elif(opc == '6'):
    total_value()

  input("press enter to continue...")