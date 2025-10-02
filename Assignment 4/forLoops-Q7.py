#author: Luka kvesic
#date: 2 october 2025
#description: print the number of even and odd numbers from a series of numbers given by the user, if they enter q then it stops
response = 0
oddStart = 1
evenStart = 2
oddCount = 1
evenCount = 1
while True:
    response = input('give a number, enter q if finished: ')
    if response == 'q':
        break
    if response.isdigit():
        response = int(response)
    oddStart = 1
    evenStart = 2
    oddCount = 1
    evenCount = 1
    while oddStart < response:
        if oddStart + 1 == response:
            break
        oddStart += 2
        oddCount += 1
    while evenStart < response:
        if evenStart+1 == response:
            break
        evenStart += 2
        evenCount += 1
    
    print('it has',evenCount,'even numbers')
    print('and has',oddCount,'odd numbers')
