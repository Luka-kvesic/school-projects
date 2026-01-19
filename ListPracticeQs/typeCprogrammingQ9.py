list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = []
list2.append(list1[len(list1)-1])
for i in range( len(list1)-1):
    list2.append(list1[i])
list1 = list2.copy()
print(list1)