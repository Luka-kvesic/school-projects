#author: Luka kvesic
#date: 04 september 2025
#description: ask if its raining and windy and give the appropriate response to it
print('answer the following with "yes" or "no"')
question1 = input('is it raining: ')
question2 = input('is it windy: ')
if (question1 == 'yes') or (question1 == 'Yes'):
   question1 = '1'
else:
    question1 = '0'
if (question2 == 'yes') or (question2 == 'Yes'):
    question2 = '1'
else:
    question2 = '0'
    
code = question1+question2
if (code == '11'):
    print('its too windy for an umbrella')
elif (code == '10'):
    print('bring an umbrella')
elif (code == '00'):
    print('have a good day')
elif (code == '01'):
    print('you dont need to bring anything')
    

# first version, correct version in other file
