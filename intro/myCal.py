
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

num1 = userNumber()
print(num1)
num2 = userNumber()

print(float(num1) + float(num2))