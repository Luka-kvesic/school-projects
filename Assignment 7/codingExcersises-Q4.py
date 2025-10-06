#author: Luka kvesic
#date: 6 october 2025
#description: programme thats converts decimal to binary

number = int(input('give a number to convert to binary: '))
combined = ""
while number != 0:
    if (number%2 == 1):
        remainder = number%2
        number = (number // 2) 
        print(int(remainder))
    elif (number%2 == 0):
        remainder = number%2
        number = number / 2
        print(int(remainder))
    remainder = int(remainder) #i didnt know how to arrange the digits in the right order as i dont think we did it, so i looked it up
    combined += str(remainder)
    backward = combined[::-1]
        
print(backward)
