#author: Luka kvesic
#date: 19 september 2025
#description: print the factorial of a non negative integer

number = int(input('what is the number'))
factorial = 1
for i in range(1, number+1):
    
    factorial = factorial * i
print(factorial) 

    
