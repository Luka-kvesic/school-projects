#author: Luka kvesic
#date: 01 september 2025
#description: enter any amount of days and tell how many hours minutes nad seconds there are

days = input('enter a random amount of days: ')
days = int(days)
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print('there are', hours, 'many hours')
print('there are', minutes, 'many minutes')
print('there are', seconds, 'many seconds')
