#author: Luka kvesic
#date: 8 dec 2025
#description: product of first 5 integers

total = 0
integer = int(input('give an integer: '))
for i in range(1, integer+1):
    if i%2 == 1:
        total += i
print(total)