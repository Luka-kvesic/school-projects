#author: Luka kvesic
#date: 26 september 2025
#description: print the total number of digits in a number

number = int(input('give a number: '))
number1 = number
digits = 0
for i in range(1, number1 + 1):
    if (number < 1):
        i = number1
    else:
        number = number / 10
        digits = digits + 1

print(digits)



