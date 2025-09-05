#author: Luka kvesic
#date: 04 september 2025
#description: ask user if they entered 1,2 or 3 and give a response depending on what they give
number = int(input('give a number between 1 and 3: '))

if (number == 1):
    print('thank you')
elif (number == 2):
    print('well done')
elif (number == 3):
    print('correct')
else:
    print('error')
