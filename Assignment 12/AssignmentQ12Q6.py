#author: Luka kvesic
#date: 4 November 2025
#description: programme that makes a new line of text that has all words reversed

word = ''
reversedString = ''
string = input('enter a string: ')

for i in range(len(string)):
    if string[i] != ' ':
        word += string[i]
    if (string[i] == ' ') or (i == len(string) - 1):
        savedWord = word
        word = ''
        reversedString += savedWord[::-1] + ' '
    
print(reversedString)