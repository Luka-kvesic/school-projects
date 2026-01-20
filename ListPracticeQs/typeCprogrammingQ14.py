list1 = [1,2,3,4,4,5,6,7,7,8,9,0]

#WORK IN PROGRESS

potentialDupes = []
duplicates = []

for i in range(len(list1)):
    print(list1,"mm")
    for i1 in range(len(potentialDupes)):
        if list1[i] == potentialDupes[i1]:
            duplicates.append(list1[i])
            print(duplicates)
            list1.pop(i)
    print(i)
    print(list1)
    potentialDupes.append(list1[i])
    print(potentialDupes)

list1.extend(duplicates)
print(duplicates)
print(list1)