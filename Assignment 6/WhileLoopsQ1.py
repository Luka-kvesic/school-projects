#author: Luka kvesic
#date: 19 september 2025
#description: programme that gets integers and average it out
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
print(average)
