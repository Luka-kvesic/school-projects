list1 = [1,2,3,4,5,6,7,8,9]
list2 = [1,2,3,4,5,7,6,8,9]
index = 0
for i in range(len(list1)):
    if list1[i] != list2[i]:
        break
    index += 1
print("the first index where they differ is: ",index)