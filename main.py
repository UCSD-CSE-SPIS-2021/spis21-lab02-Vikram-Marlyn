def getNumber():
  
  number1 = ''
  
  symbols = input("Enter a digit: ")
  
  number = int(symbols)
  
  while number > 0:
      number1 = number1 + str(number)
    
      symbols = input("Enter a digit: ")
    
      number = int(symbols)
  
  return number1
  
def sumDigits(x):

   # You will need to complete this function
  valueList = list(map(int, str(x)))
  sum2 = sum(valueList)
  print(sum2)




# The goal of this program is to practice Python constructs

def sumTwo(a,b):

   c = a + b

   return c



x = sumTwo(3,5)

print(x)


value = str(1232747437)

valueList = list(map(int,str(value)))


print(valueList)


