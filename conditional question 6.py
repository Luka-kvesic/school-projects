#author: Luka kvesic
#date: 04 september 2025
#description: ask users age and tell them what they can do with that age

age = int(input('what is your age: '))

if (age >= 18):
    print('you can vote')
elif (age == 17):
    print('you can learn to drive')
elif (age == 16):
    print('you can buy a lottery ticket')
else:
    print('you can go trick or treating')