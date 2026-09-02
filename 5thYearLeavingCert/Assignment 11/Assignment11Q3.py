#author: Luka kvesic
#date: 21 october 2025
#description: get sum of numbers in a string
sum1 = 0
string = input('please enter a string')

for i in range(len(string)):
    letter = string[i]
    if letter.isdigit() == True:
        number = int(letter)
        sum1 += number 
        continue
print(sum1)