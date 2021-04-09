def userNumber():
  while True:
    try:
      num = float(input("Enter a number: "))
      return num
    except ValueError:
        print("Please Enter a number...")  
        continue

num1 = userNumber()
print(num1)
