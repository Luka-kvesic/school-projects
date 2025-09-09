#author: Luka kvesic
#date: 02 september 2025
#description: averages 5 marks to one average grade

number1 = int(input('enter the first grade: '))
number2 = int(input('enter the second grade: '))
number3 = int(input('enter the third grade: '))
number4 = int(input('enter the fourth grade: '))
number5 = int(input('enter the fifth grade: '))

averageGrade = (number1 + number2 + number3 + number4 + number5) / 5

print('the average mark is', averageGrade)
