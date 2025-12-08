#author: Luka kvesic
#date: 8 dec 2025
#description: product of first 5 integers

total = 0
for i in range(1, 50+1):
    if i%2 == 0:
        total += i
print(total)