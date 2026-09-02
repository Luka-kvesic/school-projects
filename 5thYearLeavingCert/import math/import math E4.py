#author: Luka kvesic
#date: 2/23/2026
#description: example 9
import math


a = 2
b = 3
c = math.sqrt(math.pow(a, 2) + math.pow(a, 2))

s = (a + b + c) / 2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(s, area)
