#author: Luka kvesic
#date: 23 october 2025
#description: ask for string and step sise and add sum of all landed digits
sum1 = 0
string = input('enter a large number:')
step = int(input('enter a step size: '))


for i in range(0,len(string),step):
    number = string[i]
    sum1 += int(number)
print(sum1)