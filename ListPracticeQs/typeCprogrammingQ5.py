list1 = eval(input("enter a list of strings: "))
list2 = []
for i in range(len(list1)):
    string = str(list1[i])
    string = string[1:]
    list2.append(string)
print(list2)