#author: Luka kvesic
#date: 17 november 2025
#description: binary adder

firstBinary = input('give the first binary number')

secondBinary = input('give the second binary number')

length1 = len(firstBinary)
length2 = len(secondBinary)
newDigit = 0
digits = ''
futureDigit = 0


if length1 >= length2:
    length = length1
elif length1 <= length2:
    length = length2
    
for i in range(length):
    newDigit = int(firstBinary[len(firstBinary)-1]) + int(secondBinary[len(secondBinary)-1]) + futureDigit
    if newDigit > 1:
        newDigit -= 2
        futureDigit = 1
    newDigit = str(newDigit)
    digits += newDigit
    
print(digits[::-1])
