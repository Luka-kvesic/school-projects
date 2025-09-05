#author: Luka kvesic
#date: 05 september 2025
#description: ask if its raining and windy and give the appropriate response
raining = input('is it raining: ')
if (raining == 'yes') or (raining == 'Yes') or (raining == 'YES'):
    windy = input('is it windy: ')
    if (windy == 'yes') or (windy == 'Yes') or (windy == 'YES'):
        print('its too windy for an umbrella')
    else:
        print('bring an umbrella')
else:
    print('have a good day')

        
