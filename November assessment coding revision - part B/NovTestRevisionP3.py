#author: Luka kvesic
#date: 16 dec 2025
#description: program 3

reversedWinCardNum = ''
winCard = 8549018035096133
total   = 0
winCardString = str(winCard)
evenWinCardIndices = ''
oddWinCardIndices  = ''
#----------------step 1----------------#
winCardNum    = winCardString[0:len(winCardString)-1]
checkingDigit = winCardString[len(winCardString)-1:len(winCardString)]
#----------------step 2----------------#
for i in range(-1, -1*(len(winCardNum)+1), -1):
    reversedWinCardNum += winCardNum[i]
print(reversedWinCardNum)
#----------------step 3----------------#

for i in range(len(reversedWinCardNum)):
    if i%2 == 0:
        evenDigit = reversedWinCardNum[i]
        evenDigit = int(evenDigit) *2
        if evenDigit > 9:
            evenDigit -= 9
        total += evenDigit
    if i%2 == 1:
        oddDigit = reversedWinCardNum[i]
        oddDigit = int(oddDigit) 
        #--------step 4----------------#
        total += oddDigit
total += int(checkingDigit)
#----------------step 5----------------#
if total%10 == 0:
    print('valid')
else:
    print('invalid')
    
    