


unsortedList = eval(input("enter a list: "))

#[11,7,14,19,12]
for i in range(1,len(unsortedList)):
        marker = unsortedList[i]
        for i1 in range(i-1, -1, -1):
            if marker < unsortedList[i1]:
                unsortedList[i1+1], unsortedList[i1] = unsortedList[i1], unsortedList[i1+1]
            else:
                break
                
                
print("the sorted list is: ", unsortedList)
