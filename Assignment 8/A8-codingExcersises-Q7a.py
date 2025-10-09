#author: Luka kvesic
#date: 9 october 2025
#description: q20 a, complete sum of fraction terms
denominator = 9
topNumber = 2
total = 0
for i in range(1, 7+1):
    fraction = topNumber / denominator
    topNumber += 3
    denominator += 4
    if i%2 == 0:
        fraction = fraction * -1
    total = fraction + total
print(total)
    