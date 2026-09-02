#name       Luka kvesic
#date       2/12/2026
#programme  two digit property with sum of sqaures

currentList = []
for i1 in range(10,99):
    digit1 = i1
    for i2 in range(10,99):
        digit2 = i2
        for i3 in range(10,99):
            digit3 = i3
            altDigit1 = str(digit1)
            altDigit1 = altDigit1[::-1]
            altDigit2 = str(digit2)
            altDigit2 = altDigit2[::-1]
            altDigit3 = str(digit3)
            altDigit3 = altDigit3[::-1]                      
            altDigit1 = int(altDigit1)                   
            altDigit2 = int(altDigit2)
            altDigit3 = int(altDigit3)
            if ((digit1**2) + (digit2**2) + (digit3**2)) == ((altDigit1**2) + (altDigit2**2) + (altDigit3**2)):
                currentList = [digit1,digit2,digit3]
                print(currentList)
