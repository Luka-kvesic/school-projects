#author: Luka kvesic
#date: 21 october 2025
#description: test all python string methods


string = input('enter a string: ')

stringUpper = string.upper()
print('operation string.upper() : ', stringUpper)
stringLower = string.lower()
print('operation string.lower() : ', stringLower)
stringCount = string.count('e')
print('operation string.count("e") : ', stringCount)
stringReplace = string.replace('l', 'o')
print('operation string.replace("l", "o") : ', stringReplace)
stringIsLower = string.islower()
if stringIsLower:
    print('operation string.islower() : True')
else:
    print('operation string.islower() : False')
    
stringIsUpper = string.isupper()
if stringIsUpper:
    print('operation string.isupper() : True')
else:
    print('operation string.isupper() : False')

stringIsAlnum = string.isalnum()
if stringIsAlnum:
    print('operation string.isalnum() : True')
else:
    print('operation string.isalnum() : False')

stringIsAlpha = string.isalpha()
if stringIsAlpha:
    print('operation string.isalpha() : True')
else:
    print('operation string.isalpha() : False')
stringIsDigit = string.isdigit()
if stringIsDigit:
    print('operation string.isdigit() : True')
else:
    print('operation string.isdigit() : False')
    
stringIndex = string.index('l')
print('operation string.index("l") : ', stringIndex)

stringStrip = string.strip('h')
print('operation string.strip("h") : ', stringStrip)




