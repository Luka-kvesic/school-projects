#author: Luka kvesic
#date: 7 october 2025
#description: programme that checks if final 


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
    I = i
    if I == 0:
        if nextNumber == 4:
            print('it ends with 4')
        elif nextNumber == 8:
            print('it ends with 8')
        else:
            print('it doesnt end with either')

    


