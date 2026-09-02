# Question 16(b) 
# Name and School: luka kvesic
 
List = [4,5,9,8,10,17,99,77]
List.sort()

if len(List)%2 == 0:
    firstNum = List[(len(List)-1)//2]
    secondNum = List[(len(List)-1)//2 +1]
    median = (firstNum + secondNum) /2
elif len(List)%2 == 1:
    median = List[(len(List)//2)]
    
print("median =",median)
    

