#author: Luka kvesic
#date: 9 october 2025
#description: q20 b, sum of N amount of numbers sqaured
term = -1
total = 0
amount = int(input('enter the amount of terms: '))
for i in range(1, amount + 1):
    term += 2
    power = term ** 2
    total = total + power
    
print('sum is',total)