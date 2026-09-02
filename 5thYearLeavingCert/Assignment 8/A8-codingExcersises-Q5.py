#author: Luka kvesic
#date: 9 october 2025
#description: take integer, print its digit and most significant digit within the number and make those two things a number

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
    if i == digits:
        savedNumber = nextNumber
        savedNumber = str(savedNumber)
        savedDigit = str(digits)
print(savedDigit + savedNumber)