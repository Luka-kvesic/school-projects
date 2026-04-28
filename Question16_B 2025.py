#Question 16(b)
#Name and School: luka kvesic

temperatures=[14,23.5,72,56,45.5]
totalHeat = 0
totalNewHeat = 0
newTemp = float(input("Enter a tempature: "))
temperatures.append(newTemp)
highestTemp = 0
lowestTemp = 999999999999999999999999999999999999999999999
for i in range(len(temperatures)):
    temp = temperatures[i]
    if temp > highestTemp:
        highestTemp = temp
for i in range(len(temperatures)):
    temp = temperatures[i]
    if temp < lowestTemp:
        lowestTemp = temp
print("highest tempature =",highestTemp,"lowest tempature =",lowestTemp)

for i in range(len(temperatures)-1):
    totalHeat += temperatures[i]
for i in range(len(temperatures)):
    totalNewHeat += temperatures[i]
oldMean = totalHeat / len(temperatures)-1
newMean = totalNewHeat / len(temperatures)
if oldMean > newMean:
    print("The mean tempature is decreasing")
elif oldMean < newMean:
    print("The mean tempature is increasing")