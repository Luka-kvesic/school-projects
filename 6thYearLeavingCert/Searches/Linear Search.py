
def LinearSearch(List, x):
    if x.isdigit():
        x = int(x)
    index = 0
    while True:
        if List[index] == x:
            return index
        elif List[index] == List[-1]:
            return -1
        
        index += 1
        


itemList = eval(input("enter a list of items: "))

elementX = input("enter the item to search for: ")


print("the index is", LinearSearch(itemList, elementX))
