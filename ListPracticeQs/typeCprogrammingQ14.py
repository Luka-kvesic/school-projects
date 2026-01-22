list1 = [1,1,1,1,3,2,2,4,2,6,6,7]
potentialDupes = []
dupes = []
i = 0
running = True
while running:
    print(i)
    if i >= len(list1)-1:
        running = False
        continue
    for j in range(len(potentialDupes)):
        subRunning = True
        while subRunning:
            if list1[i] == potentialDupes[j]:
                dupes.append(list1[i])
                list1.pop(i)
            else:
                subRunning = False
           
    potentialDupes.append(list1[i])
    print(list1)
    i += 1
list1.extend(dupes)
print(list1)
