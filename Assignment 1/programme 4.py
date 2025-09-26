#author: Luka kvesic
#date: 01 september 2025
#description: add two numbers then multiply last one

number1 = input('enter the first number: ')
number2 = input('enter the second number: ')
number3 = input('and the last number: ')
number1 = float(number1)
number2 = float(number2)
number3 = float(number3)

addition_total = number1 + number2
multiplication_total = number3 * addition_total
print('the sum of the first two numbers multiplied by the last is',multiplication_total)
