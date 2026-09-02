#author: Luka kvesic
#date: 8 dec 2025
#description: product of first 50 ints that are multiples of 5

total = 1
for i in range(1, 50+1):
    if i%5 == 0:
        total *= i
print(total)