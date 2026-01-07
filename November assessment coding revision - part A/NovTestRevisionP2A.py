#author: Luka kvesic
#date: 7 jan 2026
#description: program 1

checkLength = False
continueWithCheck = False
running = True
tries = 3
dateNum = 0
dateLength = 0
i = 0
proggrameRun = True
cvv = 0
while (tries > 0) and (proggrameRun):
    cardNum = input('Welcome to CardCheck. Enter your card number: ') # 7200828282828210
    print(cardNum)
    cardCopy = cardNum[-1*(len(cardNum))]
    if cardCopy == '7':
        print('This is a zincCard')
    elif cardCopy == '8':
        print('This is a WinCard')
    else:
        tries -= 1
        print('invalid try again')
        continue
    if len(cardNum) == 16:
        continueWithCheck = True
    else:
        tries -= 1
        print('invalid try again')
        continue
    if continueWithCheck:
        date = input('Enter the card expiry date: ')
        dateCopy = int(date)
        for i in range(len(date)):
            dateNum += int(date[i])
        twoDigits = cardNum[-16:-14]
        tenthDigit = cardNum[-7]
        cvv = (dateNum * int(twoDigits)) - int(tenthDigit)
        finalNumber = cardNum[0:4]+'-'+cardNum[4:8]+'-'+cardNum[8:12]+'-'+cardNum[12:16]
        print('CVV number:', cvv)
        print('Card number:',finalNumber, 'and it is valid')
        proggrameRun = False

