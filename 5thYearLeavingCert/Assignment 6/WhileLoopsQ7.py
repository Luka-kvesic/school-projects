#author: Luka kvesic
#date: 2 october 2025
#description: asks to enter a number between 10 and 20, if its below 10 say 'too low' if its above 20 say 'too high'

number = 0
while number < 10 or number > 20:
    number = int(input('give a number between 10 and 20: '))
    if number < 10:
        print('too low')
    elif number > 20:
        print('too high')
    else:
        print('thank you')