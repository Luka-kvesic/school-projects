#author: Luka kvesic
#date: 09 september 2025
#description: print multiplication table with given nmber

number = int(input('give a number for the multiplication table: '))

for i in range(13):
    total = number * i
    print(number,'*', i,'=', total)
    
    
    
    