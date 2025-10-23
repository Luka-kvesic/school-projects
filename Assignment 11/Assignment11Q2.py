#author: Luka kvesic
#date: 21 october 2025
#description: check if string is a plaindrome
newWord = ''

string = input('enter a string: ')

newWord = string[::-1]
if newWord == string:
    print(newWord,'is a palindrome')
else:
    print(string,'is not a palindrome')