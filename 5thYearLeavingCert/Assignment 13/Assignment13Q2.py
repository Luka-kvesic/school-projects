#author: Luka kvesic
#date: 8 dec 2025
#description: sum of n ints where n is entered by user

sumOf50 = 0
integer = int(input('give an integer: '))
for i in range(1, integer+1):
    sumOf50 += i
print(sumOf50)