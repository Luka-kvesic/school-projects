
def calculateMean(List):
    total = 0
    for i in range(len(List)):
        total += List[i]
    mean = total / len(List)
    return mean
    
def calculateMedian(List):
    List.sort()
    middle = len(List)
    if middle % 2 == 0:
        median = List[middle//2]
    elif middle % 2 == 1:
        median = List[(middle-1)//2]
    return median
        
def calculateMode(List):
    List.sort()
    offset = 0
    biggestAmount = 0
    for i in range(len(List)-1, -1,-1):
        currentItem = List[i] 
        if i < len(List)-1:
            amount = 1
            i1 = 1
            while currentItem == List[i-i1]:
                amount += 1
                i1 += 1
            if amount > biggestAmount:
                biggestAmount = amount
                mode = List[i]
    return mode


def calculateFrequency(List):
    List.sort()
    frequencyTable = []
    for i in range(len(List)):
        if frequencyTable:
            for i1 in range(len(frequencyTable)):
                foundOne = False
                if frequencyTable[i1][0] == List[i]:
                    print(frequencyTable[i1])
                    frequencyTable[i1][1] += 1
                    foundOne = True
                else:
                    foundOne = False
            if not foundOne:
                frequencyTable.append([List[i],1])
        else:
            frequencyTable.append([List[i],1])
    return frequencyTable


def calculateRange(List):
    List.sort()
    lowest = List[0]
    highest = List[-1]
    Range = highest - lowest
    return Range

# [5,1,55,8,12,44,12,44,44,11,12,21]

# #List = eval(input("enter a list: "))
# 
# print("the mean is: ", calculateMean(List))
# print("the median is: ", calculateMedian(List))
# print("the mode is: ", calculateMode(List))
# print("the frequency is: ", calculateFrequency(List))
# print("the range is: ", calculateRange(List))