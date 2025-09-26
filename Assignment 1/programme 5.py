#author: Luka kvesic
#date: 01 september 2025
#description: how many pizzas had he to start and how many he ate

pizza_start = input('how many slices did you start with: ')
pizza_eaten = input('how many did you eat: ')
pizza_start = int(pizza_start)
pizza_eaten = int(pizza_eaten)

slices_left = pizza_start - pizza_eaten
print('you have', slices_left, 'slices left')
