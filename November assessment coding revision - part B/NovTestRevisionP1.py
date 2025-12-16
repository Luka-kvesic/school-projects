#author: Luka kvesic
#date: 16 dec 2025
#description: program 1


winCard = 8549018035096133
total = 0
winCardString = str(winCard)

#----------------step 1----------------#
winCardNum = winCardString[0:len(winCardString)-1]
checkingDigit = winCardString[len(winCardString)-1:len(winCardString)]
#----------------step 2----------------#
reversedWinCardNum = winCardNum[-1:-1*(len(winCardNum)+1):-1]
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
for i in range(len(oddWinCardIndices)):
    oddDigit = oddWinCardIndices[i]
    oddDigit = int(oddDigit) 
    total += oddDigit
print(total)

total += int(checkingDigit)
print(total)
#----------------step 5----------------#
if total%10 == 0:
    print('valid')
else:
    print('invalid')
