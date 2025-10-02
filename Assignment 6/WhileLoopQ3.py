#author: Luka kvesic
#date: 2 october 2025
#description: take integer number and output all even numbers

number = int(input('give a number: '))
even_number = 0
while even_number < number:
    if (even_number+1) == number:
        break
    even_number += 2
    print(even_number)
    
    
