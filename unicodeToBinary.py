#author: Luka kvesic
#date: 25 nov 2025
#description: convert unicode to binary
i = -1
value = ''
utf = input('what is the unicode point: ')
fiveDigits = False
sixDigits = False
while True:
    i += 1
    if sixDigits == False:
        if i > 3:
            break
    elif sixDigits == True:
        if i > 5:
            break
    digit = utf[i]
    print(i)
    if digit.isalpha():
        if (digit == 'u') or (digit == 'U'):
            sixDigits = True
            continue
        elif digit == '+':
            continue
        elif (digit == 'a') or (digit == 'A'):
            value += '10 '
        elif (digit == 'b') or (digit == 'B'):
            value += '11 '
        elif (digit == 'c') or (digit == 'C'):
            value += '12 '
        elif (digit == 'd') or (digit == 'D'):
            value += '13 '
        elif (digit == 'e') or (digit == 'E'):
            value += '14 '
        elif (digit == 'f') or (digit == 'F'):
            value += '15 '
    elif digit.isdigit():
        value += digit + ' '
print(value)

i2 = 0
spaceCount = 0
while True: 
    i2 += 1
    if value[i2] == ' ':
        spaceCount += 1
print(spaceCount)
    
    
    
    
    
    
    
    
    
    
    
    