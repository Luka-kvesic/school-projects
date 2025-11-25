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
value += ';'
print(value)

i2 = -1
spaceCount = 0
spaceChecker = True
while spaceChecker: 
    i2 += 1
    if value[i2] == ' ':
        spaceCount += 1
    if value[i2] == ';':
        spaceChecker = False
print(spaceCount)
    
i3 = -1
fourBits = ''
digits = ''

while True:
    i3 += 1
    print('i3', i3)
    if value[i3] == ';':
        break
    if value[i3] != ' ':
        digits += value[i3]
    elif value[i3] == ' ':
        if digits == '0':
            fourBits += '0000'
        elif digits == '1':
            fourBits += '0001'
        elif digits == '2':
            fourBits += '0010'
        elif digits == '3':
            fourBits += '0011'
        elif digits == '4':
            fourBits += '0100'
        elif digits == '5':
            fourBits += '0101'
        elif digits == '6':
            fourBits += '0110'
        elif digits == '7':
            fourBits += '0111'
        elif digits == '8':
            fourBits += '1000'
        elif digits == '9':
            fourBits += '1001'
        elif digits == '10':
            fourBits += '1010'
        elif digits == '11':
            fourBits += '1011'
        elif digits == '12':
            fourBits += '1100'
        elif digits == '13':
            fourBits += '1101'
        elif digits == '14':
            fourBits += '1110'
        elif digits == '15':
            fourBits += '1111'
        print(digits)
        digits = ''
        print(fourBits)
        print(digits)
print(fourBits)

countZeros = 0

for i in range(16):
    if fourBits[i] == '0':
        countZeros += 1
    elif fourBits[i] != '0':
        break
print(countZeros)
necessaryBits = 16 - countZeros
print('necessaryBits', necessaryBits)
answer = ''
if necessaryBits < 8:
    print('working')
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
