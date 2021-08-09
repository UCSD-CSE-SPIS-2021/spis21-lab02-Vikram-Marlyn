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


def convertWageMtoW(mWage,country):

#Calculate the pay for women in Korea based off of gender pay gap stats
  if country == 'Korea':
    wageGap = 0.315
    ratio = 1 - wageGap
    return mWage * ratio
  #Calculate the pay for women in Italy based off of gender pay gap stats
  elif country == 'Italy':
    wageGap = 0.057
    ratio = 1 - wageGap
    return mWage * ratio
  #Calculate the pay for women everywhere, besides Korea and Italy, based off of gender pay gap stats
  else:
    wageGap = 0.182
    ratio = 1 -0.182
    return mWage * ratio




