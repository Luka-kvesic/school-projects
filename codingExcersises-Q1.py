#author: Luka kvesic
#date: 2 october 2025
#description: programme that checks if a number is an armstrong number


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
for i in range(digits, 0, -1):
    numbers = number // ((10**i)/10000)
    minusNumber = numbers
    print(numbers)
    
    
    
    