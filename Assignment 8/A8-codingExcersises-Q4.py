#author: Luka kvesic
#date: 7 october 2025
#description: programme that finds largest number of list of numbers entered through keyboard

amount = int(input('how many numbers do you want to input: '))
copyNumber = 0
secondNumber = 0
for i in range(1, amount + 1):
    number = int(input('enter a number: '))
    if i == 1:
        copyNumber = number
        secondnumber = number
    if number < copyNumber and number > secondNumber:
        secondNumber = number
    if copyNumber < number:
        copyNumber = number
    number = copyNumber
print('the second largest is: ',secondNumber)


    
    
    