#author: Luka kvesic
#date: 09 september 2025
#description: sum of all odd numbers in a given number
number = 0
number1 = int(input('give a number: '))
total = 0
for i in range(number1 + 1):
    if (i%2 == 1):
        number = number + i  
    else:
        pass
print(number)



