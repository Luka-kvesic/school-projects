#author: Luka kvesic
#date: 8 dec 2025
#description: all even ints up to user value

total = 0
integer = int(input('give an integer: '))
for i in range(1, integer+1):
    if i%2 == 1:
        total += i

print(total)
