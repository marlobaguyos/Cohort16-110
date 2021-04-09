pogi = True
num = float(input("Enter a Number: "))
while(pogi == True):
  try:
    num = float(input("Enter a Number"))
    print("num: ", num)
  except ValueError:
    print("Please input float only...")
    continue
