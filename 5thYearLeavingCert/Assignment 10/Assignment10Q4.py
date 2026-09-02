#author: Luka kvesic
#date: 21 october 2025
#description: programme that removes characters with odd indexes

newString = ''
string = input('enter a string: ')

for i in range(len(string)):
    if i % 2 == 0:
        newString += string[i]
print(newString)