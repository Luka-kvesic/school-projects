list1 = [1,2,3,4,5,6,7,8,9,0,]
list2 = []
print("heres a list: ",list1)
startIndex = int(input("what index range will it start at: "))
endIndex = int(input("what index range will it stop at: "))

for i in range(startIndex,endIndex):
    list2.append(list1[i])
print(list2)
