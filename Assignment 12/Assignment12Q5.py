#author: Luka kvesic
#date: 3 november 2025
#description: programme that prints the biggest word
word      = ''
savedWord = ''
string = input('enter a string: ')

for i in range(len(string)):
    letter = string[i]
    
    if letter == ' ':
        if len(word) > len(savedWord):
            savedWord = word
            word = ''
    else:
        word += letter
if len(word) > len(savedWord):
    savedWord = word
print(savedWord)
        