


def selectionSort(unsortedList):
    
    for i in range(len(unsortedList) -1):
        marker = i
        smallestValue = 9999999999999999999999999999999999
        for i1 in range(marker, len(unsortedList)):
            currentValue = unsortedList[i1]
            if currentValue < smallestValue:
                smallestValue = currentValue
                smallestIndex = i1
        unsortedList.insert(smallestIndex, unsortedList[marker])
        unsortedList.pop(marker)
        unsortedList.insert(marker, smallestValue)
        unsortedList.pop(smallestIndex + 1)
    return unsortedList








unsortedList = eval(input("enter an unsorted list: "))

# [5,2,8,1,9,6,4]


print("the sorted list is: ", selectionSort(unsortedList))