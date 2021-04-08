#functions
def print_menu():
  print("--------------")
  print("*** PyCalc ***")
  print("--------------")
  print('[1] Sum')
  print('[2] Subtract')
  print('[3] Multiply')
  print('[4] Divide')
  print("[q] Quit")

# def sum(num1, num2):
#   return num1 + num2

# def sub(num1, num2):
#   return num1 - num2

# def mul(num1, num2):
#   return num1 * num2

# def sum(num1, num2):
#   return num1 / num2


# instructions
opc = ''
print_menu()
opc = input("Please select an option: ")
while(opc != 'q'):
  num1 = float(input("Provide Num 1: "))
  num2 = float(input("Provide Num 2: "))
  if(opc == '1'):
    res = num1 + num2
    print(f"Result: {res}")
  elif(opc == '2'):
    res = num1 - num2
    print(f"Result: {res}")
  elif(opc == '3'):
    res = num1 * num2
    print(f"Result: {res}")
  elif(opc == '4'):
    if(num2 == 0):
      print("Danger")
      break
    res = num1 / num2
    print(f"Result: {res}")
  elif(opc == 'q'):
    break
  
print("Good bye!")
    
"""
HW:
  - Multiplication
  - division:
  Note: don't allow the user to divide by 0 9/0

"""