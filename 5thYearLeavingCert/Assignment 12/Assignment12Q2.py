#author: Luka kvesic
#date: 3 november 2025
#description: write a programme to check how many words are in a string

string = input('enter a string: ')
count = 1
for i in range(len(string)):
    if string[i] == ' ':
        count += 1
print(count)
