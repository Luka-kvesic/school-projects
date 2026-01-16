list1 = eval(input("enter a list with numbers between 1 and 12: "))
list2 = []
for i in range(len(list1)):
    if list1[i] > 10:
        list2.append(10)
    else:
        list2.append(list1[i])
print(list2)