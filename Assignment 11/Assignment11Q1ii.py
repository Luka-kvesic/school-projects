#author: Luka kvesic
#date: 21 october 2025
#description: programme that reverses a string using a for loop
newWord = ''

string = input('enter a string')
i = len(string)
while i > 0:
    letter = string[i-1]
    i -= 1
    newWord += letter
print(newWord)
    
    