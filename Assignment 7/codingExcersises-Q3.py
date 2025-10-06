#author: Luka kvesic
#date: 6 october 2025
#description: programme thats converts binary to decimal

number = int(input('give a binary number: '))
number1 = number
digits = 0
total = 0
for i in range(1, number1 + 1):
    if (number < 1):
        i = number1
    else:
        number = number / 10
        digits = digits + 1

        
for i in range(digits, 0, -1):
    numbers = number1 // (10**(i-1))
    nextNumber = numbers
    if i != digits:
        nextNumber = nextNumber - minusNumber
    minusNumber = numbers*(10)
    total += (nextNumber*2)**i
print('that in decimal form is',int(total/2))
    

