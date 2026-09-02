#author: Luka kvesic
#date: 3 november 2025
#description: checks how many vowels are in a string
count = 0

string = input('enter a string: ')

for i in range(len(string)):
    string = str.lower(string)
    if (string[i] == 'a') or (string[i] == 'o')  or (string[i] == 'i') or (string[i] == 'u') or (string[i] == 'e') :
        count += 1
print('there are', count,'vowels in your string')
