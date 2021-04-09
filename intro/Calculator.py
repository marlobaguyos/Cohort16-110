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
  return float(num1) + float(num2)
def sub(num1,num2):
  return float(num1) - float(num2)
def mul(num1,num2):
  return float(num1) * float(num2)
def div(num1,num2):
  return float(num1) / float(num2)

#Alow user to enter number to do math with
def userNumber():
  hindiNum = False
  aNum = input("Enter a number: ")
  while (hindiNum == False):
    if(aNum.lower() == 'q'):
      hindiNum = True

    while(aNum.isdigit() == False):
      aNum = input("Try Again!  Please Enter first number: ")
      if(aNum.isdigit() == True):
        float(aNum)
        return aNum
      else:
        return aNum



#main

def pogi():
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
      # hindiNum = False
      print("--------Adding---------")
      # num1 = input("Enter first number: ")
      # while (hindiNum == False):
      #   if(num1.lower() == 'q'):
      #     hindiNum = True

      #   while(num1.isdigit() == False):
      #     num1 = input("Try Again!  Please Enter first number: ")
      #   else:
      #     hindiNum = True
      # print(num1)
      num1 = userNumber()
      print(f'Your first Number is {num1}')
      num2 = userNumber()
      print(f'Your second Number is {num2}')
      # num2 = input("Enter second number: ")
      # while (hindiNum == False):
      #   if(num2.lower() == 'q'):
      #     hindiNum = True

      #   while(num2.isdigit() == False):
      #     num2 = input("Try Again!  Please Enter first number: ")
      #   else:
      #     hindiNum = True
      # print(num2)
      
      print(f"{num1} + {num2} = {sum(num1,num2)}")

      # num2 = input("Enter first number: ")
      # while (hindiNum == False):
      #   cat = True
      #   while(cat == True):
      #     if(num2.isdigit() == False):
      #       num2 = input("Try Again!  Please Enter first number: ")
      #     else:
      #       cat = False
      # print(num2)

        

        # if (num1.isdigit() == False):
        #   print("Try again! Enter a Number this time!")
        # else:
        #   print(num1)
        #   hindiNum = True

        # num2 = input("Enter second number: ")
        # if(num2.lower() == 'q'):
        #   break

        # if (num2.isdigit() == False):
        #   print("Try again! Enter a Number this time!")
        # else:
        #   print(num2)
        #   hindiNum = True
  print("------------------")
  print("***** PyCalc *****")
  print("------------------")
  print("------------------")
  print("**** GameOver ****")
  print("------------------")
      

  # def firstNumber():
  # num1 = input("Enter First Number: ")
  # while(num1.isdigit() != True):
  #   num1 = input("Try again! Please enter first number: ")
  #   if(num1 == 'q'):
  #     return num1 == False
  # else:
  #   num1 = float(num1)
  # return num1



    
  # while(userChoice != 'q'):
  #   if(userChoice == '1'):
  #     print("Adding")
  #     num1 = float(input("Enter first number"))
  #     num2 = float(input("Enter second number"))
  #     print(num1 + num2)
  





pogi()
