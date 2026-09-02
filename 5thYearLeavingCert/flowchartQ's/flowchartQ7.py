#author: Luka kvesic
#date: 19 september 2025
#description: check if they are a child teenager or adult

age = int(input('what is your age: '))

if(age<13):
    print('you are a child')
else:
    if (age>=13) and (age<20):
        print('you are a teenager')
    else:
        print('you are a adult')
    