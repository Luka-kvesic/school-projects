#author: Luka kvesic
#date: 21 october 2025
#description: programme that reverses a string using a for loop
newWord = ''

string = input('enter a string: ')

for i in range(len(string),0,-1):
    letter = string[i-1]
    newWord += letter
print(newWord)

