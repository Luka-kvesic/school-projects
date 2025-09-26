#author: Luka kvesic
#date: 02 september 2025
#description: finding simple and complound interest

principle = int(input('how much is the loan: '))
interest = float(input('how much is the interest, write as a decimal: '))
years = int(input('how many years: '))

simpleInterest = principle + (interest * principle) * years
compoundInterest = principle * ((interest + 1) ** years)

print('your simple interest is: ',simpleInterest)
print('your compound interest ',compoundInterest)
