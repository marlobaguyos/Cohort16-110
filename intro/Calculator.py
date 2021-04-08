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


#Add Function
def sum(num1,num2):
  return num1 + num2

#take user input and perform calculation
def firstNumber():
  while True:
    num1 = input("Enter First Number: ")
    if num1.lower() == 'q':
      print("Game Over")
      return

    if(num1.isdigit() != True):
      print("Please enter a number")
    else:
      num1 = float(num1)
    return num1

def secondNumber():
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
#userChoice = input("Select an option")




#main
print_menu()
onOff = True
while(onOff):
  userChoice = input("Select an option: ")
  if userChoice.lower() == 'q':
    print("Game Over")
    break
  elif userChoice == '1':
    print("You want to Add things")
    print(sum(firstNumber(),secondNumber()))
    onOff = False



  
