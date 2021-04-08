def firstNumber():
  num1 = input("Enter First Number: ")
  while(num1.isdigit() != True):
    num1 = input("Try again! Please enter first number: ")
    if(num1 == 'q'):
      break
  else:
    num1 = float(num1)
  return num1
  

num1 = firstNumber()
print(num1)

def secondNumber():
  num2 = input("Enter second Number: ")
  while(num2.isdigit() != True):
    num2 = input("Try again! Please enter first number: ")
    if(num2 == 'q'):
      break
  else:
    num2 = float(num1)
  return num2