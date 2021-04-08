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

# instructions
opc = ''
print_menu()
opc = input("Please select an option: ")
while(opc != 'q'):
  num1 = input("Provide Num 1: ")
  while(type(num1) != int)
  # while(type(parse.int(num1)) == str):
  #   print("Dude enter a number!")
  #   num1 = input("Provide Num 1: ")
  #   if(type(num1) != str):
  #     break
  num2 = input("Provide Num 2: ")
  while(type(num2) == str):
    print("Dude enter a number!")
    num1 = float(input("Provide Num 1: "))
    if(type(num2) != str):
      break
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