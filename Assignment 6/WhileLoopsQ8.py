#author: Luka kvesic
#date: 2 october 2025
#description: make a programme that makes the user guess a number if its correct end it, if its too low tell it and if its too high tell them

guesses = 0
key = 44
while True:
    guess = int(input('whats your guess: '))
    if guess == key:
        print('well done')
        guesses += 1
        print('you did that in only',guesses,'guesses')
        break
    elif guess > key:
        print('too high')
        guesses += 1
    elif guess < key:
        print('too low')
        guesses += 1
    
