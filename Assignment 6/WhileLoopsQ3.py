#author: Luka kvesic
#date: 3 october 2025
#description: take integer number and output all even numbers

number = int(input('give a number: '))
count = 0
while count < number:
    count += 1
    if count%2 == 0:
        print(count)
    
    
