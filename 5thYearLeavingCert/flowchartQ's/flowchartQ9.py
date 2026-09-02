#author: Luka kvesic
#date: 19 september 2025
#description: print all odd numbers N times

N = int(input('how many numbers would you like: '))
number = 0
for i in range(N):
    number = number + 1
    if (number % 2 == 1):
        print(number)
    else:
        pass