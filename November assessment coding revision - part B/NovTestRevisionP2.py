#author: Luka kvesic
#date: 15 dec 2025
#description: program 2

reversedWinCardNum = ''
winCard = 8549018035096133
total = 0
winCardString = str(winCard)

#----------------step 1----------------#
winCardNum = winCardString[0:len(winCardString)-1]
checkingDigit = winCardString[len(winCardString)-1:len(winCardString)]
#----------------step 2----------------#
for i in range(-1, -1*(len(winCardNum)), -1):
    reversedWinCardNum += winCardNum[i]
print(reversedWinCardNum)
#----------------step 3----------------#
evenWinCardIndices = reversedWinCardNum[::2]
print(evenWinCardIndices)
oddWinCardIndices = reversedWinCardNum[1::2]
print(oddWinCardIndices)

for i in range(len(evenWinCardIndices)):
    evenDigit = evenWinCardIndices[i]
    evenDigit = int(evenDigit) *2
    if evenDigit > 9:
        evenDigit -= 9
        #--------step 4----------------#
    total += evenDigit
total += int(checkingDigit)
#----------------step 5----------------#
if total%10 == 0:
    print('valid')
else:
    print('invalid')
    
    