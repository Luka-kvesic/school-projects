#name: luka kvesic
#date: 09 september 2025
#description: ask question 5 times using for loop and add total

total = 0

for Q1 in range(5):
    number = int(input('enter a number: '))
    Q = input('do you want to add that number: ')
    if (Q == 'yes') or (Q == 'Yes') or (Q == 'YES'):
        total = total + number
    else:
        pass
print(total)
    
