#author: Luka kvesic
#date: 04 september 2025
#description: ask for a number and tell them if its too low or high or if its good
number = int(input('pick a number: '))

if (number < 10):
    print('its too low')
elif (number > 20):
    print('its too high')
else:
    print('correct')
