#name luka kvesic

list1 = eval(input("enter a list of numbers: "))

def rangefinder(list1):
    list1.sort()
    smallest = list1[0]
    biggest = list1[len(list1)-1]
    return biggest - smallest
ranje = rangefinder(list1)
print("range",ranje)
summ = 0
def averagefinder(list1):
    summ = 0
    for i in range(len(list1)):
        summ += list1[i]
        
    return summ / len(list1)

average = averagefinder(list1)
print("average",average)

def medianfinder(list1):
    list1.sort()
    length = len(list1) 
    if length %2 == 0:
        median = (list1[(length//2)-1] + list1[(length//2)]) /2
    elif length % 2 == 1:
        median = list1[(((length)//2))]
    return median
median  = medianfinder(list1)

def modefinder(list1):
    previousNum = 897158714571049856194561946571465
    amount = 0
    previousAmount = 0
    list1.sort()
    for i in range(len(list1)):
        number = list1[i]
        if number == previousNum:
            amount += 1
        elif number != previousNum:
            if amount > previousAmount:
                mode = list1[i-1]
                previousAmount = amount
                amount = 0
        previousNum = number
    return mode
      
mode = modefinder(list1)

print("median",median)
print("mode",mode)

def frequencyFinder(list1):
    frequencyList = []
    previousNum = 897158714571049856194561946571465
    amount = 1
    list1.sort()
    for i in range(len(list1)):
        number = list1[i]
        if number == previousNum:
            amount += 1
        elif number != previousNum:
            pair = (list1[i-1],amount)
            frequencyList.append(pair)
            amount = 1
        previousNum = number
    return frequencyList

frequencyList = frequencyFinder(list1)
for i in range(len(frequencyList)):
    numbar = frequencyList[i][0]
    amaunt = frequencyList[i][1]
    print(numbar, "pops up",amaunt,"times")


