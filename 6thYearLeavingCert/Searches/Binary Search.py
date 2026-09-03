


def BinarySearch(List, x):
    List.sort()
    if x.isdigit():
        x = int(x)
    low = 0
    high = len(List) - 1
    middle = (high + low) // 2
    while True:
        if List[middle] > x:
            high = middle -1
            middle = (high + low) // 2
        elif List[middle] < x:
            low = middle + 1
            middle = (high + low) // 2
        elif List[middle] == x:
            return middle
        if (low >= high) or (high <= low):
            return -1
            
# [2, 5, 8, 12, 16,56,23,72,38,91]

List = eval(input("enter the list: "))
List.sort()
elementX = input("enter the value to search for: ")

print("the index for the value is: ", BinarySearch(List, elementX))