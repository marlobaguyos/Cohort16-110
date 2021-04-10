import os

def print_menu():
  clear()
  print("-" * 20)
  print("** Tune Shuffle 1.0 **")
  print("-" * 20)

  print("[1] Register a new Album")
  print("[2] Register a new Song")
  print("[3] Display Album")

  print("[q] Quit")

def print_header(text):
  clear()
  print("-" * 20)
  print(text)
  print("-" * 20)

def clear():
  if(os.name == 'nt'):
    return os.system("cls")
  else:
    return os.system("clear")

  #return os.system('cls' if os.name == 'nt' else 'clear')