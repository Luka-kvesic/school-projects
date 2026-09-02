#author: Luka kvesic
#date: 21 october 2025
#description: replace first repeating character to $
finalString = ''
NewString = ''
string = input('enter a string: ')
letterInQuestion = string[0]

for i in range(1,len(string)):
    character = string[i]
    if character == letterInQuestion:
        NewString = string.replace(letterInQuestion, '$')
        finalString = NewString[1:]
print(letterInQuestion+finalString)
    
    