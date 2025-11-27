#author: Luka kvesic
#date: 25 nov 2025
#description: convert unicode to binary

i = -1
value = ''
utf = input('what is the unicode point: ')
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
value += ';'

i2 = -1
spaceCount = 0
spaceChecker = True
while spaceChecker: 
    i2 += 1
    if value[i2] == ' ':
        spaceCount += 1
    if value[i2] == ';':
        spaceChecker = False
combined = ''
i3 = -1
fourBits = ''
digits = ''
power = 0
bits = ''
while True:
    i3 += 1
    if value[i3] == ';':
        break
    if value[i3] != ' ':
        digits += value[i3]
    elif value[i3] == ' ':
        numbers = int(digits)
        while numbers != 0:
            if (numbers%2 == 1):
                remainder = numbers%2
                numbers = (numbers // 2) 
            elif (numbers%2 == 0):
                remainder = numbers%2
                numbers = numbers / 2
            remainder = int(remainder) 
            combined += str(remainder)
            bits = combined[::-1]
        if len(bits) < 4:
            extraZeros = 4 - len(bits)
            bits = bits[::-1]
            for i in range(extraZeros):
                bits += '0'
            bits = bits[::-1]
        fourBits += bits
            
        combined = ''
        bits = ''
        digits = ''

countZeros = 0

for i in range(16):
    if fourBits[i] == '0':
        countZeros += 1
    elif fourBits[i] != '0':
        break
necessaryBits = 16 - countZeros
answer = ''
if necessaryBits < 8:
    for i in range(-1, -necessaryBits-1, -1):
        answer += fourBits[i]
    answer += '0'*(8-necessaryBits)
    answer = answer[::-1]
        
elif necessaryBits < 12:
    for i in range(-1, -7, -1):
        answer += fourBits[i]
    answer += '01 '
    for i in range(-7, -12, -1):
        answer += fourBits[i]
    answer += '011'
    answer = answer[::-1]
elif necessaryBits < 19:
    for i in range(-1, -7, -1):
        answer += fourBits[i]
    answer += '01 '
    for i in range(-7, -13, -1):
        answer += fourBits[i]
    answer += '01 '
    for i in range(-13, -16, -1):
        answer += fourBits[i]
    answer += '00111'
    answer = answer[::-1]

print(answer)

