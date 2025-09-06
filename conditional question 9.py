#author: Luka kvesic
#date: 04 september 2025
#description: program for calculating the water bill
units = float(input('how many units did you use: '))

if (units <=100):
    calculation = units * 0.05 
    print('it will cost ',calculation)
elif (units >= 100) and (units <= 250):
    calculation = units * 0.1
    print('it will cost ',calculation)
elif (units > 250):
    calculation = units * 0.20
    print('it will cost ',calculation)
