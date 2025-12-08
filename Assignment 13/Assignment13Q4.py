#author: Luka kvesic
#date: 8 dec 2025
#description: sum of first 50 ints that are even

total = 0
for i in range(1, 50+1):
    if i%2 == 0:
        total += i

print(total)
