#author: Luka kvesic
#date: 3 november 2025
#description: write a programme to convert decimal to roman numeral

romanNumeralDigit = ''
fullRomanNumeral  = ''
number = input('enter a number: ')

length = len(number)

for i in range(0, length,1):
    if i == 3:
        firstNumeral  = 'I'
        middleNumeral = 'V'
        lastNumeral   = 'X'
    if i == 2:
        firstNumeral  = 'X'
        middleNumeral = 'L'
        lastNumeral   = 'C'
    if i == 1:
        firstNumeral  = 'C'
        middleNumeral = 'D'
        lastNumeral   = 'M'
    if i == 0:
        firstNumeral  = 'M'
        middleNumeral = ''
        lastNumeral   = ''
    digit = number[i]
    digit = int(digit)
    romanNumeralDigit = ''
    if digit < 4:
        for amount in range(1, digit+ 1):
            romanNumeralDigit += firstNumeral
            
    elif digit == 4:
        romanNumeralDigit = firstNumeral + middleNumeral
        
    elif (digit > 4) and (digit < 9):
        romanNumeralDigit = middleNumeral
        for amount in range(digit-5):
            romanNumeralDigit += firstNumeral
    
    elif (digit > 4) and (digit < 9):
        romanNumeralDigit = middleNumeral
        for amount in range(digit-5):
            romanNumeralDigit += firstNumeral
    
    elif digit == 9:
        romanNumeralDigit = firstNumeral + lastNumeral
        
    fullRomanNumeral += romanNumeralDigit
    
print('in roman numerals your number is',fullRomanNumeral)
        
    
