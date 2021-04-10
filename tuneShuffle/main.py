# imports
from display import print_menu, print_header, clear
from album import Album



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

  the_album = Album(title, genre, artist, release_year, price, album_art, related_artist, record_label)
  print(the_album)

  # push the album into the list
  catalog.append(the_album)

  print(catalog)
  input("Press Enter to continue...")




# instructions
opc = ''
while(opc != 'q' and opc != 'x'):
  clear()
  print_menu()
  opc = input("Please select an option: ")
  if(opc == '1'):
    register_album()
