#author: Luka kvesic
#date: 6 october 2025
#description: write a programme to enter numbers until the user enters 0. then you should print the count of the positive and negative numbers entered.you can assume all input is numeric
positiveCount = 0
negativeCount = 0
while True:
    numbers = int(input('give a number, it can be negative or positive: '))
    if numbers > 0:
        positiveCount += 1
    elif numbers < 0:
        negativeCount += 1
    elif numbers == 0:
        break
print('There is',positiveCount,'positive numbers entered')
print('There is',negativeCount,'negative numbers entered')
    




