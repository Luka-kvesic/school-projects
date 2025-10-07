#author: Luka kvesic
#date: 7 october 2025
#description: Write a program to take N (N > 20) as an input from the user. Print numbers from 11 to N. When the number is a multiple of 3, print "Tipsy", when it is a multiple of 7, print "Topsy". When it is a multiple of both, print "Tipsy Topsy"


count = 10
number = int(input('give a number above 20: '))


        
while count < number:
    count += 1
    if number < 20:
        print('too low')
        number = int(input('give a number above 20: '))
        continue
    if count%3 == 0 and count%7 == 0:
        print('TipsyTopsy')
    elif count%3 == 0:
        print('Tipsy')
    elif count%7 == 0:
        print('Topsy')
    else:
        print(count)
    