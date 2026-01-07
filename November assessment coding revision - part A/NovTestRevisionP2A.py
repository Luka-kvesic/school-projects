#author: Luka kvesic
#date: 7 jan 2026
#description: program 2

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
               #--------------Part 1--------------------#
    cardNum = input('Welcome to CardCheck. Enter your card number: ') # 7200828282828210
    print(cardNum)
    cardCopy = cardNum[-1*(len(cardNum))]
            #--------------Part 2 and 3--------------------#
    if cardCopy == '7':
        print('This is a zincCard')
    elif cardCopy == '8':
        print('This is a WinCard')
    else:
        tries -= 1
        print('invalid try again')
        continue
               #--------------Part 4--------------------#
    if len(cardNum) == 16:
        continueWithCheck = True
    else:
        tries -= 1
        print('invalid try again')
        continue
    if continueWithCheck:
            #--------------Part 5--------------------#
        date = input('Enter the card expiry date: ')
        dateCopy = int(date)
        for i in range(len(date)):
            dateNum += int(date[i])
        twoDigits = cardNum[-16:-14]
        tenthDigit = cardNum[-7]
        cvv = (dateNum * int(twoDigits)) - int(tenthDigit)
            #--------------Part 7--------------------#
        finalNumber = cardNum[0:4]+'-'+cardNum[4:8]+'-'+cardNum[8:12]+'-'+cardNum[12:16]
        print('CVV number:', cvv)
        print('Card number:',finalNumber, 'and it is valid')
        proggrameRun = False



