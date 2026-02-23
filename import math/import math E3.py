#author: Luka kvesic
#date: 2/23/2026
#description: example 8
import math

listy = [22, 13, 28, 13, 22, 25, 7, 13, 25]

listy = sorted(listy)

mean = sum(listy) / len(listy)
print('mean',mean) 

median = listy[round(len(listy)/2)]
print('median',median)
count = 0
amount = 0
preAmount = 0
for i in listy:
    amount = 0
    for i1 in listy:
        if i == i1:
            amount += 1
    if amount > preAmount:
        preAmount = amount
        iSaved = count
    count += 1
mode = listy[iSaved]
print('mode',mode)