


def simpleSort(unsortedList, sortedList):
    
    while unsortedList:
        smallestValue = 9999999999999999999999999999999999
        for i1 in range(len(unsortedList)):
            currentValue = unsortedList[i1]
            if currentValue < smallestValue:
                smallestValue = currentValue
                smallestIndex = i1
        unsortedList.pop(smallestIndex)
        sortedList.append(smallestValue)
    return sortedList


UnsortedList = eval(input("enter a unsorted list: "))

sortedList = []
# [5,2,8,1,9,6,4]

print("sorted list is: ",simpleSort(UnsortedList, sortedList))