# Question 16(a)
# Name and School: luka kvesic


principalInvestment = float(input("Enter the principal investment amount: "))

interest = float(input("enter the annual interest rate (e.g. 0.05 for 5% interest): "))
for i in range(1,10+ 1):
    value = (principalInvestment * interest)*i + principalInvestment
    print("Year ",i,"- Investment value:",value)
    
    