#author: Luka kvesic
#date: 27 nov 2025
#description: convert unicode to binary


fourBits = ''
byte1 = False
byte2 = False
byte3 = False
counting = False
binary = input('give the UTF 8 value: ')


if binary[0] == '0':
    byte1 = True
elif binary[0:3] == '110':
    byte2 = True
elif binary[0:4] == '1110':
    byte3 = True

if byte1:
    for i in range(1, 8):
        if (binary[i] == '0') and (counting == False):
            counting = False
            continue
        elif (binary[i] == '1') and (counting == False):
            fourBits += binary[i]
            counting = True
        elif (counting):
            fourBits += binary[i]
    if len(fourBits) < 16:
        extraZeros = 16 - len(fourBits)
        fourBits = fourBits[::-1]
        for i in range(extraZeros):
            fourBits += '0'
        fourBits = fourBits[::-1]
if byte2:
    for i in range(3, 8):
        if (binary[i] == '0') and (counting == False):
            counting = False
            continue
        elif (binary[i] == '1') and (counting == False):
            fourBits += binary[i]
            counting = True
        elif (counting):
            fourBits += binary[i]
    for i in range(10, 16):
        if (counting):
            fourBits += binary[i]

    if len(fourBits) < 16:
        extraZeros = 16 - len(fourBits)
        fourBits = fourBits[::-1]
        for i in range(extraZeros):
            fourBits += '0'
        fourBits = fourBits[::-1]

if byte3:
    for i in range(4, 8):
        if (binary[i] == '0') and (counting == False):
            counting = False
            continue
        elif (binary[i] == '1') and (counting == False):
            fourBits += binary[i]
            counting = True
        elif (counting):
            fourBits += binary[i]
    for i in range(10, 16):
        if (counting):
            fourBits += binary[i]
    for i in range(18, 24):
        if (counting):
            fourBits += binary[i]
            
    if len(fourBits) < 16:
        extraZeros = 16 - len(fourBits)
        fourBits = fourBits[::-1]
        for i in range(extraZeros):
            fourBits += '0'
        fourBits = fourBits[::-1]
        
utf = 'U+'
extraStop  = 0
extraStart = 0
halfByte = ''
number = 0
for i in range(4):
    start = 0 + extraStart
    stop  = 4 + extraStop
    for i in range(start, stop):
        halfByte += fourBits[i]
        
    for i in range(4):
        number += int(halfByte[i])*((int(halfByte[i])*2)**(3-i))
    number = str(number)
    if number == '10':
        utf += 'A'
    elif number == '11':
        utf += 'B'
    elif number == '12':
        utf += 'C'
    elif number == '13':
        utf += 'D'
    elif number == '14':
        utf += 'E'
    elif number == '15':
        utf += 'F'
    else:
        utf += number
    number = int(number)
    number = 0
    halfByte = ''
    extraStart += 4
    extraStop  += 4
print(utf)
    
            
            

