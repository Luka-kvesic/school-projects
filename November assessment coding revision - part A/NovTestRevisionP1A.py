#author: Luka kvesic
#date: 6 jan 2026
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
                  #---------------Part 1------------------#
    cardNum = input('Welcome to CardCheck. Enter your card number: ') # 7200828282828210
    print(cardNum)
    cardCopy = int(cardNum)
                  #--------------Part 2 and Part 3-------------------#
    while cardCopy > 10:
        cardCopy = cardCopy // 10
    if cardCopy == 7:
        print('this is a zincCard')
        checkLength = True
    elif cardCopy == 8:
        print('this is a winCard')
        checkLength = True
    else:
        tries -= 1
        print('invalid try again')
        continue
                 #---------------Part 4-----------------------#
    if checkLength:
        if len(cardNum) == 16:
            continueWithCheck = True
        else:
            tries -= 1
            print('invalid try again')
            continue
                #-----------------Part 5---------------------#
    if continueWithCheck:
        date = input('Enter the card expiry date: ')
        dateCopy = int(date)
        while dateCopy > 1:
            dateCopy = dateCopy // 10
            dateLength += 1
        dateCopy = int(date)
        date = int(date)
        dateCopy = int(dateCopy)
        while i < dateLength:
            i += 1
            modulusifier = ((date // 10**i) * 10**i)
            if modulusifier == 0:
                modulusifier = 100000000000000000000000000
            dateNum += dateCopy % modulusifier // 10**(i-1)
        twoDigits = cardNum[0:2]
        tenthDigit = cardNum[9]
        cvv = (dateNum * int(twoDigits)) - int(tenthDigit)
                   #--------------Part 7----------------------#
        finalNumber = cardNum[0:4]+'-'+cardNum[4:8]+'-'+cardNum[8:12]+'-'+cardNum[12:16]
        print('CVV number:', cvv)
        print('Card number:',finalNumber, 'and it is valid')
        proggrameRun = False


