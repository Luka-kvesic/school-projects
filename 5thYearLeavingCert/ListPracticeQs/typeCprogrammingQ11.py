
#A

str_list = eval(input("enter a list of strings and ill check what the longest is: "))
check2 = 0
if len(str_list) > 0:
    for i in range(len(str_list)):
        check1 = len(str_list[i])
        if check1 > check2:
            check2 = check1
    print(check2)
else:
    print("error")

#B
    
L = [1,2,33,5,6,343,9]


newList = [1,2,3,4,5,6,7]
print("heres a list: ",newList,"enter a number and ill show you the corresponding number of it of another list that i have? : ")
num = int(input("enter an index: "))
print("so the element:",newList[num],"corresponds with:",L[num])