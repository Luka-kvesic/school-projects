#author: Luka kvesic
#date: 7 october 2025
#description: programme that finds largest number of list of numbers entered through keyboard
iteration = 0
oldNumber = 0
number = 1
while True:
    if iteration != 0:
        number = input('enter another number: ')
        if number == 'end':
            break
    else:
        number = input('enter a number, enter "end" to end it: ')
        if number == 'end':
            break
        else:
            number = int(number)
    number = int(number)
    if iteration == 0:
        oldNumber = number
    if number > oldNumber:
        oldNumber = number
    iteration += 1

print(oldNumber,'is the highest number')
    