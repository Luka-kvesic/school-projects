#author: Luka kvesic
#date: 19 september 2025
#description: calculate simple interest

princeple = int(input('what is the princeple: '))
rate = float(input('what is the rate, give as a decimial: '))
time = int(input('for how many years: '))

total = princeple * (1+rate*time)
print(total)