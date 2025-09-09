#author: Luka kvesic
#date: 09 september 2025
#description: get even numbers from range

amount = int(input('how many even numbers should i give: '))

for i in range(amount):
    if (i%2 == 0):
        print(i)

    