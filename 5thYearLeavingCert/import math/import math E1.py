#author: Luka kvesic
#date: 2/23/2026
#description: example 1
import math
a = 1
b = 2
c = 3

# --------- i ---------

answer1 = math.sqrt((math.pow(a, 2))+(math.pow(b, 2))+(math.pow(c, 2)))
print(answer1)

#---------- ii --------

y = 2
e = 3

answer2 = 2 - y*(math.pow(e, 2*y)) + 4*y
print(answer2)

# ---------- iii ---------

p = 2
q = 3
r = 4
s = 5

answer3 = p + q/math.pow((r+s), 4)
print(answer3)

#------------ iv ----------


x = 2

answer4 = (math.cos(x)/math.tan(x)) + x
print(answer4)

#------------ v ---------

e = 2
x = 5

answer5 = math.fabs(math.pow(e, 2)- x)
print(answer5)

