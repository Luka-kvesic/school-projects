#author: Luka kvesic
#date: 3 october 2025
#description: print the number of even and odd numbers from a series of numbers given by the user, if they enter q then it stops
response = 0
oddCount = 0
evenCount = 0
count = 0
while True:
    response = input('give a number, enter q if finished: ')
    if response == 'q':
        break
    if response.isdigit():
        response = int(response)
    oddCount = 0
    evenCount = 0
    count = 0
    while count < response:
        count += 1
        if count%2 == 0:
            evenCount += 1
        elif count%2 == 1:
            oddCount += 1
    
    print('it has',evenCount,'even numbers')
    print('and has',oddCount,'odd numbers')
