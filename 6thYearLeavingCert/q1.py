# Q1

def lengthify(List):
    
    if List == []:
        return 0
    else:
        return 1 + lengthify(List[1:])

List = eval(input("enter a list: "))

lengthList = lengthify(List)

print(lengthList)