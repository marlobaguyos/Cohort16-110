#promt user the menu and provide options
def print_menu():
  print("--------------")
  print("*** PyCalc ***")
  print("--------------")
  print('[1] Sum')
  print('[2] Subtract')
  print('[3] Multiply')
  print('[4] Divide')
  print("[q] Quit")

#Doing Mat Function
def sum(num1,num2):
  return float(num1) + float(num2)
def sub(num1,num2):
  return float(num1) - float(num2)
def mul(num1,num2):
  return float(num1) * float(num2)
def div(num1,num2):
  return float(num1) / float(num2)

#Alow user to enter number to do math with
def userNumber():
  while True:
    try:
      num = float(input("Enter a number: "))
      return num
    except ValueError:
        print("Please Enter a number...")  
        continue

#main

def BrokenCal():
  pangit = True
  while pangit == True:
    print_menu()
    userChoice = input("Pick an option: ")
    if (userChoice.lower() == 'q'):
      print("------------------")
      print("***** PyCalc *****")
      print("------------------")
      print("------------------")
      print("**** GameOver ****")
      print("------------------")
      pangit = False
    
    elif(userChoice == '1'):
      print("--------Adding---------")
      num1 = userNumber()
      print(f'Your first Number is {num1}')
      num2 = userNumber()
      print(f'Your second Number is {num2}')
      print(f"{num1} + {num2} = {sum(num1,num2)}")

    elif(userChoice == '2'):
      print("--------Subtracting---------")
      num1 = userNumber()
      print(f'Your first Number is {num1}')
      num2 = userNumber()
      print(f'Your second Number is {num2}')
      print(f"{num1} + {num2} = {sub(num1,num2)}")
    
    elif(userChoice == '3'):
      print("--------Multiply---------")
      num1 = userNumber()
      print(f'Your first Number is {num1}')
      num2 = userNumber()
      print(f'Your second Number is {num2}')
      print(f"{num1} + {num2} = {mul(num1,num2)}")

    elif(userChoice == '4'):
      print("--------Divide---------")
      num1 = userNumber()
      print(f'Your first Number is {num1}')
      num2 = userNumber()
      while(num2 == 0):
        print("You can't divide with 0. Enter a different number: 3")
        num2 = userNumber()

      print(f'Your second Number is {num2}')
      print(f"{num1} + {num2} = {div(num1,num2)}")
      
BrokenCal()
