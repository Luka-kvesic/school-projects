#author: Luka kvesic
#date: 2 october 2025
#description: print from 1 to n using a while loop it should skip every multiple of 5

number = int(input('give a number: '))
iteration = 0
while iteration < number:
    iteration += 1
    if iteration%5 == 0:
        continue
    print(iteration)
    
    