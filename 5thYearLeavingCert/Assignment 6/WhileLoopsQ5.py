#author: Luka kvesic
#date: 2 october 2025
#description: print from 1 to n squared using a while loop  it should stop it if the iteration is 50

number = int(input('give a number: '))**2
iteration = 0
while iteration < 50:
    iteration += 1
    print(iteration)
    if iteration == number:
        break
   
    