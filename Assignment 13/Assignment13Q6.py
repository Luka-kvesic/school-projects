#author: Luka kvesic
#date: 8 dec 2025
#description: sum of first 50 integers that are multiple of 3

total = 0
for i in range(1, 50+1):
    if i%3 == 0:
        total += i

print(total)
