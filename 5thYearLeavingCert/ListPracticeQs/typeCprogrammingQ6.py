list1 = eval(input("enter a list of integers: "))
numFound = False
for i in range(len(list1)):
    if list1[i] == 5:
        place = list1.index(5)
        numFound = True
    elif (i == len(list1)-1) and not (numFound):
        print("number 5 is not in list")
if numFound:
    print("5 is in index",place)