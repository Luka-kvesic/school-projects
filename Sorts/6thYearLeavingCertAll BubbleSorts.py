
def BubbleSortV1(List):
    for i1 in range(len(List) - 1):
        swapplet1 = 0
        swapplet2 = 1
        for i in range(len(List) - 1):
            if List[swapplet1] > List[swapplet2]:
                
                swappling = List[swapplet1]
                List.pop(swapplet1)
                List.insert(swapplet2, swappling)
            swapplet1 += 1
            swapplet2 += 1
    return List

def BubbleSortV2(List):
    efficiencySkip = 0
    for i1 in range(len(List) - 1):
        
        swapplet1 = 0
        swapplet2 = 1
        for i in range(len(List) - 1 - efficiencySkip):
            if List[swapplet1] > List[swapplet2]:
                swappling = List[swapplet1]
                List.pop(swapplet1)
                List.insert(swapplet2, swappling)
            swapplet1 += 1
            swapplet2 += 1
        efficiencySkip += 1
    return List

def BubbleSortV3(List):
    efficiencySkip = 0
    for i1 in range(len(List) - 1):
        
        swapplet1 = 0
        swapplet2 = 1
        noSwaps = True
        for i in range(len(List) - 1 - efficiencySkip):
            if List[swapplet1] > List[swapplet2]:
                noSwaps = False
                swappling = List[swapplet1]
                List.pop(swapplet1)
                List.insert(swapplet2, swappling)
            swapplet1 += 1
            swapplet2 += 1
        if noSwaps:
            return List
        efficiencySkip += 1
    return List





List = eval(input("enter a list: "))
#    [10, 8, 6, 4, 2, 33,1,23]
List2 = List.copy()
List3 = List.copy()

print("sorted list V1: ",BubbleSortV1(List))
print("sorted list V2: ",BubbleSortV2(List2))
print("sorted list V3: ",BubbleSortV3(List3))
