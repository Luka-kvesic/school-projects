#author: Luka kvesic
#date: 17 november 2025
#description: binary adder

firstBinary = input('give the first binary number: ')

secondBinary = input('give the second binary number: ')

length1 = len(firstBinary)
length2 = len(secondBinary)
newDigit = 0
digits = ''
futureDigit = 0
count = 0
answer = ''
if length1 >= length2:
    length = length1 + 1
    extraZeros = length - length2
    if extraZeros == 0:
        extraZeros = 1
    secondNumber = secondBinary[::-1] + ('0'*extraZeros)
    secondNumber = secondNumber[::-1]
    firstNumber = firstBinary[::-1] + '0'
    firstNumber = firstNumber[::-1]
elif length1 <= length2:
    length = length2 + 1
    extraZeros = length - length1
    if extraZeros == 0:
        extraZeros = 1
    firstNumber = firstBinary[::-1] + ('0'*extraZeros) 
    firstNumber = firstNumber[::-1]
    secondNumber = secondBinary[::-1] + '0'
    secondNumber = secondNumber[::-1]



while True:
    if (count >= length) and (futureDigit < 1):
        break
    newDigit = int(firstNumber[length-(1+count)]) + int(secondNumber[length-(1+count)]) + futureDigit
    if newDigit > 1:
        newDigit -= 2
        futureDigit = 1
    elif newDigit < 2:
        futureDigit = 0        
    newDigit = str(newDigit)
    digits += newDigit
    count += 1
Answer = digits[::-1]
if Answer[0] == '0':
    Answer = preAnswer[1:length:1]
print('answer = ',Answer)
