#Tell user what the app is.

def print_menu():
  print("-------------------")
  print("*** PyCalculaor ***")
  print("-------------------")
  print('[1] Sum')
  print('[2] Subtract')
  print('[3] Multiply')
  print('[4] Divide')
  print("[q] Quit")

#Allow the user to cont or to quit at any time.

#Promt the user to select what they want to don
  #add
def sum(num1,num2):
  return num1 + num2
  
  #minus
  #Multiply
  #divide
  #quit
#promt the user to enter something
def firstNumber():
  num1 = input("Enter First Number: ")
  while(num1.isdigit() != True):
    num1 = input("Try again! Please enter first number: ")
    if(num1 == 'q'):
      break
  else:
    num1 = float(num1)
  return num1

def secondNumber():
  num2 = input("Enter second Number: ")
  while(num2.isdigit() != True):
    num2 = input("Try again! Please enter first number: ")
    if(num2 == 'q'):
      break
  else:
    num2 = float(num1)
  return num2

def firstNumber():
  while True:
    num1 = input("Enter First Number: ")
    if num1.lower() == 'q':
      print("Game Over")
      break

    if(num1.isdigit() != True):
      print("Please enter a number")
    else:
      num1 = float(num1)
    return num1

def SecondNumber():
  while True:
    num2 = input("Enter second Number: ")
    if num2.lower() == 'q':
      print("Game Over")
      break

    if(num2.isdigit() != True):
      print("Please enter a number")
    else:
      num2 = float(num2)
    return num2

num = input("Enter a number: ")
while(num.isdigit() != True):
  