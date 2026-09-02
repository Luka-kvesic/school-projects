#author: Luka kvesic
#date: 6 october 2025
#description: programme that checks if a number is an armstrong number


number = int(input('give a number: '))
number1 = number
digits = 0
count = 0
nextNumber = 0
total = 0


for i in range(1, number1 + 1):
    if (number < 1):
        i = number1
    else:
        number = number / 10
        digits = digits + 1


for i in range(digits, 0, -1):
    count += 1
    numbers = number1 // (10**(i-1))
    nextNumber = numbers
    if i != digits:
        nextNumber = nextNumber - minusNumber
    minusNumber = numbers*(10)
    total += nextNumber**digits


if total == number1:
    print(total,'is an armstrong number')
else:
    print(number1,'is not an armstrong number')


