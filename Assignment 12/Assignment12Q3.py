#author: Luka kvesic
#date: 3 november 2025
#description: write a programme to check if a formula has equal opening and closing parenthesis

opening = 0
closing = 0
formula = input('enter a formula: ')

for i in range(len(formula)):
    if formula[i] == '(':
        opening += 1
    if formula[i] == ')':
        closing += 1
if closing == opening:
    print('you have equal opening and closing parenthesis')
elif closing != opening:
    print('you dont have equal opening and closing parenthesis')