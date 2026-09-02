#author: Luka kvesic
#date: 8 dec 2025
#description: product of all even numbers of first 50 integers

total = 1
for i in range(1, 50+1):
    if i%2 == 0:
        total *= i

print(total)
