#author: Luka kvesic
#date: 19 september 2025
#description: programme that gets grades and average it out and gives a grade too
amount = 0
total = 0
while True:
    user_input = input('give a number you want to average: ')
    if user_input=='':
        break
    user_input = int(user_input)
    total += user_input
    amount += 1

average = total / amount
print('average is:', average)
if average >=90:
    print('your grade is: A')
elif average > 80 and average <= 89:
    print('your grade is: B')
elif average > 70 and average <= 79:
    print('your grade is: C')
elif average > 60 and average <= 69:
    print('your grade is: D')
elif average <= 59:
    print('your grade is: F')
    
