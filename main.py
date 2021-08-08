def getNumber():
  
  number1 = ''
  
  symbols = input("Enter a digit: ")
  
  number = int(symbols)
  
  while number > 0:
      number1 = number1 +str(number)
    
      symbols = input("Enter a digit: ")
    
      number = int(symbols)
  
  return number1
  

# The goal of this program is to practice Python constructs

def sumTwo(a,b):

   c = a + b

   return c



x = sumTwo(3,5)

print(x)
