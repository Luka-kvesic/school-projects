#author: Luka kvesic
#date: 5 jan 2026
#description: program 1

checkLength = False
continueWithCheck = False
running = True
tries = 3
i = 4
while tries > 0:
    cardNum = input('Welcome to CardCheck. Enter your card number: ') # 7200828282828210
    print(cardNum)
    int(cardCopy) = cardNum
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
    if checkLength:
        if len(cardNum) == 16:
            continueWithCheck = True
        else:
            tries -= 1
            print('invalid try again')
            continue
    if continueWithCheck:
        date = input('Enter the card expiry date: ')
        dateCopy = date
        while i > 0:
            cvv +=  
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        